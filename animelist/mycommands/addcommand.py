from typing import List, Optional

import rich
import typer
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt

from animelist import common
from animelist.anime import Anime, AnimeTypes, Status
from animelist.animelistdata import AnimeListData

console = rich.console.Console()


def impl_add_command(new_name: List[str], genre_flag: bool, anime_list: List[Anime]) -> None:
    """To add a new anime to your list"""

    # se genre e' True, allora considera il nome come un nuovo genere
    if genre_flag:
        new_genre = " ".join(new_name)
        if any(new_genre.lower() == genre.lower() for genre in common.GENRE_LIST):
            console.print(f"[red]Genre {new_genre} already exists in your list[/red]")
            raise typer.Exit(1)

        common.GENRE_LIST = common.GENRE_LIST + (new_genre,)
        # salva il nuovo genere nel file
        AnimeListData.write_genres_to_file(common.GENRE_LIST)
        return

    # anime name
    anime_name: str = " ".join(new_name)
    if any(anime_name.lower() == anime.name.lower() for anime in anime_list):
        console.print(f"[red]Anime {anime_name} already exists in your list[/red]")
        raise typer.Exit(1)

    # anime type
    anime_type: str = select_from_menu(items=tuple(map(lambda x: x.value, AnimeTypes)), title="anime type",
                                       default=AnimeTypes.ANIME.value)
    anime_type: AnimeTypes = AnimeTypes(anime_type)

    # anime genre
    anime_genre1 = select_from_menu(items=common.GENRE_LIST, title="anime genre", default=common.GENRE_LIST[0],
                                    show_choices=False)
    anime_genre2 = select_from_menu(items=common.GENRE_LIST, title="anime genre (optional)", default='',
                                    show_choices=False)

    # anime season
    anime_season: Optional[int] = None
    if anime_type == AnimeTypes.ANIME.value:
        anime_season = IntPrompt.ask("season", default=1)

    # anime episode
    anime_episode: int = IntPrompt.ask("episode", default=1)

    # anime status
    anime_status: str = select_from_menu(items=tuple((map(lambda x: x.value, Status))), title="anime status",
                                         default=Status.PLAN_TO_WATCH.value)
    anime_status: Status = Status(anime_status)

    # anime rating
    anime_rating: Optional[int] = None
    if anime_status is not Status.PLAN_TO_WATCH.value:
        anime_rating = IntPrompt.ask('ranting', default=1, choices=list(map(str, Anime.RATING_RANGE)))

    anime: Anime = Anime(anime_type, anime_name, (anime_genre1, anime_genre2), anime_status, anime_season,
                         anime_episode,
                         anime_rating)

    # aggiunge l'anime alla lista
    anime_list.append(anime)

    # aggiunge l'anime al file csv
    AnimeListData.append_to_csv(anime)

    common.show_anime(anime)


def select_from_menu(items: tuple[str, ...], title: str, default: str, show_choices: bool = True) -> str:
    """To select an item from a menu"""

    f_items: List[str] = [f"[{i + 1}] {item}" for i, item in enumerate(items)]
    f_items: str = '\n'.join(f_items)
    # stampa il menu
    console.print(Panel(f_items, title=title, expand=False))

    choice: str = Prompt.ask("Empty for default", choices=list(map(str, range(1, len(items) + 1))),
                             default=default, show_choices=show_choices, show_default=True)
    # restituisce la scelta predefinita
    if not choice.isdigit():
        return choice
    # la scelta utente è un numero
    return items[int(choice) - 1]
