# neoTim

neoTim is an advanced version of tim, which functioned by severless function, and noe it is based on Flask, the database still remains free MongoDB for personal user


in the src, the app.py is the backend server deamon, connect is a submodule for connect.py to the database, the the req.py is the very program you should run to ask data to your local or remote server.

and as you can see there is also a chrome extension to use the neoTIm

and there are some scripts:

set FLASK_APP=C:/Users/26440/Desktop/workGaoInMarch/neoTim/src/app.py
flask run --host=0.0.0.0 -p 3002
sudo nohup /usr/local/bin/flask run --host=0.0.0.0 -p 3002 > log.txt 2>&1 &

the default port of the program is 3002
to run it, at boot put the program at start folder --                  C:\Users\26440\AppData\Roaming\Microsoft\Windows\Start Menu\Programs
to run it background as deamon use the vbs 










