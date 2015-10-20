if [ "$EUID" != "0" ]; then
  echo "$0 $@"
  sudo -v
fi

echo "installing dependencies"
echo "======================="
sudo apt-get install python3-gi gir1.2-gtk-3.0 #gtk+3.0 
sudo apt-get install gir1.2-webkit-3.0
echo "installing webkit dependencies"
echo "=============================="
sudo apt-get install libwebkitgtk-3.0-0
echo "installing dependencies done"
echo "****************************"

echo "Now run the browser by command: python3 run.py"
