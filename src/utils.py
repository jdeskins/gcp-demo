import logging
import model

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
