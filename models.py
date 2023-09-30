from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///metflix.db")
Base = declarative_base()


user_series = Table(
    "user_series",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("series_id", Integer, ForeignKey("series.id")),
)
user_movies = Table(
    "user_movies",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("movie_id", Integer, ForeignKey("movies.id")),
)
watch_list_series = Table(
    "watch_list_series",
    Base.metadata,
    Column("watch_list_id", Integer, ForeignKey("watch_list.id")),
    Column("series_id", Integer, ForeignKey("series.id")),
)
watch_list_movies = Table(
    "watch_list_movies",
    Base.metadata,
    Column("watch_list_id", Integer, ForeignKey("watch_list.id")),
    Column("movie_id", Integer, ForeignKey("movies.id")),
)


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_title = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)

    user = relationship("Users", secondary=user_movies, back_populates="movies")
    watch_list = relationship("WatchList", secondary=watch_list_movies, back_populates="movies")


class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, autoincrement=True)
    series_title = Column(String(255), nullable=False)
    release_year = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    seasons = Column(Integer, nullable=False)

    user = relationship("Users", secondary=user_series, back_populates="series")
    watch_list = relationship("WatchList", secondary=watch_list_series, back_populates="series")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), default="")

    # Can access watch lists and if deleted, deletes all the watch lists for this user - One To Many
    watch_lists = relationship("WatchList", back_populates="user", cascade="all, delete-orphan")

    movies = relationship("Movies", secondary=user_movies, back_populates="user")
    series = relationship("Series", secondary=user_series, back_populates="user")


class WatchList(Base):
    __tablename__ = "watch_list"

    id = Column(Integer, primary_key=True, autoincrement=True)
    watch_list_name = Column(String(255), nullable=False)
    watch_list_creation_date = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Can access user - One To Many
    user = relationship("User", back_populates="watch_lists")

    movies = relationship("Movies", secondary=user_movies, back_populates="watch_list")
    series = relationship("Series", secondary=user_series, back_populates="watch_list")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
