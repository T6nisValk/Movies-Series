from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///metflix.db")
Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True, autoincrement=True)
    movie_title = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)


class Series(Base):
    __tablename__ = "series"

    series_id = Column(Integer, primary_key=True, autoincrement=True)
    series_title = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), default="")


class WatchList(Base):
    __tablename__ = "watch_list"

    watch_list_id = Column(Integer, primary_key=True, autoincrement=True)
    watch_list_name = Column(String(255), nullable=False)
    watch_list_creation_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))


if __name__ == "__main__":
    Base.metadata.create_all(engine)
