import os
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from dotenv import load_dotenv
from log import logger
import random

from grpc_api.vk_message import get_nn_msg


load_dotenv()


def run():
    session = requests.Session()
    vk_session = vk_api.VkApi(token=os.getenv('TOKEN'))

    longpool = VkLongPoll(vk_session)
    vk = vk_session.get_api()
    for event in longpool.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            vk.messages.send(
                user_id=event.user_id,
                #message=get_nn_msg(event.user_id, event.text),
                message=event.text,
                random_id=random.randint(-pow(2, 16), pow(2, 16) - 1)
            )


run()
