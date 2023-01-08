from pathlib import Path
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
)
from controller import *
from gui.main_window.home.main import Home
from gui.main_window.selectservice.main import SelectService
from gui.main_window.about.main import About
from gui.main_window.signup.main import AddUsers
from .. import login

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def mainWindow():
    MainWindow()


class MainWindow(Toplevel):
    global user

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("SHORTPIX VISUAL EFFECTS")

        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        self.home_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.home_btn, "home"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.home_btn.place(x=7.0, y=133.0, width=208.0, height=47.0)

        button_image_2 = PhotoImage(file=relative_to_assets("button_4.png"))
        self.rooms_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.rooms_btn, "abt"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.rooms_btn.place(x=7.0, y=183.0, width=208.0, height=47.0)

        button_image_3 = PhotoImage(file=relative_to_assets("button_6.png"))
        self.guests_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.guests_btn, "service"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.guests_btn.place(x=7.0, y=233.0, width=208.0, height=47.0)

        button_image_4 = PhotoImage(file=relative_to_assets("button_2.png"))
        self.about_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.about_btn, "adduser"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.about_btn.place(x=7.0, y=283.0, width=208.0, height=47.0)

        button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.admin_login,
            relief="flat",
        )
        self.logout_btn.place(x=0.0, y=333.0, width=215.0, height=47.0)

        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="SHORTPIX",
            fill="#FFFFFF",
            font=("Montserrat Bold", 36 * -1),
        )

        self.canvas.create_text(
            341.0,
            213.0,
            anchor="nw",
            text="(The screens below",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        self.canvas.create_text(
            420.0,
            272.0,
            anchor="nw",
            text="will come here)",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        # Loop through windows and place them
        self.windows = {
            "home": Home(self),
            "abt": About(self),
            "service": SelectService(self),
            "adduser": AddUsers(self),
        }
        self.handle_btn_press(self.home_btn, "home")
        self.sidebar_indicator.place(x=0, y=133)
        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)
        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def admin_login(self):
        self.destroy()
        login.gui.loginWindow()

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set current Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

    def handle_dashboard_refresh(self):
        # Recreate the dash window
        self.windows["home"] = Home(self)
