import json
import os

song_list = os.listdir('./audio_samples')  # ['bass.mp3', 'hihat.mps3', 'kick.mp3', 'mr_world.mp3', 'shaker.mp3', 'snap.mp3', 'snare.mp3', 'sound.mp3']

song_keys = []
for song in song_list:
    name, _ = os.path.splitext(song)
    song_keys.append(name.upper())

config = [song_list, song_keys]
with open('audio_info.json', 'w', encoding="utf-8") as f:
    json.dump(config, f, indent=4)