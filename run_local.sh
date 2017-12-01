#!/bin/bash

dev_appserver.py -A lw-gcp-demo --host=0.0.0.0 --enable_sendmail --datastore_path=data/dev_appserver.datastore src
