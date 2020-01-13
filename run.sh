#!/bin/bash

lxterminal --command="python app.py" &
lxterminal --command="lt -p 5000 -s fastdigital -h http://localtunnel.me --allow-invalid-cert true"