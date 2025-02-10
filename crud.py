from models import User, engine
from sqlmodel import Session, select

def create_user(username: str, email: str):
    user = User(username=username, email=email)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

def get_user(user_id: int):
    with Session(engine) as session:
        statement = select(User).where(User.id == user_id)
        result = session.exec(statement)
        return result.one()

def update_user(user_id: int, username: Optional[str] = None, email: Optional[str] = None):
    with Session(engine) as session:
        user = session.get(User, user_id)
        if username:
            user.username = username
        if email:
            user.email = email
        session.add(user)
        session.commit()
        session.refresh(user)
    return user

def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()