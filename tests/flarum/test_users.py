from tests import ENGINE
from sqlmodel import select, Session

from flarum_migrations.utilities import flarum_hash_password
from flarum_migrations.models.flarum.discussions import FlarumDiscussion
from flarum_migrations.models.flarum.posts import FlarumPost
from flarum_migrations.models.flarum.users import FlarumUser


def test_user_select():
    """
        Attempt to select some user from the database.
    """

    with Session(ENGINE) as session:
        user = session.exec(select(FlarumUser)).first()

        if user:
            print(user.username)
            print(f"Achievements: {[achievement.name for achievement in user.achievements]}")

        else:
            print('No user found.')



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
            user.posts = [
                FlarumPost(discussion=discussion, content=f'Test post 1 in "{discussion.title}"'),
                FlarumPost(discussion=discussion, content=f'Test post 2 in "{discussion.title}"'),
            ]
            session.commit()
            session.refresh(user)
            session.refresh(discussion)

            print(discussion.id, discussion.title)
            print(f'First post: "{discussion.posts[0].content}" [...]')


        if delete:
            session.delete(user)

            for discussion in discussions:
                session.delete(discussion)

            session.commit()

        print("OK")



if __name__ == '__main__':
    test_user_select()
    test_user_create_and_delete()
