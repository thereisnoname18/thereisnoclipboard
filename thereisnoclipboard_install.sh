#!/bin/bash
echo Initializing application download...
wget https://github.com/thereisnoname18/thereisnoclipboard/releases/download/v1.0.0/thereisnoclipboard_autostart.desktop
echo autostart file downloaded
wget https://github.com/thereisnoname18/thereisnoclipboard/releases/download/v1.0.0/thereisnoclipboard
echo binary file downloaded
wget https://iconsplace.com/wp-content/uploads/_icons/ff0000/256/png/clipboard-icon-14-256.png
mv clipboard-icon-14-256.png ./thereisnoclipboard_icon.png
cp thereisnoclipboard_autostart.desktop ./thereisnoclipboard_application.desktop
echo application file downloaded
echo application download successful
echo Initialising installation procedure...
sudo mkdir /usr/bin/thereisnoclipboard
sudo mv thereisnoclipboard  /usr/bin/thereisnoclipboard
sudo chmod +x /usr/bin/thereisnoclipboard/thereisnoclipboard   
echo binary file installed
sudo mv thereisnoclipboard_icon.png /usr/bin/thereisnoclipboard
echo application icon installed
sudo cp thereisnoclipboard_application.desktop /usr/share/applications
mv thereisnoclipboard_application.desktop $HOME/.local/share/applications
echo application file installed
mv thereisnoclipboard_autostart.desktop $HOME/.config/autostart
echo autostart file installed
echo installation successful
echo reboot the system to ensure that the autostart works
