from tests import ENGINE
from sqlmodel import select, Session

from flarum_migrations.utilities import flarum_hash_password
from flarum_migrations.models.flarum.users import FlarumUser
from flarum_migrations.models.flarum.discussions import FlarumDiscussion


def test_user_select():
    """
        Attempt to select some user from the database.
    """

    with Session(ENGINE) as session:
        user = session.exec(select(FlarumUser)).first()
        print(user.username if user else 'No user found.')
        print(f"Achievements: {[achievement.name for achievement in user.achievements]}")



def test_user_create_and_delete(delete: bool=True):
    """
        Creates an user.
    """

    with Session(ENGINE) as session:
        discussions = [
            FlarumDiscussion(title='Test Discussion 1', slug='test-discussion-1'),
            FlarumDiscussion(title='Test Discussion 2', slug='test-discussion-2'),
        ]

        user = FlarumUser(username='testingier', email='testingier@test.gov', password=flarum_hash_password('test'), discussions=discussions)

        session.add(user)
        session.commit()
        session.refresh(user)

        print(user.id, user.username)

        for discussion in user.discussions:
            print(discussion.id, discussion.title)
        
        if delete:
            session.delete(user)
            for discussion in discussions:
                session.delete(discussion)
            
            session.commit()

        print("OK")



if __name__ == '__main__':
    test_user_select()
    test_user_create_and_delete()
