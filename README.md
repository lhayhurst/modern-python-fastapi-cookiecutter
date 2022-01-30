
# modern-python-fastapi-cookiecutter

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) project used to quickly create a [FastAPI](https://fastapi.tiangolo.com/) Python project. The project uses a ["hypermodern"](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769) Python stack:
* [Poetry](https://python-poetry.org/) 
* [Black](https://github.com/psf/black)
* [Nox](https://nox.thea.codes/en/stable/)
* [flake8](https://flake8.pycqa.org/en/latest/)
* [mypy](http://mypy-lang.org/)
* [pytest](https://docs.pytest.org/en/6.2.x/)
* [Github actions](https://docs.github.com/en/actions)

At present, it only supports `SQLite` as a database backend. In future releases, it will support both `Postgres` and `mysql`.

# Requirements
* Python 3.7 or greater
* [Poetry](https://python-poetry.org/) 
* [SQLite](https://www.sqlite.org/index.html)

## Getting Started

1. Install python3. The [first article]((https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)) in the series linked above should get you started (he recommends `pyenv`). For example, if using `pyenv`, run `pyenv local 3.9.2` (if using python v 3.9.2).
2. Install `poetry`; see the project homepage or [this article](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/).
3. [Install cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)
4 Run cookiecutter on this project, either cloning this repo locally and:
```shell
cookiecutter modern-python-fastapi-cookiecutter
```
or by running it via url:
```shell
cookiecutter https://github.com/lhayhurst/modern-python-fastapi-cookiecutter.git

```

You can then follow the instructions in the generated `README.md` for building your running, running tests, and running the web server.

From a FASTApi perspective, the project ships with toy object model: a `User` class, and a `MicroBlogPost` class with a relationship back to the user. 