#!/bin/bash 

echo ""
echo -n

echo  "Web Service PORT: " 
read port

echo ""
echo -n


echo "Starting ..."

curl -X GET http://0.0.0.0:$port/hadoop

