import logging
import model
import urllib, urllib2
import json

from google.appengine.api import memcache


def as_dict(guest):
    return {'id': guest.key.id(), 'first': guest.first, 'last': guest.last}


def get_guests():
    guests = model.all_guests()
    r = [as_dict(guest) for guest in guests]
    return r


def get_cached_guests():
    json = memcache.get('guests')
    if json is None:
        logging.info('Getting from datastore...')
        data = model.all_guests()
        json = [as_dict(guest) for guest in data]
        memcache.add('guests', json, 120)
    return json


def get_weather(zipcode):
    key = ('weather_%s' % zipcode)
    weather = memcache.get(key)
    if weather is None:
        logging.info('Get weather for zip: %s' % zipcode)
        query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="%s")' % zipcode
        params = {'q': query, 'format': 'json'}
        querystring = urllib.urlencode(params)
        url = 'https://query.yahooapis.com/v1/public/yql?' + querystring
        response = urllib2.urlopen(url)
        data = json.load(response)

        # Set values from dictionary
        channel = data['query']['results']['channel']
        city = channel['location']['city']
        region = channel['location']['region']
        temp = channel['item']['condition']['temp']
        wind = channel['wind']['speed']
        weather = {
            'city': city,
            'region': region,
            'temp': temp,
            'wind': wind,
        }
        memcache.add(key, weather, 300)  # Cache for 5 minutes
    return weather
