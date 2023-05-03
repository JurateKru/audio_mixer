from pygame import mixer
from time import sleep
import PySimpleGUI as sg
import os

song_list = os.listdir('./audio_samples')  # ['bass.mp3', 'hihat.mps3', 'kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snap.mp3', 'snare.mp3', 'sound.mp3']
# print(song_list)
# exit()

def play_sound(channel:int, sound:int):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
    channel_n.play(sound, loops=-1)
    # sleep(frequency)

def stop_sound(channel:int):
    channel_n = mixer.Channel(channel)
    channel_n.stop()

mixer.init()

layout = [
    [sg.Text('Audio Mixer', font=('Helvetica', 20))],
    [sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button('Kick', key='kick', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Shaker', key='shaker', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('World Wide', key='mr_world', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Bass', key='bass', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Hihat', key='hihat', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Snap', key='snap', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Snare', key='snare', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Sound', key='sound', size=(10, 3), font=('Helvetica', 14))],
    [sg.Text('Stop playing:', font=('Helvetica', 12))],
    [sg.Button('Kick', key='stop_kick', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Shaker', key='stop_shaker', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('World Wide', key='stop_mr_world', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Bass', key='stop_bass', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Hihat', key='stop_hihat', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Snap', key='stop_snap', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Snare', key='stop_snare', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Sound', key='stop_sound', size=(10, 3), font=('Helvetica', 14))]
]

window = sg.Window("Audio mixer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'kick':
        play_sound(0, 2)
    elif event == 'mr_world':
        play_sound(1, 3)
    elif event == 'shaker':
        play_sound(2, 4)
    elif event == 'bass':
        play_sound(3, 0)
    elif event == 'hihat':
        play_sound(4, 1)
    elif event == 'snap':
        play_sound(5, 5)
    elif event == 'snare':
        play_sound(6, 6)
    elif event == 'sound':
        play_sound(7, 7)
    elif event == 'stop_kick':
        stop_sound(0)
    elif event == 'stop_mr_world':
        stop_sound(1)
    elif event == 'stop_shaker':    
        stop_sound(2)
    elif event == 'stop_bass':    
        stop_sound(3)
    elif event == 'stop_hihat':    
        stop_sound(4)
    elif event == 'stop_snap':    
        stop_sound(5)
    elif event == 'stop_snare':    
        stop_sound(6)
    elif event == 'stop_sound':    
        stop_sound(7)

window.close()
