from typing import List, Optional

import rich
from rich.panel import Panel

from animelist.anime import Anime
from animelist.animelistdata import AnimeListData

# inizializzazione della lista di anime
anime_list = AnimeListData.read_from_csv()

# inizializzazione della lista di generi
GENRE_LIST: tuple[str, ...] = AnimeListData.read_genres_from_file()

console = rich.console.Console()


def get_anime_from_name(existing_name: str, animelist: List[Anime]) -> Optional[Anime]:
    """Get anime from name"""

    matches = [anime for anime in animelist if anime.name.lower().startswith(existing_name.lower())]
    return min(matches, key=lambda anime: len(anime.name), default=None)


def show_anime(anime: Anime) -> None:
    """Show anime"""

    panel = Panel.fit(
        f"Type: [bold blue]{anime.anime_type.value}[/bold blue]\n"
        f"Genre: [bold green]{', '.join(anime.genre)}[/bold green]\n"
        f"Season: [bold yellow]{anime.season}[/bold yellow]\n"
        f"Episode: [bold magenta]{anime.episode}[/bold magenta]\n"
        f"Status: [bold red]{anime.status.value}[/bold red]\n"
        f"Rating: [bold white]{anime.rating}[/bold white]\n"
    )
    panel.title = f"[bold red]{anime.name}[/bold red]"

    console.print(panel)
