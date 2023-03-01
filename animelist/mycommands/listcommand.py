import re
from typing import List, Optional, Match

import rich
import typer
from rich.table import Table

from animelist.anime import Anime, Status

console = rich.console.Console()


def impl_list_command(existing_genre: Optional[str], existing_status: Optional[Status], existing_rating: Optional[str],
                      anime_list: List[Anime]) -> None:
    """To list all anime in your list"""

    table = Table(title="My Anime List")

    table.add_column("Name", justify="left", style="cyan")
    table.add_column("Genre", justify="left", style="cyan")
    table.add_column("Status", justify="left", style="cyan")
    table.add_column("Rating", justify="center", style="cyan")
    table.add_column("Type", justify="center", style="cyan")

    # filter by genre
    if existing_genre:
        anime_list = [anime for anime in anime_list if existing_genre.lower() in map(str.lower, anime.genre)]

    # filter by status
    if existing_status:
        anime_list = [anime for anime in anime_list if existing_status == anime.status]

    # [< | <= | = | > | >=]rating
    if existing_rating:
        if existing_rating.isdigit():
            anime_list = [anime for anime in anime_list if anime.rating == int(existing_rating)]
        else:
            pattern: str = r'[<>]=?'
            match: Optional[Match[str]] = re.search(pattern, existing_rating)

            if not match:
                raise typer.BadParameter(f"Rating {existing_rating} is not valid")

            operator: str = match.group()
            match operator:
                case "<":
                    anime_list = [anime for anime in anime_list if anime.rating < int(existing_rating[1:])]
                case "<=":
                    anime_list = [anime for anime in anime_list if anime.rating <= int(existing_rating[2:])]
                case ">":
                    anime_list = [anime for anime in anime_list if anime.rating > int(existing_rating[1:])]
                case ">=":
                    anime_list = [anime for anime in anime_list if anime.rating >= int(existing_rating[2:])]

    max_length: int = 8
    for anime in anime_list:
        # format name
        f_name: str = anime.name[:max_length] + "..." if len(anime.name) > max_length else anime.name
        # format genre
        f_genre = ", ".join(anime.genre) if anime.genre[1] else anime.genre[0]

        table.add_row(f_name, f_genre, anime.status, str(anime.rating), str(anime.anime_type.value))

    console.print(table)


