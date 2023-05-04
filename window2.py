import PySimpleGUI as sg

def configure(sound_list):
    layout2 = [
    [sg.Text('Choose button to change: ')],
    [sg.Combo(sound_list, key='buttons', enable_events=True, s=(50,70))],
    [sg.Text('Input sound name: ')],
    [sg.Input('Write here', key='button_name', enable_events=True,  s=(50,70))],
    [sg.Button('Done', key='exit', enable_events=True, size=(5, 1))]
     ]
    
    window = sg.Window("Audio mixer", layout2)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'exit'):
            break
        elif event == 'buttons':
            choosen_sound = values['buttons']
        elif event == 'button_name':
            choosen_name = values['button_name']
    
    window.close()
    return choosen_sound, choosen_name
        
