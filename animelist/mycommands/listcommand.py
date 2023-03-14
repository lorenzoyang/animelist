import re
from typing import List, Optional

import typer
from rich.table import Table

from animelist import common
from animelist.anime import Anime, Status


def impl_list_command(existing_genre: Optional[str], existing_status: Optional[Status], existing_rating: Optional[str],
                      number: Optional[int],
                      anime_list: List[Anime]) -> None:
    """To list all anime in your list"""

    table = Table(title="My Anime List", show_lines=True)
    table.add_column("Name", justify="left", style="cyan")
    table.add_column("Genre", justify="left", style="cyan")
    table.add_column("Status", justify="center", style="cyan")
    table.add_column("Rating", justify="center", style="cyan")
    table.add_column("Type", justify="center", style="cyan")

    # filter by genre
    if existing_genre:
        anime_list = [anime for anime in anime_list if existing_genre.lower() in map(str.lower, anime.genre)]

    # filter by status
    if existing_status:
        anime_list = [anime for anime in anime_list if existing_status == anime.status]

    if existing_rating:
        if existing_rating.isdigit():
            anime_list = [anime for anime in anime_list if anime.rating == int(existing_rating)]
        elif __check_rating_format(existing_rating):
            # non necessario
            try:
                min_val, max_val = map(int, existing_rating.split(":"))
            except ValueError:
                typer.echo(f"Invalid rating: {existing_rating}")
                raise typer.Exit(1)

            #  < min_val or > max_val, if min_val or max_val is not given, all anime that have a rating smaller or
            #  bigger than the given value will be shown
            anime_list = [anime for anime in anime_list if
                          (not min_val or anime.rating >= min_val) and (not max_val or anime.rating <= max_val)]
        else:
            typer.echo(f"Invalid rating format: {existing_rating}")
            raise typer.Exit(1)

    # sort by rating
    anime_list = sorted(anime_list, key=lambda anime: anime.rating)

    if not number:
        number = len(anime_list)
    # print the last {number} anime
    for anime in anime_list[-number:]:
        # format genre
        f_genre = ", ".join(anime.genre) if anime.genre[1] else anime.genre[0]

        table.add_row(anime.name, f_genre, anime.status, str(anime.rating), str(anime.anime_type.value))

    common.console.print(table)


def __check_rating_format(rating: str) -> bool:
    """Check if the rating is in the correct format"""

    pattern = r'^(\d+):(\d+)|(\d+):|:(\d+)$'
    return bool(re.match(pattern, rating))
