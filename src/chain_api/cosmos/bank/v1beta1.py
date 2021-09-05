# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/bank/v1beta1/bank.proto, cosmos/bank/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
import grpclib

from .cosmos.base import v1beta1


@dataclass
class Params(betterproto.Message):
    """Params defines the parameters for the bank module."""

    send_enabled: List["SendEnabled"] = betterproto.message_field(1)
    default_send_enabled: bool = betterproto.bool_field(2)


@dataclass
class SendEnabled(betterproto.Message):
    """
    SendEnabled maps coin denom to a send_enabled status (whether a denom is
    sendable).
    """

    denom: str = betterproto.string_field(1)
    enabled: bool = betterproto.bool_field(2)


@dataclass
class Input(betterproto.Message):
    """Input models transaction input."""

    address: str = betterproto.string_field(1)
    coins: List[v1beta1.Coin] = betterproto.message_field(2)


@dataclass
class Output(betterproto.Message):
    """Output models transaction outputs."""

    address: str = betterproto.string_field(1)
    coins: List[v1beta1.Coin] = betterproto.message_field(2)


@dataclass
class Supply(betterproto.Message):
    """
    Supply represents a struct that passively keeps track of the total supply
    amounts in the network. This message is deprecated now that supply is
    indexed by denom.
    """

    total: List[v1beta1.Coin] = betterproto.message_field(1)


@dataclass
class DenomUnit(betterproto.Message):
    """
    DenomUnit represents a struct that describes a given denomination unit of
    the basic token.
    """

    # denom represents the string name of the given denom unit (e.g uatom).
    denom: str = betterproto.string_field(1)
    # exponent represents power of 10 exponent that one must raise the base_denom
    # to in order to equal the given DenomUnit's denom 1 denom = 1^exponent
    # base_denom (e.g. with a base_denom of uatom, one can create a DenomUnit of
    # 'atom' with exponent = 6, thus: 1 atom = 10^6 uatom).
    exponent: int = betterproto.uint32_field(2)
    # aliases is a list of string aliases for the given denom
    aliases: List[str] = betterproto.string_field(3)


@dataclass
class Metadata(betterproto.Message):
    """Metadata represents a struct that describes a basic token."""

    description: str = betterproto.string_field(1)
    # denom_units represents the list of DenomUnit's for a given coin
    denom_units: List["DenomUnit"] = betterproto.message_field(2)
    # base represents the base denom (should be the DenomUnit with exponent = 0).
    base: str = betterproto.string_field(3)
    # display indicates the suggested denom that should be displayed in clients.
    display: str = betterproto.string_field(4)
    # name defines the name of the token (eg: Cosmos Atom)
    name: str = betterproto.string_field(5)
    # symbol is the token symbol usually shown on exchanges (eg: ATOM). This can
    # be the same as the display.
    symbol: str = betterproto.string_field(6)


@dataclass
class MsgSend(betterproto.Message):
    """
    MsgSend represents a message to send coins from one account to another.
    """

    from_address: str = betterproto.string_field(1)
    to_address: str = betterproto.string_field(2)
    amount: List[v1beta1.Coin] = betterproto.message_field(3)


@dataclass
class MsgSendResponse(betterproto.Message):
    """MsgSendResponse defines the Msg/Send response type."""

    pass


@dataclass
class MsgMultiSend(betterproto.Message):
    """
    MsgMultiSend represents an arbitrary multi-in, multi-out send message.
    """

    inputs: List["Input"] = betterproto.message_field(1)
    outputs: List["Output"] = betterproto.message_field(2)


@dataclass
class MsgMultiSendResponse(betterproto.Message):
    """MsgMultiSendResponse defines the Msg/MultiSend response type."""

    pass


class MsgStub(betterproto.ServiceStub):
    """Msg defines the bank Msg service."""

    async def send(
        self,
        *,
        from_address: str = "",
        to_address: str = "",
        amount: List[v1beta1.Coin] = [],
    ) -> MsgSendResponse:
        """
        Send defines a method for sending coins from one account to another
        account.
        """

        request = MsgSend()
        request.from_address = from_address
        request.to_address = to_address
        if amount is not None:
            request.amount = amount

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Msg/Send",
            request,
            MsgSendResponse,
        )

    async def multi_send(
        self, *, inputs: List["Input"] = [], outputs: List["Output"] = []
    ) -> MsgMultiSendResponse:
        """
        MultiSend defines a method for sending coins from some accounts to
        other accounts.
        """

        request = MsgMultiSend()
        if inputs is not None:
            request.inputs = inputs
        if outputs is not None:
            request.outputs = outputs

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Msg/MultiSend",
            request,
            MsgMultiSendResponse,
        )
