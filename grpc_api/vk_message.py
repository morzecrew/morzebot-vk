import grpc
from grpc_api.message import vk_message_pb2, vk_message_pb2_grpc
from log import logger


def get_nn_msg(_user_id: int, _message: str):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = vk_message_pb2_grpc.VkSerivceStub(channel)
        response: vk_message_pb2.VkMessage = stub.receive_vk_msg(vk_message_pb2.VkMessage(_user_id, _message))
    
    logger.success(f"Vk message from server: {response.message}")
    return response.message
