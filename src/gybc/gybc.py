#import twitter
import webcolors
import gybc.statuses as statuses
import gybc.carmfg as carmfg

def word_is_color(word):
    return word in webcolors.CSS3_NAMES_TO_HEX

for status in statuses.texts():
    found_colors = []
    found_makes = []
    for word in status.lower().split(" "):
        if word_is_color(word):
            found_colors.append(word)
        if word in carmfg.makers:
            found_makes.append(word)
    if not found_colors or not found_makes:
        print(status)
    print("Possible make and color: %s / %s" % (str(found_makes), str(found_colors)))