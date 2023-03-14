from typing import List, Optional

import typer

from animelist import common
from animelist.anime import Status, AnimeTypes
from animelist.mycommands.addcommand import impl_add_command
from animelist.mycommands.listcommand import impl_list_command
from animelist.mycommands.removecommand import impl_remove_command
from animelist.mycommands.showcommand import impl_show_command
from animelist.mycommands.updatecommand import impl_update_command
from animelist.mycommands.watchcommand import impl_watch_command

# cli app object
app = typer.Typer()


@app.command("list")
def list_command(
        existing_genre: Optional[str] = typer.Option(None, "--genre", "-g", help="To filter your list by genre",
                                                     show_default=False),

        existing_status: Optional[Status] = typer.Option(None, "--status", "-st", help="To filter your list by status",
                                                         show_default=False, case_sensitive=False),

        existing_rating: Optional[str] = typer.Option(None, "--rating", "-r",
                                                      help="To filter your list by rating ([min]:[max])",
                                                      show_default=False),

        number: Optional[int] = typer.Option(None, "--number", "-n", help="To show the first n anime in your list",
                                             show_default=False)
) -> None:
    """To list all the anime in your list"""

    impl_list_command(existing_genre, existing_status, existing_rating, number, common.anime_list)


@app.command("show")
def show_command(
        existing_name: List[str] = typer.Argument(...)) -> None:
    """To show information about a specific media in your list"""

    impl_show_command(existing_name, common.anime_list)


@app.command("add")
def add_command(
        new_name: List[str] = typer.Argument(...),

        genre_flag: bool = typer.Option(False, "--genre", "-g", help="treat the value of the name as the genre",
                                        show_default=True)) -> None:
    """To add a new anime to your list"""

    impl_add_command(new_name, genre_flag, common.anime_list)


@app.command("remove")
def remove_command(
        existing_name: List[str] = typer.Argument(...),

        genre_flag: bool = typer.Option(False, "--genre", "-g", help="treat the value of the name as the genre",
                                        show_default=True)) -> None:
    """To remove an anime from your list"""

    impl_remove_command(existing_name, genre_flag, common.anime_list)


@app.command("update")
def update_command(
        existing_name: List[str] = typer.Argument(...),

        new_type: Optional[AnimeTypes] = typer.Option(None, "--type", "-t", help="a new type", show_default=False,
                                                      case_sensitive=False),

        new_name: Optional[List[str]] = typer.Option(None, "--name", "-n", help="a new name", show_default=False),

        new_genre: Optional[list[str]] = typer.Option(None, "--genre", "-g", help="a new genre", show_default=False),

        new_season: Optional[int] = typer.Option(None, "--season", "-s", help="a new season", show_default=False),

        new_episode: Optional[int] = typer.Option(None, "--episode", "-e", help="a new episode", show_default=False),

        new_status: Optional[Status] = typer.Option(None, "--status", "-st", help="a new status", show_default=False,
                                                    case_sensitive=False),

        new_rating: Optional[int] = typer.Option(None, "--rating", "-r", help="a new rating", show_default=False),
) -> None:
    """To update an anime of your list"""

    impl_update_command(existing_name, new_type, new_name, new_genre, new_season, new_episode, new_status, new_rating,
                        common.anime_list)


@app.command("watch")
def watch_command(
        existing_name: List[str] = typer.Argument(...),

        episode: int = typer.Option(1, "--episode", "-e", help="Number of anime episodes to watch",
                                    show_default=True)) -> None:
    """To watch an anime from your list"""

    impl_watch_command(existing_name, episode, common.anime_list)


if __name__ == "__main__":
    app()
