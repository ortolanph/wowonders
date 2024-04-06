from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Header, ListView, ListItem, Label, Static, Footer


class LabelItem(ListItem):

    def __init__(self, value: str):
        super().__init__()
        self.value = value

    def compose(self) -> ComposeResult:
        yield Label(self.value)


def create_items(items) -> [LabelItem]:
    return list(map(lambda item: LabelItem(item), items))


class StagePanel(Widget):

    def __init__(self, stage_data):
        super().__init__()
        self.stage_data = stage_data

    def compose(self) -> ComposeResult:
        with Static("Stages", id="stages_pane"):
            yield Label("Stages")
            yield ListView(*create_items(self.stage_data), classes="lists")


class MyTUIApp(App):
    BINDINGS = [("x", "exit_app", "Exit Application")]
    TITLE = "WOW Answers Text Browser"
    CSS_PATH = "../../wow_tui_styles/wow_tui.css"
    stages = ["France - Paris", "Madrid - Spain", "Lisbon - Portugal"]

    def compose(self) -> ComposeResult:
        yield Header()
        yield StagePanel(self.stages)
        yield Label("None", id="information")
        yield Footer()

    def action_exit_app(self):
        self.app.exit()

    def on_list_view_selected(self, event: ListView.Selected):
        self.query_one("#information", Label).update(event.item.value)
