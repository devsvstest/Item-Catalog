Item Catalog
==============
==============


#Instructions


Pull the project into a local directory from Github using the
link https://github.com/devsvstest/Item-Catalog

Inside Catalog folder, execute 'python itemCatalog_db.py' to create tables 
and run lotsofitems.py to populate the database with some initial values.

Execute the command 'python itemCatalog_Server.py' to start the server. 
This server starts listening on Port 5000 by default, make sure to update it 
as per your requirements in the file itemCatalog_Server.py


#Description

Item Catalog displays the items that are there in database.
Logged in users can add new items and also edit/delete the items created by them.
It also provides a json end point. 

It provides oauth2 authentication using google and facebook providers.

Users can login and logout.


#Database

Item_user
---------
    id (Integer, Primary Key)
    name (String(80))
    email (String(100))
    picture (String(250))

Catalog
--------
    id (Integer, Primary Key)
    title (String(80))
    category (String(80))
    description (String(250))
    created_datetime (DateTime)
    user_id (Integer, ForeignKey(refers to Item_user's id))

