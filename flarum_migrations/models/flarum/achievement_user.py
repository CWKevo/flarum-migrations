import typing as t
import sqlmodel as sql



class FlarumAchievementUser(sql.SQLModel, table=True):
    """
        Model for achievement <-> user relationship.

        https://discuss.flarum.org/d/26675
    """

    __tablename__ = 'achievement_user'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the `achievement_user` row."""

    user_id: t.Optional[int] = sql.Field(default=None, foreign_key="users.id", primary_key=True)
    """The ID of the user who has the achievement."""
    achievement_id: t.Optional[int] = sql.Field(default=None, foreign_key="achievements.id", primary_key=True)
    """The ID of the achievement that belongs to the user."""
