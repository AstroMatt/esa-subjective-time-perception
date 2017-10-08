from devutils.tests import Test


class LoggerTest(Test):
    fixtures = [
        'logger.json',
    ]

    assert_http_status = [
        {'status': 200, 'url': '/admin/logger/httprequest/'},
        {'status': 200, 'url': '/admin/logger/httprequest/add/'},
        {'status': 200, 'url': '/admin/logger/httprequest/1/change/'},

        {'status': 200, 'url': '/admin/logger/errorlogger/'},
        {'status': 200, 'url': '/admin/logger/errorlogger/add/'},
        {'status': 200, 'url': '/admin/logger/errorlogger/1/change/', 'skip': True},
    ]
