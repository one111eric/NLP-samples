from transformers import pipeline
import sys

nlp = pipeline(task='sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

def start():
    while True:
        try:
            user_input = input()
            result = nlp(user_input)

            print(result)   
            
        except KeyboardInterrupt:
            sys.exit(0)
        except EOFError:
            return

start()