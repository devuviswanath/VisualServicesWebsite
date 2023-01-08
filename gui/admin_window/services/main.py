from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *
import controller as db_controller

from .add_services.gui import AddServices
from .view_services.main import ViewServices
from .update_services.main import UpdateServices

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def services():
    Services()


class Services(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.services_data = db_controller.get_services()

        self.configure(bg="#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            "add": AddServices(self),
            "view": ViewServices(self),
            "edit": UpdateServices(self),
        }

        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=1013.0, height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0, height=506.0)

    def refresh_entries(self):
        self.reservation_data = db_controller.get_reservations()
        self.windows.get("view").handle_refresh()
