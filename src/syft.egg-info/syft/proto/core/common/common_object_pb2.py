# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/common/common_object.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/common/common_object.proto",
    package="syft.core.common",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%proto/core/common/common_object.proto\x12\x10syft.core.common"x\n\x0c\x43ommonObject\x12)\n\nuid_object\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12=\n\x15object_with_id_object\x18\x02 \x01(\x0b\x32\x1e.syft.core.common.ObjectWithID"1\n\x0cObjectWithID\x12!\n\x02id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID"\x14\n\x03UID\x12\r\n\x05value\x18\x01 \x01(\x0c\x62\x06proto3',
)


_COMMONOBJECT = _descriptor.Descriptor(
    name="CommonObject",
    full_name="syft.core.common.CommonObject",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uid_object",
            full_name="syft.core.common.CommonObject.uid_object",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="object_with_id_object",
            full_name="syft.core.common.CommonObject.object_with_id_object",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=59,
    serialized_end=179,
)


_OBJECTWITHID = _descriptor.Descriptor(
    name="ObjectWithID",
    full_name="syft.core.common.ObjectWithID",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="id",
            full_name="syft.core.common.ObjectWithID.id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=181,
    serialized_end=230,
)


_UID = _descriptor.Descriptor(
    name="UID",
    full_name="syft.core.common.UID",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="syft.core.common.UID.value",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=232,
    serialized_end=252,
)

_COMMONOBJECT.fields_by_name["uid_object"].message_type = _UID
_COMMONOBJECT.fields_by_name["object_with_id_object"].message_type = _OBJECTWITHID
_OBJECTWITHID.fields_by_name["id"].message_type = _UID
DESCRIPTOR.message_types_by_name["CommonObject"] = _COMMONOBJECT
DESCRIPTOR.message_types_by_name["ObjectWithID"] = _OBJECTWITHID
DESCRIPTOR.message_types_by_name["UID"] = _UID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommonObject = _reflection.GeneratedProtocolMessageType(
    "CommonObject",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMONOBJECT,
        "__module__": "proto.core.common.common_object_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.common.CommonObject)
    },
)
_sym_db.RegisterMessage(CommonObject)

ObjectWithID = _reflection.GeneratedProtocolMessageType(
    "ObjectWithID",
    (_message.Message,),
    {
        "DESCRIPTOR": _OBJECTWITHID,
        "__module__": "proto.core.common.common_object_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.common.ObjectWithID)
    },
)
_sym_db.RegisterMessage(ObjectWithID)

UID = _reflection.GeneratedProtocolMessageType(
    "UID",
    (_message.Message,),
    {
        "DESCRIPTOR": _UID,
        "__module__": "proto.core.common.common_object_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.common.UID)
    },
)
_sym_db.RegisterMessage(UID)


# @@protoc_insertion_point(module_scope)
