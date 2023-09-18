import telebot

bot = telebot.TeleBot('6517864114:AAHZq_58aQi_MAnkj39ymzGREdczaDylxbg')
tasks = ['first', 'second']
flag = 'nix'
answers = {'first': '13', 'second': 'I love you', 'third': '20', 'forth': '10', 'fifth': 'Spiegel', 'sixth': '70773'}


@bot.message_handler(commands=['start'])
def start(msg):
    global flag
    flag = 'nix'
    first_msg = 'Hallo Lea, alles Gute zum Geburtstag!!!'
    second_msg = 'Heute werden du und ich eine kleine Quest spielen. Um Ihr Geschenk zu finden, müssen Sie mehrere Aufgaben erledigen.'
    third_msg = 'Spielregeln für heute: \n1) Wenn Sie etwas nicht verstehen, schreiben Sie mir. \n2) Sie müssen jede Antwort auf die Aufgabe an diesen Bot senden. \n3) Und versuchen Sie einfach, mich zu finden'
    messages = [first_msg, second_msg, third_msg]
    for m in messages:
        bot.send_message(msg.chat.id, m)

    forth_msg = 'Wenn Sie bereit sind, schreiben Sie etwas'
    bot.send_message(msg.chat.id, forth_msg)


def check(msg):
    if msg.text == answers[flag]:
        return True
    return False


def task1(msg):
    first_msg = 'Beginnen wir mit etwas Einfachem.'
    second_msg = 'Wie alt bin ich auf diesem Foto?'
    messages = [first_msg, second_msg]
    for m in messages:
        bot.send_message(msg.chat.id, m)
    photo = open('photo/1.jpg', 'rb')
    bot.send_photo(msg.chat.id, photo)


def task2(msg):
    first_msg = 'In der Nähe Ihrer Schule steht etwas, das nach dem ersten Bundeskanzler der Bundesrepublik Deutschland benannt ist'
    second_msg = 'Go there!'
    third_msg = 'Neben dem Namen dieses Ortes auf dem Geländer befindet sich ein Zettel mit einem Geheimwort für die Lösung dieser Aufgabe.'
    bot.send_message(msg.chat.id, first_msg)
    bot.send_message(msg.chat.id, second_msg)
    bot.send_message(msg.chat.id, third_msg)
    photo = open('photo/2.jpg', 'rb')
    bot.send_photo(msg.chat.id, photo)
    forth_msg = 'Hier ist ein kleiner Hinweis für Sie'
    bot.send_message(msg.chat.id, forth_msg)


def task3(msg):
    first_msg = 'Großartig, du hast diese Aufgabe erledigt. Dieses Foto wurde 2016 aufgenommen'
    bot.send_message(msg.chat.id, first_msg)
    photo = open('photo/3.jpg', 'rb')
    bot.send_photo(msg.chat.id, photo)
    second_msg = 'Gestern wurde mir an der Universität eine sehr schwierige Aufgabe gestellt. Ich hoffe, Sie können mir bei der Lösung helfen'
    bot.send_message(msg.chat.id, second_msg)


def task4(msg):
    first_msg = 'Ich habe diese Quest gestern Abend vorbereitet. Ich hatte solche Angst, weil es sehr dunkel war. Nur die Lichter auf der Brücke haben mich gerettet. Zählen Sie, wie viele es sind, sonst habe ich es vergessen...'
    bot.send_message(msg.chat.id, first_msg)


def task5(msg):
    first_msg = 'Morgens siehst du mich,\nAber nicht, wenn ich dunkel wie die Nacht bin.\nIch spiegele, was vor mir liegt,\nDoch ich habe keine Tiefe oder Höhe.\nWas bin ich?'
    second_msg = 'In Ingolstadt bin ich ganz groß und stehe nicht weit von dir entfernt. Finden Sie mich, ich habe eine Notiz bei mir'
    bot.send_message(msg.chat.id, first_msg)
    bot.send_message(msg.chat.id, second_msg)


def task6(msg):
    first_msg = 'Sie müssen einen fünfstelligen Code eingeben. Der Spiegel wird Ihnen helfen'
    photo = open('photo/6.jpg', 'rb')
    bot.send_photo(msg.chat.id, photo)
    bot.send_message(msg.chat.id, first_msg)


def end(msg):
    first_msg = 'Wunderbar. Sie haben Ihr Geschenk freigeschaltet. Es befindet sich am Theaterplatz. '
    second_msg = 'Gehen Sie schnell dort!'
    bot.send_message(msg.chat.id, first_msg)
    photo = open('photo/7.jpg', 'rb')
    bot.send_photo(msg.chat.id, photo)
    bot.send_message(msg.chat.id, second_msg)


@bot.message_handler()
def get_message(msg):
    global flag
    print(flag)
    if flag == 'nix':
        flag = 'first'
        task1(msg)
        return

    if flag == 'first':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch')
        else:
            flag = 'second'
            task2(msg)
            return

    elif flag == 'second':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch')
        else:
            flag = 'third'
            task3(msg)
            return

    elif flag == 'third':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch. Sei sehr vorsichtig')
        else:
            flag = 'forth'
            task4(msg)
            return

    elif flag == 'forth':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch')
        else:
            flag = 'fifth'
            task5(msg)
            return

    elif flag == 'fifth':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch')
        else:
            flag = 'sixth'
            task6(msg)
            return

    elif flag == 'sixth':
        if not check(msg):
            bot.send_message(msg.chat.id, 'Falsch. Sei sehr vorsichtig')
        else:
            flag = 'end'
            end(msg)

    elif flag == 'end':
        link = 'https://maps.app.goo.gl/FpJx8fjhw43wots89'
        bot.send_message(msg.chat.id, link)


bot.polling(none_stop=True)
