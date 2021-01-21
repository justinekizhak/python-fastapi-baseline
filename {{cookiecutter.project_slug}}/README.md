# {{cookiecutter.project_name}}

## Install dependencies

```sh
poetry install
```

## Poetry

### To install all packages

```sh
poetry install
```

### To add new package

```sh
poetry add <package-name> # or poetry add --dev <package-name>
```

### To go into poetry shell

```sh
poetry shell
```

### To get help

```sh
poetry --help
```

Poetry Docs: https://python-poetry.org/

## Devfile

[Checkout the devfile](https://dgenerate.aziraz.com/?q=eyJhdXRob3IiOiJ7e2Nvb2tpZWN1dHRlci5hdXRob3JfbmFtZX19IDx7e2Nvb2tpZWN1dHRlci5hdXRob3JfZW1haWx9fT4iLCJkZXNjcmlwdGlvbiI6IkFsbCB0aGUgY29tbWFuZHMgcmVxdWlyZWQgZm9yIGJ1aWxkaW5nIGFuZCBkZXBsb3lpbmcgdGhlIGFwcGxpY2F0aW9uIiwibW9kdWxlcyI6W3sibW9kdWxlX3R5cGUiOiJncm91cCIsIm5hbWUiOiJkZXBsb3kiLCJyZXF1aXJlcyI6WyJidWlsZCBhbmQgcnVuIiwib3BlbiBicm93c2VyIl19LHsiY29tbWFuZHMiOlsicHl0aG9uIC1tIHdlYmJyb3dzZXIgaHR0cDovL2xvY2FsaG9zdCJdLCJkZXNjcmlwdGlvbiI6Ik9wZW4gdGhlIGJyb3dzZXIgd2l0aCB0aGUgdXJsLiIsIm1vZHVsZV90eXBlIjoicGhvbnkiLCJuYW1lIjoib3BlbiBicm93c2VyIn0seyJjb21tYW5kcyI6WyJkb2NrZXIgYnVpbGQgLXQge2ltYWdlX25hbWV9IC4iLCJkb2NrZXIgcnVuIC1kIC0tbmFtZSB7Y29udGFpbmVyX25hbWV9IC1wIDgwOjgwIHtpbWFnZV9uYW1lfSJdLCJjb25zdGFudHMiOlt7ImtleSI6ImNvbnRhaW5lcl9uYW1lIiwidmFsdWUiOiJwcm9qZWN0X2FxdWF6X2NvbnRhaW5lciJ9LHsia2V5IjoiaW1hZ2VfbmFtZSIsInZhbHVlIjoicHJvamVjdF9hcXVhel9pbWFnZSJ9XSwiZGVzY3JpcHRpb24iOiJCdWlsZCBhbmQgZGVwbG95IHRoZSBkb2NrZXIgY29udGFpbmVyIHdpdGggcHJvZHVjdGlvbiBzZXR0aW5ncy5cblxuRm9yIGZ1bGwgZG9jdW1lbnRhdGlvbiBvbiB0aGUgZG9ja2VyIHNldHRpbmdzIGNoZWNrIHRoZSBVUkwuIiwibW9kdWxlX3R5cGUiOiJwaG9ueSIsIm5hbWUiOiJidWlsZCBhbmQgcnVuIiwidXJsIjoiaHR0cHM6Ly9naXRodWIuY29tL3RpYW5nb2xvL3V2aWNvcm4tZ3VuaWNvcm4tZG9ja2VyIn0seyJjb21tYW5kcyI6WyJweXRob24zIC1tIHt7Y29va2llY3V0dGVyLnByb2plY3Rfcm9vdH19Il0sImRlc2NyaXB0aW9uIjoiUnVuIHRoZSBhcHBsaWNhdGlvbiBpbiBkZXZlbG9wbWVudCBtb2RlIiwibW9kdWxlX3R5cGUiOiJwaG9ueSIsIm5hbWUiOiJkZXYifV19)

## Run project

Install pipx for better dev experience

### Development mode

```sh
pipx run ddot run -m dev

# OR

python3 -m {{cookiecutter.project_root}}
```

### Production mode

```sh
pipx run ddot run -m prod
```

### Help

```sh
python3 -m {{cookiecutter.project_root}} --help
```

## API docs

API docs are available at

ReDoc is the default. SwaggerUI is also available.

### ReDoc

http://localhost:5000/api

### Swagger UI

http://localhost:5000/api/swagger

## Support for `.env` files

`.env` files are supported.

Also stage based env files are also supported.

Stages supported:

- Development
- Production

Also includes support for `.local` files as well.

`.local` files have the higher priority over the non local files.

Supported files:

- `.env.development.local`
- `.env.development`
- `.env.production.local`
- `.env.production`

### ENV values

These variables will always be opposite of the `PRODUCTION_ENV` variable.

- `SERVER_RELOAD`
- `DEBUG`

Even though they are part of the `BaseSettings` their value will always be
overridden by the above logic.

## Testing

### Isolated testing

```sh
tox
```

### Testing once

```sh
pytest
```

### TDD

```sh
pytest-watch
```

### Type checking

```sh
mypy
```

### Linting, typechecking all at once

```sh
tox -e check
```

## Installing Pre commit hook

```sh
pre-commit install
```
