from mongoengine import connect,Document, ListField, StringField, URLField, FloatField, DateField
from mongoengine import Document, ListField, StringField, URLField
import os

# MongoDB connection details
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_DB = os.environ.get('MONGO_DB', 'test_k8s')

# Connect to MongoDB
connect(db=MONGO_DB, host=MONGO_HOST, port=MONGO_PORT)


class Numbers(Document):
    ts = DateField(required=True)
    number = FloatField(required=True)