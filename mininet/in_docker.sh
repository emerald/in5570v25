#!/usr/bin/env bash

set -euo pipefail

docker run \
  --interactive --tty --rm \
  --volume "$(pwd):/home/docker/src/" \
  --workdir "/home/docker/src/" \
  --network host \
  portoleks/in5570v25:latest \
  bash -c "$1"
