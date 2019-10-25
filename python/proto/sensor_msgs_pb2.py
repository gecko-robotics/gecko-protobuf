# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/sensor_msgs.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import standard_msgs_pb2 as proto_dot_standard__msgs__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/sensor_msgs.proto',
  package='sensor_msgs',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17proto/sensor_msgs.proto\x12\x0bsensor_msgs\x1a\x19proto/standard_msgs.proto\"\xdc\x01\n\x03Imu\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x32\n\x13linear_acceleration\x18\x02 \x01(\x0b\x32\x15.standard_msgs.Vector\x12/\n\x10\x61ngular_velocity\x18\x03 \x01(\x0b\x32\x15.standard_msgs.Vector\x12.\n\x0borientation\x18\x04 \x01(\x0b\x32\x19.standard_msgs.Quaternion\x12-\n\x0emagnetic_field\x18\x05 \x01(\x0b\x32\x15.standard_msgs.Vector\"\x99\x01\n\x07ImuInfo\x12\x1e\n\x16orientation_covariance\x18\x01 \x03(\x01\x12#\n\x1b\x61ngular_velocity_covariance\x18\x02 \x03(\x01\x12&\n\x1elinear_acceleration_covariance\x18\x03 \x03(\x01\x12!\n\x19magnetic_field_covariance\x18\x04 \x03(\x01\"|\n\x05Image\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\r\x12\x12\n\ncompressed\x18\x04 \x01(\x08\x12\x10\n\x08\x65ncoding\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12\x11\n\ttimestamp\x18\x07 \x01(\x01\"z\n\nCameraInfo\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\r\n\x05width\x18\x03 \x01(\r\x12\r\n\x01\x44\x18\x04 \x03(\x01\x42\x02\x10\x01\x12\r\n\x01K\x18\x05 \x03(\x01\x42\x02\x10\x01\x12\r\n\x01R\x18\x06 \x03(\x01\x42\x02\x10\x01\x12\r\n\x01P\x18\x07 \x03(\x01\x42\x02\x10\x01\"\x8a\x01\n\tLaserScan\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x17\n\x0f\x61ngle_increment\x18\x02 \x01(\x01\x12\x11\n\trange_min\x18\x03 \x01(\x01\x12\x11\n\trange_max\x18\x04 \x01(\x01\x12\x12\n\x06ranges\x18\x05 \x03(\x01\x42\x02\x10\x01\x12\x17\n\x0bintensities\x18\x06 \x03(\x01\x42\x02\x10\x01\"\xb5\x02\n\tNavSatFix\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\x12-\n\x06status\x18\x05 \x01(\x0e\x32\x1d.sensor_msgs.NavSatFix.Status\x12/\n\x07service\x18\x06 \x01(\x0e\x32\x1e.sensor_msgs.NavSatFix.Service\"6\n\x06Status\x12\x07\n\x03\x46IX\x10\x00\x12\x0b\n\x07SBASFIX\x10\x01\x12\x0b\n\x07GBASFIX\x10\x02\x12\t\n\x05NOFIX\x10\x03\"F\n\x07Service\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x07\n\x03GPS\x10\x01\x12\x0b\n\x07GLONASS\x10\x02\x12\x0b\n\x07\x43OMPASS\x10\x04\x12\x0b\n\x07GALILEO\x10\x08\"\xed\x02\n\x0c\x42\x61tteryState\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x02\x12\x0e\n\x06\x63harge\x18\x04 \x01(\x02\x12\x10\n\x08\x63\x61pacity\x18\x05 \x01(\x02\x12\x38\n\ntechnology\x18\x06 \x01(\x0e\x32$.sensor_msgs.BatteryState.Technology\x12\x30\n\x06status\x18\x07 \x01(\x0e\x32 .sensor_msgs.BatteryState.Status\"H\n\nTechnology\x12\x08\n\x04NIMH\x10\x00\x12\x08\n\x04LION\x10\x01\x12\x08\n\x04LIPO\x10\x02\x12\x08\n\x04LIFE\x10\x03\x12\x08\n\x04NICD\x10\x04\x12\x08\n\x04LIMN\x10\x05\"P\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08\x43HARGING\x10\x01\x12\x0f\n\x0b\x44ISCHARGING\x10\x02\x12\x10\n\x0cNOT_CHARGING\x10\x03\x12\x08\n\x04\x46ULL\x10\x04\"\xae\x01\n\x05Range\x12\x11\n\ttimestamp\x18\x01 \x01(\x01\x12%\n\x04type\x18\x02 \x01(\x0e\x32\x17.sensor_msgs.Range.Type\x12\x0b\n\x03\x66ov\x18\x03 \x01(\x02\x12\x11\n\trange_min\x18\x04 \x01(\x02\x12\x11\n\trange_max\x18\x05 \x01(\x02\x12\r\n\x05range\x18\x06 \x01(\x02\")\n\x04Type\x12\x0e\n\nULTRASOUND\x10\x00\x12\x06\n\x02IR\x10\x01\x12\t\n\x05LIDAR\x10\x02\x62\x06proto3')
  ,
  dependencies=[proto_dot_standard__msgs__pb2.DESCRIPTOR,])



