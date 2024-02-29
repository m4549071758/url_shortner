from sqlalchemy import create_engine, Column, TEXT, DATETIME, CHAR, INTEGER
from datetime import datetime
from sqlalchemy.orm import scoped_session, sessionmaker
import secrets
from sqlalchemy.ext.declarative import declarative_base
from db_config import MYSQL_USER, MYSQL_PASSWORD, HOST, MYSQL_DB_NAME

engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{HOST}/{MYSQL_DB_NAME}")
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class Urls(Base):
    __tablename__ = "urls"
    id = Column(INTEGER(), primary_key=True, autoincrement=True)
    url = Column(TEXT, nullable=False)
    token = Column(CHAR(6), nullable=False, index=True)
    created_at = Column(DATETIME, default=datetime.now)

    def __init__(self, url=None, token=None):
        self.url = url
        self.token = token

Base.metadata.create_all(engine)
Base.query = db_session.query_property()