# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/evidence/v1beta1/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/evidence/v1beta1/query.proto\x12\x17\x63osmos.evidence.v1beta1\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/api/annotations.proto\"s\n\x14QueryEvidenceRequest\x12M\n\revidence_hash\x18\x01 \x01(\x0c\x42\x36\x18\x01\xfa\xde\x1f\x30github.com/cometbft/cometbft/libs/bytes.HexBytes\x12\x0c\n\x04hash\x18\x02 \x01(\t\"?\n\x15QueryEvidenceResponse\x12&\n\x08\x65vidence\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"U\n\x17QueryAllEvidenceRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x7f\n\x18QueryAllEvidenceResponse\x12&\n\x08\x65vidence\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse2\xc5\x02\n\x05Query\x12\x9b\x01\n\x08\x45vidence\x12-.cosmos.evidence.v1beta1.QueryEvidenceRequest\x1a..cosmos.evidence.v1beta1.QueryEvidenceResponse\"0\x82\xd3\xe4\x93\x02*\x12(/cosmos/evidence/v1beta1/evidence/{hash}\x12\x9d\x01\n\x0b\x41llEvidence\x12\x30.cosmos.evidence.v1beta1.QueryAllEvidenceRequest\x1a\x31.cosmos.evidence.v1beta1.QueryAllEvidenceResponse\")\x82\xd3\xe4\x93\x02#\x12!/cosmos/evidence/v1beta1/evidenceB/Z-github.com/cosmos/cosmos-sdk/x/evidence/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.evidence.v1beta1.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/cosmos/cosmos-sdk/x/evidence/types'
  _QUERYEVIDENCEREQUEST.fields_by_name['evidence_hash']._options = None
  _QUERYEVIDENCEREQUEST.fields_by_name['evidence_hash']._serialized_options = b'\030\001\372\336\0370github.com/cometbft/cometbft/libs/bytes.HexBytes'
  _QUERY.methods_by_name['Evidence']._options = None
  _QUERY.methods_by_name['Evidence']._serialized_options = b'\202\323\344\223\002*\022(/cosmos/evidence/v1beta1/evidence/{hash}'
  _QUERY.methods_by_name['AllEvidence']._options = None
  _QUERY.methods_by_name['AllEvidence']._serialized_options = b'\202\323\344\223\002#\022!/cosmos/evidence/v1beta1/evidence'
  _QUERYEVIDENCEREQUEST._serialized_start=187
  _QUERYEVIDENCEREQUEST._serialized_end=302
  _QUERYEVIDENCERESPONSE._serialized_start=304
  _QUERYEVIDENCERESPONSE._serialized_end=367
  _QUERYALLEVIDENCEREQUEST._serialized_start=369
  _QUERYALLEVIDENCEREQUEST._serialized_end=454
  _QUERYALLEVIDENCERESPONSE._serialized_start=456
  _QUERYALLEVIDENCERESPONSE._serialized_end=583
  _QUERY._serialized_start=586
  _QUERY._serialized_end=911
# @@protoc_insertion_point(module_scope)