_NAVSATFIX_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='sensor_msgs.NavSatFix.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIX', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SBASFIX', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GBASFIX', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOFIX', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1021,
  serialized_end=1075,
)
_sym_db.RegisterEnumDescriptor(_NAVSATFIX_STATUS)

_NAVSATFIX_SERVICE = _descriptor.EnumDescriptor(
  name='Service',
  full_name='sensor_msgs.NavSatFix.Service',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLONASS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPASS', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GALILEO', index=4, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1077,
  serialized_end=1147,
)
_sym_db.RegisterEnumDescriptor(_NAVSATFIX_SERVICE)

_BATTERYSTATE_TECHNOLOGY = _descriptor.EnumDescriptor(
  name='Technology',
  full_name='sensor_msgs.BatteryState.Technology',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NIMH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIPO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIFE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICD', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIMN', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1361,
  serialized_end=1433,
)
_sym_db.RegisterEnumDescriptor(_BATTERYSTATE_TECHNOLOGY)

_BATTERYSTATE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='sensor_msgs.BatteryState.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARGING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCHARGING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_CHARGING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1435,
  serialized_end=1515,
)
_sym_db.RegisterEnumDescriptor(_BATTERYSTATE_STATUS)

_RANGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='sensor_msgs.Range.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ULTRASOUND', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIDAR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1651,
  serialized_end=1692,
)
_sym_db.RegisterEnumDescriptor(_RANGE_TYPE)


_IMU = _descriptor.Descriptor(
  name='Imu',
  full_name='sensor_msgs.Imu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.Imu.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration', full_name='sensor_msgs.Imu.linear_acceleration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity', full_name='sensor_msgs.Imu.angular_velocity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orientation', full_name='sensor_msgs.Imu.orientation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnetic_field', full_name='sensor_msgs.Imu.magnetic_field', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=68,
  serialized_end=288,
)


_IMUINFO = _descriptor.Descriptor(
  name='ImuInfo',
  full_name='sensor_msgs.ImuInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orientation_covariance', full_name='sensor_msgs.ImuInfo.orientation_covariance', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular_velocity_covariance', full_name='sensor_msgs.ImuInfo.angular_velocity_covariance', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_acceleration_covariance', full_name='sensor_msgs.ImuInfo.linear_acceleration_covariance', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='magnetic_field_covariance', full_name='sensor_msgs.ImuInfo.magnetic_field_covariance', index=3,
      number=4, type=1, cpp_type=5, label=3,
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
  serialized_start=291,
  serialized_end=444,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='sensor_msgs.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='sensor_msgs.Image.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='sensor_msgs.Image.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='sensor_msgs.Image.depth', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compressed', full_name='sensor_msgs.Image.compressed', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoding', full_name='sensor_msgs.Image.encoding', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='sensor_msgs.Image.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.Image.timestamp', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=446,
  serialized_end=570,
)


_CAMERAINFO = _descriptor.Descriptor(
  name='CameraInfo',
  full_name='sensor_msgs.CameraInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.CameraInfo.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='sensor_msgs.CameraInfo.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='sensor_msgs.CameraInfo.width', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='D', full_name='sensor_msgs.CameraInfo.D', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='K', full_name='sensor_msgs.CameraInfo.K', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='R', full_name='sensor_msgs.CameraInfo.R', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='P', full_name='sensor_msgs.CameraInfo.P', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=572,
  serialized_end=694,
)


_LASERSCAN = _descriptor.Descriptor(
  name='LaserScan',
  full_name='sensor_msgs.LaserScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.LaserScan.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angle_increment', full_name='sensor_msgs.LaserScan.angle_increment', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='sensor_msgs.LaserScan.range_min', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='sensor_msgs.LaserScan.range_max', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ranges', full_name='sensor_msgs.LaserScan.ranges', index=4,
      number=5, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intensities', full_name='sensor_msgs.LaserScan.intensities', index=5,
      number=6, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
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
  serialized_start=697,
  serialized_end=835,
)


_NAVSATFIX = _descriptor.Descriptor(
  name='NavSatFix',
  full_name='sensor_msgs.NavSatFix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.NavSatFix.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='sensor_msgs.NavSatFix.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='sensor_msgs.NavSatFix.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='sensor_msgs.NavSatFix.altitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='sensor_msgs.NavSatFix.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='service', full_name='sensor_msgs.NavSatFix.service', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NAVSATFIX_STATUS,
    _NAVSATFIX_SERVICE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=838,
  serialized_end=1147,
)


