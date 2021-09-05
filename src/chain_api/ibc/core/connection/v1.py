# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ibc/core/connection/v1/connection.proto, ibc/core/connection/v1/query.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
import grpclib

from .cosmos.base.query import v1beta1
from .google import protobuf
from .ibc.core.client import v1
from .ibc.core.commitment import v1


class State(betterproto.Enum):
    """
    State defines if a connection is in one of the following states: INIT,
    TRYOPEN, OPEN or UNINITIALIZED.
    """

    # Default State
    STATE_UNINITIALIZED_UNSPECIFIED = 0
    # A connection end has just started the opening handshake.
    STATE_INIT = 1
    # A connection end has acknowledged the handshake step on the counterparty
    # chain.
    STATE_TRYOPEN = 2
    # A connection end has completed the handshake.
    STATE_OPEN = 3


@dataclass
class MsgConnectionOpenInit(betterproto.Message):
    """
    MsgConnectionOpenInit defines the msg sent by an account on Chain A to
    initialize a connection with Chain B.
    """

    client_id: str = betterproto.string_field(1)
    connection_id: str = betterproto.string_field(2)
    counterparty: "Counterparty" = betterproto.message_field(3)
    version: str = betterproto.string_field(4)
    signer: str = betterproto.string_field(5)


@dataclass
class MsgConnectionOpenTry(betterproto.Message):
    """
    MsgConnectionOpenTry defines a msg sent by a Relayer to try to open a
    connection on Chain B.
    """

    client_id: str = betterproto.string_field(1)
    desired_connection_id: str = betterproto.string_field(2)
    counterparty_chosen_connection_id: str = betterproto.string_field(3)
    client_state: protobuf.Any = betterproto.message_field(4)
    counterparty: "Counterparty" = betterproto.message_field(5)
    counterparty_versions: List[str] = betterproto.string_field(6)
    proof_height: v1.Height = betterproto.message_field(7)
    # proof of the initialization the connection on Chain A: `UNITIALIZED ->
    # INIT`
    proof_init: bytes = betterproto.bytes_field(8)
    # proof of client state included in message
    proof_client: bytes = betterproto.bytes_field(9)
    # proof of client consensus state
    proof_consensus: bytes = betterproto.bytes_field(10)
    consensus_height: v1.Height = betterproto.message_field(11)
    signer: str = betterproto.string_field(12)


@dataclass
class MsgConnectionOpenAck(betterproto.Message):
    """
    MsgConnectionOpenAck defines a msg sent by a Relayer to Chain A to
    acknowledge the change of connection state to TRYOPEN on Chain B.
    """

    connection_id: str = betterproto.string_field(1)
    counterparty_connection_id: str = betterproto.string_field(2)
    version: str = betterproto.string_field(3)
    client_state: protobuf.Any = betterproto.message_field(4)
    proof_height: v1.Height = betterproto.message_field(5)
    # proof of the initialization the connection on Chain B: `UNITIALIZED ->
    # TRYOPEN`
    proof_try: bytes = betterproto.bytes_field(6)
    # proof of client state included in message
    proof_client: bytes = betterproto.bytes_field(7)
    # proof of client consensus state
    proof_consensus: bytes = betterproto.bytes_field(8)
    consensus_height: v1.Height = betterproto.message_field(9)
    signer: str = betterproto.string_field(10)


@dataclass
class MsgConnectionOpenConfirm(betterproto.Message):
    """
    MsgConnectionOpenConfirm defines a msg sent by a Relayer to Chain B to
    acknowledge the change of connection state to OPEN on Chain A.
    """

    connection_id: str = betterproto.string_field(1)
    # proof for the change of the connection state on Chain A: `INIT -> OPEN`
    proof_ack: bytes = betterproto.bytes_field(2)
    proof_height: v1.Height = betterproto.message_field(3)
    signer: str = betterproto.string_field(4)


