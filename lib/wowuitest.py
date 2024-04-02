from textual.app import App, ComposeResult
from tkinter import Label


class HelloWorld(App):
    def compose(self) -> ComposeResult:
        yield Label("Hello Textual")
