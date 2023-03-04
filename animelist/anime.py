from enum import Enum
from typing import Tuple, Union, Optional


class AnimeTypes(str, Enum):
    """Enum for anime types."""

    ANIME = 'anime'
    MANGA = 'manga'
    FILM = 'film'


class Status(str, Enum):
    """Enum for anime status."""

    WATCHING = 'watching'
    COMPLETED = 'completed'
    ON_HOLD = 'onHold'
    DROPPED = 'dropped'
    PLAN_TO_WATCH = 'planToWatch'


def is_valid_enum(enum_class: Union[AnimeTypes, Status], enum_str: Union[str, int]) -> bool:
    """Check if the given string is a valid enum value."""

    try:
        _ = enum_class[enum_str]
    except KeyError:
        return False
    return True


class Anime:
    """Anime class."""

    RATING_RANGE = range(1, 6)

    def __init__(self, anime_type: AnimeTypes, name: str, genre: Tuple[str, str], status: Status, season: Optional[int],
                 episode: int, rating: Optional[int]) -> None:
        """Initialize an anime object."""

        self.__anime_type = anime_type
        self.__name = name
        self.__genre = genre
        self.__status = status
        self.__season = season
        self.__episode = episode
        self.__rating = rating

    @property
    def anime_type(self) -> AnimeTypes:
        """Return the anime type."""

        return self.__anime_type

    @anime_type.setter
    def anime_type(self, anime_type: AnimeTypes) -> None:
        """Set the anime type."""

        self.__anime_type = anime_type

    @property
    def name(self) -> str:
        """Return the anime name."""

        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Set the anime name."""

        self.__name = name

    @property
    def genre(self) -> Tuple[str, str]:
        """Return the anime genre."""

        return self.__genre

    @genre.setter
    def genre(self, genre: Tuple[str, str]) -> None:
        """Set the anime genre."""

        self.__genre = genre

    @property
    def status(self) -> Status:
        """Return the anime status."""

        return self.__status

    @status.setter
    def status(self, status: Status) -> None:
        """Set the anime status."""

        self.__status = status

    @property
    def season(self) -> int:
        """Return the anime season."""

        return self.__season

    @season.setter
    def season(self, season: int) -> None:
        """Set the anime season."""

        self.__season = season

    @property
    def episode(self) -> int:
        """Return the anime episode."""

        return self.__episode

    @episode.setter
    def episode(self, episode: int) -> None:
        """Set the anime episode."""

        self.__episode = episode

    @property
    def rating(self) -> int:
        """Return the anime rating."""

        return self.__rating

    @rating.setter
    def rating(self, rating: int) -> None:
        """Set the anime rating."""

        self.__rating = rating

    def __eq__(self, other: 'Anime') -> bool:
        """Return True if the anime name is equal to the other anime name."""

        return self.__name == other.__name

    def __lt__(self, other: 'Anime') -> bool:
        """Return True if the anime name is less than the other anime name."""

        return self.__name < other.__name

    def __str__(self) -> str:
        """Return the string representation of the anime object."""

        return f'{self.__name} {self.__genre} {self.__status} {self.__season} {self.__episode} {self.__rating}'

    def __repr__(self) -> str:
        """Return the string representation of the anime object."""

        return self.__str__()
