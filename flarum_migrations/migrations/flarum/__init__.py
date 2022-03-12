import typing as t
from sqlmodel import SQLModel

from .users import FlarumUser


ALL_FLARUM_MODELS: t.Type[SQLModel] = [
    FlarumUser
]
