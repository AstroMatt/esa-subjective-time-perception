from django.db import models

"""
experiment = {
    'start': '2016-11-19T23:16:04.039Z',
    'end': '2016-11-19T23:16:04.039Z',
    
    'trial': {
        'location': 'Experiment over the internet',
        'polarization': 'horizontal',
        'device': 'computer 1',
        'order': ['blue', 'red', 'white'],
        'number': 1
    },
    
    'survey': {
        'age': '28',
        'email': 'imie@nazwisko.tld',
        'condition': 'normal',
        'gender': 'male',
        'rhythm': 'average'
    },

    'events':  [{'datetime': '2016-11-19T23:16:04.040Z', 'target': 'experiment', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:04.040Z', 'target': 'survey', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:04.040Z', 'target': 'survey', 'action': 'end'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'black', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'black', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'black', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'black', 'action': 'end'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'blue', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'blue', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'blue', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'blue', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'blue', 'action': 'end'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'red', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'red', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'red', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'red', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'red', 'action': 'end'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'white', 'action': 'start'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'white', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:46.828Z',  'target': 'white', 'action': 'click'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'white', 'action': 'end'},
             {'datetime': '2016-11-19T23:16:04.040Z',  'target': 'experiment', 'action': 'end'}]
     }      
}
"""  

class Experiment(models.Model):
    pass
    
    
class Trial(models.Model):
    experiment = models.ForeignKey(to='api_v1.Experiment')
    location = models.CharField(max_length=50)
    polarization = models.CharField(max_length=50)
    device = models.CharField(max_length=50)
    order = models.CharField(max_length=50)
    number = models.PositiveSmallIntegerField()
    
class Survey(models.Model)
    experiment = models.ForeignKey(to='api_v1.Experiment')
    age = models.PositiveSmallIntegerField()
    email = models.EmailField()
    condition = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    thythm = models.CharField(max_length=50)
    
class Event(models.Model):
    experiment = models.ForeignKey(to='api_v1.Experiment')
    datetime = DateTimeField()
    target = models.CharField(max_length=50)
    action = models.CharField(max_length=50)
    
    