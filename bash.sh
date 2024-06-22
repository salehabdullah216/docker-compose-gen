#!/bin/bash

if [ "$#" -gt 0 ]; then
    python3 generate_docker_compose.py "$@"
else
    python3 generate_docker_compose.py
fi
