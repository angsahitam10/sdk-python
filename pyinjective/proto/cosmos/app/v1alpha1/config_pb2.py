# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/app/v1alpha1/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/app/v1alpha1/config.proto\x12\x13\x63osmos.app.v1alpha1\x1a\x19google/protobuf/any.proto\"y\n\x06\x43onfig\x12\x32\n\x07modules\x18\x01 \x03(\x0b\x32!.cosmos.app.v1alpha1.ModuleConfig\x12;\n\x0fgolang_bindings\x18\x02 \x03(\x0b\x32\".cosmos.app.v1alpha1.GolangBinding\"\x7f\n\x0cModuleConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12;\n\x0fgolang_bindings\x18\x03 \x03(\x0b\x32\".cosmos.app.v1alpha1.GolangBinding\"?\n\rGolangBinding\x12\x16\n\x0einterface_type\x18\x01 \x01(\t\x12\x16\n\x0eimplementation\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.app.v1alpha1.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CONFIG']._serialized_start=84
  _globals['_CONFIG']._serialized_end=205
  _globals['_MODULECONFIG']._serialized_start=207
  _globals['_MODULECONFIG']._serialized_end=334
  _globals['_GOLANGBINDING']._serialized_start=336
  _globals['_GOLANGBINDING']._serialized_end=399
# @@protoc_insertion_point(module_scope)
