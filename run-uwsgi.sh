#!/bin/sh
# requires uwsgi to be installed, eg: pip install uwsgi

mypath=$(cd `dirname $0` && pwd)

params="$mypath/uwsgi.ini"

if [ -n "$VIRTUAL_ENV" ] ; then
    params="$params -H $VIRTUAL_ENV"
fi

uwsgi $params
