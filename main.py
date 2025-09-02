import pyautogui
import time
from playsound3 import playsound
import os

mvdIsDead = "./mvd_is_dead.png"
netZapisei = "./net_zapisei.png"
unauthImage = "./unauth.png"

sound1 = "preryivistyiy-zvuk.mp3"
sound2 = "smeh-pod-zvuk-gorna.mp3"
errSound = "error.mp3"

CONFIDENCE = 0.9
SLEEP_SECONDS = 10

def main():
    print("Сейчас начнется мониторинг. Нажмите на окно браузера.")
    time.sleep(2)

    print("Запущен мониторинг Госуслуг...")
    while True:
        try:
            pyautogui.press('f5')
            time.sleep(SLEEP_SECONDS)

            if unauth():
                break

            found = pyautogui.locateOnScreen(mvdIsDead, confidence=CONFIDENCE)
            if found:
                print(f"[{time.strftime('%H:%M:%S')}] Пока нет записей.")


        except pyautogui.ImageNotFoundException:
            print(f"[{time.strftime('%H:%M:%S')}] ЗАПИСИ ЕСТЬ! 🔔")
            playsound(sound1)
            playsound(sound2)
            break

        except Exception as e:
            print("Ошибка типа:", type(e).__name__)
            playsound(errSound)
            break

    return 0


def unauth() -> bool:
    try:
        found = pyautogui.locateOnScreen(unauthImage, confidence=CONFIDENCE)
        if found:
            playsound(errSound)
            print(f"[{time.strftime('%H:%M:%S')}] Необходимо авторизоваться")
            return True
        return False

    except pyautogui.ImageNotFoundException:
        # its ok
        return False


if __name__ == "__main__":
    main()

