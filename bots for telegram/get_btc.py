import requests
from yobit import get_btc
from time import sleep

token = '**********************************************'
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chai_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {
            'chat_id': chai_id,
            'text': message_text
        }
        return message
    return None


def send_messuge(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    # Отвечать только на новые смс
    # получаем update_id каждого обновления, и затем сравнивать новую с посл
    # d = get_updates()
    # print(type(d))
    # with open('updates.json', 'w', encoding='utf-8') as file:
    #     json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            # if text == '/btc':
            if 'курс' in text:
                send_messuge(chat_id, get_btc())
        else:
            continue

        sleep(1)


if __name__ == '__main__':
    main()
