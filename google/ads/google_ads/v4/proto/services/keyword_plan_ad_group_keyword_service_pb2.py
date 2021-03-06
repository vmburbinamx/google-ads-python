# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads_v4/proto/services/keyword_plan_ad_group_keyword_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.google_ads.v4.proto.resources import keyword_plan_ad_group_keyword_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads_v4/proto/services/keyword_plan_ad_group_keyword_service.proto',
  package='google.ads.googleads.v4.services',
  syntax='proto3',
  serialized_options=_b('\n$com.google.ads.googleads.v4.servicesB%KeywordPlanAdGroupKeywordServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V4.Services\312\002 Google\\Ads\\GoogleAds\\V4\\Services\352\002$Google::Ads::GoogleAds::V4::Services'),
  serialized_pb=_b('\nRgoogle/ads/googleads_v4/proto/services/keyword_plan_ad_group_keyword_service.proto\x12 google.ads.googleads.v4.services\x1aKgoogle/ads/googleads_v4/proto/resources/keyword_plan_ad_group_keyword.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto\"x\n#GetKeywordPlanAdGroupKeywordRequest\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xe0\x41\x02\xfa\x41\x34\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword\"\xd2\x01\n\'MutateKeywordPlanAdGroupKeywordsRequest\x12\x18\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x03\xe0\x41\x02\x12]\n\noperations\x18\x02 \x03(\x0b\x32\x44.google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperationB\x03\xe0\x41\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\"\x94\x02\n\"KeywordPlanAdGroupKeywordOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12N\n\x06\x63reate\x18\x01 \x01(\x0b\x32<.google.ads.googleads.v4.resources.KeywordPlanAdGroupKeywordH\x00\x12N\n\x06update\x18\x02 \x01(\x0b\x32<.google.ads.googleads.v4.resources.KeywordPlanAdGroupKeywordH\x00\x12\x10\n\x06remove\x18\x03 \x01(\tH\x00\x42\x0b\n\toperation\"\xb7\x01\n(MutateKeywordPlanAdGroupKeywordsResponse\x12\x31\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.Status\x12X\n\x07results\x18\x02 \x03(\x0b\x32G.google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordResult\">\n%MutateKeywordPlanAdGroupKeywordResult\x12\x15\n\rresource_name\x18\x01 \x01(\t2\xdc\x04\n KeywordPlanAdGroupKeywordService\x12\xf9\x01\n\x1cGetKeywordPlanAdGroupKeyword\x12\x45.google.ads.googleads.v4.services.GetKeywordPlanAdGroupKeywordRequest\x1a<.google.ads.googleads.v4.resources.KeywordPlanAdGroupKeyword\"T\x82\xd3\xe4\x93\x02>\x12</v4/{resource_name=customers/*/keywordPlanAdGroupKeywords/*}\xda\x41\rresource_name\x12\x9e\x02\n MutateKeywordPlanAdGroupKeywords\x12I.google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest\x1aJ.google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsResponse\"c\x82\xd3\xe4\x93\x02\x44\"?/v4/customers/{customer_id=*}/keywordPlanAdGroupKeywords:mutate:\x01*\xda\x41\x16\x63ustomer_id,operations\x1a\x1b\xca\x41\x18googleads.googleapis.comB\x8c\x02\n$com.google.ads.googleads.v4.servicesB%KeywordPlanAdGroupKeywordServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v4/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V4.Services\xca\x02 Google\\Ads\\GoogleAds\\V4\\Services\xea\x02$Google::Ads::GoogleAds::V4::Servicesb\x06proto3')
  ,
  dependencies=[google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETKEYWORDPLANADGROUPKEYWORDREQUEST = _descriptor.Descriptor(
  name='GetKeywordPlanAdGroupKeywordRequest',
  full_name='google.ads.googleads.v4.services.GetKeywordPlanAdGroupKeywordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.GetKeywordPlanAdGroupKeywordRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002\372A4\n2googleads.googleapis.com/KeywordPlanAdGroupKeyword'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=491,
)


_MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST = _descriptor.Descriptor(
  name='MutateKeywordPlanAdGroupKeywordsRequest',
  full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\340A\002'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=494,
  serialized_end=704,
)


_KEYWORDPLANADGROUPKEYWORDOPERATION = _descriptor.Descriptor(
  name='KeywordPlanAdGroupKeywordOperation',
  full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation.update_mask', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation.create', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='update', full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation.update', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation.remove', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='operation', full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation.operation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=707,
  serialized_end=983,
)


_MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE = _descriptor.Descriptor(
  name='MutateKeywordPlanAdGroupKeywordsResponse',
  full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1169,
)


_MUTATEKEYWORDPLANADGROUPKEYWORDRESULT = _descriptor.Descriptor(
  name='MutateKeywordPlanAdGroupKeywordResult',
  full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1171,
  serialized_end=1233,
)

_MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST.fields_by_name['operations'].message_type = _KEYWORDPLANADGROUPKEYWORDOPERATION
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2._KEYWORDPLANADGROUPKEYWORD
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['update'].message_type = google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2._KEYWORDPLANADGROUPKEYWORD
_KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['create'])
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['create'].containing_oneof = _KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['update'])
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['update'].containing_oneof = _KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation']
_KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation'].fields.append(
  _KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['remove'])
