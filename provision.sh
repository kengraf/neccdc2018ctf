#!/bin/bash
#Check if the user running the script is root.
#If not, exit the script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

#Get the OS and the version.
#If it isn't Ubuntu 14.04, exit the script
os_version=$( cat /etc/lsb-release )
#echo "$os_version"
if [[ $os_version != *"Ubuntu 16.04"* ]]; then
  echo "Incorrect OS. You must be using Ubuntu 16.04. Other versions are not supported."
  exit 1
fi


total_mem=$( grep MemTotal /proc/meminfo | awk '{print $2}' )
echo "$total_mem"

#Check to see if  all packages are up to date.
echo "Next task: sudo apt-get update"
sudo apt-get update
if [ $? != 0 ]; then
  echo "This was unsuccessful. Please read why."
  exit 1
else
  echo "Successfully updated packages"
fi

echo "Next task: sudo apt-get -y install python-pip"
#sudo apt install python-pip
sudo apt-get -y install python-pip
if [ $? != 0 ]; then
  echo "This was unsuccessful."
  exit 1
else
  echo "Successfully installed pip"
fi

echo "Next task: pip --no-cache-dir install pandas"
pip --no-cache-dir install pandas
if [ $? != 0 ]; then
  echo "This was unsuccessful."
  exit 1
else
  echo "Successfully installed pandas"
fi

echo "Next task: sudo apt-get install python-mysqldb"
sudo apt-get install -y python-mysqldb
if [ $? != 0 ]; then
  echo "This was unsuccessful."
  exit 1
else
  echo "Successfully installed pandas"
fi

echo "Next task: Check if Git is installed"
git --version > /dev/null
if [ $? != 0 ]; then
  echo "Git is not installed. Installing git.."
  sudo apt-get git
  if [ $? != 0 ]; then
    echo "Git failed to installed"
    exit 1
  fi
else
  echo "Git is already installed. Proceeding..."
fi

#Clone the FBCTF repo
echo "Next task: Clone the FBCTF repo"
git clone https://github.com/facebook/fbctf
if [ $? != 0 ]; then
  echo "Failed to clone the FBCTF repo"
  exit 1
else
  echo "Successfully cloned the FBCTF repo"
fi

#CD into FBCTF directory and run provisioning script.
cd fbctf
source ./extra/lib.sh
quick_setup install prod
