FROM python:3.10-slim AS base

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN apt-get update \
  && apt-get install --no-install-recommends -y curl unzip \
  && rm -rf /var/lib/apt/lists/*

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code

# Creating folders, and files for a project:
COPY . /code

RUN ./pants package "$APPLICATION"

FROM base as final
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random

WORKDIR /app
COPY --from=base /code/dist/*/*.pex /app
ENTRYPOINT ["/bin/sh"]

