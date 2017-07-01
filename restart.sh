#/bin/bash

kill `cat ./tmp/slavett.pid`
gunicorn -w 1 -b 0.0.0.0:30030 run:app -p ./tmp/slavett.pid &