import os
import time
import telepot
import helper
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.environ['BOT_TOKEN']

# The function on_chat creates an inline keyboard
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Temperature inside', callback_data='temp_in')],
                   [InlineKeyboardButton(text='Humidity inside', callback_data='humid_in')],
                   [InlineKeyboardButton(text='Temperature outside', callback_data='temp_out')],
                   [InlineKeyboardButton(text='Take Picture', callback_data='temp_pic')]
               ])

    bot.sendMessage(chat_id, "Welcome to the weather bot of Wahe3bru's. What would you like to know?", reply_markup=keyboard)

# The function on_callback_query pprocess the data from Thingspeak and react according to the pushed button

def on_callback_query(msg):

    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')

    print('Callback Query:', query_id, from_id, query_data)

    if(query_data == 'temp_in'):
        in_humid, in_temp = helper.sensor_reading()

        bot.sendMessage(from_id, text='The temperature inside: ' + str(in_temp) + '°C')

    elif(query_data == 'humid_in'):
        in_humid, in_temp = helper.sensor_reading()

        bot.sendMessage(from_id, text="The humidity inside: " + str(in_humid) + '%')

    elif(query_data == 'temp_out'):
        _, out_temp, _, _ = helper.get_weather_from_OWM(api_call)
        bot.sendMessage(from_id, text='The temperature outside: ' + str(out_temp) + '°C')

    elif(query_data == 'temp_pic'):
        helper.take_photo()
        fp = open('SendPic.jpg', 'rb')
        # file_info = telepot.InputFileInfo('SendPic.jpg', fp, 'image/jpg')
        # telepot.InputFile('photo', file_info)
        bot.sendPhoto(from_id, photo=fp)


#initialize the functions
api_key = os.getenv('OWMapi_key')
api_call = helper.create_OWM_api_call(api_key)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
