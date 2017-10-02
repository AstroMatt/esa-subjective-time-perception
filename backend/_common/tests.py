from devutils.tests import Test


class CommonTest(Test):
    fixtures = [
        'fixtures/common.json',
    ]

    assert_http_200 = [
        '/index.html',
        '/cache.html',
        '/howto.html',
        '/_debug/index.html',
        '/_debug/main.js',
        '/admin/',
    ]
