# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: tendermint/types/validator.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .tendermint import crypto


@dataclass
class ValidatorSet(betterproto.Message):
    validators: List["Validator"] = betterproto.message_field(1)
    proposer: "Validator" = betterproto.message_field(2)
    total_voting_power: int = betterproto.int64_field(3)


@dataclass
class Validator(betterproto.Message):
    address: bytes = betterproto.bytes_field(1)
    pub_key: crypto.PublicKey = betterproto.message_field(2)
    voting_power: int = betterproto.int64_field(3)
    proposer_priority: int = betterproto.int64_field(4)


@dataclass
class SimpleValidator(betterproto.Message):
    pub_key: crypto.PublicKey = betterproto.message_field(1)
    voting_power: int = betterproto.int64_field(2)
