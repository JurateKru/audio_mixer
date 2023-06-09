from pygame import mixer
import PySimpleGUI as sg
import json
from backend import configure, play_sound, stop_sound

# READS .json CONFIG FILE AND RETURNS 2 LISTS [sound names with extension] [default button names by sound name]
with open('audio_info.json', 'r') as f:
    song_list, song_keys = json.load(f)

# TRACKS STATE OF VAR "playing" (True/False)
active_songs = []

def button(channel, index, event, playing):
    if not playing:
        channel_name = song_keys[event]
        play_sound(channel, index, song_list)
        window[event].Update(channel_name, button_color=('white', 'green'))
        active_songs.append(event)
    elif event == "configure":
        channel_name = song_keys[channel]
        window[channel].Update(channel_name, button_color=('white', 'black'))
    else:
        channel_name = song_keys[event]
        stop_sound(channel)
        window[event].Update(channel_name, button_color=('white', 'black'))
        active_songs.remove(event)

# SETS VAR "playing" BOOL STATE TO TRACK IF SOUND/BUTTON IS ON/OFF
def song_status(sound):
    if sound in active_songs:
        playing = True
    else: 
        playing = False
    return playing

# pygame mixer CLASS instance
mixer.init()

# LIST TO CREATE AND TRACK INDEX OF EACH SOUNDNAME
all_channels = []
for index, song in enumerate(song_keys):
    all_channels.append(index)

# SimpleGUI BUTTON LAYOUT (2x4) + BUTTON TO CALL CONFIGURATION WINDOW
layout = [    
    [sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button(song_keys[i], key=all_channels[i], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14), border_width=2) for i in range(0, 4)],
    [sg.Button(song_keys[i], key=all_channels[i], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14), border_width=2) for i in range(4, 8)],
    [sg.Button("Configure", key='configure', button_color=('black', 'grey'), size=(55, 1), font=('Helvetica', 12), border_width=3)]
]

# PySimpleGUI Window CLASS
window = sg.Window("Audio mixer", layout)

# DEFAULT BEGGINING VAR "playing" STATE FOR ALL BUTTONS
playing = False

while True:
    # CREATES MAIN WINDOW WITH BUTTONS, NAMES, ETC.
    event, values = window.read()
    # CHECKS FOR WINDOW CLOSED EVENT
    if event == sg.WIN_CLOSED:
        # AFTER WINDOW_CLOSED EVENT, WRITES UPDATED BUTTON NAMES TO JSON
        with open('audio_info.json', 'w') as f:
            json.dump([song_list, song_keys], f)
        break
    elif event == "configure":
        # OPENS CONFIG WINDOW, ASSIGNS USER CHOSEN BUTTON WITH USER WRITEN NEW BUTTON NAME
        choosen_channel, choosen_name = configure(all_channels)
        song_keys[choosen_channel] = choosen_name
        button(choosen_channel, choosen_channel, event, playing)
    else:
        # CHECKS BY INDEX WHICH BUTTON USER CLICKED
        for i in range(8):
            if event == all_channels[i]:
                playing = song_status(event)
                button(i, i, event, playing)

window.close()