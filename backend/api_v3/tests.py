import json
from backend.tests import Test


class APIv3Test(Test):
    fixtures = [
        'api-v3.json',
    ]

    assert_http_status = [
        {'status': 200, 'url': '/admin/api_v3/result/'},
        {'status': 200, 'url': '/admin/api_v3/result/add/'},
        {'status': 200, 'url': '/admin/api_v3/result/1/change/'},
    ]

    def test_API_OPTIONS(self):
        return

    def test_API_POST(self):
        data = json.loads('{"results":true,"device":"lcd","location":"internet","regularity":5,"timeout":2,"colors":["green","blue","yellow","red","white"],"clicks":[{"datetime":"2017-10-03T10:05:45.833Z","color":"green"},{"datetime":"2017-10-03T10:05:46.529Z","color":"green"},{"datetime":"2017-10-03T10:05:46.731Z","color":"green"},{"datetime":"2017-10-03T10:05:46.914Z","color":"green"},{"datetime":"2017-10-03T10:05:47.127Z","color":"green"},{"datetime":"2017-10-03T10:05:47.400Z","color":"green"},{"datetime":"2017-10-03T10:05:47.627Z","color":"green"},{"datetime":"2017-10-03T10:05:48.606Z","color":"blue"},{"datetime":"2017-10-03T10:05:48.872Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.040Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.223Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.396Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.569Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.769Z","color":"blue"},{"datetime":"2017-10-03T10:05:49.994Z","color":"blue"},{"datetime":"2017-10-03T10:05:50.184Z","color":"blue"},{"datetime":"2017-10-03T10:05:50.414Z","color":"blue"},{"datetime":"2017-10-03T10:05:50.606Z","color":"blue"},{"datetime":"2017-10-03T10:05:51.192Z","color":"yellow"},{"datetime":"2017-10-03T10:05:51.463Z","color":"yellow"},{"datetime":"2017-10-03T10:05:51.666Z","color":"yellow"},{"datetime":"2017-10-03T10:05:51.856Z","color":"yellow"},{"datetime":"2017-10-03T10:05:52.049Z","color":"yellow"},{"datetime":"2017-10-03T10:05:52.267Z","color":"yellow"},{"datetime":"2017-10-03T10:05:52.450Z","color":"yellow"},{"datetime":"2017-10-03T10:05:52.664Z","color":"yellow"},{"datetime":"2017-10-03T10:05:52.856Z","color":"yellow"},{"datetime":"2017-10-03T10:05:53.040Z","color":"yellow"},{"datetime":"2017-10-03T10:05:54.497Z","color":"red"},{"datetime":"2017-10-03T10:05:54.800Z","color":"red"},{"datetime":"2017-10-03T10:05:54.986Z","color":"red"},{"datetime":"2017-10-03T10:05:55.176Z","color":"red"},{"datetime":"2017-10-03T10:05:55.389Z","color":"red"},{"datetime":"2017-10-03T10:05:55.609Z","color":"red"},{"datetime":"2017-10-03T10:05:55.793Z","color":"red"},{"datetime":"2017-10-03T10:05:55.979Z","color":"red"},{"datetime":"2017-10-03T10:05:56.226Z","color":"red"},{"datetime":"2017-10-03T10:05:56.423Z","color":"red"},{"datetime":"2017-10-03T10:05:57.426Z","color":"white"},{"datetime":"2017-10-03T10:05:57.856Z","color":"white"},{"datetime":"2017-10-03T10:05:58.042Z","color":"white"},{"datetime":"2017-10-03T10:05:58.242Z","color":"white"},{"datetime":"2017-10-03T10:05:58.423Z","color":"white"},{"datetime":"2017-10-03T10:05:58.607Z","color":"white"},{"datetime":"2017-10-03T10:05:58.819Z","color":"white"},{"datetime":"2017-10-03T10:05:59.024Z","color":"white"},{"datetime":"2017-10-03T10:05:59.222Z","color":"white"},{"datetime":"2017-10-03T10:05:59.399Z","color":"white"}],"start_datetime":"2017-10-03T10:05:32.458Z","email":"test@test.pl","survey_age":"29","survey_gender":"male","survey_condition":"rested","survey_heart_rate":"60","survey_bp_systolic":"","survey_bp_diastolic":"","survey_temperature":"35.0","survey_time":"after-sleep","end_datetime":"2017-10-03T10:05:59.439Z"}')
        response = self.client.post('/api/v3/', data)
        self.assertEqual(response.status_code, 200)
