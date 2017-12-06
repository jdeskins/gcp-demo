#!/bin/bash

set -ue

while getopts ":A:" opt; do
  case $opt in
    A) app_id="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

gcloud datastore create-indexes --project ${app_id} src/index.yaml
