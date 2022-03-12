import typing as t

from pathlib import Path

from sqlmodel import create_engine, SQLModel
from sqlalchemy.future.engine import Engine
from sqlalchemy import inspect

from flarum_migrations.utilities import add_column


# Overwrite __doc__ with README, so that pdoc can render it:
README_PATH = Path(__file__).parent.parent.absolute() / Path('README.md')
try:
    with open(README_PATH, 'r', encoding="UTF-8") as readme:
        __readme__ = readme.read()
except Exception:
    __readme__ = "Failed to read README.md!"

__doc__ = __readme__



def fm_create_engine(database_models: t.List[t.Type[SQLModel]], *args, **kwargs) -> Engine:
    """
        Creates a Flarum migrations database engine.

        This returns the standard `Engine` object.
        But, in addition to that, it also creates all missing
        columns for tables, so it can be migrated properly
        (no 'missing column' errors).
    """

    engine = create_engine(*args, **kwargs)

    for model in database_models:
        for column in inspect(model).columns:
            add_column(engine, model.__tablename__, column)

    return engine
