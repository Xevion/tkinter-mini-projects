from random import random
import math

def gen():
    #int(return random()*(16)-12)
    return random()*(16)-12

top = gen()
bot = gen()

for _ in range(5000000):
    top = max(gen(), top)
    bot = min(gen(), bot)
print("bot {} top {}".format(bot, top))