apt install python-pip #python 2

pip install paho-mqtt

sudo apt-get install python-dev python-rpi.gpio

wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key

sudo apt-key add mosquitto-repo.gpg.key

cd /etc/apt/sources.list.d/

sudo wget http://repo.mosquitto.org/debian/mosquitto-wheezy.list

sudo apt-get update

sudo apt-get install mosquitto
