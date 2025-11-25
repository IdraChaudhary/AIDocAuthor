from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    projects = relationship('Project', back_populates='owner')

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    doc_type = Column(String, default='docx')  # 'docx' or 'pptx'
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='projects')
    sections = relationship('Section', back_populates='project', cascade='all, delete')

class Section(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, default='')
    order = Column(Integer, default=0)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='sections')

class Refinement(Base):
    __tablename__ = 'refinements'
    id = Column(Integer, primary_key=True, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'))
    prompt = Column(Text)
    output = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
