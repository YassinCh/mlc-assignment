#!/bin/sh

UVICORN_ADDITIONAL_FLAGS=""

if [ "${UVICORN_RELOAD}" = "1" ]; then
   UVICORN_ADDITIONAL_FLAGS="${UVICORN_ADDITIONAL_FLAGS} --reload-dir assessment"
fi

poetry --quiet run python -m alembic upgrade head
poetry --quiet run python -m uvicorn assessment.main:app --host 0.0.0.0 --port 8080 --log-config config.ini $UVICORN_ADDITIONAL_FLAGS