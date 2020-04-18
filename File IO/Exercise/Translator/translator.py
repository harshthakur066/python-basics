from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('input.txt', mode='r') as file:
        msg = file.read()
        translation = translator.translate(msg)
        print(translation)
        with open('output.txt', mode='w') as file2:
            # file2.write(translation)                 # bug in the package translate
            pass
except FileNotFoundError:
    print('something went wrong')
