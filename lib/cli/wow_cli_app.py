import typer

from lib.formatter.wow_cli_formatter import *
from lib.service.wow_service import WOWService

app = typer.Typer(rich_markup_mode="rich")


# Queries
# Find answers by level id
# get_stages_by_country
# get_stages_by_landmark
# search_stage
# search_levels_by_words

# Utils
# Export to JSON
# Export a level to PDF
# Export all levels to PDF

@app.command(
    help="Finds answers by level id with level and stage information",
    short_help="Finds answers by level id"
)
def find_answers_by_level(level_id: int):
    service = WOWService()

    level_data = service.load_level_data(level_id)
    level_answers = service.load_answers(level_id)

    print_level_header(level_data["level_info"]["level_id"], level_data["level_info"]["level_letters"])
    print_level_stage_info(level_data["stage_info"])
    print_level_answers(level_answers)
