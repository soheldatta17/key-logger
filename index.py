from pynput.keyboard import Listener
from collections import defaultdict

word_freq = defaultdict(int)
current_word = ""

def log_key(key):
    global current_word

    key = str(key).replace("'", "")
    if key == "Key.space" or key == "Key.enter":
        if current_word:
            word_freq[current_word] += 1
            current_word = ""
        print("\r", word_freq,"\n")
    elif key == "Key.backspace":
        current_word = current_word[:-1]
    elif len(key) == 1:
        current_word += key.lower()

    

with Listener(on_press=log_key) as listener:
    listener.join()
