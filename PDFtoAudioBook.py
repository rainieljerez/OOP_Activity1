import pyttsx3
from PyPDF2 import PdfReader


with open(r"C:\Users\CLienT\Downloads\orwellanimalfarm_TTS_READY2.pdf" , 'rb') as pdf_file:

    reader = PdfReader(pdf_file)
    number_of_pages = len(reader.pages)

    engine = pyttsx3.init()


    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    for i in range(min(70, number_of_pages)):
        page = reader.pages[i]
        page_content = page.extract_text()

        if page_content:
            print(f"Reading page {i+1}")
            engine.say(page_content)


            engine.save_to_file(page_content, f'pdf_audio_page_{i+1}.mp3')

    engine.runAndWait()
    engine.stop()