import asyncio
import os
import threading

def get_bot_dirs():
    return [os.path.join(d, o)[2:] for o in os.listdir(d)
                    if os.path.isdir(os.path.join(d,o))
                    and os.path.join(d,o).startswith('./bot_')]

d = '.'
bot_dirs = get_bot_dirs()
bots = []

for bot in bot_dirs:
    bot_mod = __import__(bot, globals(), locals(), [bot], 0)
    bot_class = getattr(bot_mod, bot)
    bot_cls = getattr(bot_class, bot)
    my_bot = bot_cls()
    bots.append(threading.Thread(target=my_bot.run))
    # bots.append(my_bot)

for bot in bots:
    bot.start()
