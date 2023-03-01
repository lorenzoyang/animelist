from typing import List

import typer

from animelist import common
from animelist.anime import Anime


def impl_show_command(existing_name: List[str], anime_list: List[Anime]) -> None:
    """To show information about a specific media in your list"""

    anime_name = " ".join(existing_name)
    anime = common.get_anime_from_name(anime_name, anime_list)
    if anime is None:
        typer.echo(f"Anime {anime_name} not found")
        raise typer.Exit(1)
    common.show_anime(anime)
