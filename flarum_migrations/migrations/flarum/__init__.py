import typing as t
from sqlmodel import SQLModel

from .access_tokens import FlarumAccessToken
from .users import FlarumUser


ALL_FLARUM_MODELS: t.Type[SQLModel] = [
    FlarumAccessToken,
    FlarumUser
]
