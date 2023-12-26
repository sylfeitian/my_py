import json
from collections import namedtuple

# Define the fields of the named tuple
fields = [
    "ab_test_groups",
    "android_id",
    "boottime",
    "carrier",
    "cellular_provider",
    "channel",
    "country",
    "device_name_digest",
    "device_type",
    "disk",
    "idfa",
    "imei",
    "ip",
    "jb",
    "language",
    "mac",
    "machine",
    "memory",
    "model",
    "oaid",
    "osn",
    "osv",
    "phone_type",
    "sys_updated_at",
    "time_zone",
    "ua",
    "umeng_token",
    "unique_device_id",
    "user_id",
    "v",
]

# Create the named tuple class
User = namedtuple("User", fields)

# Create an instance of the named tuple
user = User(
    ab_test_groups="1:B,2:B,3:B,7:B,$:A,11:B,13:A,14:B,15:B,16:B,17:B,18:B,19:B,20:B,21:B,22:A,23:B,24:B",
    android_id="",
    boottime="1679128033",
    carrier="中国电信",
    cellular_provider="",
    channel="app store",
    country="CN",
    device_name_digest="c3725328b80a0b2cd8cac086537fec34",
    device_type="Not Available",
    disk="255870980096",
    idfa="",
    imei="",
    ip="100.121.146.123:13320",
    jb=False,
    language="zh-Hans-CN",
    mac="",
    machine="iPhone13,2",
    memory="3882827776",
    model="D53gAP",
    oaid="",
    osn="iOS",
    osv="15.2",
    phone_type="iOS",
    sys_updated_at="1640228349.413610",
    time_zone="28800",
    ua="Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML,like Gecko) Mobile/15E148",
    umeng_token="b05ed10c1ad4a1882e972ec365baa7b47a5da96c55cfe39749535be3ef23e6bc",
    unique_device_id="1617207409757945856v6.3.2",
    user_id=0,
    v="6.4.1",
)

print(json.dumps(user._asdict()))

print(user.sys_updated_at)
