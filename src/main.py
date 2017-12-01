# Copyright 2013 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#             http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import webapp2
import model


def as_dict(guest):
    return {'id': guest.key.id(), 'first': guest.first, 'last': guest.last}


class RestHandler(webapp2.RequestHandler):
    def dispatch(self):
        super(RestHandler, self).dispatch()

    def cached_json(self, r):
        self.response.headers['content-type'] = 'application/json'
        self.response.headers['Cache-Control'] = 'public, max-age=120'
        self.response.write(json.dumps(r))

    def send_json(self, r):
        self.response.headers['content-type'] = 'application/json'
        self.response.write(json.dumps(r))


class CachedQueryHandler(RestHandler):
    def get(self):
        guests = model.all_guests()
        r = [as_dict(guest) for guest in guests]
        self.cached_json(r)


class QueryHandler(RestHandler):
    def get(self):
        guests = model.all_guests()
        r = [as_dict(guest) for guest in guests]
        self.send_json(r)


class UpdateHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        guest = model.update_guest(r['id'], r['first'], r['last'])
        r = as_dict(guest)
        self.send_json(r)


class InsertHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        guest = model.insert_guest(r['first'], r['last'])
        r = as_dict(guest)
        self.send_json(r)


class DeleteHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        model.delete_guest(r['id'])


APP = webapp2.WSGIApplication([
    ('/rest/cached', CachedQueryHandler),
    ('/rest/query', QueryHandler),
    ('/rest/insert', InsertHandler),
    ('/rest/delete', DeleteHandler),
    ('/rest/update', UpdateHandler),
], debug=True)
