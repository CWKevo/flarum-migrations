import typing as t
import sqlmodel as sql

from datetime import datetime, date

if t.TYPE_CHECKING:
    from .access_tokens import FlarumAccessToken



class FlarumUser(sql.SQLModel, table=True):
    """
        A Flarum user model.
    """

    __tablename__ = 'users'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True, index=True)
    """ID of the user."""

    username: str = sql.Field(max_length=100, sa_column_kwargs={'unique': True})
    """Username of the user."""
    nickname: t.Optional[str] = sql.Field(max_length=255)
    """User's nickname."""

    email: str = sql.Field(max_length=150, sa_column_kwargs={'unique': True})
    """User's email address."""
    is_email_confirmed: bool = False
    """Whether the user's email address has been confirmed."""

    password: str = sql.Field(max_length=100)
    """User's password (`bcrypt` hashed)."""

    bio: t.Optional[t.Text]
    """User's bio."""
    avatar_url: t.Optional[str] = sql.Field(max_length=100)
    """User's avatar URL."""

    preferences: t.Dict[str, str] = {}
    """User's preferences data (for notifications, and other settings such as draft autosave interval)."""

    joined_at: t.Optional[datetime] = sql.Field(index=True)
    """Date and time when the user joined the forum."""
    last_seen_at: t.Optional[datetime] = sql.Field(index=True)
    """Date and time when the user was last seen on the forum."""
    marked_all_as_read_at: t.Optional[datetime]
    """Date and time when the user marked all discussions as read."""
    read_notifications_at: t.Optional[datetime]
    """Date and time when the user read their notifications."""

    new_achievements: str = '[]'
    """JSON-encoded list of new achievements earned by the user."""

    read_flags_at: t.Optional[datetime]
    """Date and time when the user read flagged posts."""
    suspended_until: t.Optional[datetime]
    """Date and time when the user's suspension expires."""
    suspend_reason: t.Optional[t.Text]
    """Reason for the user's suspension."""
    suspend_message: t.Optional[t.Text]
    """Message for user's suspension."""

    discussion_count: int = sql.Field(default=0, index=True)
    """Number of discussions the user has created."""
    comment_count: int = sql.Field(default=0, index=True)
    """Number of posts the user has created."""

    first_post_approval_count: int = 0
    """Number of posts requiring approval."""
    first_discussion_approval_count: int = 0
    """Number of discussions requiring approval."""

    birthday: t.Optional[date]
    """Date of user's birthday."""
    showDobDate: bool = True
    """Whether the user's birthday should be shown."""
    showDobYear: bool = True
    """Whether the user's birthday's year should be shown."""

    tagList: t.Optional[str] = sql.Field(max_length=150, index=True)
    staffBadge: t.Optional[str] = sql.Field(max_length=150, index=True)

    blocks_byobu_pd: bool = False
    """Whether the user has blocked private discussions."""
    cover: t.Optional[str] = sql.Field(max_length=150)
    """URL to user's cover image."""
    minotar: t.Optional[str] = sql.Field(max_length=36)
    """URL to user's minotar avatar."""
    username_history: t.Dict[str, str] = {}
    """Username history."""
    social_buttons: t.Optional[t.Text]
    """JSON-encoded list of social buttons."""
    signature: t.Optional[t.Text]
    """User's signature."""
    location: t.Optional[t.Text]
    """User's location."""

    twofa_secret: t.Optional[str] = sql.Field(max_length=120)
    """User's two-factor authentication secret."""
    twofa_active: bool = False
    """Whether the user has enabled two-factor authentication."""
    twofa_codes: t.Optional[str] = sql.Field(max_length=200)
    """JSON-encoded list of two-factor authentication codes."""

    unread_messages: int = 0
    """Number of unread messages."""

    invite_code: t.Optional[str] = sql.Field(max_length=128)
    votes: int = 0
    last_vote_time: t.Optional[datetime]
    """Date and time when the user last voted."""
    rank: t.Optional[str] = sql.Field(max_length=255)
    """User's rank."""
    money: float = 0
    """User's money."""

    disclose_posted_on: bool = True
    """Whether the user's `'posted on <device>'` header should be shown above posts."""
    shadow_banned_until: t.Optional[datetime]
    """Date and time when the user's shadow ban expires."""


    access_tokens: t.List['FlarumAccessToken'] = sql.Relationship(back_populates='user')
    """List of access tokens for the user."""