@dataclass
class ConnectionEnd(betterproto.Message):
    """
    ConnectionEnd defines a stateful object on a chain connected to another
    separate one. NOTE: there must only be 2 defined ConnectionEnds to
    establish a connection between two chains.
    """

    # client associated with this connection.
    client_id: str = betterproto.string_field(1)
    # IBC version which can be utilised to determine encodings or protocols for
    # channels or packets utilising this connection
    versions: List[str] = betterproto.string_field(2)
    # current state of the connection end.
    state: "State" = betterproto.enum_field(3)
    # counterparty chain associated with this connection.
    counterparty: "Counterparty" = betterproto.message_field(4)


@dataclass
class IdentifiedConnection(betterproto.Message):
    """
    IdentifiedConnection defines a connection with additional connection
    identifier field.
    """

    # connection identifier.
    id: str = betterproto.string_field(1)
    # client associated with this connection.
    client_id: str = betterproto.string_field(2)
    # IBC version which can be utilised to determine encodings or protocols for
    # channels or packets utilising this connection
    versions: List[str] = betterproto.string_field(3)
    # current state of the connection end.
    state: "State" = betterproto.enum_field(4)
    # counterparty chain associated with this connection.
    counterparty: "Counterparty" = betterproto.message_field(5)


@dataclass
class Counterparty(betterproto.Message):
    """
    Counterparty defines the counterparty chain associated with a connection
    end.
    """

    # identifies the client on the counterparty chain associated with a given
    # connection.
    client_id: str = betterproto.string_field(1)
    # identifies the connection end on the counterparty chain associated with a
    # given connection.
    connection_id: str = betterproto.string_field(2)
    # commitment merkle prefix of the counterparty chain
    prefix: v1.MerklePrefix = betterproto.message_field(3)


@dataclass
class ClientPaths(betterproto.Message):
    """ClientPaths define all the connection paths for a client state."""

    # list of connection paths
    paths: List[str] = betterproto.string_field(1)


@dataclass
class ConnectionPaths(betterproto.Message):
    """
    ConnectionPaths define all the connection paths for a given client state.
    """

    # client state unique identifier
    client_id: str = betterproto.string_field(1)
    # list of connection paths
    paths: List[str] = betterproto.string_field(2)


@dataclass
class Version(betterproto.Message):
    """
    Version defines the versioning scheme used to negotiate the IBC verison in
    the connection handshake.
    """

    # unique version identifier
    identifier: str = betterproto.string_field(1)
    # list of features compatible with the specified identifier
    features: List[str] = betterproto.string_field(2)


@dataclass
class QueryConnectionRequest(betterproto.Message):
    """
    QueryConnectionRequest is the request type for the Query/Connection RPC
    method
    """

    # connection unique identifier
    connection_id: str = betterproto.string_field(1)


@dataclass
class QueryConnectionResponse(betterproto.Message):
    """
    QueryConnectionResponse is the response type for the Query/Connection RPC
    method. Besides the connection end, it includes a proof and the height from
    which the proof was retrieved.
    """

    # connection associated with the request identifier
    connection: "ConnectionEnd" = betterproto.message_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # merkle proof path
    proof_path: str = betterproto.string_field(3)
    # height at which the proof was retrieved
    proof_height: v1.Height = betterproto.message_field(4)


@dataclass
class QueryConnectionsRequest(betterproto.Message):
    """
    QueryConnectionsRequest is the request type for the Query/Connections RPC
    method
    """

    pagination: v1beta1.PageRequest = betterproto.message_field(1)


@dataclass
class QueryConnectionsResponse(betterproto.Message):
    """
    QueryConnectionsResponse is the response type for the Query/Connections RPC
    method.
    """

    # list of stored connections of the chain.
    connections: List["IdentifiedConnection"] = betterproto.message_field(1)
    # pagination response
    pagination: v1beta1.PageResponse = betterproto.message_field(2)
    # query block height
    height: v1.Height = betterproto.message_field(3)


@dataclass
class QueryClientConnectionsRequest(betterproto.Message):
    """
    QueryClientConnectionsRequest is the request type for the
    Query/ClientConnections RPC method
    """

    # client identifier associated with a connection
    client_id: str = betterproto.string_field(1)


