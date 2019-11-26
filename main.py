import eel

import re

eel.init('web')
eel.start('index.html', block=False)


@eel.expose
def process(pattern, string):
    string = re.sub(f'({pattern})', r'<mark>\1</mark>', string)
    eel.showResult(string)


while True:
    eel.sleep(1)
