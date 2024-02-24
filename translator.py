from translate import Translator
translator = Translator(to_lang='es')

try:
    with open('translate.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        with open('translate_3.txt', mode='a') as file2:
            file2.write(translation)
except FileNotFoundError:
    print("file not found")



