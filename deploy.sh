#!/bin/bash

set -ue

while getopts ":A:v:" opt; do
  case $opt in
    A) app_id="$OPTARG"
    ;;
    v) version="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

gcloud app deploy src --project ${app_id} -v ${version}