_KEYWORDPLANADGROUPKEYWORDOPERATION.fields_by_name['remove'].containing_oneof = _KEYWORDPLANADGROUPKEYWORDOPERATION.oneofs_by_name['operation']
_MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE.fields_by_name['results'].message_type = _MUTATEKEYWORDPLANADGROUPKEYWORDRESULT
DESCRIPTOR.message_types_by_name['GetKeywordPlanAdGroupKeywordRequest'] = _GETKEYWORDPLANADGROUPKEYWORDREQUEST
DESCRIPTOR.message_types_by_name['MutateKeywordPlanAdGroupKeywordsRequest'] = _MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST
DESCRIPTOR.message_types_by_name['KeywordPlanAdGroupKeywordOperation'] = _KEYWORDPLANADGROUPKEYWORDOPERATION
DESCRIPTOR.message_types_by_name['MutateKeywordPlanAdGroupKeywordsResponse'] = _MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE
DESCRIPTOR.message_types_by_name['MutateKeywordPlanAdGroupKeywordResult'] = _MUTATEKEYWORDPLANADGROUPKEYWORDRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKeywordPlanAdGroupKeywordRequest = _reflection.GeneratedProtocolMessageType('GetKeywordPlanAdGroupKeywordRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETKEYWORDPLANADGROUPKEYWORDREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.keyword_plan_ad_group_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanAdGroupKeywordService.GetKeywordPlanAdGroupKeyword][google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordService.GetKeywordPlanAdGroupKeyword].
  
  
  Attributes:
      resource_name:
          Required. The resource name of the ad group keyword to fetch.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.GetKeywordPlanAdGroupKeywordRequest)
  ))
_sym_db.RegisterMessage(GetKeywordPlanAdGroupKeywordRequest)

MutateKeywordPlanAdGroupKeywordsRequest = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanAdGroupKeywordsRequest', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST,
  __module__ = 'google.ads.googleads_v4.proto.services.keyword_plan_ad_group_keyword_service_pb2'
  ,
  __doc__ = """Request message for
  [KeywordPlanAdGroupKeywordService.MutateKeywordPlanAdGroupKeywords][google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordService.MutateKeywordPlanAdGroupKeywords].
  
  
  Attributes:
      customer_id:
          Required. The ID of the customer whose Keyword Plan ad group
          keywords are being modified.
      operations:
          Required. The list of operations to perform on individual
          Keyword Plan ad group keywords.
      partial_failure:
          If true, successful operations will be carried out and invalid
          operations will return errors. If false, all operations will
          be carried out in one transaction if and only if they are all
          valid. Default is false.
      validate_only:
          If true, the request is validated but not executed. Only
          errors are returned, not results.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsRequest)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanAdGroupKeywordsRequest)

KeywordPlanAdGroupKeywordOperation = _reflection.GeneratedProtocolMessageType('KeywordPlanAdGroupKeywordOperation', (_message.Message,), dict(
  DESCRIPTOR = _KEYWORDPLANADGROUPKEYWORDOPERATION,
  __module__ = 'google.ads.googleads_v4.proto.services.keyword_plan_ad_group_keyword_service_pb2'
  ,
  __doc__ = """A single operation (create, update, remove) on a Keyword Plan ad group
  keyword.
  
  
  Attributes:
      update_mask:
          The FieldMask that determines which resource fields are
          modified in an update.
      operation:
          The mutate operation.
      create:
          Create operation: No resource name is expected for the new
          Keyword Plan ad group keyword.
      update:
          Update operation: The Keyword Plan ad group keyword is
          expected to have a valid resource name.
      remove:
          Remove operation: A resource name for the removed Keyword Plan
          ad group keyword is expected, in this format:  ``customers/{cu
          stomer_id}/keywordPlanAdGroupKeywords/{kp_ad_group_keyword_id}
          ``
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordOperation)
  ))
