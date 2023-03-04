from typing import List, Optional

import rich

from animelist.anime import Anime
from animelist.animelistdata import AnimeListData

# inizializzazione della lista di anime
anime_list = AnimeListData.read_from_csv()

# inizializzazione della lista di generi
GENRE_LIST: tuple[str, ...] = AnimeListData.read_genres_from_file()

console = rich.console.Console()


def get_anime_from_name(existing_name: str, anime_list: List[Anime]) -> Optional[Anime]:
    """Get anime from name"""

    matches = [anime for anime in anime_list if anime.name.lower().startswith(existing_name.lower())]
    return min(matches, key=lambda anime: len(anime.name), default=None)


def show_anime(anime: Anime) -> None:
    """Show anime"""

    console.print(f"Name: {anime.name}")
    console.print(f"Type: {anime.anime_type}")
    console.print(f"Genre: {', '.join(anime.genre)}")
    console.print(f"Season: {anime.season}")
    console.print(f"Episode: {anime.episode}")
    console.print(f"Status: {anime.status}")
    console.print(f"Rating: {anime.rating}")
