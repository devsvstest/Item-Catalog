#!/usr/bin/env python3
# Item Catalog

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from itemCatalog_db import Catalog, Base, Item_user


engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


#
item1 = Catalog(title="Snowboard", description="None",
                category="Snowboarding", user_id=1)

session.add(item1)
session.commit()

#
item2 = Catalog(title="Stick", description="None",
                category="Hockey",  user_id=1)

session.add(item2)
session.commit()

#
item3 = Catalog(title="Goggles", description="None",
                category="Snowboarding", user_id=1)

session.add(item3)
session.commit()

#
item4 = Catalog(title="Two shinguards", description="None",
                category="Soccer", user_id=1)

session.add(item4)
session.commit()

#
item5 = Catalog(title="Shinguard", description="None",
                category="Soccer", user_id=1)

session.add(item5)
session.commit()

#
item6 = Catalog(title="Frisbee", description="None",
                category="Frisbee", user_id=1)

session.add(item6)
session.commit()

#
item7 = Catalog(title="Bat", description="None",
                category="Baseball", user_id=1)

session.add(item7)
session.commit()

#
item8 = Catalog(title="Jersey", description="None",
                category="Soccer", user_id=1)

session.add(item8)
session.commit()

#
item9 = Catalog(title="Soccer Cleats", description="None",
                category="Soccer", user_id=1)

session.add(item9)
session.commit()
