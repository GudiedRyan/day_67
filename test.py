from main import morse_dict, MorseTranslator

def test_dict():
    assert morse_dict['a'] == '.-'

def test_string():
    morse = MorseTranslator()
    assert morse.translate(phrase='Hello there!') == '.... . .-.. .-.. --- / - .... . .-. . -.-.--'