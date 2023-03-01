from enum import Enum
from typing import Tuple, Union, Optional


class AnimeTypes(str, Enum):
    ANIME = 'anime'
    MANGA = 'manga'
    FILM = 'film'


class Status(str, Enum):
    WATCHING = 'watching'
    COMPLETED = 'completed'
    ON_HOLD = 'onHold'
    DROPPED = 'dropped'
    PLAN_TO_WATCH = 'planToWatch'


def is_valid_enum(enum_class: Union[AnimeTypes, Status], enum_str: Union[str, int]) -> bool:
    try:
        _ = enum_class[enum_str]
    except KeyError:
        return False
    return True


class Anime:
    RATING_RANGE = range(1, 6)

    def __init__(self, anime_type: AnimeTypes, name: str, genre: Tuple[str, str], status: Status, season: Optional[int],
                 episode: int, rating: Optional[int]) -> None:
        self.__anime_type = anime_type
        self.__name = name
        self.__genre = genre
        self.__status = status
        self.__season = season
        self.__episode = episode
        self.__rating = rating

    @property
    def anime_type(self) -> AnimeTypes:
        return self.__anime_type

    @anime_type.setter
    def anime_type(self, anime_type: AnimeTypes) -> None:
        self.__anime_type = anime_type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def genre(self) -> Tuple[str, str]:
        return self.__genre

    @genre.setter
    def genre(self, genre: Tuple[str, str]) -> None:
        self.__genre = genre

    @property
    def status(self) -> Status:
        return self.__status

    @status.setter
    def status(self, status: Status) -> None:
        self.__status = status

    @property
    def season(self) -> int:
        return self.__season

    @season.setter
    def season(self, season: int) -> None:
        self.__season = season

    @property
    def episode(self) -> int:
        return self.__episode

    @episode.setter
    def episode(self, episode: int) -> None:
        self.__episode = episode

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, rating: int) -> None:
        self.__rating = rating

    def __eq__(self, other: 'Anime') -> bool:
        return self.__name == other.__name

    def __lt__(self, other: 'Anime') -> bool:
        return self.__name < other.__name

    def __str__(self) -> str:
        return f'{self.__name} {self.__genre} {self.__status} {self.__season} {self.__episode} {self.__rating}'

    def __repr__(self) -> str:
        return self.__str__()
