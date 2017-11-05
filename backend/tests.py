import logging
from django.contrib.auth.models import User
from django.test import TestCase


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime).19s] %(levelname).4s %(message)s')


class Test(TestCase):

    assert_http_status = [
    ]

    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.user = User.objects.create_superuser('testrunner', 'test@test.com', 'testrunner')
        self.client.login(username='testrunner', password='testrunner')

    def tearDown(self):
        self.client.logout()
        self.user.delete()

    def test_url(self):
        errors = []

        for row in self.assert_http_status:
            url = row['url']
            status = row['status']

            if row.get('skip'):
                msg = 'skip'
                logging.warning(f'{msg:4} {url}')
                continue

            response = self.client.get(url)

            if response.status_code == status:
                self.logger.info(f'{response.status_code:4} {url}')
            else:
                self.logger.error(f'{response.status_code:4} {url}')
                errors.append(url)

        if errors:
            raise AssertionError(f'HTTP errors {errors}')
