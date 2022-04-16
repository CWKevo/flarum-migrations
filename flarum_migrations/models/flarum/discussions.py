import typing as t
import sqlmodel as sql

from datetime import datetime

if t.TYPE_CHECKING:
    from .users import FlarumUser



class FlarumDiscussion(sql.SQLModel, table=True):
    """
        Model for Flarum discussion
    """

    __tablename__ = 'discussions'
    id: t.Optional[int] = sql.Field(default=None, primary_key=True)
    """ID of the discussion."""

    title: str = sql.Field(max_length=200)
    """Title of the discussion."""
    slug: str = sql.Field(max_length=255)
    """Slug of the discussion, used in the URL (format: `<discussion.id>-<discussion.title>`, discussion title is converted to an URL safe string)."""

    comment_count: int = 1
    """Number of comments (posts) in the discussion."""
    participant_count: int = 0
    """How many users have participated in the discussion?"""
    post_number_index: int = 0
    """Index of the last post in the discussion."""

    created_at: datetime = datetime.now()
    """Date and time when the discussion was created."""
    user: t.Optional['FlarumUser'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.user_id==FlarumUser.id", "lazy": "joined"})
    """User who created the discussion."""
    user_id: t.Optional[int] = sql.Field(default=None, foreign_key='users.id')
    """ID of the discussion's author."""
    first_post_id: t.Optional[int]
    """ID of the first post in the discussion."""

    last_posted_at: t.Optional[datetime]
    """Date and time when the last post was created."""
    last_posted_user: t.Optional['FlarumUser'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.last_posted_user_id==FlarumUser.id", "lazy": "joined"})
    """User who created the last post in the discussion."""
    last_posted_user_id: t.Optional[int] = sql.Field(default=None, foreign_key='users.id')
    """ID of the user who created the last post."""
    last_post_id: t.Optional[int]
    """ID of the last post in the discussion."""
    last_post_number: t.Optional[int]
    """Number of the last post in the discussion."""

    hidden_at: t.Optional[datetime]
    """Date and time when the discussion was hidden."""
    hidden_user: t.Optional['FlarumUser'] = sql.Relationship(back_populates='hid_discussions', sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.hidden_user_id==FlarumUser.id", "lazy": "joined"})
    """User who hid the discussion."""
    hidden_user_id: t.Optional[int] = sql.Field(default=None, foreign_key='users.id')
    """ID of the user who hid the discussion."""

    is_private: bool = False
    """Whether the discussion is private."""
    is_approved: bool = True
    """Whether the discussion is approved."""
    is_locked: bool = False
    """Whether the discussion is locked."""
    is_sticky: bool = False
    """Whether the discussion is sticky."""

    best_answer_post_id: t.Optional[int]
    """ID of the post that is the best answer."""
    best_answer_user: t.Optional['FlarumUser'] = sql.Relationship(sa_relationship_kwargs={"primaryjoin": "FlarumDiscussion.best_answer_user_id==FlarumUser.id", "lazy": "joined"})
    """User who posted the best answer in the discussion."""
    best_answer_user_id: t.Optional[int] = sql.Field(default=None, foreign_key='users.id')
    """ID of the user who posted the best answer in the discussion."""
    best_answer_notified: bool = True
    """Whether the author was notified of best answer."""
    best_answer_set_at: t.Optional[datetime]
    """Date and time when the best answer was set."""

    view_count: int = 0
    """Number of times the discussion was viewed."""
    replyTemplate: t.Text = ''
    """Template for the reply form."""
    language_id: t.Optional[int]
    """ID of the language used for the discussion."""

    is_stickiest: bool = False
    """Whether the discussion is stickiest."""
    is_tagSticky: bool = False
    is_first_moved: bool = False

    votes: int = 0
    """Number of votes for the discussion."""
    hotness: float = 0.0
    """Hotness of the discussion."""
    shadow_hidden_at: t.Optional[datetime]
    """Date and time when the discussion was hidden."""
    show_to_all: bool = False
    """Whether the discussion is visible to everyone."""
