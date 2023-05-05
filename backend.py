import PySimpleGUI as sg
from pygame import mixer

def configure(channel:int):
    """
    Description:
        Configuration window for letting user assign audio mixer button names
    
    Args:
        :param channel:            channel number passed in as index (integer)
        
    Reurns:
        choosen_channel as channel index (button position)
        choosen_name as user inputed new button name
    """
    layout2 = [
    [sg.Text('Choose button to change: ')],
    [sg.Combo(channel, key='buttons', enable_events=True, s=(50,70))],
    [sg.Text('Input sound name: ')],
    [sg.Input('Write here', key='button_name', enable_events=True,  s=(50,70))],
    [sg.Button('Done', key='exit', enable_events=True, size=(5, 1))]
     ]
    
    window = sg.Window("Audio mixer", layout2)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exit'):
            break
        # USER CHOOSEN BUTTON TO RENAME BY INDEX(CHANNEL ID IN THIS CASE)
        elif event == 'buttons':
            choosen_channel = values['buttons']
        # USER CHOOSEN NEW BUTTON NAME
        elif event == 'button_name':
            choosen_name = values['button_name']
    window.close()
    return choosen_channel, choosen_name

# CREATES CHANNEL OBJ, TARGETS SOUNDFILE, PLAYS SOUND INDEFINATELLY
def play_sound(channel:int, sound:int, song_list:list):
    """
    Description:
        Creates pygame module, mixer class object to be able to use up to 8 channels to play sound files in parallel
    Args:
        :param channel:             channel number passed in as index (integer)
        :sound:int:                 sound file number passed in as index (integer)
        :song_list:list:            sound files names list from directory
    """
    channel_n = mixer.Channel(channel)
    sound = mixer.Sound(f'audio_samples/{song_list[sound]}')
    channel_n.play(sound, loops=-1)

def stop_sound(channel:int):
    """
    Description:
        Stops currently playing sound
    Args:
        :param channel:             channel number passed in as index (integer)
    """
    channel_n = mixer.Channel(channel)
    channel_n.stop()

