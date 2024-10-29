from google.cloud import ndb


class Contact(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()

client = ndb.Client()
with client.context():
    ancestor_key = ndb.Key("ContactGroup", "work")
    contact1 = Contact(parent=ancestor_key,
                   name="John Smith",
                   phone="555 617 8993",
                   email="john.smith@gmail.com")
    contact1.put()
    contact2 = Contact(parent=ancestor_key,
                   name="Jane Doe",
                   phone="555 445 1937",
                   email="jane.doe@gmail.com")
    contact2.put()
