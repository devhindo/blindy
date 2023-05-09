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

def ls():
    for cmd in cmds.keys():
        print(cmd)

def quit():
    exit()

# actual program

cmds = {
    'pdf-to-mp3': pdf_to_mp3,
    'ls': ls,
    'exit': quit
}

while(True):
    cmd = input('Enter a command or (ls) for available commands: ')
    args = cmd.split()
    if args[0] in cmds:
        cmds[args[0]](*args[1:])
    else:
        print('Invalid command')
