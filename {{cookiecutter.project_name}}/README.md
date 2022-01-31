![Build Status](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.package_name}}/actions/workflows/python-app.yml/badge.svg)

# {{cookiecutter.package_name}}

{{cookiecutter.description}}

## Getting Started

1. Install python3. The [first article]((https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)) in the series linked above should get you started (he recommends `pyenv`). For example, if using `pyenv`, run `pyenv local 3.9.2` (if using python v 3.9.2).
2. Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
3. Build the project. If you prefer make, you can run:

```bash
make deps
```

This will run `poetry install` and `poetry run nox --install-only`. You can run `make help` to see more make targets. Alternatively, you can just run `poetry`'s CLI; see [the Makefile](Makefile)'s make targets for inspiration. 

4. Run `make test` to run the tests
5. Run `make alembic-revision` to generate your first database revision (note, you may need to change the database user, password, host, and db in `database.py`)
6. Run `make alembic-migration` to migrate the revision into the database.
7. Run `./bin/run-server` to start the web server.
8. Goto [the web server's docs page](http://127.0.0.1:8000/docs)

```bash
make clean
```

Will clean out your install. 


## Configuration

This file has some standard config files:

* The overall project is configured via a [PEP518](https://www.python.org/dev/peps/pep-0518/) [pyproject.toml](pyproject.toml) file. If you fork this repo, you should probably change it. It contains the [black](https://pypi.org/project/black/) settings, the project dependencies, a [pytest](https://docs.pytest.org/en/stable/index.html) configuration, and a 
* the [.gitignore](.gitignore) contains obvious gitignores. 
* the [noxfile.py](noxfile.py) contains nox targets for running `safety` and your `tests`. It uses the [nox-poetry](https://pypi.org/project/nox-poetry/) project for nox-poetry integration.
* The [.flake8](.flake8) has a minimal [flake8](https://flake8.pycqa.org/en/latest/) configuration.
* The [mypy.ini](mypy.ini) has a minimal [mypy](http://mypy-lang.org/) configuration.

## Adding a new python dependency

By way of example, you want to add scipy. Then you simply run:

```bash
poetry add scipy
```
