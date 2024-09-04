FROM python:3.11.9-bookworm AS poetry
ENV POETRY_VERSION="1.8.3" 

RUN pip install "poetry==${POETRY_VERSION}"

WORKDIR /calculate_pi

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

COPY README.md LICENSE.txt /calculate_pi/
COPY calculate_pi /calculate_pi/calculate_pi/

RUN poetry build


FROM python:3.11.9-bookworm
LABEL maintainer="Erik Ferlanti <eferlanti@tacc.utexas.edu>"

# Update OS
RUN apt-get update && apt-get install -y \
    vim-tiny \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Configure Python/Pip
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /calculate_pi

COPY --from=poetry /calculate_pi/requirements.txt .

RUN pip install -r requirements.txt

COPY --from=poetry /calculate_pi/dist/*.whl ./

RUN pip install *.whl

COPY README.md LICENSE.txt /calculate_pi/

CMD [ "calculate-pi", "--help" ]
