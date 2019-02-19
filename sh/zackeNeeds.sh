read -p "Do you want to install all updates? (y/n) " first
if [ "$first" = "y" ]; then
	sudo apt-get update
	sudo apt-get upgrade -y
else
  echo "No"
fi


read -p "Do you want to install a webserver? (y/n) " second
if [ "$second" = "y" ]; then
	
