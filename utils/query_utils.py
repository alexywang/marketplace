# Converts a Django query into a json
from items.models import Item
from django.db.models import Model
from django.db.models.fields.files import ImageFieldFile, ImageField
from django.db import models
import simplejson as json
import copy
from datetime import date, datetime
from django.core.serializers import serialize

# TODO
def query_to_json(query_set, exclude_fields=[]):
    query_json = []
    for obj in query_set:
        query_json.append(object_to_json(obj, exclude_fields))

    return json.dumps(query_json)

# TODO
def object_to_json(obj, exclude_fields=[]):
    obj_json = {}
    field_names = get_field_names(obj)
    for field in field_names:
        if field in exclude_fields:
            continue
        field_val = getattr(obj, field)
        if is_object(field_val): # recursively serialize
            obj_json[field] = object_to_json(field_val, exclude_fields)
        else:   # else add it to the json
            # handle datatypes
            if isinstance(field_val, datetime):
                obj_json[field] = field_val.strftime("%m/%d/%Y, %H:%M:%S")
            elif isinstance(field_val, date):
                obj_json[field] = field_val.strftime('%m/%d/%Y')
            elif isinstance(field_val, ImageField):
                obj_json[field] = field_val.url
            elif isinstance(field_val, ImageFieldFile):
                pass
            else:
                obj_json[field] = field_val

    return obj_json

def get_field_names(obj):
    return [x.name for x in obj._meta.fields]

def is_object(field):
    return isinstance(type(field), type(Model))

