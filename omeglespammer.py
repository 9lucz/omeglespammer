from pyomegle import OmegleClient
from pyomegle import OmegleHandler
import time

h = OmegleHandler(loop=True)
c = OmegleClient(h, wpm=47, lang="pt")


c.start()

input_str = "mensagem1"
input_str2 = "mensagem2"
input_str3 = "mensagem3"

while 1:
    time.sleep(3)
    c.send(input_str)
    time.sleep(1)
    c.send(input_str2)
    time.sleep(1)
    c.send(input_str3)
    time.sleep(3)
    c.next()
