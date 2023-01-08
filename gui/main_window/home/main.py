from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def home():
    Home()


class Home(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            80.0,
            30.0,
            anchor="nw",
            text="WE PROVIDE VISUAL EFFECTS SERVICES",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("ed1.png"))
        image_2 = self.canvas.create_image(350.0, 250.0, image=self.image_image_2)

        self.canvas.create_text(
            197.0,
            370.0,
            anchor="nw",
            text="© 2021-22 Shortpix ltd, All rights reserved",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            80.0,
            80.0,
            anchor="nw",
            text="Shortpix develops high quality, visual effects for advertising agencies,",
            fill="#777777",
            font=("Montserrat Medium", 18 * -1),
        )

        self.canvas.create_text(
            120.0,
            107.0,
            anchor="nw",
            text="videographers, film studios and many more businesses.",
            fill="#777777",
            font=("Montserrat Medium", 18 * -1),
        )
