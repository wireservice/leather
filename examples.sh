#!/bin/bash

export PYTHONPATH="$PYTHONPATH:$(pwd)"

for f in examples/*.py; do
    echo $f
    python $f
done
