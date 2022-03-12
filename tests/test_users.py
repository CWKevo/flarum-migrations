from tests import ENGINE
from sqlmodel import select, Session

from flarum_migrations.migrations.flarum.users import FlarumUser


def test_user_select():
    """
        Attempt to select some user from the database.
    """

    with Session(ENGINE) as session:
        user = session.exec(select(FlarumUser)).first()
        print(user.username if user else 'No user found.')



if __name__ == '__main__':
    test_user_select()
