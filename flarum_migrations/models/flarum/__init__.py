import typing as t
from sqlmodel import SQLModel

from .access_tokens import FlarumAccessToken
from .achievement_user import FlarumAchievementUser
from .achievements import FlarumAchievement
from .discussions import FlarumDiscussion
from .users import FlarumUser


ALL_FLARUM_MODELS: t.Type[SQLModel] = [
    FlarumAccessToken,
    FlarumAchievementUser,
    FlarumAchievement,
    FlarumUser,
    FlarumDiscussion
]
