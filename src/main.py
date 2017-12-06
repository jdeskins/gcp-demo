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
import logging
import os
import webapp2
import model
import utils


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


class VersionHandler(RestHandler):
    def get(self):
        version = os.environ.get("CURRENT_VERSION_ID")
        self.send_json({'version': version})


class CachedQueryHandler(RestHandler):
    def get(self):
        guests = utils.get_cached_guests()
        self.cached_json(guests)


class WeatherHandler(RestHandler):
    def get(self, zipcode):
        weather = utils.get_weather(zipcode)
        self.cached_json(weather)


class QueryHandler(RestHandler):
    def get(self):
        guests = utils.get_guests()
        self.send_json(guests)


class UpdateHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        guest = model.update_guest(r['id'], r['first'], r['last'])
        r = utils.as_dict(guest)
        self.send_json(r)


class InsertHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        guest = model.insert_guest(r['first'], r['last'])
        r = utils.as_dict(guest)
        self.send_json(r)


class DeleteHandler(RestHandler):
    def post(self):
        r = json.loads(self.request.body)
        model.delete_guest(r['id'])


class WarmupHandler(RestHandler):
    def get(self):
        # Do stuff here to warm up the instance
        self.send_json({"status": "warmup request finished ok."})


APP = webapp2.WSGIApplication([
    webapp2.Route('/api/cached', CachedQueryHandler),
    webapp2.Route('/api/query', QueryHandler),
    webapp2.Route('/api/insert', InsertHandler),
    webapp2.Route('/api/delete', DeleteHandler),
    webapp2.Route('/api/update', UpdateHandler),
    webapp2.Route('/api/version', VersionHandler),
    webapp2.Route('/_ah/warmup', WarmupHandler),
    webapp2.Route('/api/weather/<zipcode:\d+>', WeatherHandler),
], debug=True)
