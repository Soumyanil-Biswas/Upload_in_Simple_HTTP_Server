#!/bin/bash

NC='\033[0m'
GREEN='\033[0;32m'

sed -i '$ d' ~/.bashrc

echo -e "
${GREEN}Please provide your useraccount password to successfully uninstall${NC}"

prsnt=`pwd`

echo $prsnt

Path=$(grep * prev_SysPATH.txt)

echo $Path

sudo echo "export PATH="$PATH:$Path"" >> ~/.bashrc


rm -R ../${prsnt##*/}

