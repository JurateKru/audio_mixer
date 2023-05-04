from pygame import mixer
import PySimpleGUI as sg
import os
import json
from window2 import configure
song_list = os.listdir('./audio_samples')  # ['bass.mp3', 'hihat.mps3', 'kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snap.mp3', 'snare.mp3', 'sound.mp3']
song_keys = []
for song in song_list:
    name, _ = os.path.splitext(song)
    song_keys.append(name.upper())

audio_info = {}

for i, song in enumerate(song_list):
    name, ext = os.path.splitext(song)
    audio_info[song_keys[i]] = {
        'filename': song,
        'directory': 'audio_samples',
        'button_name': song_keys[i],
        'button_location': (i % 4, i // 4) # Assumes a 4x2 layout
    }

with open('audio_info.json', 'w', encoding="utf-8") as f:
    json.dump(audio_info, f, indent=4)

with open('audio_info.json', 'r') as f:
    data = json.load(f)

song_keys = list(data.keys())

def play_sound(channel:int, sound:int):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
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
     [sg.Button("Go to configurator window", key='configure',button_color=('black', 'grey'), size=(55, 1), font=('Helvetica', 12), border_width=3)]
]

window = sg.Window("Audio mixer", layout)

playing = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "configure":  # TESTAVIMAS NAUJO LANGO
        new_button, new_name = configure(song_keys)
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
