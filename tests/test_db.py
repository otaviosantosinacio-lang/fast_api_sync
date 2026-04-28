from sqlalchemy import select

from src.fast_api.models import User


def test_creat_user(session):

    user = User(
        username='OtavioTest',
        email='otaviotest@otavio.com',
        password='senhaotaviotest',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'otaviotest@otavio.com')
    )
    assert result.username == 'OtavioTest'
    assert result.email == 'otaviotest@otavio.com'
    assert result.password == 'senhaotaviotest'
