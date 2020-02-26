

# The Forum 
The url for the app is  https://superstore.pythonanywhere.com/


## Project description
This is website store that I built that allows the user to replicate the functionality off any online web store.
For example it allows the user to browse through the store, add items to a basket, update or delete the
items in your basket, add and delete items to the store's database (you have to be admin to do so), 
checkout by filling in your details and picking the method of payment.

Although you need to be admin in order to add or delete the items from the database, 
I have added an admin dashboard that does not require authorization. 
From this dashboard you can check the number of items left, customers purchased orders and so much more.

Disclaimer
The is not a real store but a demonstration store and because of that it does not take any real money, 
credit cards, etc but it does replicate the buying functionality found in any web store. 
The pictures used were taking from Topshop and the NeXT website to demonstrate the functionality of the store.



## Technologies used
1. Python 3.6
1. Flask
1. HTML
1. Bootstrap
1. Sqlite3
1. SQLAlchemy
1. Bootstrap


## How to run this in your local system
1. Create a virtual environment optional
1. Create a **name** for your directory
1. Go into your new directory
1. Clone the repository by using the command git clone https://github.com/EgbieAndersonUku1/<repository name here> **.** The full stop at end copies all the folder and directories and sub-directories into the your chosen directory without creating the based folder.
1. Type the command "**pip install -r requirements.txt**" (making sure you are in the root directory) this will install all the dependencies on your virtual environment

1. (First time use only) Open a command terminal make sure you are in the forum root folder and type the command: 
    1. python app.py db init
    1. python app.py db migrate
    1. python app.py db upgrade
    1. Next open a python terminal and type the following command
        1. from create_app import db
        1. db.create_all()

1. Next we need to create our admin user. Make you are in the root store folder open a terminal and type
    1. python "create_admin.py" file and this should create your password.

1. Open the **settings.py** and enter the full path to **imgs** folder. The path will be different depending
if it is on a Windows, Mac or Linux. Windows you must use double slash "\\" and "/" for Mac or Linux. Regardless of what OS
the final path must end either with "/imgs" or "\\imgs"
1. Next run the command ** flask run** If you get an error type in the command
    1. set FLASK_APP=app.py
    1. ** flask run **
1. Open a browser of your choice and type in **http://127.0.0.1:5000** and watch app go
1. To use a demonstration of the app go to **https://superstore.pythonanywhere.com/**

1. For any bugs found hit me up at "egbieuku@hotmail.com"

