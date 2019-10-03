BOT_TOKEN = '649207486:AAGrtOkaZB6tePNICrqsX641jWJBXGCT-YU'

def log(message):
    print('\n ------------')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1} (username: {4}). (id = {2}) \nТекст = {3}'.format(message.from_user.first_name,
                                                                            message.from_user.last_name,
                                                                            str(message.from_user.id),
                                                                            message.text,
                                                                            message.from_user.username))