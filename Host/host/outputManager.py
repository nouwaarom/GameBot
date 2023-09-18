from pyflite import PyFlite

class OutputManager:

    def __init__(self, withVoice):
        self.withVoice = withVoice
        self.voice = "awb"

        if withVoice:
            self.pf = PyFlite()

    def say(self, message):

        if self.withVoice:
            self.pf.text2speech(message, self.voice)
        else:
            print message

