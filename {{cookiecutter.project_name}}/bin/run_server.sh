#!/usr/bin/env bash
set -Eeuo pipefail
PYTHONPATH=src poetry run uvicorn {{cookiecutter.package_name}}.main:app "$@"