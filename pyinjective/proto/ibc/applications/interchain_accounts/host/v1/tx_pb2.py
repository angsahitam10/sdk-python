# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/applications/interchain_accounts/host/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.applications.interchain_accounts.host.v1 import host_pb2 as ibc_dot_applications_dot_interchain__accounts_dot_host_dot_v1_dot_host__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5ibc/applications/interchain_accounts/host/v1/tx.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto\x1a\x37ibc/applications/interchain_accounts/host/v1/host.proto\"p\n\x0fMsgUpdateParams\x12\x11\n\tauthority\x18\x01 \x01(\t\x12J\n\x06params\x18\x02 \x01(\x0b\x32\x34.ibc.applications.interchain_accounts.host.v1.ParamsB\x04\xc8\xde\x1f\x00\"\x19\n\x17MsgUpdateParamsResponse2\x9c\x01\n\x03Msg\x12\x94\x01\n\x0cUpdateParams\x12=.ibc.applications.interchain_accounts.host.v1.MsgUpdateParams\x1a\x45.ibc.applications.interchain_accounts.host.v1.MsgUpdateParamsResponseBLZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types'
  _MSGUPDATEPARAMS.fields_by_name['params']._options = None
  _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _MSGUPDATEPARAMS._serialized_start=182
  _MSGUPDATEPARAMS._serialized_end=294
  _MSGUPDATEPARAMSRESPONSE._serialized_start=296
  _MSGUPDATEPARAMSRESPONSE._serialized_end=321
  _MSG._serialized_start=324
  _MSG._serialized_end=480
# @@protoc_insertion_point(module_scope)
