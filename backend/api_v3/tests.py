from devutils.tests import Test


class APIv3Test(Test):
    fixtures = [
        'api-v3.json',
    ]

    assert_http_status = [
        {'status': 200, 'url': '/admin/api_v3/result/'},
        {'status': 200, 'url': '/admin/api_v3/result/add/'},
        {'status': 200, 'url': '/admin/api_v3/result/1/change/', 'skip': True},
    ]
