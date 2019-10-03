import telebot
from telebot import types

from Config import BOT_TOKEN, log

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup()
    faculty_1_button = types.InlineKeyboardButton(text='1', callback_data='faculty_1')
    faculty_2_button = types.InlineKeyboardButton(text='2', callback_data='faculty_2')
    faculty_3_button = types.InlineKeyboardButton(text="3", callback_data='faculty_3')
    faculty_4_button = types.InlineKeyboardButton(text="4", callback_data='faculty_4')
    faculty_5_button = types.InlineKeyboardButton(text='5', callback_data='faculty_5')
    keyboard.add(faculty_1_button, faculty_2_button, faculty_3_button, faculty_4_button, faculty_5_button)
    bot.send_message(message.chat.id, 'Привет, я бот с расписанием, на данный момент я могу показывать расписнаие только для 482 группы, но у меня еще все впереди. Вебери свой факультет!' ,
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, choose_faculty)
    log(message)



def choose_faculty(message):
    if message.text == '4':
        keyboard = types.ReplyKeyboardMarkup()
        group_461_button = types.InlineKeyboardButton(text='461', callback_data='group_461')
        group_462_button = types.InlineKeyboardButton(text='462', callback_data='group_462')
        group_464_button = types.InlineKeyboardButton(text='464', callback_data='group_464')
        group_465_button = types.InlineKeyboardButton(text='465', callback_data='group_465')
        group_466_button = types.InlineKeyboardButton(text='466', callback_data='group_466')
        group_471_button = types.InlineKeyboardButton(text='471', callback_data='group_471')
        group_472_button = types.InlineKeyboardButton(text='472', callback_data='group_472')
        group_474_button = types.InlineKeyboardButton(text='474', callback_data='group_474')
        group_475_button = types.InlineKeyboardButton(text='475', callback_data='group_475')
        group_476_button = types.InlineKeyboardButton(text='476', callback_data='group_476')
        group_481_button = types.InlineKeyboardButton(text='481', callback_data='group_481')
        group_482_button = types.InlineKeyboardButton(text='482', callback_data='group_482')
        group_484_button = types.InlineKeyboardButton(text='484', callback_data='group_484')
        group_485_button = types.InlineKeyboardButton(text='485', callback_data='group_485')
        group_486_button = types.InlineKeyboardButton(text='486', callback_data='group_486')
        group_492_button = types.InlineKeyboardButton(text='492', callback_data='group_492')
        group_493_button = types.InlineKeyboardButton(text='493', callback_data='group_493')
        group_494_button = types.InlineKeyboardButton(text='494', callback_data='group_494')
        group_495_button = types.InlineKeyboardButton(text='495', callback_data='group_495')
        group_496_button = types.InlineKeyboardButton(text='496', callback_data='group_496')
        group_497_button = types.InlineKeyboardButton(text='497', callback_data='group_497')
        keyboard.add(group_461_button,group_462_button, group_464_button, group_465_button, group_466_button, group_471_button, group_472_button, group_474_button,
        group_475_button, group_476_button, group_481_button, group_482_button, group_484_button, group_485_button, group_486_button, group_492_button,
        group_493_button, group_494_button, group_495_button, group_496_button, group_497_button)
        bot.send_message(message.chat.id, 'Вебери свою группу!', reply_markup=keyboard)
    log(message)


bot.polling(none_stop=True, interval=0)