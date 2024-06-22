#!/bin/bash

if [ "$#" -gt 0 ]; then
    python3 doccomp.py "$@"
else
    python3 doccomp.py
fi
