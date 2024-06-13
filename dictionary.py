import requests
import threading
import time
import os

'''
-----------------------------------------------------------------
|   BEFORE GOING ON:                                            |
|   - I KNOW MY CODE MAY LOOK BAD TO YOU BUT THIS IS MY         |
|   FIRST PROJECT ABOUT APIs AND MAY BE THIS WILL HELP ME       |
|   FAMILIAR WITH APIs FUNCTIONS, TASKS, ... IN PYTHON AND      |
|   IN OTHER PROGRAMMING LANGUAGES.                             |
|   - OH, AND ALSO THE THREADINGS TOO!                          |
|   - SORRY FOR MY BAD ENGLIH THOUGH                            |
|                               - MINEPLANT BITPYTH -           |
-----------------------------------------------------------------
'''

def R_Read(data):
    try:
        JsonConv = dict(eval(str(data[0])))
        print('Definition for {}'.format(JsonConv['word']).center(60, '-'))
        print('{:30}{:100}'.format('Word:', JsonConv['word']))
        try: print('{:30}{:100}'.format('Phonetic:', JsonConv['phonetic']))
        except KeyError: print("{:30}<Sorry! We don't have that phonetic now, so may be try again later>".format('Phonetic:'))
        print('Meanings:')
        for i1 in JsonConv['meanings']:
            for i, j in i1.items():
                if i == 'partOfSpeech': 
                    print('{:30}{:100}'.format('Part of speech:', str(j)))
                    print('----------------------------------------------------------')
                if i == "definitions":
                    for i3 in j:
                        for i2, j2 in i3.items():
                            if len(j2) > 0:
                                print('{:30}{:100}'.format(str(i2)+':', str(j2)))
                        print()
        print()
        print('----------------------------------------------------------')
        print('{:30}{:100}'.format("Link to the API:", "https://dictionaryapi.dev/"))
        print('{:30}{:100}'.format('Lisence Informations:', 'CC BY-SA 3.0 | URL: https://creativecommons.org/licenses/by-sa/3.0'))
        print('{:30}{:100}'.format('Source URL:', 'https://en.wiktionary.org/wiki/'+JsonConv['word']))
    except KeyError as E:
        if str(E) == '0' or str(E) == 'word':
            print('                                                                                          ') # That is for fixing the '\r' bug, I put this cuz I'm too lazy to fix it
            print("No Definitions Found")
            print("Sorry pal, we couldn't find definitions for the word you were looking for.")
            print("You can try the search again at later time or head to the web instead.")
        else:
            print('                                                                                          ')
            print("Nuh uh... You can't use my program right now...")
            print("Cuz my program is broken now, may be wait until I fix it or do it yourself")
            print('Thank you a lot !!!')
    except Exception:
        print('                                                                                          ')
        raise Exception

def GETVOCAB(word: str):
    URL = 'https://api.dictionaryapi.dev/api/v2/entries/en/'+word
    re = requests.get(url=URL)
    data = re.json()
    R_Read(data)

def load(mess: str):
    l = ['.', '..', '...', ' ..', '  .', '   ']
    for i in l:
        print(mess+i, end='\r') #The bug is here, and IDK how to fix that, But may be I'll find a sollution for it.
        time.sleep(0.25)

while True:
    print('                                                                              ')
    print('Type //cls to clear the screen, //exit to exit the program.')
    word = input("Enter a word: ").lower()
    if word == '//cls':
        os.system('cls')
    elif word == '//exit': exit()
    else:
        t1 = threading.Thread(target=GETVOCAB, args=(word,))
        t1.start()

        while t1.is_alive():
            load('Retrieving informations from api.dictionaryapi.dev')
