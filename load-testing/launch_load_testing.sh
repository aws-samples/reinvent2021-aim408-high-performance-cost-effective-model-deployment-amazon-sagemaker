#!/bin/bash
ENDPOINT_NAME=$1
port=$2
bind_port=$((port-2523))
export ENDPOINT_NAME

echo "Load testing $ENDPOINT_NAME on web port $port and bind port $bind_port"

locust -f locustfile.py --worker --loglevel ERROR --autostart \
       --autoquit 10 --master-port $bind_port & 

locust -f locustfile.py --worker --loglevel ERROR --autostart \
       --autoquit 10 --master-port $bind_port &

echo "Accessing locust dashboard at http://0.0.0.0:${port}"

locust -f locustfile.py -u 300 -r 5 -t 15m --web-port $port \
       --print-stats --only-summary --loglevel ERROR \
       --autostart --autoquit 10 --master --master-bind-port $bind_port