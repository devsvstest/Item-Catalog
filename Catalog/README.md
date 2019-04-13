Item Catalog
==============


Instructions
-------------


Pull the project into a local directory from Github using the
link https://github.com/devsvstest/Item-Catalog

Inside Catalog folder, execute 'python itemCatalog_db.py' to create tables 
and run lotsofitems.py to populate the database with some initial values.

Execute the command 'python itemCatalog_Server.py' to start the server. 
This server starts listening on Port 5000 by default, make sure to update it 
as per your requirements in the file itemCatalog_Server.py


Description
-------------


Item Catalog displays the items that are there in database.
Logged in users can add new items and also edit/delete the items created by them.
It also provides a json end point. 

It provides oauth2 authentication using google and facebook providers.

Users can login and logout.


Database
----------


#Item_user
    id (Integer, Primary Key)
    name (String(80))
    email (String(100))
    picture (String(250))

#Catalog
    id (Integer, Primary Key)
    title (String(80))
    category (String(80))
    description (String(250))
    created_datetime (DateTime)
    user_id (Integer, ForeignKey(refers to Item_user's id))


IP Address of the host
-----------------------


13.234.69.5


URL
----


http://www.shruthivs.com/


Softwares Installed
----------------------


* postgresql
* sqlalchemy
* flask
* random
* httplib2
* sessionmaker
* oauth2client
* random
* requests


Configurations
-----------------


* Using postgresql create database 'catalog'
* Create user 'catalog', set password to 'catalog'
* Update your initialization python script to access the database 'catalog'
* Enable new virtual host  at /etc/apache2/sites-available/ and point it to access your wsgi file
* Grant necessary permission and set up log files in the virtual host set up file
* Create wsgi file in /var/www/FlaskApp directory and point it to your python app
* Make sure you are running server on port 80
* Create database schema by executing the 'itemCatalog_db.py'
* restart apache server 
* Access the website http://www.shruthivs.com/ and login using your google account
* Execute lotsofitems.py to populate the database
* Test the functionality of the app

