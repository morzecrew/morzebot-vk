# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import grpc_api.message.vk_message_pb2 as vk__message__pb2


class VkSerivceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.receive_vk_msg = channel.unary_unary(
                '/vk_message.VkSerivce/receive_vk_msg',
                request_serializer=vk__message__pb2.VkMessage.SerializeToString,
                response_deserializer=vk__message__pb2.VkMessage.FromString,
                )


class VkSerivceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def receive_vk_msg(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VkSerivceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'receive_vk_msg': grpc.unary_unary_rpc_method_handler(
                    servicer.receive_vk_msg,
                    request_deserializer=vk__message__pb2.VkMessage.FromString,
                    response_serializer=vk__message__pb2.VkMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vk_message.VkSerivce', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class VkSerivce(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def receive_vk_msg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vk_message.VkSerivce/receive_vk_msg',
            vk__message__pb2.VkMessage.SerializeToString,
            vk__message__pb2.VkMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
