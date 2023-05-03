from pygame import mixer
from time import sleep
import PySimpleGUI as sg
import os

song_list = os.listdir('./audio_samples')  # ['bass.mp3', 'hihat.mps3', 'kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snap.mp3', 'snare.mp3', 'sound.mp3']
# print(song_list)

song_list_no_ext = []
for song in song_list:
    name, _ = os.path.splitext(song)
    song_list_no_ext.append(name.upper())

print(song_list_no_ext)
# exit()

def play_sound(channel:int, sound:int):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
    channel_n.play(sound, loops=-1)

def stop_sound(channel:int):
    channel_n = mixer.Channel(channel)
    channel_n.stop()

def button(channel, index, event, playing):
    if not playing:
        play_sound(channel, index)
        window[event].Update(event, button_color=('white', 'green')) 
        playing = True
    else:
        stop_sound(channel)
        window[event].Update(event, button_color=('white', 'black')) 
        playing = False
    return playing

mixer.init()

layout = [
    [sg.Text('Audio Mixer', font=('Helvetica', 20))],
    [sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button(song_list_no_ext[0], key=song_list_no_ext[0], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[1], key=song_list_no_ext[1], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[2], key=song_list_no_ext[2], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[3], key=song_list_no_ext[3], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14))],
     [sg.Button(song_list_no_ext[4], key=song_list_no_ext[4], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[5], key=song_list_no_ext[5], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[6], key=song_list_no_ext[6], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[7], key=song_list_no_ext[7], button_color=('white', 'black'), size=(10, 3), font=('Helvetica', 14))],
    # [sg.Text('Stop playing:', font=('Helvetica', 12))],
    # [sg.Button(song_list_no_ext[0], key='SOUND0', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[1], key='SOUND1', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[2], key='SOUND2', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[3], key='SOUND3', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[4], key='SOUND4', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[5], key='SOUND5', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[6], key='SOUND6', size=(10, 3), font=('Helvetica', 14)),
    #  sg.Button(song_list_no_ext[7], key='SOUND7', size=(10, 3), font=('Helvetica', 14))]
]

window = sg.Window("Audio mixer", layout)

playing = False

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == song_list_no_ext[0]:
        playing = button(0, 0, event, playing)
    elif event == song_list_no_ext[1]:
        playing = button(1, 1, event, playing)
    elif event == song_list_no_ext[2]:
        playing = button(2, 2, event, playing)
    elif event == song_list_no_ext[3]:
        playing = button(3, 3, event, playing)
    elif event == song_list_no_ext[4]:
        playing = button(4, 4, event, playing)
    elif event == song_list_no_ext[5]:
        playing = button(5, 5, event, playing)
    elif event == song_list_no_ext[6]:
        playing = button(6, 6, event, playing)
    elif event == song_list_no_ext[7]:
        playing = button(7, 7, event, playing)

window.close()
