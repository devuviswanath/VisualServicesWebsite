from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()


class About(Frame):
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
            36.0,
            43.0,
            anchor="nw",
            text="OUR SERVICES INCLUDES THE FOLLOWING",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(203.0, 205.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(565.0, 205.0, image=self.image_image_3)

        self.canvas.create_text(
            56.0,
            138.0,
            anchor="nw",
            text="MOTION GRAPHICS",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0,
            138.0,
            anchor="nw",
            text="MATTE PAINTING",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_rectangle(
            56.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_rectangle(
            418.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_text(
            197.0,
            352.0,
            anchor="nw",
            text="© 2021-22 Shortpix ltd, All rights reserved",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            418.0,
            207.0,
            anchor="nw",
            text="Our matte- painting team has",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            223.0,
            anchor="nw",
            text="trained professionals who implements ",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            239.0,
            anchor="nw",
            text="various techniques to combine ",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            255.0,
            anchor="nw",
            text="a matte-painted image with live-action footage.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            207.0,
            anchor="nw",
            text="We have an excellent team in",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            223.0,
            anchor="nw",
            text="the field of motion graphics.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            239.0,
            anchor="nw",
            text="they create the illusion of motion or rotation,",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            255.0,
            anchor="nw",
            text=" and are usually use in multimedia projects.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
