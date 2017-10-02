from devutils.tests import Test


class APIv3Test(Test):
    fixtures = [
        'fixtures/api-v3.json',
    ]

    assert_http_200 = [
        '/admin/api_v3/result/',
        '/admin/api_v3/result/add/',
    ]
