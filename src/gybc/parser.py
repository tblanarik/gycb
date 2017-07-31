import webcolors
from nltk.tokenize import wordpunct_tokenize
import datetime
import statuses
import carmfg


def word_is_color(word):
    return word in webcolors.CSS3_NAMES_TO_HEX

def word_is_year(word):
    try:
        word_int = int(word)
        return 1900 <= word_int <= datetime.datetime.now().year + 1
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
        if word_is_color(word):
            results['color'].append(word)
        if word in carmfg.makers:
            results['make'].append(word)
        if word_is_year(word):
            results['year'].append(word)

    return results

def main():
    for sentence in statuses.texts():
        print(sentence)
        print(parse_tweet(sentence))
        print("\n")

if __name__ == "__main__":
    main()