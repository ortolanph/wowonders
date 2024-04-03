from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class WOWUI(App):
    TITLE = "WOW Answers"
    SUB_TITLE = "WOW Answers Catalog"
    CSS_PATH = "../style/wowui.tcss"
    BINDINGS = [("x", "exit", "Exit")]

    @property
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("bla", classes="stages")
        yield Footer()

    def action_exit(self):
        self.app.exit()
