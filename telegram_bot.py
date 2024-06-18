from telegram.ext import Updater
import telegram
from datetime import datetime
import config

token = config.token_bot
id = config.id_chat_telegram
bot = telegram.Bot(token=token,)

date = datetime.today()

updater = Updater(token= token, use_context=True)
dispatcher = updater.dispatcher

def iniciado():
    bot.send_message(text=f'Buscador de pisos iniciado correctamente \n{date}', chat_id=id)

def resultado_msg(titulo, link):
    bot.send_message(text=f'¡Nuevo Piso Publicado! \n\n{titulo}\n{link}', chat_id=id)

def funcionando(hora_actual):
    global funcionando_msg
    funcionando_msg = bot.send_message(text=f'Última Búsqueda: {hora_actual}', chat_id=id)

def fin():
    bot.send_message(text='Programa Finalizado', chat_id=id)

def update_funcionando(hora_actual):
    bot.editMessageText(message_id = funcionando_msg.message_id, text=f'Última Búsqueda: {hora_actual}', chat_id=id)

def pin():
    bot.pin_chat_message(chat_id = id, message_id = funcionando_msg.message_id)

def unpin():
    bot.unpin_all_chat_messages(chat_id = id)

def busqueda_en_curso():
    bot.editMessageText(message_id = funcionando_msg.message_id, text=f'Búsqueda en curso', chat_id=id)

def msg(mensaje):
    bot.send_message(text=f'{mensaje}', chat_id=id)