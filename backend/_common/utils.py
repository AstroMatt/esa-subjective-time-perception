import datetime
import json


def json_decode(request):
    def decode_json(obj):
        for key, value in obj.items():
            if 'datetime' in key:
                obj[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
            elif key == 'colors':
                obj[key] = ','.join(value)
        return obj
    return json.loads(request, object_hook=decode_json)
