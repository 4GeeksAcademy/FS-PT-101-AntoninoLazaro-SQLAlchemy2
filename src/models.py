from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    
    profile: Mapped['Profile'] = relationship(back_populates='user', uselist=False)
    post: Mapped['Post'] = relationship(back_populates='user')
    classroom: Mapped['Classroom'] = relationship(back_populates='user')


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            'profile':self.profile,
            'post':self.post,
            'classroom':self.classroom
        }

class Profile(db.Model):
    __tablename__ = 'profiles'
    id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str] = mapped_column(String(120))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='profile')

    def serialize(self):
        return {
            "id": self.id,
            "bio": self.bio,
            "user_id": self.user_id
        }

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]=mapped_column(String(150))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='post')


    def serialize(self):
        return {
            "id": self.id,
        }


class Classroom(db.Model):
    __tablename__= 'classrooms'
    id: Mapped[int] = mapped_column(primary_key=True)
    className: Mapped[str]=mapped_column(String(50))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped['User'] = relationship(back_populates='classroom')


    def serialize(self):
        return {
            "id": self.id,
            'className':self.className
        }


