import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import SingletonThreadPool

slqlite_db = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'bierepong.db')
engine = create_engine(f'sqlite:///{slqlite_db}', echo=False, connect_args={'check_same_thread': False},
                       poolclass=SingletonThreadPool)
Base = declarative_base(engine)

Session = scoped_session(sessionmaker(bind=engine, autoflush=False))
