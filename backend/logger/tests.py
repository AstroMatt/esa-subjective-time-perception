from devutils.tests import Test


class LoggerTest(Test):
    fixtures = [
        'fixtures/logger.json',
    ]

    assert_http_200 = [
        '/admin/logger/httprequest/',
        '/admin/logger/httprequest/add/',

        '/admin/logger/errorlogger/',
        '/admin/logger/errorlogger/add/'
    ]
