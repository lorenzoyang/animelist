from typing import List, Optional

import typer
from rich.prompt import Confirm

from animelist import common
from animelist.anime import AnimeTypes, Status, Anime
from animelist.animelistdata import AnimeListData


def impl_update_command(
        existing_name: List[str],
        new_type: Optional[AnimeTypes],
        new_name: Optional[List[str]],
        new_genre: Optional[List[str]],
        new_season: Optional[int],
        new_episode: Optional[int],
        new_status: Optional[Status],
        new_rating: Optional[int],
        anime_list: List[Anime]
) -> None:
    """To update an anime in your list"""

    # anime name
    anime_name: str = " ".join(existing_name)
    anime: Anime = common.get_anime_from_name(anime_name, anime_list)
    if anime is None:
        common.console.print(f"Anime {anime_name} not found", style="bold red")
        raise typer.Exit(1)

    check_update_items(new_type, new_name, new_genre, new_season, new_episode, new_status, new_rating, anime_list)

    confirmation = Confirm.ask(f"Are you sure you want to update\n[red]{anime.name}[/red]\nfrom your list?")
    if not confirmation:
        raise typer.Exit()

    if new_type:
        anime.anime_type = new_type

    if new_name:
        new_name: str = " ".join(new_name)
        anime.name = new_name

    if new_genre:
        anime.genre = tuple(new_genre)

    if new_season:
        anime.season = new_season

    if new_episode:
        anime.episode = new_episode

    if new_status:
        anime.status = new_status

    if new_rating:
        anime.rating = new_rating

    AnimeListData.write_to_csv(anime_list)

    common.show_anime(anime)


def check_update_items(
        new_type: Optional[AnimeTypes],
        new_name: Optional[str],
        new_genre: Optional[List[str]],
        new_season: Optional[int],
        new_episode: Optional[int],
        new_status: Optional[Status],
        new_rating: Optional[int],
        anime_list: List[Anime]
) -> None:
    """Check if items to update are valid"""

    if new_type:
        pass

    if new_name:
        new_name: str = " ".join(new_name)
        if common.get_anime_from_name(new_name, anime_list) is not None:
            raise typer.BadParameter(f"Anime {new_name} already exists")

    if new_genre:
        if len(new_genre) > 2:
            raise typer.BadParameter(f"Too many genres")
        for g in new_genre:
            if g.lower() not in map(str.lower, common.GENRE_LIST):
                raise typer.BadParameter(f"Invalid genre: {g}")

    if new_season:
        if new_season <= 0:
            raise typer.BadParameter(f"Season {new_season} is not valid")

    if new_episode:
        if new_episode <= 0:
            raise typer.BadParameter(f"Episode {new_episode} is not valid")

    if new_status:
        pass

    if new_rating:
        min_rating: int = Anime.RATING_RANGE.start
        max_rating: int = Anime.RATING_RANGE.stop - 1
        if not (min_rating <= new_rating <= max_rating):
            raise typer.BadParameter(f"Rating {new_rating} is not valid: must be between {min_rating} and {max_rating}")
