from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

{% if cookiecutter.database == "postgresql" %}
DATABASE_URL = "postgresql://user:password@host/db"
{% elif cookiecutter.database == "SQLite" %}
DATABASE_URL = "sqlite:///./{{cookiecutter.package_name}}.sqlite"
{% elif cookiecutter.database == "MySQL" %}
DATABASE_URL = "mysql+mysqlconnector://user:password@host/db"
{% endif %}

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # this is SQLite only, not needed for other dbs
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
