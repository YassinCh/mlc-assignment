FROM python:3.12.2-alpine3.19

# Configure poetry
ENV POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=0 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Install gcc
RUN apk add --no-cache gcc musl-dev libffi-dev

# Upgrade pip
RUN pip install --upgrade pip

# Install poetry
RUN pip install poetry==${POETRY_VERSION}

# Set workdir
WORKDIR /home/docker/app

# Copy project.toml and poetry.lock
COPY pyproject.toml ./

# Install all dependecies
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# Create non-root user
RUN adduser -D docker

# Set non-root user
USER docker

# Copy the current directory contents into the container at /home/docker/app
COPY --chown=docker:docker . .

# Expose the default port on which the server runs
EXPOSE 8080

# Run the entrypoint.sh script by default
CMD ["sh", "/home/docker/app/entrypoint.sh"]
