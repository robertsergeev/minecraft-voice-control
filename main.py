import keyboard
import time
import pyautogui
import speech_recognition as sr

recognizer = sr.Recognizer()
last_key = ""

commands = {
    "иди вперёд": lambda: press_key('W'),
    "иди назад": lambda: press_key('S'),
    "иди налево": lambda: press_key('A'),
    "иди направо": lambda: press_key('D'),
    "остановись": lambda: release_last_key(),
    "поверни направо": lambda: pyautogui.move(100, 0, 1),
    "поверни налево": lambda: pyautogui.move(-100, 0, 1),
    "прыжок": lambda: press_key(57, 0.1), 
    "удар": lambda: pyautogui.click(button='left'),
    "поставь блок": lambda: pyautogui.click(button='right'),
    "открой инвентарь": lambda: press_key('E', 0.1),
    "беги": lambda: press_key('left ctrl', 0.1), 
    "крадись": lambda: press_key('left shift', 0.1), 
    "съешь": lambda: press_key('right click', 0.5),  
    "используй предмет": lambda: pyautogui.click(button='right'), 
    "быстрый слот 1": lambda: press_key('1', 0.1),
    "быстрый слот 2": lambda: press_key('2', 0.1),
    "быстрый слот 3": lambda: press_key('3', 0.1),
    "быстрый слот 4": lambda: press_key('4', 0.1),
    "быстрый слот 5": lambda: press_key('5', 0.1),
    "быстрый слот 6": lambda: press_key('6', 0.1),
}

def press_key(key, delay=0):
    global last_key
    keyboard.press(key)
    if key in ['W', 'A', 'S', 'D']:
        last_key = key
    if delay > 0:
        time.sleep(delay)
        keyboard.release(key)

def release_last_key():
    global last_key
    if last_key:
        keyboard.release(last_key)
        last_key = ""

while True:
    with sr.Microphone(0, sample_rate=48000) as source:
        audio = recognizer.listen(source)
        print("Слушаю: ")

        try:
            text = recognizer.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + text)

            for command in commands:
                if command in text:
                    commands[command]()
                    break
                             
        
        except sr.UnknownValueError:
            print("Не удалось распознать речь!")
