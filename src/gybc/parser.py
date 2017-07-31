import webcolors
from nltk.tokenize import wordpunct_tokenize
import datetime
import gybc.statuses as statuses
import gybc.carmfg as carmfg
import re

def word_is_color(word):
    if word in webcolors.CSS3_NAMES_TO_HEX:
        return word
    else:
        return False

def word_is_car_make(word):
    word = re.sub('\d', '', word)
    if word in carmfg.makers:
        return word
    elif word in carmfg.make_corrected:
        return carmfg.make_corrected[word]
    return False

def word_is_year(word):
    try:
        word_int = int(word)
        if 1900 <= word_int <= datetime.datetime.now().year + 1:
            return word
    except:
        return False

def parse_tweet(sentence):
    sentence = sentence.lower()
    results = {'color': [],
               'make': [],
               'model': [],
               'year' : [],
               'license': []
               }
    for word in wordpunct_tokenize(sentence):
        color = word_is_color(word)
        if color:
            results['color'].append(color)

        make = word_is_car_make(word)
        if make:
            results['make'].append(make)

        year = word_is_year(word)
        if year:
            results['year'].append(year)

    return results

def main():
    for sentence in statuses.texts():
        results = parse_tweet(sentence)
        #if not results['color']:
        #    print("COLOR FAILURE: " + sentence)
        if results['make']:
            #print("MAKE FAILURE: " + sentence)
            print(results['make'])
        #print(sentence + " " + str())
        #print("\n")

if __name__ == "__main__":
    main()