# thereisnoclipboard
Thereisnoclipboard is Clipboard manager that has a unique hotkey for each copied data
This app offers you to copy multiple texts in a different locations by pressing ctrl+c+ , to store your value in that specific key. It also offers an option to add your own hotkey(eg. ctrl+m) for either copying or pasting. It shows the copied data with respect to the key and the current hotkeys for copying and pasting. A help button is provided for any further help.

This app opens on start up. the following instructions will help you use the app:

How to run:

1)Run the multiclipboard_install.sh file (run ./thereisnoclipboard_install.sh in the in the directory that contains this file)(do not run with sudo). 

2)Reboot the computer to make sure that the app opens on startup

How to use:

1)Enter hotkey for copy and that for paste(default is ctrl+c and ctrl+v respectively). This will be the keys you will have to press in order to copy and paste. Leave this space empty for using the default hotkeys.

2)Click on 'activate clipboard' to activate the clipboard.

3)To copy or paste hold +,where is the value you entered for the hotkey and is any alphabet or number(DO NOT use default hotkeys like ctrl+c+q as the system will do the default function(i.e. ctrl+q, this will quit the tab)after copying). eg:ctrl+c+1 will copy your data in key <1> ctrl+p+1 will paste this data (while releasing keys, release p or c first and then release).

NOTES:

1)This app is currently functional only in linux OS

2)You must log in as superuser or have root permissions to use the app

3)You can still use your normal copy and paste(just ctrl+c or ctrl+v) while the program is running.

4)DO NOT use any of the systems default hotkeys(except ctrl+c and ctrl+v) for copy and pasting hotkeys as they may cause some errors.
