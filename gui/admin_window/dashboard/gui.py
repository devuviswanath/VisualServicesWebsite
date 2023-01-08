from pathlib import Path
import numpy as np
from tkinter.constants import ANCHOR, N
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Frame, Canvas, Entry, PhotoImage, Button, N
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def dashboard():
    Dashboard()


class Dashboard(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        canvas.place(x=0, y=0)
        canvas.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(115.0, 81.0, image=canvas.entry_image_1)
        entry_1 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_1.place(x=55.0, y=30.0 + 2, width=120.0, height=0)

        canvas.create_text(
            56.0,
            45.0,
            anchor="nw",
            text="Total users",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        # Users Text
        canvas.create_text(
            164.0,
            63.0,
            anchor="ne",
            text=db_controller.users(),
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
            justify="right",
        )

        canvas.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(299.0, 81.0, image=canvas.entry_image_2)
        entry_2 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_2.place(x=239.0, y=30.0 + 2, width=120.0, height=0)

        canvas.create_text(
            240.0,
            45.0,
            anchor="nw",
            text="Users for services",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        canvas.create_text(
            346.0,
            63.0,
            anchor="ne",
            text=db_controller.services(),
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
            justify="right",
        )

        canvas.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = canvas.create_image(177.0, 286.0, image=canvas.entry_image_3)
        entry_3 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_3.place(x=55.0, y=175.0 + 2, width=244.0, height=0)

        canvas.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = canvas.create_image(481.0, 286.0, image=canvas.entry_image_4)
        entry_4 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_4.place(x=358.0, y=175.0 + 2, width=246.0, height=0)

        canvas.entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
        entry_bg_7 = canvas.create_image(483.0, 81.0, image=canvas.entry_image_7)
        entry_7 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_7.place(x=423.0, y=30.0 + 2, width=120.0, height=0)

        canvas.create_text(
            424.0,
            45.0,
            anchor="nw",
            text="No of admins",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        canvas.create_text(
            540.0,
            63.0,
            anchor="ne",
            text=db_controller.admins(),
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        canvas.entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
        entry_bg_9 = canvas.create_image(391.0, 150.0, image=canvas.entry_image_9)
        entry_9 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 150),
        )
        entry_9.place(x=41.0, y=149.0 + 2, width=700.0, height=0)

        canvas.create_text(
            56.0,
            191.0,
            anchor="nw",
            text="Service - By Type",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        canvas.create_text(
            56.0,
            230.0,
            anchor="nw",
            text="Click on show button below to see graph",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_graphs_service,
            relief="flat",
        )
        button_1.place(x=56.0, y=322.0, width=190.0, height=48.0)

        canvas.create_text(
            359.0,
            191.0,
            anchor="nw",
            text="Users - By City",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        canvas.create_text(
            359.0,
            223.0,
            anchor="nw",
            text="Click on show button below to see graph",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_graphs_users,
            relief="flat",
        )
        button_2.place(x=359.0, y=322.0, width=190.0, height=48.0)

    def show_graphs_service(self):
        # creating data set
        service_types = db_controller.get_unique_services()
        service_type = []
        service_number = []
        for i in service_types:
            service_type.append(i[0])
        for i in service_type:
            service_number.append(db_controller.get_services_count(i))
        # Creating explode data
        explode = (0.1, 0.0)
        # Creating color parameters
        colors = ("orange", "cyan", "brown",
                  "grey", "indigo", "beige")
        # Wedge properties
        wp = {'linewidth': 1, 'edgecolor': "green"}

        # Creating autocpt arguments
        def func(pct, allvalues):
            absolute = int(pct / 100. * np.sum(allvalues))
            return "{:.1f}%\n({:d} )".format(pct, absolute)
        # Creating plot
        fig, ax = plt.subplots(figsize=(10, 7))
        wedges, texts, autotexts = ax.pie(service_number,
                                          autopct=lambda pct: func(pct, service_number),
                                          explode=explode,
                                          labels=service_type,
                                          shadow=True,
                                          colors=colors,
                                          startangle=90,
                                          wedgeprops=wp,
                                          textprops=dict(color="black"))
        # Adding legend
        ax.legend(wedges, service_type,
                  title="Services",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(autotexts, size=8, weight="bold")
        ax.set_title("Services by type")
        # show plot
        plt.show()

    def show_graphs_users(self):
        # creating data set
        cities = db_controller.get_unique_cities()
        city = []
        users = []
        for i in cities:
            city.append(i[0])
        for i in city:
            users.append(db_controller.get_city_count(i))
        plt.style.use('Solarize_Light2')
        barplot = plt.bar(city, users)

        for bar in barplot:
            y_value = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2.0, y_value, int(y_value), va='bottom')

        plt.title("Users by City")
        plt.xlabel('City')
        plt.ylabel('Number of People')
        plt.show()

