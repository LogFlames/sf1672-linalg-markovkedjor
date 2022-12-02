from gtts import gTTS

text = input("Säga: ")
tts = gTTS(text, lang="sv")

tts.save("text.mp3")
