FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    g++ \
    make \
    libspatialindex-dev \
    libgeos-dev \
    libproj-dev \
    proj-data \
    libgdal-dev \
    gdal-bin \
    curl \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=1.8.2
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /workspace
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root

CMD ["bash"]

