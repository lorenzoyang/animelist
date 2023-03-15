import csv
import os
import pathlib
from typing import List, Optional

from animelist.anime import Anime, AnimeTypes, Status


class AnimeListData:
    """Class for the anime list data"""

    HOME_DIR = os.path.expanduser("~")
    # il nome della cartella dove salvare i dati
    DIRECTORY_NAME = os.path.join(HOME_DIR, 'MyAnimeListData')

    # il percorso del file csv per salvare lista di anime
    ANIME_PATH: str = os.path.join(DIRECTORY_NAME, 'anime_data.csv')
    # il percorso del file csv per salvare lista di generi
    GENRES_PATH: str = os.path.join(DIRECTORY_NAME, 'genres_data.csv')

    # il delimitatore per il file csv
    CSV_DELIMITER: str = '|'

    @classmethod
    def initialize(cls: 'AnimeListData') -> None:
        """create the directory and the files if they don't exist"""

        pathlib.Path(cls.DIRECTORY_NAME).mkdir(parents=True, exist_ok=True)

        if not os.path.exists(cls.ANIME_PATH):
            open(cls.ANIME_PATH, 'a').close()
        if not os.path.exists(cls.GENRES_PATH):
            open(cls.GENRES_PATH, 'a').close()
            cls.write_genres_to_file(cls.predefined_genres_list())

    @classmethod
    def write_to_csv(cls: 'AnimeListData', anime_list: List[Anime]) -> None:
        """Write the anime list to the csv file"""

        # sort the anime list by rating
        anime_list = sorted(anime_list, key=lambda a: a.rating)
        with open(cls.ANIME_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=cls.CSV_DELIMITER)
            for anime in anime_list:
                writer.writerow(anime.to_csv_row())

    @classmethod
    def append_to_csv(cls: 'AnimeListData', anime: Anime) -> None:
        """Append the anime to the csv file"""

        with open(cls.ANIME_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=cls.CSV_DELIMITER)
            writer.writerow(anime.to_csv_row())

    @classmethod
    def read_from_csv(cls: 'AnimeListData') -> List[Anime]:
        """Read the anime list from the csv file"""

        cls.initialize()

        anime_list = []
        with open(cls.ANIME_PATH, newline='') as csvfile:
            anime_reader = csv.reader(csvfile, delimiter=cls.CSV_DELIMITER)
            for row in anime_reader:
                anime_type: AnimeTypes = AnimeTypes(row[0])
                name: str = row[1]

                genre_list: List[str] = row[2].split(",")
                genre: tuple[str, str] = (genre_list[0], genre_list[1])

                status: Status = Status(row[3])
                season: int = int(row[4])

                episode: Optional[int] = int(row[5])
                if episode == Anime.EMPTY_EPISODE:
                    episode = None

                rating: Optional[int] = int(row[6])
                if rating == Anime.EMPTY_RATING:
                    rating = None

                anime: Anime = Anime(anime_type, name, genre, status, season, episode, rating)

                anime_list.append(anime)

        return anime_list

    @classmethod
    def write_genres_to_file(cls: 'AnimeListData', genre_list: tuple[str, ...]) -> None:
        """Write the genres to the genres file"""

        with open(cls.GENRES_PATH, 'w') as file:
            for genre in genre_list:
                file.write(genre + '\n')

    @classmethod
    def read_genres_from_file(cls: 'AnimeListData') -> tuple[str, ...]:
        """Read the genres from the genres file"""

        cls.initialize()

        with open(cls.GENRES_PATH, 'r') as file:
            return tuple(file.read().splitlines())

    @classmethod
    def predefined_genres_list(cls):
        """Return the predefined genres list"""

        return (
            'Adventure', 'Action', 'Comedy', 'Slice of Life', 'Drama', 'Fantasy', 'Supernatural', 'Magic', 'Mystery',
            'Horror', 'Psychological', 'Sci-Fi', 'Romance')
