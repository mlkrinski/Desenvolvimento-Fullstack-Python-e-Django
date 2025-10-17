#!/usr/bin/env bash
set -o errexit  # Para o deploy falhar se der erro

poetry install
poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate
