import os
import sys

from rich.console import RenderableType
from rich.traceback import Traceback
from rich.syntax import Syntax
from rich.panel import Panel

from textual.widgets import Placeholder, Header, Footer, FileClick, ScrollView, DirectoryTree
from textual.reactive import Reactive
from textual.widget import Widget
from textual.app import App


class ColorChanger(App):
    def on_key(self, event):
        if event.key.isdigit():
            self.background = f"on color({event.key})"


class SimpleApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), Placeholder(), edge="top")


class Hover(Widget):
    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello [b]World[/b]", style="on red" if self.mouse_over else "")

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class HoverApp(App):
    async def on_mount(self) -> None:
        hovers = (Hover() for _ in range(10))
        await self.view.dock(*hovers, edge="top")


class Quitter(App):
    async def on_load(self, event):
        await self.bind("q", "quit")


class Colorized(App):
    async def on_load(self, event):
        await self.bind("q", "quit")
        await self.bind("r", 'color("red")')
        await self.bind("b", 'color("blue")')
        await self.bind("g", 'color("green")')

    async def action_color(self, color: str):
        self.background = f"on {color}"


class SmoothApp(App):
    async def on_load(self) -> None:
        await self.bind('b', 'toggle_sidebar', 'Toggle sidebar')
        await self.bind("q", "quit", 'Quit')

    show_bar = Reactive(False)

    def watch_show_bar(self, show_bar:bool):
        self.bar.animate('layout_offset_x', 0 if show_bar else -40)

    def action_toggle_sidebar(self) -> None:
        self.show_bar = not self.show_bar

    async def on_mount(self) -> None:
        footer = Footer()
        self.bar = Placeholder(name='left')

        await self.view.dock(footer, edge='bottom')
        await self.view.dock(Placeholder(), Placeholder(), edge="top")
        await self.view.dock(self.bar, edge="left", size=40, z=1)

        self.bar.layout_offset_x = -40


class MyApp(App):
    async def on_load(self) -> None:
        """Sent before going in to application mode"""

        # Bind the keybindings
        await self.bind('b', 'view.toggle("sidebar")', 'Toggle sidebar')
        await self.bind("q", "quit", 'Quit')
        await self.bind("j", "key_up", 'Move up')
        await self.bind("k", "key_down", 'Move down')

        # Get the path to show
        try:
            self.path = sys.argv[1]
        except IndexError:
            self.path = os.path.abspath(
                os.path.join(os.path.basename(__file__), "../../")
            )

    async def on_mount(self) -> None:
        """Call after terminal goes into application mode"""

        # Create widgets
        # In this a scroll view for the code and directory tree
        self.body = ScrollView()
        self.directory = DirectoryTree(self.path, 'code')

        # Dock widgets
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        # Note the directory is also in a scroll view
        await self.view.dock(
            ScrollView(self.directory),
            edge="left",
            size=48,
            name='sidebar'
        )
        await self.view.dock(self.body, edge='top')

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked"""
        syntax: RenderableType
        try:
            # Construct a syntax object for the path in the message
            syntax = Syntax.from_path(
                message.path,
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme='dracula'
            )
        except Exception:
            # The file might be a binary file
            # So raise the error
            syntax = Traceback(theme='dracula', width=None, show_locals=True)
        self.app.sub_title = os.path.basename(message.path)
        await self.body.update(syntax)
    
    
# ColorChanger.run(log='textual.log')
# SimpleApp.run(log='textual.log')
# HoverApp.run(log='textual.log')
# Quitter.run(log='textual.log')
# Colorized.run(log='textual.log')
# SmoothApp.run(log='textual.log')
MyApp.run(title='Code Viewer', log='textual.log')
