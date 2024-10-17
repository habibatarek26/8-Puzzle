from customtkinter import *
import customtkinter as ctk


def show_board(app, frame_side_length, padding, initial_state=None):
    entries = []

    for row in range(3):
        for col in range(3):
            frame = CTkFrame(master=app,
                             width=frame_side_length,
                             height=frame_side_length,
                             corner_radius=0,
                             fg_color="#f78a53")

            frame.place(relx=0.395 + row * (padding / 800), rely=0.375 + col * (padding / 600))

    for row in range(3):
        for col in range(3):
            frame = CTkFrame(master=app,
                             width=frame_side_length,
                             height=frame_side_length,
                             corner_radius=0,
                             fg_color="#ffd23f")

            frame.place(relx=0.4 + row * (padding / 800), rely=0.38 + col * (padding / 600))

            if initial_state is None:
                entry = CTkEntry(master=frame,
                                 width=frame_side_length,
                                 height=frame_side_length,
                                 font=("Digital-7 Mono", 28, "bold"),
                                 text_color="#f3fcf0",
                                 border_color="#ffd23f",
                                 fg_color="#ffd23f")
                entry.place(relx=0.5, rely=0.5, anchor="center")

                entries.append(entry)
            else:
                entry = CTkLabel(master=frame,
                                 width=frame_side_length,
                                 height=frame_side_length,
                                 font=("Digital-7 Mono", 28, "bold"),
                                 text=f"{initial_state[col][row]}",
                                 text_color="#f3fcf0",
                                 fg_color="#ffd23f")
                entry.place(relx=0.5, rely=0.5, anchor="center")

    return entries


def is_valid(initial_state, algorithm):

    #TBC
    if algorithm:
        return True

    return False


def btn_event(app, algorithm, entries):
    initial_state = []
    for entry in entries:
        value = entry.get()
        initial_state.append(value)

    if is_valid(initial_state, algorithm):
        title = ctk.CTkFrame(master=app,
                             height=50,
                             width=800,
                             fg_color="#540d6e")

        title.place(relx=0.5225, rely=0.3, anchor="center")
        print(f"Initial State: {initial_state}")
        print(f"Algorithm selected: {algorithm}")

    else:
        title = ctk.CTkLabel(master=app,
                             text="Invalid Initial State",
                             text_color="red",
                             font=("Digital-7 Mono", 28, "bold"))
        title.place(relx=0.5225, rely=0.3, anchor="center")


def initiate_gui():
    app = CTk()

    app.geometry("800x600")
    app.configure(fg_color="#540d6e")

    title = ctk.CTkLabel(master=app, text="8 Puzzle AI Solver", font=("Digital-7 Mono", 28, "bold"))
    title.place(relx=0.5225, rely=0.075, anchor="center")

    option_algorithm = ctk.StringVar(value="")

    combobox = ctk.CTkComboBox(master=app,
                               width=200,
                               variable=option_algorithm,
                               values=["BFS", "DFS", "Iterative DFS", "A*"],
                               dropdown_font=("Digital-7 Mono", 18),
                               font=("Digital-7 Mono", 21, "bold"),
                               state="readonly")
    combobox.place(relx=0.5225, rely=0.15, anchor="center")

    frame_side_length = 50
    padding = 70

    entries = show_board(app, frame_side_length, padding)

    btn = ctk.CTkButton(master=app,
                        width=80,
                        height=35,
                        corner_radius=25,
                        fg_color="#ee4266",
                        border_color="#c7ef00",
                        hover_color="#a1286a",
                        text="Start",
                        font=("Digital-7 Mono", 20, "bold"),
                        command=lambda: btn_event(app, option_algorithm.get(), entries))
    btn.place(relx=0.5225, rely=0.22, anchor="center")

    app.mainloop()


initiate_gui()
