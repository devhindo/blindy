from gtts import gTTS
import fitz

def pdf_to_string(pdf_path):
    doc = fitz.open(pdf_path)
    pdf_text = ''
    for page in doc:
        pdf_text += page.get_text()
    doc.close()
    return pdf_text

def pdf_to_mp3(pdf_path, mp3_path, lang='en', tld='co.uk'):
    mp3 = gTTS(text=pdf_to_string(pdf_path), lang=lang, tld='co.uk')
    mp3.save(mp3_path)