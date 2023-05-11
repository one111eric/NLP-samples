import spacy
from spacy import displacy
import sys


nlp = spacy.load('en_core_web_trf')

def start():
    while True:
        try:
            user_input = input()
            doc = nlp(user_input)

            for word in doc.ents:
                print(word.text,word.label_)
            
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            return

start()