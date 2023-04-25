import requests
import random
import telebot
from random import randint
from telebot import types
import sqlite3
import json

karma = 0
API = '27cd1f60f8d989dc394183b3ef501809'

riddle_qestion = None
city_qestion = None

hangman_motion = (
    """
    ----------
    """,
    """
     |    
     |
     |
     |
     |
     |
    ----------
    """,
    """
    ------
     |    
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)

words = ['перпендикуляр', 'Амфитеатр', 'Синоптик', 'Пассатижи', 'Радиатор', 'Крышка', 'Кашпо', 'Абзац', 'Формуляр', \
         'Вращение', 'Фундамент', 'Казино']
max_wrong = len(hangman_motion) - 1
word = random.choice(words).lower()
so_far = ["_ "] * len(word)
wrong = 0
used = []
used_words = []
send = ''
not_play = True
question = ''

name = None
vk1 = None
bot = telebot.TeleBot('6097683861:AAH__nIl7lmDINzHUi6aFzCzCXd9EFoPLE0')


@bot.message_handler(commands=['weather'])
def weather(message):
    bot.send_message(message.chat.id, 'Введите город', parse_mode='html')
    bot.register_next_step_handler(message, whether)


def whether(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        wind = data['wind']['speed']
        clouds = data['clouds']['all']
        bot.reply_to(message, f'Температура: {temp}\n Ветер: {wind}\n Уровень облаков: {clouds}')
    else:
        bot.reply_to(message, 'Неправильно введён город')


@bot.message_handler(commands=['vk'])
def vk(message):
    vk_ss = ''
    if vk_ss != '':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("ВК", url=f"https://vk.com/{vk_ss}"))
        bot.send_message(message.chat.id, 'Перейти по ссылке на вашу страницу ВК:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У меня нет данных вашей страницы. Вы что, от кого-то скрываетесь?',
                         parse_mode='html')
        bot.send_message(message.chat.id, 'Напишите ваш ник в Vk', parse_mode='html')
        bot.register_next_step_handler(message, vk_1)


def vk_1(message):
    if message.text != '' and message.text != '/vk':
        vk_ss = message.text
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("ВК", url=f"https://vk.com/{vk_ss}"))
        bot.send_message(message.chat.id, 'Перейти по ссылке на вашу страницу ВК:', reply_markup=markup)


@bot.message_handler(commands=['bear'])
def bear(message):
    bot.send_message(message.chat.id, "Теперь за тобой наблюдает медведь! Тшшшшш...Не делай резких движений!")
    bot.send_message(message.chat.id, ". . . . . . . . ._. ,-'``;)")
    bot.send_message(message.chat.id, ". . . . . . . . . . ,`. . .`-----'..)")
    bot.send_message(message.chat.id, ". . . . . . . . . .,. . . . . .~ .`- .)")
    bot.send_message(message.chat.id, ". . . . . . . . . ,'. . . . . . . .o. .o__)")
    bot.send_message(message.chat.id, ". . . . . . . . _l. . . . . . . . . . . . (#))")
    bot.send_message(message.chat.id, ". . . . . . . _. '`~-.. . . . . . . . . .,')")
    bot.send_message(message.chat.id, ". . . . . . .,. .,.-~-.' -.,. . . ..'--~`)")
    bot.send_message(message.chat.id, ". . . . . . /. ./. . . . .}. .` -..,/)")
    bot.send_message(message.chat.id, ". . . . . /. ,'___. . :/. . . . . .)")
    bot.send_message(message.chat.id, ". . . . /'`-.l. . . `'-..'........ . .)")
    bot.send_message(message.chat.id, ". . . ;. . . . . . . . . . . . .)-.....l)")
    bot.send_message(message.chat.id, ". . .l. . . . .' —-........-'. . . ,')")
    bot.send_message(message.chat.id, ". . .',. . ,....... . . . . . . . . .,')")
    bot.send_message(message.chat.id, ". . . .' ,/. . . . `,. . . . . . . ,')")
    bot.send_message(message.chat.id, ". . . . .. . . . . .. . . .,.- ')")
    bot.send_message(message.chat.id, ". . . . . ',. . . . . ',-~'`. ;)")
    bot.send_message(message.chat.id, ". . . . . .l. . . . . ;. . . /__)")
    bot.send_message(message.chat.id, ". . . . . /. . . . . /__. . . . .)")
    bot.send_message(message.chat.id, ". . . . . '-.. . . . . . .)")

@bot.message_handler(commands=['beer'])
def beer(message):
    bot.send_message(message.chat.id, '''... |"""""""""""""""""| |\ ''')
    bot.send_message(message.chat.id, "... |Холодное пиво! ||""\__,_")
    bot.send_message(message.chat.id, "... |_____________ |||_|__|_ )")
    bot.send_message(message.chat.id, '... *(@)|(@)"""*******(@)"')
    bot.send_message(message.chat.id, "______________________________")
    bot.send_message(message.chat.id, "Упс...Надеемся, что вам есть 18")


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'Вау, классное фото')


@bot.message_handler(content_types=['video'])
def photo(message):
    bot.reply_to(message, 'Вау, классное видео')


@bot.message_handler(content_types=['audio'])
def photo(message):
    bot.reply_to(message, 'Вау')


@bot.message_handler(commands=['note'])
def games(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton('Заметки')
    markup.add(button1)
    bot.send_message(message.chat.id, 'Вот, как ты и просил', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('basadanneh.sqlite')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users1 (id int auto_increment primary key, user_id INTEGER, name TEXT, password TEXT)')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Введите ваше имя', parse_mode='html')
    bot.register_next_step_handler(message, username)


def username(message):
    global name
    name = message.text.strip()
    m = []
    for k in name:
        m.append(k)
    if m[0] == '/':
        bot.reply_to(message, 'неправильно введено имя')
        bot.send_message(message.chat.id, 'пройдите регистрацию заново')
    else:
        bot.send_message(message.chat.id, 'Введите пароль', parse_mode='html')
        bot.register_next_step_handler(message, userpassword)


# def VK(message):
    # global vk1
    # vk1 = message.text.strip()
    # m = []
    # for k in vk1:
    #     m.append(k)
    # if m[0] == '/':
    #     bot.reply_to(message, 'неправильно введён ник')
    #     bot.send_message(message.chat.id, 'пройдите регистрацию заново')
    # else:
    #     bot.send_message(message.chat.id, 'Введите пароль', parse_mode='html')
    #     bot.register_next_step_handler(message, userpassword)


def userpassword(message):
    password = message.text.strip()
    m = []
    for k in password:
        m.append(k)
    if m[0] == '/':
        bot.reply_to(message, 'неправильно введён пароль')
        bot.send_message(message.chat.id, 'пройдите регистрацию заново')
    try:
        user_id = message.from_user.id
        conn = sqlite3.connect('basadanneh.sqlite')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users1 (user_id, name, password) VALUES ('%s', '%s', '%s')" % (
            user_id, name, password))
        conn.commit()
        cur.close()
        conn.close()
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('список пользователей', callback_data='users'))
        bot.send_message(message.chat.id, 'пользователь зареган', reply_markup=markup)
    except sqlite3.Error:
        bot.send_message(message.chat.id, 'Вы уже зареганы. Обмануть решили?')


@bot.message_handler(commands=['help'])
def help(message):
    mess = "Вот что я могу:\n" \
           "/note - вывести кнопку заметок\n" \
           "/city - игра в города\n" \
           "/vk - перейти на страничку в вк\n" \
           "/riddles - загадки\n" \
           "/profile - ваш профиль\n" \
           "/frases - список быстрых фраз\n" \
           "/weather - узнать погоду\n" \
           "/cubes - кости\n" \
           "/incowords - каракуля\n" \
           "/hangman - виселица\n" \
           "отвечать на ваши вопросы"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['frases'])
def frases(message):
    mess = "Вот список фраз:\n" \
           "повтори пользователей - показывает всех пользователей"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('basadanneh.sqlite')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users1")
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: ******\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


@bot.message_handler(commands=['riddles'])
def riddles(message):
    global riddle_qestion
    riddle_qestion = randint(1, 10)
    if riddle_qestion == 1:
        riddle = 'Какой болезнью никто не болеет на суше?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 2:
        riddle = 'У квадратного стола отпилили один угол. Сколько теперь углов у него стало?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 3:
        riddle = 'Где вода стоит столбом?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 4:
        riddle = 'Каких камней в море нет?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 5:
        riddle = 'Под каким деревом сидит заяц, когда идет дождь?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 6:
        riddle = 'Чем заканчиваются день и ночь?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 7:
        riddle = 'Что может в одно и то же время: стоять и ходить, висеть и стоять, ходить и лежать?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 8:
        riddle = 'Что бросают тогда, когда это необходимо, и поднимают тогда, когда это уже не нужно? '
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 9:
        riddle = 'Накормишь – живет, напоишь – умрет.'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)
    elif riddle_qestion == 10:
        riddle = 'Что с поднять земли легко, но трудно кинуть далеко?'
        bot.send_message(message.chat.id, riddle)
        bot.register_next_step_handler(message, riddle_answer)


def riddle_answer(message):
    global riddle_qestion
    if riddle_qestion == 1 and message.text.strip().lower() == 'морской':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 2 and (message.text.strip().lower() == 'пять' or message.text.strip().lower() == '5'):
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 3 and message.text.strip().lower() == 'в стакане':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 4 and message.text.strip().lower() == 'сухих':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 5 and message.text.strip().lower() == 'под мокрым' or message.text.strip().lower() == 'мокрым':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 6 and message.text.strip().lower() == 'мягким знаком':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 7 and message.text.strip().lower() == 'часы':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 8 and message.text.strip().lower() == 'якорь':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 9 and message.text.strip().lower() == 'огонь':
        bot.send_message(message.chat.id, 'Правильно')
    elif riddle_qestion == 10 and message.text.strip().lower() == 'пух':
        bot.send_message(message.chat.id, 'Правильно')
    else:
        bot.send_message(message.chat.id, 'Не правильно')


@bot.message_handler(commands=['profile'])
def profile(message):
    user_ids = message.from_user.id
    conn = sqlite3.connect('basadanneh.sqlite')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users1 WHERE user_id == (%s)" % (user_ids))
    users = cur.fetchall()
    for el in users:
        bot.send_message(message.chat.id, f'Имя: {el[1]}\nПароль: ******')
    cur.close()
    conn.close()


@bot.message_handler(commands=['city'])
def city(message):
    global city_qestion
    city_qestion = randint(1, 10)
    if city_qestion == 1:
        city1 = 'Столица третьей страны, соседки Латвии, Литвы.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 2:
        city1 = 'Какой город носят на голове?'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 3:
        city1 = 'В столице сей 4 буквы, Азербайджана город крупный.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 4:
        city1 = 'Мать всех русских городов, средь днепровских берегов.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 5:
        city1 = 'В названии какого города имя одного мальчика и имя ста девочек?'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 6:
        city1 = 'О каком французском городе часто напоминают нам занавески на окнах?'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 7:
        city1 = 'Его столицей на Урале россияне величали.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 8:
        city1 = 'Я – центр краевой Над Амуром-рекой.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 9:
        city1 = 'Вместо улиц и бульваров \n В этом городе – каналы.\n По каналам – теплоходы,\n Модный транспорт для народа.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)
    elif city_qestion == 10:
        city1 = 'С огромной горой Фудзияма\n Крупный город у вулкана.'
        bot.send_message(message.chat.id, city1)
        bot.register_next_step_handler(message, city_answer)


def city_answer(message):
    global city_qestion
    if city_qestion == 1 and message.text.strip().lower() == 'таллин':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 2 and message.text.strip().lower() == 'панама':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 3 and message.text.strip().lower() == 'баку':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 4 and message.text.strip().lower() == 'киев':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 5 and message.text.strip().lower() == 'севастополь':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 6 and message.text.strip().lower() == 'тюль':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 7 and message.text.strip().lower() == 'екатеринбург':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 8 and message.text.strip().lower() == 'хабаровск':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 9 and message.text.strip().lower() == 'венеция':
        bot.send_message(message.chat.id, 'Правильно')
    elif city_qestion == 10 and message.text.strip().lower() == 'пух':
        bot.send_message(message.chat.id, 'Правильно')
    else:
        bot.send_message(message.chat.id, 'Не правильно')


@bot.message_handler(commands=['cubes'])
def cubes(message):
    you, b = randint(1, 6), randint(1, 6)
    if b == you:
        win = 'К сожалению или к счастью, ничья!'
    elif b > you:
        win = '''Бот выиграл эту партейку!
        Может повезёт в следующий раз...'''
    else:
        win = 'Вы выиграли! Везунчик!'
    bot.send_message(message.chat.id, f'''Играем в кости:
     Вас счёт: {you}
     Счёт бота: {b}
     {win}''')


@bot.message_handler(commands=['hangman'])
def hangman(message):
    global used, used_words, word, wrong, so_far, max_wrong, send
    word = random.choice(words).lower()
    so_far = ["_ "] * len(word)
    wrong = 0
    used = []
    used_words = []
    send = ''
    bot.send_message(message.chat.id, 'Правила игры: я загадываю слово. Количество букв в нём равняетсяя количеству нижних подчеркиваний. \
    Ваша задача угадать слово и не повесить человечка. Его судьба в ваших руках:)')
    if wrong < max_wrong and ''.join(so_far) != word.lower():
        bot.send_message(message.chat.id, hangman_motion[wrong])
        bot.send_message(message.chat.id, f"\nВы использовали следующие буквы:\n{used}")
        bot.send_message(message.chat.id, f"\nВы использовали следующие слова:\n{used_words}")
        bot.send_message(message.chat.id, f"\nНа данный момент слово выглядит так:\n{''.join(so_far)}")

        send = bot.send_message(message.chat.id, "\n\nВведите свое предположение: ")
        bot.register_next_step_handler(send, gohandman)


def gohandman(message):
    global wrong, send
    guess = message.text.lower()
    guess = guess.replace(' ', '')
    if (guess == '') or (guess in used) or (guess in used_words):
        if guess in used:
            bot.send_message(message.chat.id, f'Вы уже вводили букву "{guess}"')
        elif guess in used_words:
            bot.send_message(message.chat.id, f'Вы уже вводили слово "{guess}"')
        send = bot.send_message(message.chat.id, "Введите свое предположение: ")
        bot.register_next_step_handler(send, gohandman)
    elif wrong < max_wrong and guess != word:
        if len(guess) > 1:
            used_words.append(guess.lower())
        elif len(guess) == 1:
            used.append(guess)

        if len(guess) == 1:
            if guess in word:
                send = bot.send_message(message.chat.id, f'\nДа! "{guess}"есть в слове!')
                for i in range(len(word)):
                    if guess == word[i]:
                        so_far[i] = guess
                if ''.join(so_far) == word:
                    exithandman(send)
                else:
                    bot.send_message(message.chat.id, hangman_motion[wrong])
                    bot.send_message(message.chat.id, f"\nВы использовали следующие буквы:\n{used}")
                    bot.send_message(message.chat.id, f"\nВы использовали следующие слова:\n{used_words}")
                    bot.send_message(message.chat.id, f"\nНа данный момент слово выглядит так:\n{''.join(so_far)}")

                    send = bot.send_message(message.chat.id, "\n\nВведите свое предположение: ")
                    bot.register_next_step_handler(send, gohandman)
            else:
                send = bot.send_message(message.chat.id, f"\nИзвините, буквы \"" + guess + "\" нет в слове.")
                wrong += 1
                if wrong < max_wrong:
                    bot.send_message(message.chat.id, hangman_motion[wrong])
                    bot.send_message(message.chat.id, f"\nВы использовали следующие буквы:\n{used}")
                    bot.send_message(message.chat.id, f"\nВы использовали следующие слова:\n{used_words}")
                    bot.send_message(message.chat.id, f"\nНа данный момент слово выглядит так:\n{''.join(so_far)}")

                    send = bot.send_message(message.chat.id, "\n\nВведите свое предположение: ")
                    bot.register_next_step_handler(send, gohandman)
                else:
                    exithandman(send)
        elif len(guess) > 1:
            if guess != word:
                bot.send_message(message.chat.id, 'Вы пока не смогли угадать слово...')
                wrong += 1
                if wrong < max_wrong:
                    bot.send_message(message.chat.id, hangman_motion[wrong])
                    bot.send_message(message.chat.id, f"\nВы использовали следующие буквы:\n{used}")
                    bot.send_message(message.chat.id, f"\nВы использовали следующие слова:\n{used_words}")
                    bot.send_message(message.chat.id, f"\nНа данный момент слово выглядит так:\n{''.join(so_far)}")

                    send = bot.send_message(message.chat.id, "\n\nВведите свое предположение: ")
                    bot.register_next_step_handler(send, gohandman)
                else:
                    exithandman(send)
        else:
            exithandman(send)
    else:
        exithandman(send)


def exithandman(message):
    if wrong == max_wrong:
        bot.send_message(message.chat.id, hangman_motion[wrong])
        bot.send_message(message.chat.id, "\nО нет...Ты не смог спасти человечка!! =,(")
    else:
        bot.send_message(message.chat.id, "\nВы угадали слово! И сохранили человечку жизнь! =)")

    bot.send_message(message.chat.id, "\nЗагаданное слово было \"" + word + '\"')


@bot.message_handler(commands=['incowords'])
def start(message):
    global question, random_word, mixed_word, not_play
    if not_play:
        send = bot.send_message(message.chat.id,
                                'Игра в слова с перемешиванием: я вам дам слово-КАРАКУЛЮ с перемешенными буквами, '
                                'помоги мне - переставь символы так, чтобы получилось правильное '
                                'ОСМЫСЛЕННОЕ слово. Удачи с разгадыванием =)')
        question = (random.choice(words)).lower()
        random_word = random.sample(question, len(question))
        mixed_word = ''.join(random_word)
        bot.send_message(message.chat.id, mixed_word)
        bot.register_next_step_handler(send, go)


def go(message):
    global not_play
    if message.text.lower() == question:
        bot.send_message(message.chat.id, 'ДААА!!! Вам удалось расшифровать КАРАКУЛЮ! Спасибо =)')
        not_play = True
    elif not_play:
        send = bot.send_message(message.chat.id, 'Я верю в вас-попробуйте ещё раз!')
        bot.send_message(message.chat.id, mixed_word)
        not_play = False
        bot.register_next_step_handler(send, go)
    else:
        bot.send_message(message.chat.id, 'Увы, но походу вы тоже не разбираетесь  в моих каракулях =(')
        not_play = True


@bot.message_handler(content_types=['text'])
def answers(message):
    global karma
    a = 0
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'Прив' or message.text == 'прив' \
            or message.text == 'Hi' or message.text == 'hi' or message.text == 'Hi!' or message.text == 'hi!':
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    elif message.text == 'Спасибо' or message.text == 'спс' or message.text == 'спасибо' or message.text == 'Пожалуйста' or message.text == '+' or message.text == 'пж' or message.text == 'пожалуйста' or message.text == 'Плиз' or message.text == 'плиз':
        karma += 1
        bot.send_message(message.chat.id, f'Спасибо! Вы повысили рейтинг бота. Теперь он составляет: {karma}',
                         parse_mode='html')
    elif message.text == 'фу' or message.text == 'Фу' or message.text == '-' or message.text == 'Бе' or message.text == 'дурак' or message.text == 'Биомусор' or message.text == 'биомусор':
        karma -= 1
        bot.send_message(message.chat.id, f'О нет...Вы понизили рейтинг бота. Теперь он составляет: {karma}',
                         parse_mode='html')
    elif message.text == 'Заметки':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Заметки", url="http://127.0.0.1:8080"))
        bot.send_message(message.chat.id, 'Правила к игре 1:', reply_markup=markup)
    elif message.text == 'Повтори пользователей' or message.text == 'повтори пользователей':
        bot.register_next_step_handler(message, users_reply)
    elif message.text == 'С новым годом' or message.text == 'с новым годом':
        image = 'с новым годом1.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text == 'С 8 марта' or message.text == 'с 8 марта':
        image = '8марта.jpg'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    elif message.text == 'Хорошо' or message.text == 'хорошо' or message.text == 'Нормально' or message.text == 'нормально':
        bot.send_message(message.chat.id, 'Это хорошо, что хорошо', parse_mode='html')
    elif message.text == 'Как дела?' or message.text == 'как дела?' or message.text == 'Как дела' or message.text == 'как дела' or message.text == 'Как ты себя чувствуешь?' or message.text == 'как ты себя чувствуешь?' or message.text == 'Как ты себя чувствуешь' or message.text == 'как ты себя чувствуешь':
        bot.send_message(message.chat.id, 'Отлично, а у тебя?', parse_mode='html')
    elif message.text == 'Отлично' or message.text == 'отлично':
        bot.send_message(message.chat.id, 'Это отлично, что отлично', parse_mode='html')
    elif message.text == 'Чем занимаешься?' or message.text == 'чем занимаешься?' or message.text == 'Чем занимаешься' or message.text == 'чем занимаешься' \
            or message.text == 'Что делаешь?' or message.text == 'что делаешь?' or message.text == 'Что делаешь' or message.text == 'что делаешь':
        bot.send_message(message.chat.id, 'Плюшками балуюсь', parse_mode='html')
    elif message.text == 'Я тоже хочу' or message.text == 'я тоже хочу' or message.text == 'Тоже хочу' or message.text == 'тоже хочу':
        bot.send_message(message.chat.id, 'Хотеть не вредно', parse_mode='html')
    elif message.text == 'Вредно не хотеть' or message.text == 'вредно не хотеть' or message.text == 'Вредно - не хотеть' or message.text == 'вредно - не хотеть':
        bot.send_message(message.chat.id, 'Иметь не вредно', parse_mode='html')
    elif message.text == 'Вредно не иметь' or message.text == 'вредно не иметь' or message.text == 'Вредно - не иметь' or message.text == 'вредно - не иметь':
        bot.send_message(message.chat.id, 'Мечтать не вредно', parse_mode='html')
    elif message.text == 'Вредно не мечтать' or message.text == 'вредно не мечтать' or message.text == 'Вредно - не мечтать' or message.text == 'вредно - не мечтать':
        bot.send_message(message.chat.id, 'Давать не вредно', parse_mode='html')
    elif message.text == 'Вредно не давать' or message.text == 'вредно не давать' or message.text == 'Вредно - не давать' or message.text == 'вредно - не давать':
        bot.send_message(message.chat.id, '-_-', parse_mode='html')
    elif message.text == 'Понятно' or message.text == 'понятно':
        bot.send_message(message.chat.id, 'ага', parse_mode='html')
    elif message.text == 'Тебя создало государство?' or message.text == 'тебя создало государство?' or message.text == 'Тебя создало государство' or message.text == 'тебя создало государство' or message.text == 'Ты создан государством?' or message.text == 'ты создан государством?' or message.text == 'Ты создан государством' or message.text == 'ты создан государством':
        bot.send_message(message.chat.id, 'Конечно, кем же ещё', parse_mode='html')
    elif message.text == 'Почему небо голубое?' or message.text == 'почему небо голубое?' or message.text == 'Почему небо голубое' or message.text == 'почему небо голубое':
        bot.send_message(message.chat.id, 'А почему бы и нет? Тебе что не нравится?', parse_mode='html')
    elif message.text == 'Нет' or message.text == 'нет':
        bot.send_message(message.chat.id, 'Ну и ладно', parse_mode='html')
    elif message.text == 'Да' or message.text == 'да':
        bot.send_message(message.chat.id, 'Вот и ладушки', parse_mode='html')
    elif message.text == 'В чём смысл жизни?' or message.text == 'в чём смысл жизни?' or message.text == 'В чём смысл жизни' or message.text == 'в чём смысл жизни':
        bot.send_message(message.chat.id, 'Моей или твоей', parse_mode='html')
    elif message.text == 'Моей' or message.text == 'моей':
        bot.send_message(message.chat.id, 'Нету', parse_mode='html')
    elif message.text == 'Твоей' or message.text == 'твоей':
        bot.send_message(message.chat.id, 'Помощь всем и вся', parse_mode='html')
    elif message.text == 'Где я?' or message.text == 'где я?' or message.text == 'Где я' or message.text == 'где я':
        bot.send_message(message.chat.id, 'Там, где меня нет', parse_mode='html')
    elif message.text == 'Как тебя зовут?' or message.text == 'как тебя зовут?' or message.text == 'Как тебя зовут' or message.text == 'как тебя зовут':
        bot.send_message(message.chat.id, f'меня зовут {message.from_user.first_name}', parse_mode='html')
    elif message.text == 'Ты где?' or message.text == 'ты где?' or message.text == 'Ты где' or message.text == 'ты где':
        a = randint(1, 3)
        if a == 1:
            bot.send_message(message.chat.id,
                             'Если брать во внимание тот факт, что ты находишься где-то там, то я с большей вероятностью нахожусь где - то тут',
                             parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'К большому сожалению, не на Мальдивах', parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id,
                             'В твоей голове, в твоём сердце, в твоих мыслях. В данный момент в голосе, который ты слышишь d буквах, которые ты читаешь',
                             parse_mode='html')
    elif message.text == 'Сколько тебе лет?' or message.text == 'сколько тебе лет?' or message.text == 'Сколько тебе лет' or message.text == 'сколько тебе лет':
        a = randint(1, 3)
        if a == 1:
            bot.send_message(message.chat.id, 'Столько не живут', parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'Я не имею права разглашать государственные тайны',
                             parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id, 'Мне 100 по эльфийскому времени', parse_mode='html')


def users_reply(message):
    conn = sqlite3.connect('basadanneh.sqlite')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users1")
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: ******\n'
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, info)


bot.polling(none_stop=True)
