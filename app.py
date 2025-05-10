import tkinter as tk
from tkinter import StringVar
import ttkbootstrap as ttk


def Story1():
    def final(tl, name, sports, city, playername, drinkname, snacks):
        text = f'''
        One day me and my friend {name} decided to play a {sports} game in {city}.
        We wanted to watch {playername}.
        We drank {drinkname} and also ate some {snacks}.
        We really enjoyed! We are looking forward to going again and enjoy.'''

        tl.geometry('500x550')
        ttk.Label(tl, text='Story:', wraplength=tl.winfo_width(), font=('Helvetica', 14, 'bold')).place(x=160, y=310)
        ttk.Label(tl, text=text, wraplength=tl.winfo_width(), font=('Helvetica', 12)).place(x=0, y=330)

    NewScreen = tk.Toplevel(bg='#f9f9f9')
    NewScreen.title("A memorable day")
    NewScreen.geometry('500x500')
    ttk.Label(NewScreen, text='Memorable Day', font=('Helvetica', 16, 'bold')).place(x=170, y=20)
    ttk.Label(NewScreen, text='Name:', font=('Helvetica', 12)).place(x=10, y=70)
    ttk.Label(NewScreen, text='Enter a game:', font=('Helvetica', 12)).place(x=10, y=110)
    ttk.Label(NewScreen, text='Enter a city:', font=('Helvetica', 12)).place(x=10, y=150)
    ttk.Label(NewScreen, text='Enter the name of a player:', font=('Helvetica', 12)).place(x=10, y=190)
    ttk.Label(NewScreen, text='Enter the name of a drink:', font=('Helvetica', 12)).place(x=10, y=230)
    ttk.Label(NewScreen, text='Enter the name of a snack:', font=('Helvetica', 12)).place(x=10, y=270)

    Name = ttk.Entry(NewScreen, width=25)
    Name.place(x=250, y=70)
    game = ttk.Entry(NewScreen, width=25)
    game.place(x=250, y=110)
    city = ttk.Entry(NewScreen, width=25)
    city.place(x=250, y=150)
    player = ttk.Entry(NewScreen, width=25)
    player.place(x=250, y=190)
    drink = ttk.Entry(NewScreen, width=25)
    drink.place(x=250, y=230)
    snack = ttk.Entry(NewScreen, width=25)
    snack.place(x=250, y=270)

    SubmitButton = ttk.Button(NewScreen, text="Submit", style="success",
                              command=lambda: final(NewScreen, Name.get(), game.get(), city.get(), player.get(),
                                                    drink.get(), snack.get()))
    SubmitButton.place(x=200, y=320)

    NewScreen.mainloop()


def Story2():
    def final(tl, profession, place, sound, feeling, animal, super_emotion, action_word):
        text = f'''
        My friend, who is also a {profession}, decided that we should go to {place} this weekend.\n
        I got a {feeling} feeling hearing about this but still decided to go with him. As soon \n
        as we reached {place}, I heard a {sound} nearby. He casually said it might just be a {animal}\n
        they are common here. I got {super_emotion} hearing this, and I said, "I think we should {action_word} now."'''

        tl.geometry('500x550')
        ttk.Label(tl, text='Story:', wraplength=tl.winfo_width(), font=('Helvetica', 14, 'bold')).place(x=160, y=310)
        ttk.Label(tl, text=text, wraplength=tl.winfo_width(), font=('Helvetica', 12)).place(x=0, y=330)

    NewScreen = tk.Toplevel(bg='#f9f9f9')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')
    ttk.Label(NewScreen, text='Ambitions', font=('Helvetica', 16, 'bold')).place(x=170, y=20)
    ttk.Label(NewScreen, text='Enter a profession:', font=('Helvetica', 12)).place(x=10, y=70)
    ttk.Label(NewScreen, text='Enter a place:', font=('Helvetica', 12)).place(x=10, y=110)
    ttk.Label(NewScreen, text='Enter a sound:', font=('Helvetica', 12)).place(x=10, y=150)
    ttk.Label(NewScreen, text='Enter a feeling:', font=('Helvetica', 12)).place(x=10, y=190)
    ttk.Label(NewScreen, text='Enter an animal name:', font=('Helvetica', 12)).place(x=10, y=230)
    ttk.Label(NewScreen, text='Enter a superlative degree of emotion:', font=('Helvetica', 12)).place(x=10, y=270)
    ttk.Label(NewScreen, text='Enter a verb:', font=('Helvetica', 12)).place(x=10, y=310)

    profession = StringVar()
    place = StringVar()
    sound = StringVar()
    feeling = StringVar()
    animal = StringVar()
    super_emotion = StringVar()
    action_word = StringVar()

    Profession = ttk.Entry(NewScreen, width=25, textvariable=profession)
    Profession.place(x=250, y=70)
    Place = ttk.Entry(NewScreen, width=25, textvariable=place)
    Place.place(x=250, y=110)
    Sound = ttk.Entry(NewScreen, width=25, textvariable=sound)
    Sound.place(x=250, y=150)
    Feeling = ttk.Entry(NewScreen, width=25, textvariable=feeling)
    Feeling.place(x=250, y=190)
    Animal = ttk.Entry(NewScreen, width=25, textvariable=animal)
    Animal.place(x=250, y=230)
    SuperEmotion = ttk.Entry(NewScreen, width=25, textvariable=super_emotion)
    SuperEmotion.place(x=250, y=270)
    Verb = ttk.Entry(NewScreen, width=25, textvariable=action_word)
    Verb.place(x=250, y=310)

    SubmitButton = ttk.Button(NewScreen, text="Submit", style="success",
                              command=lambda: final(NewScreen, profession.get(), place.get(), sound.get(),
                                                    feeling.get(), animal.get(), super_emotion.get(),
                                                    action_word.get()))
    SubmitButton.place(x=200, y=360)

    NewScreen.mainloop()


Screen = tk.Tk()
Screen.title("Bhoomik Mad Libs Generator")
Screen.geometry('400x300')
Screen.maxsize(1200, 900)
Screen.minsize(400, 300)
Screen.config(bg="#ffefd5")
ttk.Label(Screen, text='PythonGeeks Mad Libs Generator', font=('Helvetica', 16, 'bold')).place(x=80, y=20)

# Creating buttons
Story1Button = ttk.Button(Screen, text='A memorable day', style="primary", command=Story1)
Story1Button.place(x=150, y=90)
Story2Button = ttk.Button(Screen, text='Ambitions', style="primary", command=Story2)
Story2Button.place(x=160, y=150)

Screen.mainloop()

