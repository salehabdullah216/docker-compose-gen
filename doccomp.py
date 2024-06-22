import subprocess
import json
import yaml
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_running_containers():
    try:
        result = subprocess.run(['docker', 'ps', '--format', '{{.Names}}'], stdout=subprocess.PIPE, check=True)
        return result.stdout.decode().splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching running containers: {e}")
        sys.exit(1)

def get_container_details(container_name):
    try:
        result = subprocess.run(['docker', 'inspect', container_name], stdout=subprocess.PIPE, check=True)
        return json.loads(result.stdout)[0]
    except subprocess.CalledProcessError as e:
        print(f"Error inspecting container {container_name}: {e}")
        return None
    except json.JSONDecodeError:
        print(f"Failed to parse JSON output for {container_name}")
        return None

def process_ports(details):
    ports = []
    for binding in details:
        try:
            ports.append(f"{binding['HostPort']}:{binding['ContainerPort']}")
        except KeyError:
            print("Available keys in 'binding':", binding.keys())  # Debugging line
            raise
    return ports

def process_volumes(details):
    return [f"{mount['Source']}:{mount['Destination']}" for mount in details['Mounts']]

def generate_docker_compose(container_names, output_file):
    compose_data = {
        'version': '3',
        'services': {}
    }

    with ThreadPoolExecutor() as executor:
        future_to_name = {executor.submit(get_container_details, name): name for name in container_names}

        for future in as_completed(future_to_name):
            name = future_to_name[future]
            details = future.result()
            if details is None:
                continue  # Skip this container if details couldn't be fetched

            image = details['Config']['Image']
            ports = process_ports(details)
            volumes = process_volumes(details)
            environment = details['Config'].get('Env', [])

            service = {
                'image': image,
                'ports': ports,
                'volumes': volumes,
                'environment': environment,
            }

            compose_data['services'][name] = service

    with open(output_file, 'w') as file:
        yaml.dump(compose_data, file, default_flow_style=False)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Generate a Docker Compose file from running containers.')
    parser.add_argument('containers', nargs='*', help='Names of containers to include')
    parser.add_argument('-o', '--output', default='docker-compose.yml', help='Output file name')
    args = parser.parse_args()

    container_names = args.containers or get_running_containers()

    if not container_names:
        print("No containers found to include in the Docker Compose file.")
        sys.exit(1)

    generate_docker_compose(container_names, args.output)
