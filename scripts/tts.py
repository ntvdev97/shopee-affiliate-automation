from gtts import gTTS

def generate_voice(text, output):
    tts = gTTS(text=text, lang='vi')
    tts.save(output)