_sym_db.RegisterMessage(KeywordPlanAdGroupKeywordOperation)

MutateKeywordPlanAdGroupKeywordsResponse = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanAdGroupKeywordsResponse', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE,
  __module__ = 'google.ads.googleads_v4.proto.services.keyword_plan_ad_group_keyword_service_pb2'
  ,
  __doc__ = """Response message for a Keyword Plan ad group keyword mutate.
  
  
  Attributes:
      partial_failure_error:
          Errors that pertain to operation failures in the partial
          failure mode. Returned only when partial\_failure = true and
          all errors occur inside the operations. If any errors occur
          outside the operations (e.g. auth errors), we return an RPC
          level error.
      results:
          All results for the mutate.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordsResponse)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanAdGroupKeywordsResponse)

MutateKeywordPlanAdGroupKeywordResult = _reflection.GeneratedProtocolMessageType('MutateKeywordPlanAdGroupKeywordResult', (_message.Message,), dict(
  DESCRIPTOR = _MUTATEKEYWORDPLANADGROUPKEYWORDRESULT,
  __module__ = 'google.ads.googleads_v4.proto.services.keyword_plan_ad_group_keyword_service_pb2'
  ,
  __doc__ = """The result for the Keyword Plan ad group keyword mutate.
  
  
  Attributes:
      resource_name:
          Returned for successful operations.
  """,
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v4.services.MutateKeywordPlanAdGroupKeywordResult)
  ))
_sym_db.RegisterMessage(MutateKeywordPlanAdGroupKeywordResult)


DESCRIPTOR._options = None
_GETKEYWORDPLANADGROUPKEYWORDREQUEST.fields_by_name['resource_name']._options = None
_MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST.fields_by_name['customer_id']._options = None
_MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST.fields_by_name['operations']._options = None

_KEYWORDPLANADGROUPKEYWORDSERVICE = _descriptor.ServiceDescriptor(
  name='KeywordPlanAdGroupKeywordService',
  full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312A\030googleads.googleapis.com'),
  serialized_start=1236,
  serialized_end=1840,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeywordPlanAdGroupKeyword',
    full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordService.GetKeywordPlanAdGroupKeyword',
    index=0,
    containing_service=None,
    input_type=_GETKEYWORDPLANADGROUPKEYWORDREQUEST,
    output_type=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_keyword__plan__ad__group__keyword__pb2._KEYWORDPLANADGROUPKEYWORD,
    serialized_options=_b('\202\323\344\223\002>\022</v4/{resource_name=customers/*/keywordPlanAdGroupKeywords/*}\332A\rresource_name'),
  ),
  _descriptor.MethodDescriptor(
    name='MutateKeywordPlanAdGroupKeywords',
    full_name='google.ads.googleads.v4.services.KeywordPlanAdGroupKeywordService.MutateKeywordPlanAdGroupKeywords',
    index=1,
    containing_service=None,
    input_type=_MUTATEKEYWORDPLANADGROUPKEYWORDSREQUEST,
    output_type=_MUTATEKEYWORDPLANADGROUPKEYWORDSRESPONSE,
    serialized_options=_b('\202\323\344\223\002D\"?/v4/customers/{customer_id=*}/keywordPlanAdGroupKeywords:mutate:\001*\332A\026customer_id,operations'),
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDPLANADGROUPKEYWORDSERVICE)

DESCRIPTOR.services_by_name['KeywordPlanAdGroupKeywordService'] = _KEYWORDPLANADGROUPKEYWORDSERVICE

# @@protoc_insertion_point(module_scope)
