#!/bin/sh
# requires gunicorn to be installed, eg: pip install gunicorn

export PYWB_CONFIG_FILE=./cci-config.yaml
gunicorn -w 4 pywb.apps.wayback -b 0.0.0.0:8080
