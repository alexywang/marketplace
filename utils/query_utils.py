# Converts a Django query into a json
from items.models import Item
from django.db.models import Model
from django.db import models
import simplejson as json
import copy
from datetime import datetime
from django.core.serializers import serialize

# TODO
def query_to_json(query_set):
    query_json = []
    for obj in query_set:
        query_json.append(object_to_json(obj))

    return json.dumps(query_json)

# TODO
def object_to_json(obj):
    obj_json = {}
    field_names = get_field_names(obj)
    for field in field_names:
        field_val = getattr(obj, field)
        if is_object(field_val): # recursively serialize
            obj_json[field] = object_to_json(field_val)
        else:   # else add it to the json
            # handle datatypes
            if isinstance(field_val, datetime):
                obj_json[field] = field_val.strftime("%m/%d/%Y, %H:%M:%S")
            elif isinstance(field_val, Model):
                obj_json[field] = field_val.url
            else:
                obj_json[field] = field_val

    return json.dumps(obj_json, use_decimal=True)

def get_field_names(obj):
    return [x.name for x in obj._meta.fields]

def is_object(field):
    return isinstance(type(field), type(Model))

