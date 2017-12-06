from google.appengine.ext import ndb


class Guest(ndb.Model):
    first = ndb.StringProperty()
    last = ndb.StringProperty()
    food = ndb.StringProperty()


def all_guests():
    return Guest.query()


def get_guests_by_food(food):
    return Guest.query(Guest.food == food).order(Guest.last, Guest.first)


def update_guest(id, first, last, food):
    guest = Guest(id=id, first=first, last=last, food=food)
    guest.put()
    return guest


def insert_guest(first, last, food):
    guest = Guest(first=first, last=last, food=food)
    guest.put()
    return guest


def delete_guest(id):
    key = ndb.Key(Guest, id)
    key.delete()
