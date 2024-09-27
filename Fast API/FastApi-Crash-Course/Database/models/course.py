from datetime import datetime, timezone
import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType

from ..db_setup import Base
from .user import User
from .mixins import Timestamp

# Define the ContentType Enum
class ContentType(enum.Enum):
    VIDEO = "video"
    ARTICLE = "article"
    QUIZ = "quiz"

# Course model
class Course(Timestamp, Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_by = relationship(User)
    sections = relationship("Section", back_populates="course")  # Changed to plural for clarity
    student_courses = relationship("StudentCourse", back_populates="course")


# Section model
class Section(Timestamp, Base):
    __tablename__ = "sections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=True)

    course = relationship("Course", back_populates="sections")
    content_blocks = relationship("ContentBlock", back_populates="section")


# ContentBlock model
class ContentBlock(Timestamp, Base):
    __tablename__ = "content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    type = Column(Enum(ContentType), nullable=False)  # Fixed: Added ContentType enum
    url = Column(URLType, nullable=True)
    content = Column(Text, nullable=True)
    section_id = Column(Integer, ForeignKey("sections.id"), nullable=True)  # Fixed: ForeignKey refers to 'sections'

    section = relationship("Section", back_populates="content_blocks")
    completed_content_blocks = relationship("CompletedContentBlock", back_populates="content_block")


# StudentCourse model
class StudentCourse(Timestamp, Base):
    """
    student can be assigned to courses
    """
    __tablename__ = "student_courses"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    completed = Column(Boolean, default=False)

    student = relationship(User, back_populates="student_courses")
    course = relationship("Course", back_populates="student_courses")


# CompletedContentBlock model
class CompletedContentBlock(Timestamp, Base):
    """
    this shows when student has completed a content block
    """
    __tablename__ = "completed_content_blocks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content_block_id = Column(Integer, ForeignKey("content_blocks.id"), nullable=False)
    url = Column(URLType, nullable=True)
    feedback = Column(Text, nullable=True)
    grade = Column(Integer, default=0)

    student = relationship(User, back_populates="student_content_blocks")
    content_block = relationship("ContentBlock", back_populates="completed_content_blocks")


