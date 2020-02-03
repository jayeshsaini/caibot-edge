#!/bin/bash

lxterminal --command="python /home/pi/Desktop/caibot-edge/app.py" &&
lxterminal --command="python Smart_Asset_Monitoring_UK.py" &&
lxterminal --command="lt -p 5000 -s fastdigital -h 'https://tunnel.datahub.at' "
