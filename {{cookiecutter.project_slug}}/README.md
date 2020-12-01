# {{cookiecutter.project_name}}

## Run project

### Development mode

```sh
python3 -m {{cookiecutter.project_root}}

# OR

python3 -m {{cookiecutter.project_root}} --no-prod
```

### Production mode

```sh
python3 -m {{cookiecutter.project_root}} --prod
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
