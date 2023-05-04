from pygame import mixer
import PySimpleGUI as sg
import json
from window2 import configure

with open('audio_info.json', 'r') as f:
    song_list, song_keys = json.load(f)

def play_sound(channel:int, sound:int):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_keys[sound]}.mp3')
    channel_n.play(sound, loops=-1)

def stop_sound(channel:int):
    channel_n = mixer.Channel(channel)
    channel_n.stop()

active_songs = []
def button(channel, index, event, playing):
    if not playing:
        play_sound(channel, index)
        window[event].Update(event, button_color=('white', 'green')) 
        active_songs.append(event)
    else:
        stop_sound(channel)
        window[event].Update(event, button_color=('white', 'black')) 
        active_songs.remove(event)

def song_status(sound):
    if sound in active_songs:
        playing = True
    else: 
        playing = False
    return playing

mixer.init()

layout = [
[sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button(song_keys[0], key=song_keys[0], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[1], key=song_keys[1], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[2], key=song_keys[2], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[3], key=song_keys[3], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2)],
     [sg.Button(song_keys[4], key=song_keys[4], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[5], key=song_keys[5], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[6], key=song_keys[6], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2),
     sg.Button(song_keys[7], key=song_keys[7], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14),border_width=2)],
     [sg.Button("Go to configurator window", key='configure', button_color=('black', 'grey'), size=(55, 1), font=('Helvetica', 12), border_width=3)]
]

window = sg.Window("Audio mixer", layout)

playing = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        with open('audio_info.json', 'w') as f:
            json.dump([song_list, song_keys], f)
        break
    elif event == "configure":  # TESTAVIMAS NAUJO LANGO
        choosen_button, choosen_name = configure(song_keys)
        song_keys[choosen_button] = choosen_name
    elif event == song_keys[0]:
        playing = song_status(event)
        button(0, 0, event, playing)
    elif event == song_keys[1]:
        playing = song_status(event)
        button(1, 1, event, playing)
    elif event == song_keys[2]:
        playing = song_status(event)
        button(2, 2, event, playing)
    elif event == song_keys[3]:
        playing = song_status(event)
        button(3, 3, event, playing)
    elif event == song_keys[4]:
        playing = song_status(event)
        button(4, 4, event, playing)
    elif event == song_keys[5]:
        playing = song_status(event)
        button(5, 5, event, playing)
    elif event == song_keys[6]:
        playing = song_status(event)
        button(6, 6, event, playing)
    elif event == song_keys[7]:
        playing = song_status(event)
        button(7, 7, event, playing)

window.close()
