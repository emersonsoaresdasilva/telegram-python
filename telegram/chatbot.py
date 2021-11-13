import time
import random
import telepot

def opcoes(mensagem):
    chat_id = mensagem['chat']['id']
    comando = mensagem['text']

    if comando == '/temp':
        bot.sendMessage(chat_id, random.randint(1, 100))
    elif comando == '/frase':
        bot.sendMessage(chat_id, random.choice(menssagens))

menssagens = ['Rumo ao Hexa, Vai Brasillllll!', 'Sou estudante, ainda não sou formado...']
mensagem = random.choice(menssagens)

bot = telepot.Bot(input('Digite seu token: '))
bot.message_loop(opcoes)
print('Aguardando comandos...')

while True:
    time.sleep(10)