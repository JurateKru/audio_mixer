from pygame import mixer
from time import sleep
import PySimpleGUI as sg
import os

song_list = os.listdir('./audio_samples')  # ['kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snare.mp3']
# print(song_list)
# exit()

def play_sound(channel:int, sound:int, frequency:float):
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
    channel_n.play(sound, loops=-1)
    sleep(frequency)

def stop_sound(channel:int):
    channel_n = mixer.Channel(channel)
    channel_n.stop()

mixer.init()
shaker = mixer.Sound('shaker.mp3')
kick = mixer.Sound('kick.mp3')

layout = [
    [sg.Text('Audio Mixer', font=('Helvetica', 20))],
    [sg.Text('Select an audio to play:', font=('Helvetica', 12))],
    [sg.Button('Kick', key='kick', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Shaker', key='shaker', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('World Wide', key='world_wide', size=(10, 3), font=('Helvetica', 14))],
    [sg.Text('Stop playing:', font=('Helvetica', 12))],
    [sg.Button('Kick', key='stop_kick', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('Shaker', key='stop_shaker', size=(10, 3), font=('Helvetica', 14)),
     sg.Button('World Wide', key='stop_world_wide', size=(10, 3), font=('Helvetica', 14))]
]

window = sg.Window("Audio mixer", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'kick':
        play_sound(1, 0, 1)
    elif event == 'world_wide':
        play_sound(2, 1, 1)
    elif event == 'shaker':
        play_sound(3, 2, 1)
    elif event == 'stop_kick':
        stop_sound(1)
    elif event == 'stop_world_wide':
        stop_sound(2)
    elif event == 'stop_shaker':    
        stop_sound(3)

window.close()