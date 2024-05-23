#Importando a Biblioteca telebot
import telebot
import random

#Colocando a Chave API em uma variavel
CHAVE_API = '7160418088:AAEtEvcM3NpS3c58vlpT1NqsEUYvXxSrcyE'

#Vinculando a chave API com a biblioteca e colocando ela dentro de uma variavel
bot = telebot.TeleBot(CHAVE_API)

#Comando 5
@bot.message_handler(commands=['5'])
def responder(mensagem):
    cinco = '''
Trabalhe conosco 💙

Legal! Ficamos muito felizes com seu interesse.

Você pode conferir e se candidatar as vagas abertas através do nosso site: https://www.pedlabs.com.br/git init

Aguardamos sua candidatura. 😉🤖💙'''
    bot.reply_to(mensagem, cinco)

def verificar(mensagem, *args, **kwargs):
    if mensagem.text.lower() == '/4':
        return True
    else:
        return False

def saudacao_personalizada(nome):
    saudacoes = [
        f'Olá, {nome}! Tudo bem? Estou a disposição..',
        f'Oi, {nome}! Como vai? Como posso te ajudar?',
        f'Como está indo, {nome}? Como posso te ajudar hoje?'
    ]
    return random.choice(saudacoes)

# Comando 4
@bot.message_handler(func=verificar)
def responder(mensagem, *args, **kwargs):
    if mensagem.text.lower() == '/4':
        # Obtendo o nome do usuário
        nome_usuario = mensagem.from_user.first_name
        # Gerando saudação personalizada
        saudacao = saudacao_personalizada(nome_usuario)
        # Enviando a mensagem
        bot.send_message(mensagem.chat.id, saudacao)

#Comando telegram
@bot.message_handler(commands=['telegram'])
def responder(mensagem):
    telegram = '''
Só aguardar que um de nossos consultor já irá falar com você!'''
    bot.reply_to(mensagem, telegram)

#Comando 3
@bot.message_handler(commands=['3'])
def responder(mensagem):
    tres = '''
Clique no link abaixo e fale com um consultor via WhatsApp:
https://api.whatsapp.com/send/?phone=5514991295361&text&type=phone_number&app_absent=0

Ou digite /telegram e aguarde um de nosso atendentes entrar em contato'''
    bot.reply_to(mensagem, tres)

#Demonstraão
@bot.message_handler(commands=['demo'])
def responder(mensagem):
    demo = '''
Só aguardar que um de nossos atendentes já irá lhe auxiliar...'''
    bot.reply_to(mensagem, demo)

#Comando 2
@bot.message_handler(commands=['2'])
def responder(mensagem):
    dois = '''
Saber mais sobre! 🤖

O Pedbot é uma plataforma especializada em atendimento via WhatsApp para farmácias! 

A melhor maneira de te apresentar a plataforma é através de uma demonstração de uso com um dos nossos especialistas. Dessa forma você consegue ver na prática e bater um papo sobre como a plataforma se adequa ao seu negócio. 

Vamos agendar uma demonstração? /demo'''
    bot.reply_to(mensagem, dois)

#Comando 1
@bot.message_handler(commands=['1'])
def responder(mensagem):
    um = '''
Contratar Pedbot 🚀

Oba! Que bom que você quer começar otimizar seu WhatsApp!

Para continuar seu atendimento, por favor me diga:

- Seu nome
- Sua empresa
- Seu cargo

Em breve um dos nossos especialistas irá te atender. 🤖💙'''
    bot.reply_to(mensagem, um)


#Código principal
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    primeira_msg = '''
Olá! Esse é o canal comercial da PedBot!

Somos a maior plataforma especialista em farmácias para atendimento em WhatsApp.

É ótimo ter você aqui 💙. Selecione uma das opções abaixo para continuar o seu atendimento: 

Digite /1 Para: Quero marcar uma reunião para contratar a plataforma 🚀

Digite /2 Para: Quero saber mais sobre a PedBot 🤖

Digite /3 Para: Quero falar com um consultor 🙋‍♀️

Digite /4 Para: Já sou cliente do PedBot 😊

Digite /5 Para: Quero trabalhar com a PedBot 💙'''
    bot.reply_to(mensagem, primeira_msg)


bot.polling()