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
* Live debugging on logging
* Stackdriver Comparison Report
* Public Cache

 
## App Stats
URL: [http://localhost:8080/_ah/stats/]()

## Test Split Deployment

```
PROJECT_ID=[YOUR_PROJECT_ID]
while true; do curl https://${PROJECT_ID}.appspot.com/api/version; echo ""; sleep .5; done
```
