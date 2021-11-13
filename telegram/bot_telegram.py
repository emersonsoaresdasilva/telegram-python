import telepot

bot = telepot.Bot(input('Digite seu token: '))
print(bot.getMe())