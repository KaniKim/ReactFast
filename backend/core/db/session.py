import os
from contextvars import ContextVar, Token
from os.path import join, dirname
from typing import Union

from dotenv import load_dotenv
from sqlalchemy import Update, Delete, Insert
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

session_context: ContextVar[str] = ContextVar("session_context")
dotenv_path = join(dirname(__file__), ".env_db")
load_dotenv(dotenv_path)

WRITER_DB_URL = os.environ.get("WRITER_DB_URL")
READER_DB_URL = os.environ.get("READER_DB_URL")
def get_session_context() -> str:
    return session_context.get()

def set_session_context(session_id: str) -> Token:
    return session_context.set(session_id)

def reset_session_context(context: Token) -> None:
    session_context.reset(context)

engines = {
    "writer": create_async_engine(WRITER_DB_URL, pool_recycle=3600),
    "reader": create_async_engine(READER_DB_URL, pool_recycle=3600)
}

class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None, **kwargs):
        if self._flushing or isinstance(clause, (Update, Delete, Insert)):
            return engines["writer"].sync_engine
        else:
            return engines["reader"].sync_engine

async_session_factory = async_sessionmaker(class_=AsyncSession, async_scoped_session=RoutingSession)

session: Union[AsyncSession, async_scoped_session] = async_scoped_session(
    session_factory=async_session_factory,
    scopefunc=get_session_context,
)

Base = declarative_base()