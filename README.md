# Google Cloud Demo

Walk through the features of Google Cloud App Engine Standard
 
## App Stats
[http://localhost:8080/_ah/stats/]()

## Test Split Deployment

```
PROJECT_ID=[YOUR_PROJECT_ID]
while true; do curl https://${PROJECT_ID}.appspot.com/api/version; echo ""; sleep .5; done
```
