from devutils.tests import Test


class CommonTest(Test):
    fixtures = [
        'auth.user.json',
    ]

    assert_http_status = [
        {'status': 302, 'url': '/'},
        {'status': 200, 'url': '/admin/'},
        {'status': 200, 'url': '/index.html', 'skip': True},
        {'status': 200, 'url': '/cache.html', 'skip': True},
        {'status': 200, 'url': '/howto.html', 'skip': True},
        {'status': 200, 'url': '/_debug/index.html', 'skip': True},
        {'status': 200, 'url': '/_debug/main.js', 'skip': True},
    ]
