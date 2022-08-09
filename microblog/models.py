from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from core.db import Base
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'Microblog_posts'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String(320))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('user.id'))
    user_id = relationship("User")
