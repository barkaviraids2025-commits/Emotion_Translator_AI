# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text
def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["happy", "joy", "excited", "great"]):
        return "😊 Happy"
    elif any(word in text for word in ["sad", "unhappy", "cry", "depressed"]):
        return "😢 Sad"
    elif any(word in text for word in ["angry", "mad", "furious"]):
        return "😡 Angry"
    elif any(word in text for word in ["fear", "scared", "afraid"]):
        return "😨 Fear"
    else:
        return "😐 Neutral"

def translate_text(text, target_lang = "ta"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client":"gtx",
        "sl":"en",
        "tl":target_lang,
        "dt":"t",
        "q":text
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[0][0][0]
    except Exception as e:
        return f"Translation failed: {e}"
if __name__ == "__main__":
    while True:
        print("\nChoose target language:")
        print("1. Tamil")
        print("2. Hindi")
        print("3. French")
        print("4. Spanish")
        print("5. Japanese")
        print("6. Chinese")
        print("7. German")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == "8":
            print("Exiting program. Bye!")
            break

        lang_map = {
            "1": "ta",
            "2": "hi",
            "3": "fr",
            "4": "es",
            "5": "ja",
            "6": "zh-CN",
            "7": "de"
        }

        target_lang = lang_map.get(choice, "ta")

        text = input("Enter text to translate: ")
        text = clean_text(text)
        emotion = detect_emotion(text)
        print("Detected Emotion:", emotion)

        translated = translate_text(text, target_lang)
        print("Translated text:", translated)
    
