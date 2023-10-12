# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from exchange import injective_oracle_rpc_pb2 as exchange_dot_injective__oracle__rpc__pb2


class InjectiveOracleRPCStub(object):
    """InjectiveOracleRPC defines gRPC API of Exchange Oracle provider.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.OracleList = channel.unary_unary(
                '/injective_oracle_rpc.InjectiveOracleRPC/OracleList',
                request_serializer=exchange_dot_injective__oracle__rpc__pb2.OracleListRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__oracle__rpc__pb2.OracleListResponse.FromString,
                )
        self.Price = channel.unary_unary(
                '/injective_oracle_rpc.InjectiveOracleRPC/Price',
                request_serializer=exchange_dot_injective__oracle__rpc__pb2.PriceRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__oracle__rpc__pb2.PriceResponse.FromString,
                )
        self.StreamPrices = channel.unary_stream(
                '/injective_oracle_rpc.InjectiveOracleRPC/StreamPrices',
                request_serializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesResponse.FromString,
                )
        self.StreamPricesByMarkets = channel.unary_stream(
                '/injective_oracle_rpc.InjectiveOracleRPC/StreamPricesByMarkets',
                request_serializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsRequest.SerializeToString,
                response_deserializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsResponse.FromString,
                )


class InjectiveOracleRPCServicer(object):
    """InjectiveOracleRPC defines gRPC API of Exchange Oracle provider.
    """

    def OracleList(self, request, context):
        """List all oracles
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Price(self, request, context):
        """Gets the price of the oracle
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamPrices(self, request, context):
        """StreamPrices streams new price changes for a specified oracle. If no oracles
        are provided, all price changes are streamed.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamPricesByMarkets(self, request, context):
        """StreamPrices streams new price changes markets
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InjectiveOracleRPCServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'OracleList': grpc.unary_unary_rpc_method_handler(
                    servicer.OracleList,
                    request_deserializer=exchange_dot_injective__oracle__rpc__pb2.OracleListRequest.FromString,
                    response_serializer=exchange_dot_injective__oracle__rpc__pb2.OracleListResponse.SerializeToString,
            ),
            'Price': grpc.unary_unary_rpc_method_handler(
                    servicer.Price,
                    request_deserializer=exchange_dot_injective__oracle__rpc__pb2.PriceRequest.FromString,
                    response_serializer=exchange_dot_injective__oracle__rpc__pb2.PriceResponse.SerializeToString,
            ),
            'StreamPrices': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamPrices,
                    request_deserializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesRequest.FromString,
                    response_serializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesResponse.SerializeToString,
            ),
            'StreamPricesByMarkets': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamPricesByMarkets,
                    request_deserializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsRequest.FromString,
                    response_serializer=exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective_oracle_rpc.InjectiveOracleRPC', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InjectiveOracleRPC(object):
    """InjectiveOracleRPC defines gRPC API of Exchange Oracle provider.
    """

    @staticmethod
    def OracleList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_oracle_rpc.InjectiveOracleRPC/OracleList',
            exchange_dot_injective__oracle__rpc__pb2.OracleListRequest.SerializeToString,
            exchange_dot_injective__oracle__rpc__pb2.OracleListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Price(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/injective_oracle_rpc.InjectiveOracleRPC/Price',
            exchange_dot_injective__oracle__rpc__pb2.PriceRequest.SerializeToString,
            exchange_dot_injective__oracle__rpc__pb2.PriceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_oracle_rpc.InjectiveOracleRPC/StreamPrices',
            exchange_dot_injective__oracle__rpc__pb2.StreamPricesRequest.SerializeToString,
            exchange_dot_injective__oracle__rpc__pb2.StreamPricesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamPricesByMarkets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/injective_oracle_rpc.InjectiveOracleRPC/StreamPricesByMarkets',
            exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsRequest.SerializeToString,
            exchange_dot_injective__oracle__rpc__pb2.StreamPricesByMarketsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
