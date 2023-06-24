import speech_recognition as sr

def wavToString(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='ja-JP')
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "あ"
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "あ"
