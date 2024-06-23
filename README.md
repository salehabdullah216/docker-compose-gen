# Docker Compose Generator

This script generates a `docker-compose.yml` file for your Docker containers. It can either autodetect running containers or use specified container names provided as arguments.

## Prerequisites

- Python 3.x
- Docker
- pip for Python package installation

## Installation

Clone this repository and install the required packages:

```bash
git clone https://github.com/salehabdullah216/docker-compose-gen.git
cd docker-compose-generator
pip install pyyaml
```

## Usage

### Autodetect Running Containers

To generate a `docker-compose.yml` file for all running containers, run:

```bash
./setup.sh
```

### Specify Container Names

To generate for specific containers, provide their names:

```bash
./setup.sh adguard pihole watchtower
# Example usage: ./setup.sh container1 container2 container3
```

### Specify Output File Name

To use a different output file name:

```bash
./setup.sh -o custom-compose.yml
```

### Python Script Details

Run `generator.py` directly with optional arguments:

```bash
python3 generator.py [container_names] -o [output_file]
```

## Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
