# Docker Compose Generator

This tool simplifies the creation of `docker-compose.yml` files, automating the setup of Docker environments. Docker Compose is a tool for defining and running multi-container Docker applications. With this generator, you can quickly configure and manage your Docker containers either by autodetecting running containers or specifying them manually.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration Options](#configuration-options)
- [Contributing](#contributing)
- [License](#license)
- [FAQ](#faq)

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

## FAQ
