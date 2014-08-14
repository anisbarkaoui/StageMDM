#!/bin/bash


echo -n
echo " ---------    StratusLab Node Menu   ---------"
echo "|---------------------------------------------|"
echo "|                     |                       |"
echo "|    1- List nodes    |    3- Node details    |"
echo "|                     |                       |"
echo "|---------------------------------------------|"
echo "|                     |                       |"
echo "|    2- Create node   |    4- Kill node       |"
echo "|                     |                       |"
echo " ---------------------------------------------"

 
echo -n
read num
if   [ $num = 1 ]; then ./WS-List-nodes.sh
elif [ $num = 2 ]; then ./WS-Create-node.sh
elif [ $num = 3 ]; then ./WS-Status-node-id
elif [ $num = 4 ]; then ./WS-Kill-node-id
else  echo"invalid choice ..." && clear && ./node-menu
fi

