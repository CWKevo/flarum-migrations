from tests import ENGINE
from sqlmodel import select, Session

from flarum_migrations.models.flarum.access_tokens import FlarumAccessToken


def test_access_token_select():
    """
        Attempt to select some access token data from the database.
    """

    with Session(ENGINE) as session:
        access_token = session.exec(select(FlarumAccessToken)).first()
        print(access_token.title if access_token else 'No access token found.')



if __name__ == '__main__':
    test_access_token_select()
