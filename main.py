import time
import speech_recognition as sr
import pygame
import os

# Път към папката с песни
music_folder = "C:\\Users\\tkolo\\Desktop\\music"  # Заменете този път със своя собствен

# Инициализация на библиотеките
r = sr.Recognizer()
pygame.mixer.init()

def play_audio(file_name):
    file_path = os.path.join(music_folder, file_name)
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def rewind_audio(seconds):
    pos = pygame.mixer.music.get_pos()
    pygame.mixer.music.rewind()
    time.sleep(seconds)
    pygame.mixer.music.set_pos(pos)

# Главна функция
def main():
    while True:
        with sr.Microphone() as source:
            print("Изчакване на команда...")
            audio = r.listen(source)

        try:
            command = r.recognize_google(audio, language="bg-BG").lower()
            print("Разпозната команда: " + command)

            if "зареди" in command:
                # Пример: "Зареди песен1.mp3"
                file_name = command.split("зареди")[1].strip() +".mp3"
                play_audio(file_name)
            elif "готови" in command:
                # Пример: "Готови"
                play_audio()
            elif "стоп" in command:
                # Пример: "Стоп"
                stop_audio()
            elif "върни" in command:
                # Пример: "Върни 10 секунди назад"
                seconds = int(command.split("върни")[1].split("секунди назад")[0])
                rewind_audio(seconds)
        except sr.UnknownValueError:
            print("Гласовата команда не е разпозната.")
        except sr.RequestError as e:
            print("Грешка при изпращането на заявка към гласовия модул: {0}".format(e))

if __name__ == "__main__":
    main()
