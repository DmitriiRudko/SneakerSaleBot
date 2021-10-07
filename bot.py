import telebot
from databaseModel import Database
import configurate
from telebot import types
import FarfetchArrayParams
from MainController import MainController
client = telebot.TeleBot(configurate.config['token'])


@client.message_handler(commands=['start'])
def start(message):
    Database.addUser(self=Database,id=message.chat.id)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    gender = types.KeyboardButton('🙎‍♂/️🙍‍♀ Пол')
    brand = types.KeyboardButton('™️ Бренд')
    color = types.KeyboardButton('🟢 Цвет')
    price = types.KeyboardButton('💵 Цена️')
    size = types.KeyboardButton('📏 Размер')
    search = types.KeyboardButton('🔍 Поиск')
    markup.add(gender, brand, size, color, price, search)
    client.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup=markup)

@client.message_handler(content_types=['text'])
def selectColor(message):
    if message.text == '🔍 Поиск':
        client.send_message(message.chat.id, 'Выполняю поиск ⏳')
        SneakerList = MainController.getSneakerList(self=MainController, id=message.chat.id)
        if (len(SneakerList)):
            client.send_message(message.chat.id,'К сожалению ничего не наеденно 😔'+'\n'+'попробуйте изменить парметры поиска')
        for s in SneakerList:
            client.send_photo(message.chat.id, photo=s.imgUrl, caption=s.name+'\n'+s.price+'\n'+s.url)
    if message.text == '🟢 Цвет':
        markup = types.InlineKeyboardMarkup()
        white = types.InlineKeyboardButton(text='⚪️', callback_data='white')
        black = types.InlineKeyboardButton(text='⚫️', callback_data='black')
        brown = types.InlineKeyboardButton(text='🟤', callback_data='brown')
        red = types.InlineKeyboardButton(text='🔴', callback_data='red')
        orange = types.InlineKeyboardButton(text='🟠', callback_data='orange')
        yellow = types.InlineKeyboardButton(text='🟡', callback_data='yellow')
        purple = types.InlineKeyboardButton(text='🟣', callback_data='purple')
        blue = types.InlineKeyboardButton(text='🔵', callback_data='blue')
        green = types.InlineKeyboardButton(text='🟢', callback_data='green')
        noneColor = types.InlineKeyboardButton(text='Любой цвет', callback_data='any')
        markup.add(white, black, brown, green, blue, purple, yellow, orange, red,noneColor)
        client.send_message(message.chat.id, 'Выберете цвет', reply_markup=markup)
    elif message.text == '🙎‍♂/️🙍‍♀ Пол':
        markup = types.InlineKeyboardMarkup()
        Men = types.InlineKeyboardButton(text='🙎‍♂', callback_data='1')
        Women = types.InlineKeyboardButton(text='🙍‍♀', callback_data='0')
        markup.add(Men, Women)
        client.send_message(message.chat.id, 'Выберете размерную сетку', reply_markup=markup)
    elif message.text == '™️ Бренд':
        markup = types.InlineKeyboardMarkup()
        Adidas = types.InlineKeyboardButton(text='Adidas', callback_data='adidas')
        Nike = types.InlineKeyboardButton(text='Nike', callback_data='Nike')
        NewBalance = types.InlineKeyboardButton(text='New Balance', callback_data='New Balance')
        Converse = types.InlineKeyboardButton(text='Converse', callback_data='Converse')
        markup.add(Adidas, Nike, NewBalance, Converse)
        client.send_message(message.chat.id, 'Выберете брэнд', reply_markup=markup)
    elif message.text == '📏 Размер':
        markup = types.InlineKeyboardMarkup()
        size37 = types.InlineKeyboardButton(text='37', callback_data='37')
        size375 = types.InlineKeyboardButton(text='37.5', callback_data='37.5')
        size38 = types.InlineKeyboardButton(text='38', callback_data='38')
        size385 = types.InlineKeyboardButton(text='38.5', callback_data='38.5')
        size39 = types.InlineKeyboardButton(text='39', callback_data='39')
        size395 = types.InlineKeyboardButton(text='39.5', callback_data='39.5')
        size40 = types.InlineKeyboardButton(text='40', callback_data='40')
        size405 = types.InlineKeyboardButton(text='40.5', callback_data='40.5')
        size41 = types.InlineKeyboardButton(text='41', callback_data='41')
        size415 = types.InlineKeyboardButton(text='41.5', callback_data='41.5')
        size42 = types.InlineKeyboardButton(text='42', callback_data='42')
        size425 = types.InlineKeyboardButton(text='42.5', callback_data='42.5')
        size43 = types.InlineKeyboardButton(text='43', callback_data='43')
        size435 = types.InlineKeyboardButton(text='43.5', callback_data='43.5')
        size44 = types.InlineKeyboardButton(text='44', callback_data='44')
        size445 = types.InlineKeyboardButton(text='44.5', callback_data='44.5')
        size45 = types.InlineKeyboardButton(text='45', callback_data='45')
        size455 = types.InlineKeyboardButton(text='45.5', callback_data='45.5')
        size46 = types.InlineKeyboardButton(text='46', callback_data='46')
        size465 = types.InlineKeyboardButton(text='46.5', callback_data='46.5')
        size465 = types.InlineKeyboardButton(text='46.5', callback_data='46.5')
        markup.add(size37,size375, size38, size385,size39,size39,size395,size40,size405,size41,size415,size42,size425,size43,size435,
                   size44,size445,size45,size455,size46,size465)
        client.send_message(message.chat.id, 'Выберете раземер 📏', reply_markup=markup)
    elif message.text == '💵 Цена️':
        priceLow = client.send_message(message.chat.id, 'Введите нижний порог цены ⬇️')
        client.register_next_step_handler(priceLow, lowPrice)
def lowPrice(message):
        Database.changeParams(self=Database,id=message.chat.id, param='priceLow', value=message.text)
        priceHigh = client.send_message(message.chat.id, 'Введите верхний порог цены ⬆️')
        client.register_next_step_handler(priceHigh,highPrice)
def highPrice(message):
        Database.changeParams(self=Database,id=message.chat.id, param='priceHigh', value=message.text)
        print(message.text)

@client.callback_query_handler(func=lambda call: True)
def genderSelect(call):
    if (call.data == '1'):
        Database.changeParams(self=Database,id=call.message.chat.id, param='gender', value=1)
        return
    elif(call.data == '0'):
        Database.changeParams(self=Database,id=call.message.chat.id, param='gender', value=0)
        return
    elif(call.data in FarfetchArrayParams.colors):
        Database.changeParams(self=Database,id=call.message.chat.id, param='color', value=call.data)
        return
    elif (call.data in FarfetchArrayParams.brands):
        Database.changeParams(self=Database,id=call.message.chat.id, param='brand', value=call.data)
        return
    elif (37 <= float(call.data) <= 46.5):
        Database.changeParams(self=Database,id=call.message.chat.id, param='size', value=call.data)
client.polling(none_stop=True, interval=0)
