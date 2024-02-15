from mongoengine import connect,Document, ListField, StringField, URLField, FloatField, DateField
from mongoengine import Document, ListField, StringField, URLField

connect(db="test_k8s", host="localhost", port=27017)


class Numbers(Document):
    ts = DateField(required=True)
    number = FloatField(required=True)