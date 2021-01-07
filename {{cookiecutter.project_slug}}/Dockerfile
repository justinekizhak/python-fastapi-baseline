FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

ENV MODULE_NAME={{cookiecutter.project_root}}.__main__

ADD pyproject.toml /app
ADD poetry.lock /app
COPY *.env /app
ADD {{cookiecutter.project_root}} /app/{{cookiecutter.project_root}}

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install