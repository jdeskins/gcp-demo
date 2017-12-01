from google.appengine.ext import ndb


class Guest(ndb.Model):
    first = ndb.StringProperty()
    last = ndb.StringProperty()


def all_guests():
    return Guest.query()


def update_guest(id, first, last):
    guest = Guest(id=id, first=first, last=last)
    guest.put()
    return guest


def insert_guest(first, last):
    guest = Guest(first=first, last=last)
    guest.put()
    return guest


def delete_guest(id):
    key = ndb.Key(Guest, id)
    key.delete()