_BATTERYSTATE = _descriptor.Descriptor(
  name='BatteryState',
  full_name='sensor_msgs.BatteryState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.BatteryState.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voltage', full_name='sensor_msgs.BatteryState.voltage', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current', full_name='sensor_msgs.BatteryState.current', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='charge', full_name='sensor_msgs.BatteryState.charge', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='sensor_msgs.BatteryState.capacity', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='technology', full_name='sensor_msgs.BatteryState.technology', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='sensor_msgs.BatteryState.status', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BATTERYSTATE_TECHNOLOGY,
    _BATTERYSTATE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1515,
)


_RANGE = _descriptor.Descriptor(
  name='Range',
  full_name='sensor_msgs.Range',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='sensor_msgs.Range.timestamp', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='sensor_msgs.Range.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fov', full_name='sensor_msgs.Range.fov', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_min', full_name='sensor_msgs.Range.range_min', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_max', full_name='sensor_msgs.Range.range_max', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range', full_name='sensor_msgs.Range.range', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RANGE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1518,
  serialized_end=1692,
)

_IMU.fields_by_name['linear_acceleration'].message_type = proto_dot_standard__msgs__pb2._VECTOR
_IMU.fields_by_name['angular_velocity'].message_type = proto_dot_standard__msgs__pb2._VECTOR
_IMU.fields_by_name['orientation'].message_type = proto_dot_standard__msgs__pb2._QUATERNION
_IMU.fields_by_name['magnetic_field'].message_type = proto_dot_standard__msgs__pb2._VECTOR
_NAVSATFIX.fields_by_name['status'].enum_type = _NAVSATFIX_STATUS
_NAVSATFIX.fields_by_name['service'].enum_type = _NAVSATFIX_SERVICE
_NAVSATFIX_STATUS.containing_type = _NAVSATFIX
_NAVSATFIX_SERVICE.containing_type = _NAVSATFIX
_BATTERYSTATE.fields_by_name['technology'].enum_type = _BATTERYSTATE_TECHNOLOGY
_BATTERYSTATE.fields_by_name['status'].enum_type = _BATTERYSTATE_STATUS
_BATTERYSTATE_TECHNOLOGY.containing_type = _BATTERYSTATE
_BATTERYSTATE_STATUS.containing_type = _BATTERYSTATE
_RANGE.fields_by_name['type'].enum_type = _RANGE_TYPE
_RANGE_TYPE.containing_type = _RANGE
DESCRIPTOR.message_types_by_name['Imu'] = _IMU
DESCRIPTOR.message_types_by_name['ImuInfo'] = _IMUINFO
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['CameraInfo'] = _CAMERAINFO
DESCRIPTOR.message_types_by_name['LaserScan'] = _LASERSCAN
DESCRIPTOR.message_types_by_name['NavSatFix'] = _NAVSATFIX
DESCRIPTOR.message_types_by_name['BatteryState'] = _BATTERYSTATE
DESCRIPTOR.message_types_by_name['Range'] = _RANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Imu = _reflection.GeneratedProtocolMessageType('Imu', (_message.Message,), {
  'DESCRIPTOR' : _IMU,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.Imu)
  })
_sym_db.RegisterMessage(Imu)

ImuInfo = _reflection.GeneratedProtocolMessageType('ImuInfo', (_message.Message,), {
  'DESCRIPTOR' : _IMUINFO,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.ImuInfo)
  })
_sym_db.RegisterMessage(ImuInfo)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.Image)
  })
_sym_db.RegisterMessage(Image)

CameraInfo = _reflection.GeneratedProtocolMessageType('CameraInfo', (_message.Message,), {
  'DESCRIPTOR' : _CAMERAINFO,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.CameraInfo)
  })
_sym_db.RegisterMessage(CameraInfo)

LaserScan = _reflection.GeneratedProtocolMessageType('LaserScan', (_message.Message,), {
  'DESCRIPTOR' : _LASERSCAN,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.LaserScan)
  })
_sym_db.RegisterMessage(LaserScan)

NavSatFix = _reflection.GeneratedProtocolMessageType('NavSatFix', (_message.Message,), {
  'DESCRIPTOR' : _NAVSATFIX,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.NavSatFix)
  })
_sym_db.RegisterMessage(NavSatFix)

BatteryState = _reflection.GeneratedProtocolMessageType('BatteryState', (_message.Message,), {
  'DESCRIPTOR' : _BATTERYSTATE,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.BatteryState)
  })
_sym_db.RegisterMessage(BatteryState)

Range = _reflection.GeneratedProtocolMessageType('Range', (_message.Message,), {
  'DESCRIPTOR' : _RANGE,
  '__module__' : 'proto.sensor_msgs_pb2'
  # @@protoc_insertion_point(class_scope:sensor_msgs.Range)
  })
_sym_db.RegisterMessage(Range)


_CAMERAINFO.fields_by_name['D']._options = None
_CAMERAINFO.fields_by_name['K']._options = None
_CAMERAINFO.fields_by_name['R']._options = None
_CAMERAINFO.fields_by_name['P']._options = None
_LASERSCAN.fields_by_name['ranges']._options = None
_LASERSCAN.fields_by_name['intensities']._options = None
# @@protoc_insertion_point(module_scope)