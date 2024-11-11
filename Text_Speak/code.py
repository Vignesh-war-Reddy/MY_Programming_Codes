import pyttsx3
import nltk
from nltk.corpus import wordnet

# Ensure nltk data is downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')

class Speaking:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

class GFG:
    def __init__(self):
        self.speak = Speaking()

    def Dictionary(self):
        self.speak.speak("Which word do you want to find the meaning of, sir?")
        
        # Taking the string input
        query = str(input())
        synsets = wordnet.synsets(query)

        if not synsets:
            self.speak.speak("No meaning found.")
            print("No meaning found.")
            return

        for synset in synsets:
            meaning = f"The meaning of {query} as a {synset.pos()} is: {synset.definition()}"
            self.speak.speak(meaning)
            print(f"{synset.name()} ({synset.pos()}): {synset.definition()}")

if __name__ == '__main__':
    gfg = GFG()
    gfg.Dictionary()
