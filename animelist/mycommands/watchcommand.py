from typing import List

import rich.console
import typer

from animelist import common
from animelist.anime import Anime

console = rich.console.Console()


def impl_watch_command(
        existing_name: List[str],
        episode: int,
        anime_list: List[Anime]
) -> None:
    """To watch an anime in your list"""

    anime_name: str = " ".join(existing_name)
    anime: Anime = common.get_anime_from_name(anime_name, anime_list)
    if anime is None:
        console.print(f"Anime {anime_name} not found", style="bold red")
        raise typer.Exit(1)
    anime.episode = anime.episode + episode
    common.show_anime(anime)
