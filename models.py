from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///metflix.db")
Base = declarative_base()


class Movies(Base):
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


class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)


class ToWatchList(Base):
    __tablename__ = "to_watch_list"

    watch_list_id = Column(Integer, primary_key=True, autoincrement=True)
    watch_list_name = Column(String(255), nullable=False)
    watch_list_creation_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"))


class ToWatchMovies(Base):
    __tablename__ = "to_watch_movies"

    movies_id = Column(Integer, primary_key=True, autoincrement=True)
    movies_title = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)
    is_watched = Column(Boolean, default=False)

    watch_list_id = Column(Integer, ForeignKey("to_watch_list.watch_list_id"))


class ToWatchSeries(Base):
    __tablename__ = "to_watch_series"

    series_id = Column(Integer, primary_key=True, autoincrement=True)
    series_title = Column(String(255), nullable=False)
    rating = Column(Integer, nullable=False)
    is_watched = Column(Boolean, default=False)

    watch_list_id = Column(Integer, ForeignKey("to_watch_list.watch_list_id"))


Base.metadata.create_all(engine)
