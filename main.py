morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    ' ': '/'
}

class MorseTranslator:

    def __init__(self):
        self.dict = morse_dict
        self.string = None
        self.string_list = None
        self.morse_list = []
        self.morse_string = None
        
    def translate(self, phrase: str):
        self.string = phrase.lower()
        self.string_list = list(self.string)
        for char in self.string_list:
            morse_char = self.dict[char]
            self.morse_list.append(morse_char)
        self.morse_string = " ".join(self.morse_list)
        return self.morse_string
            
