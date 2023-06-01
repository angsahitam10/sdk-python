# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/mint/v1beta1/mint.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63osmos/mint/v1beta1/mint.proto\x12\x13\x63osmos.mint.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x11\x61mino/amino.proto\"\xb2\x01\n\x06Minter\x12O\n\tinflation\x18\x01 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12W\n\x11\x61nnual_provisions\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\xb2\x03\n\x06Params\x12\x12\n\nmint_denom\x18\x01 \x01(\t\x12[\n\x15inflation_rate_change\x18\x02 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12S\n\rinflation_max\x18\x03 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12S\n\rinflation_min\x18\x04 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12Q\n\x0bgoal_bonded\x18\x05 \x01(\tB<\xd2\xb4-\ncosmos.Dec\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\x12\x17\n\x0f\x62locks_per_year\x18\x06 \x01(\x04:!\x98\xa0\x1f\x00\x8a\xe7\xb0*\x18\x63osmos-sdk/x/mint/ParamsB+Z)github.com/cosmos/cosmos-sdk/x/mint/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.mint.v1beta1.mint_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/cosmos/cosmos-sdk/x/mint/types'
  _MINTER.fields_by_name['inflation']._options = None
  _MINTER.fields_by_name['inflation']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _MINTER.fields_by_name['annual_provisions']._options = None
  _MINTER.fields_by_name['annual_provisions']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['inflation_rate_change']._options = None
  _PARAMS.fields_by_name['inflation_rate_change']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['inflation_max']._options = None
  _PARAMS.fields_by_name['inflation_max']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['inflation_min']._options = None
  _PARAMS.fields_by_name['inflation_min']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS.fields_by_name['goal_bonded']._options = None
  _PARAMS.fields_by_name['goal_bonded']._serialized_options = b'\322\264-\ncosmos.Dec\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000'
  _PARAMS._options = None
  _PARAMS._serialized_options = b'\230\240\037\000\212\347\260*\030cosmos-sdk/x/mint/Params'
  _MINTER._serialized_start=124
  _MINTER._serialized_end=302
  _PARAMS._serialized_start=305
  _PARAMS._serialized_end=739
# @@protoc_insertion_point(module_scope)
