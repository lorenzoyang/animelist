from typing import List

import typer
from rich.prompt import Confirm

from animelist import common
from animelist.anime import Anime
from animelist.animelistdata import AnimeListData


def impl_remove_command(existing_name: List[str], genre_flag: bool, anime_list: List[Anime]) -> None:
    """To remove an anime from your list"""

    # se genre e' True, allora considera il nome come un nuovo genere
    if genre_flag:
        existing_genre = " ".join(existing_name)
        if not any(existing_genre.lower() == genre.lower() for genre in common.GENRE_LIST):
            common.console.print(f"[red]Genre {existing_genre} does not exist in your list[/red]")
            raise typer.Exit(1)

        common.GENRE_LIST = tuple(genre for genre in common.GENRE_LIST if genre.lower() != existing_genre.lower())
        # salva il nuovo genere nel file
        AnimeListData.write_genres_to_file(common.GENRE_LIST)
        return

    # anime name
    anime_name: str = " ".join(existing_name)
    anime: Anime = common.get_anime_from_name(anime_name, anime_list)

    if anime is None:
        common.console.print(f"[red]Anime {anime_name} does not exist in your list[/red]")
        raise typer.Exit(1)

    confirmation = Confirm.ask(f"Are you sure you want to remove\n[red]{anime.name}[/red]\nfrom your list?")
    if confirmation:
        anime_list.remove(anime)
        # salva la lista modificata nel file
        AnimeListData.write_to_csv(anime_list)