@dataclass
class QueryClientConnectionsResponse(betterproto.Message):
    """
    QueryClientConnectionsResponse is the response type for the
    Query/ClientConnections RPC method
    """

    # slice of all the connection paths associated with a client.
    connection_paths: List[str] = betterproto.string_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # merkle proof path
    proof_path: str = betterproto.string_field(3)
    # height at which the proof was generated
    proof_height: v1.Height = betterproto.message_field(4)


@dataclass
class QueryConnectionClientStateRequest(betterproto.Message):
    """
    QueryConnectionClientStateRequest is the request type for the
    Query/ConnectionClientState RPC method
    """

    # connection identifier
    connection_id: str = betterproto.string_field(1)


@dataclass
class QueryConnectionClientStateResponse(betterproto.Message):
    """
    QueryConnectionClientStateResponse is the response type for the
    Query/ConnectionClientState RPC method
    """

    # client state associated with the channel
    identified_client_state: v1.IdentifiedClientState = betterproto.message_field(1)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(2)
    # merkle proof path
    proof_path: str = betterproto.string_field(3)
    # height at which the proof was retrieved
    proof_height: v1.Height = betterproto.message_field(4)


@dataclass
class QueryConnectionConsensusStateRequest(betterproto.Message):
    """
    QueryConnectionConsensusStateRequest is the request type for the
    Query/ConnectionConsensusState RPC method
    """

    # connection identifier
    connection_id: str = betterproto.string_field(1)
    version_number: int = betterproto.uint64_field(2)
    version_height: int = betterproto.uint64_field(3)


@dataclass
class QueryConnectionConsensusStateResponse(betterproto.Message):
    """
    QueryConnectionConsensusStateResponse is the response type for the
    Query/ConnectionConsensusState RPC method
    """

    # consensus state associated with the channel
    consensus_state: protobuf.Any = betterproto.message_field(1)
    # client ID associated with the consensus state
    client_id: str = betterproto.string_field(2)
    # merkle proof of existence
    proof: bytes = betterproto.bytes_field(3)
    # merkle proof path
    proof_path: str = betterproto.string_field(4)
    # height at which the proof was retrieved
    proof_height: v1.Height = betterproto.message_field(5)


class QueryStub(betterproto.ServiceStub):
    """Query provides defines the gRPC querier service"""

    async def connection(self, *, connection_id: str = "") -> QueryConnectionResponse:
        """Connection queries an IBC connection end."""

        request = QueryConnectionRequest()
        request.connection_id = connection_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connection",
            request,
            QueryConnectionResponse,
        )

    async def connections(
        self, *, pagination: Optional[v1beta1.PageRequest] = None
    ) -> QueryConnectionsResponse:
        """Connections queries all the IBC connections of a chain."""

        request = QueryConnectionsRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/Connections",
            request,
            QueryConnectionsResponse,
        )

    async def client_connections(
        self, *, client_id: str = ""
    ) -> QueryClientConnectionsResponse:
        """
        ClientConnections queries the connection paths associated with a client
        state.
        """

        request = QueryClientConnectionsRequest()
        request.client_id = client_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ClientConnections",
            request,
            QueryClientConnectionsResponse,
        )

    async def connection_client_state(
        self, *, connection_id: str = ""
    ) -> QueryConnectionClientStateResponse:
        """
        ConnectionClientState queries the client state associated with the
        connection.
        """

        request = QueryConnectionClientStateRequest()
        request.connection_id = connection_id

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionClientState",
            request,
            QueryConnectionClientStateResponse,
        )

    async def connection_consensus_state(
        self,
        *,
        connection_id: str = "",
        version_number: int = 0,
        version_height: int = 0,
    ) -> QueryConnectionConsensusStateResponse:
        """
        ConnectionConsensusState queries the consensus state associated with
        the connection.
        """

        request = QueryConnectionConsensusStateRequest()
        request.connection_id = connection_id
        request.version_number = version_number
        request.version_height = version_height

        return await self._unary_unary(
            "/ibc.core.connection.v1.Query/ConnectionConsensusState",
            request,
            QueryConnectionConsensusStateResponse,
        )
