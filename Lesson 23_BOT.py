import requests
import random

private_key = '5189445488:AAGA6S-dWiabmi2OhyRaGdjX3SQ9bMxOV7E'
url = f'https://api.telegram.org/bot{private_key}/'


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'hi' or get_message_text(
                    update).lower() == 'hello' or get_message_text(update).lower() == 'hey' or get_message_text(
                update).lower() == '/start':
                send_message(get_chat_id(update), "Greetings! Type 'Dice'")
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            elif get_message_text(update).lower() == 'qa03':
                send_message(get_chat_id(update), "Cloud")
            else:
                send_message(get_chat_id(update), "Sorry, I don't undersand you. Type dice :(")
            update_id += 1


if __name__ == '__main__':
    main()
