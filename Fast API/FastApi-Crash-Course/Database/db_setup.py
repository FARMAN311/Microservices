from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:newpassword@localhost:5433/fast_lms"
#"postgresql+psycopg2://postgres:yourpassword@localhost:5432/mydatabase"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
"""
Breakdown:

Dialect and Driver: postgresql+psycopg2

Dialect: Specifies the type of database. Here, it's postgresql.
Driver: Specifies the DBAPI to use. Here, it's psycopg2.
Username: postgres

The username to authenticate with the PostgreSQL database.
Password: Not specified in your URL.

If your database requires a password, it should be included here (e.g., postgres:yourpassword).
Host: Syed

The hostname or IP address where your PostgreSQL server is running. Syed appears to be the hostname in your case.
Port: Not specified in your URL.

PostgreSQL's default port is 5432. If your server uses a different port, specify it (e.g., Syed:5433).
Database Name: postgres

The name of the specific database you want to connect to.
"""

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()