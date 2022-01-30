from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./{{cookiecutter.package_name}}.sqlite"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # this is SQLite only, not needed for other dbs
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
