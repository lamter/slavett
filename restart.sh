#/bin/bash

kill `cat ./tmp/slavett.pid`
gunicorn -w 1 run:app -p ./tmp/slavett.pid &