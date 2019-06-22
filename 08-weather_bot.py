
import time
import telepot
import helper
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

# store the TOKEN for the Telegram Bot
TOKEN = '620578061:AAFrBCb3MWp-7MgtvrvpYmQgQNGWTck_Kog'

#lt's write all the functions

#The function on_chat creates an inline keyboard

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Temperature inside', callback_data='temp_in')],
                   [InlineKeyboardButton(text='Humidity inside', callback_data='humid_in')],
                   [InlineKeyboardButton(text='Temperature outside', callback_data='temp_out')]
               ])

    bot.sendMessage(chat_id, "Welcome to the weather bot of Wahe3bru's. What would you like to know?", reply_markup=keyboard)

#The function on_callback_query pprocess the data from Thingspeak and react according to the pushed button

def on_callback_query(msg):

    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    print('Callback Query:', query_id, from_id, query_data)

    if(query_data == 'temp_in'):
        bot.sendMessage(from_id, text='The temperature inside: ' + '23' + '°C')

    elif(query_data == 'umid'):
        bot.sendMessage(from_id, text="The humidity inside: " + '78' + '%')

    elif(query_data == 'press'):
        bot.sendMessage(from_id, text='The temperature outside: ' + '13' + '°C')


#initialize the functions


bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
