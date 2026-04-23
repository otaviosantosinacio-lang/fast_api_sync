from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from src.fast_api.models import User, table_registry


def test_creat_user():
  

    
    with Session(engine) as session:
        user = User(
            username='OtavioTest',
            email='otaviotest@otavio.com',
            password='senhaotaviotest',
        )

        session.add(user)
        session.commit()
        
        result = session.scalar(select(User).where(User.email == 'otaviotest@otavio.com'))
    assert result.username == 'OtavioTest'
    assert result.email == 'otaviotest@otavio.com'
    assert result.password == 'senhaotaviotest'
