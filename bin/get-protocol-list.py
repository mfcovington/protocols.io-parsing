import json
import os
import urllib.parse
import urllib.request

PROTOCOLS_IO_ACCESS_TOKEN = os.environ['PROTOCOLS_IO_ACCESS_TOKEN']

url = 'https://protocols.io/api/open/get_protocols'
values = {
    'access_token': PROTOCOLS_IO_ACCESS_TOKEN,
}

data = urllib.parse.urlencode(values).encode("utf-8")
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()

for protocol in protocol_list:
    print('{}: {}'.format(protocol['protocol_id'], protocol['protocol_name']))
