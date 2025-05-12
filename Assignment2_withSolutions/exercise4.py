import re

lookup = {
    'doa': 'dead on arrival',
    'gf': 'girlfriend',
    'bf': 'boyfriend',
    'btw': 'by the way',
    'lol': 'laughing out loud',
}

Input = "I was lol when my bf’s phone was doa."
Target_output = "I was laughing out loud when my boyfriend’s phone was dead on arrival."


def convert_to_fulltext(text):
    for abbr, ft in lookup.items():
        text = re.sub(fr"\b{abbr}'?\b", ft, text)
    return text


print(Input)
print(convert_to_fulltext(Input))
