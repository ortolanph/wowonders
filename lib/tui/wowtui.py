from textual.app import App, ComposeResult
from textual.widgets import Header, ListView, ListItem, Label, Static, Footer

from lib.service.wow_service import WOWService


class LabelItem(ListItem):

    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def compose(self) -> ComposeResult:
        yield Label(self.value)


def create_items(items) -> [LabelItem]:
    return list(map(lambda item: LabelItem(item), items))


class StagePanel(Static):

    def __init__(self, stage_data):
        super().__init__()
        self.stage_data = stage_data

    def compose(self) -> ComposeResult:
        with Static("Stages", id="stages_panel"):
            yield Label(f"Stages - ({len(self.stage_data)})")
            yield ListView(*create_items(self.stage_data), classes="lists", id="stage_list")


class LevelPanel(Static):

    def __init__(self):
        super().__init__()

    def update_levels(self, levels_data):
        self.query_one("#level_list", ListView).clear()

        for level_data in levels_data:
            self.query_one("#level_list", ListView).append(LabelItem(level_data))

        self.query_one("#levels_label", Label).update(f"Levels ({len(levels_data)})")

    def compose(self) -> ComposeResult:
        with Static("Stages", id="levels_panel"):
            yield Label("Levels - No Items", id="levels_label")
            yield ListView(LabelItem("No Items"), classes="lists", id="level_list")


class AnswerPanel(Static):

    def __init__(self):
        super().__init__()

    def update_answers(self, answers):
        self.query_one("#answer_list", ListView).clear()

        for answer in answers:
            self.query_one("#answer_list", ListView).append(LabelItem(answer))

        self.query_one("#answers_label", Label).update(f"Answers ({len(answers)})")

    def compose(self) -> ComposeResult:
        with Static("Answers", id="answers_panel"):
            yield Label("Answers - No Answers", id="answers_label")
            yield ListView(LabelItem("No Answers"), classes="lists", id="answer_list")


class WOWTUIApp(App):
    BINDINGS = [("x", "exit_app", "Exit Application")]
    TITLE = "WOW Answers Text Browser"
    CSS_PATH = "../../wow_tui_styles/wow_tui.css"
    stages = []

    service = WOWService()
    stage_data = dict()
    level_data = dict()
    answer_data: [str] = []

    level_panel = LevelPanel()
    answer_panel = AnswerPanel()

    def __init__(self):
        super().__init__()
        self.stage_data = self.service.load_stage_data()
        self.stages = list(self.stage_data.keys())

    def compose(self) -> ComposeResult:
        yield Header()

        yield StagePanel(self.stages)
        yield self.level_panel
        yield self.answer_panel

        yield Footer()

    def action_exit_app(self):
        self.app.exit()

    def on_list_view_selected(self, event: ListView.Selected):
        if event.list_view.id == "stage_list":
            stage_name = event.item.value
            self.level_data = self.service.load_levels(self.stage_data[stage_name])
            self.level_panel.update_levels(list(self.level_data.keys()))

        if event.list_view.id == "level_list":
            level_name = event.item.value
            self.answer_data = self.service.load_answers(self.level_data[level_name])
            self.answer_panel.update_answers(self.answer_data)
