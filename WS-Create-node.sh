#!/bin/bash

echo ""
echo -n

echo  "Web Service PORT: "
read port

echo ""
echo -n
echo "Starting ..."
echo "-----------------------------"
echo ""
echo -n
echo  "CPU in [1 .. 10]"
echo -n "CPU =   "
read cpu
echo ""
echo -n
echo "-----------------------------"
echo ""
echo -n
echo "Ram in [256 .. 20000]"
echo -n "Ram =  "
read ram
echo ""
echo -n
echo "-----------------------------"
echo ""
echo -n
echo "Running ..."

curl -X POST  http://0.0.0.0:$port/hadoop --data cpu=$cpu --data ram=$ram

