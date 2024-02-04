"""
Class to hold and get audio files
"""


class Audio:

    def __init__(self):
        self.__bg_music = 'assets/audio/theme_forest.mp3'

    def get_bg_audio(self):
        return self.__bg_music


