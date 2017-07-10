#/bin/bash

gunicorn -w 1 -b 0.0.0.0:30030 run:app