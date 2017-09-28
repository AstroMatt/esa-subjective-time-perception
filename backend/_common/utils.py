import datetime


def json_datetime_decoder(data):

    for key, value in data.items():
        if not value:
            data[key] = None

        if 'datetime' in key:
            data[key] = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=datetime.timezone.utc)
        elif key == 'colors':
            data[key] = ','.join(value)

    return data
