from pygame import mixer
from time import sleep
import PySimpleGUI as sg
import os

song_list = os.listdir('./audio_samples')  # ['bass.mp3', 'hihat.mps3', 'kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snap.mp3', 'snare.mp3', 'sound.mp3']

song_list_no_ext = []
for song in song_list:
    name, ext = os.path.splitext(song)
    song_list_no_ext.append(name.upper())

# print(song_list_no_ext)
# exit()

def play_sound(channel:int, sound:int):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
    channel_n.play(sound, loops=-1)

def stop_sound(channel:int):
    channel_n = mixer.Channel(channel)
    channel_n.stop()

mixer.init()

layout = [
    [sg.Text('Audio Mixer', font=('Helvetica', 20))],
    [sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button(song_list_no_ext[0], key=song_list_no_ext[0], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[1], key=song_list_no_ext[1], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[2], key=song_list_no_ext[2], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[3], key=song_list_no_ext[3], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[4], key=song_list_no_ext[4], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[5], key=song_list_no_ext[5], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[6], key=song_list_no_ext[6], size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[7], key=song_list_no_ext[7], size=(10, 3), font=('Helvetica', 14))],
    [sg.Text('Stop playing:', font=('Helvetica', 12))],
    [sg.Button(song_list_no_ext[0], key='SOUND0', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[1], key='SOUND1', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[2], key='SOUND2', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[3], key='SOUND3', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[4], key='SOUND4', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[5], key='SOUND5', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[6], key='SOUND6', size=(10, 3), font=('Helvetica', 14)),
     sg.Button(song_list_no_ext[7], key='SOUND7', size=(10, 3), font=('Helvetica', 14))]
]

window = sg.Window("Audio mixer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == song_list_no_ext[0]:
        play_sound(0, 0)
    elif event == song_list_no_ext[1]:
        play_sound(1, 1)
    elif event == song_list_no_ext[2]:
        play_sound(2, 2)
    elif event == song_list_no_ext[3]:
        play_sound(3, 3)
    elif event == song_list_no_ext[4]:
        play_sound(4, 4)
    elif event == song_list_no_ext[5]:
        play_sound(5, 5)
    elif event == song_list_no_ext[6]:
        play_sound(6, 6)
    elif event == song_list_no_ext[7]:
        play_sound(7, 7)
    elif event == 'SOUND0':
        stop_sound(0)
    elif event == 'SOUND2':
        stop_sound(1)
    elif event == 'SOUND1':    
        stop_sound(2)
    elif event == 'SOUND3':    
        stop_sound(3)
    elif event == 'SOUND4':    
        stop_sound(4)
    elif event == 'SOUND5':    
        stop_sound(5)
    elif event == 'SOUND6':    
        stop_sound(6)
    elif event == 'SOUND7':    
        stop_sound(7)

window.close()
