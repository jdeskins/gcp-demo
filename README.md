# Google Cloud Demo

Walk through the features of Google Cloud App Engine Standard.

Topics include:
* Static files
* Custom headers
* Local development
* Pre-warm instance
* Logging
* App stats
* Memcache
* Canary deploy
* Live debugging
* Live logging
* Stackdriver Comparison Report
* Public Cache
* HTTP/2

 
## App Stats

You can view stats for the app when developing locally.
[http://localhost:8080/_ah/stats/]()


## Create datastore index
```
./create-index.sh -A ${PROJECT_ID}
```
Open Datastore / Indexes page in console to see when index has finished building.
May take a few minutes depending on size of existing data.

## Test Split Deployment

```
PROJECT_ID=[YOUR_PROJECT_ID]
while true; do curl https://${PROJECT_ID}.appspot.com/api/version; echo ""; sleep .5; done
```

## HTTP2 Demo

Demo of the difference between serving files over HTTP/1.1 vs HTTP/2
[https://http2.akamai.com/demo]()

