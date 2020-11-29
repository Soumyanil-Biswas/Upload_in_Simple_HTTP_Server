#!/bin/bash

BLUE='\033[0;34m'
NC='\033[0m'
GREEN='\033[0;32m'

echo -e "
${BLUE}Setting the script directory in system path${NC} ..."

echo $PATH > prev_SysPATH.txt


prsnt=`pwd`

echo $prsnt

#echo -e "${Blue}Which Shell do you use as default?${NC}: "
#read shell

#rc="rc"

#echo $rc

#file="$shell$rc"

#echo "$file"
#echo -e "
#${GREEN}Please provide your useraccount password to successfully complete the setup${NC}"
    
#sudo echo "export PATH="$PATH:$prsnt"" >> ~/.file

sudo echo "export PATH="$PATH:$prsnt"" >> ~/.bashrc

sudo chmod 744 Py_Server
sudo chmod 744 UPLOAD
