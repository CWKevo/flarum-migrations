from sqlmodel import select, Session

from flarum_migrations import fm_create_engine
from flarum_migrations.migrations.flarum import ALL_FLARUM_MODELS
from flarum_migrations.migrations.flarum.users import FlarumUser


ENGINE = fm_create_engine(ALL_FLARUM_MODELS, 'sqlite:///tests/test.db')


def test_user_select():
    """
        Attempt to select some user from the database.
    """

    with Session(ENGINE) as session:
        user = session.exec(select(FlarumUser)).first()
        print(user.username if user else 'No user found.')



if __name__ == '__main__':
    test_user_select()
