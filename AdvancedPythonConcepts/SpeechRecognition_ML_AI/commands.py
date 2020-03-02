import subprocess
import os
from .get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ['yes', 'affirmative', 'si', 'sure', 'do it', 'yeah', 'confirm']
        self.cancel = ['no', 'negative', 'negative soldier', "dont't", 'wait', 'cancel']

    def discover(self, text):
        if 'what' in text and 'name' in text:
            if 'my' in text:
                self.respond('You havent told me your name yet')
            else:
                self.respond('My name is python commander. How are you?')
        else:
            f = Fetcher('https://www.google.com/search?q=', text)
            answer = f.lookup()
            self.respond(answer)


        if 'launch' in text or 'open' in text:
            app = text.split(' ', 1)[-1]
            # Command on MacOS to lauch any application
            self.respond('Opening ', app)
            os.system('open  -a' + app + '.app')

    def respond(self, response):
        print(response)
        subprocess.call('ptts ' + response, shell=True)