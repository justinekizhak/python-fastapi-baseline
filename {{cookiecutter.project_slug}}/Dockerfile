FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV MODULE_NAME={{cookiecutter.project_root}}.__main__
ENV PRODUCTION_ENV=True

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* /app

RUN poetry install --no-root --no-dev

COPY *.env /app

COPY {{cookiecutter.project_root}} /app/{{cookiecutter.project_root}}
