from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Genre(BaseModel):
    id: str = Field(alias='genre_id')
    name: str = Field(alias='genre_name')


class Person(BaseModel):
    id: str = Field(alias='person_id')
    name: str = Field(alias='person_name')


class ElasticsearchData(BaseModel):
    id: str
    imdb_rating: Optional[float]
    genres: list[Genre]
    genre: list[str]
    title: str
    description: str | None
    director: list[str]
    actors_names: list[str]
    writers_names: list[str]
    directors: list[Person]
    actors: list[Person]
    writers: list[Person]
    modified: datetime
