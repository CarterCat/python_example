import json

from collections import namedtuple

##

data = {"a": 1, "b": 2, "c": 3}

string = json.dumps(data)

data = json.loads(string)

fn = lambda data: {k: str(v) for (k,v) in data.items()}

data = json.loads(string, object_hook=fn)

def fn(data):
    data["b"] = str(data["b"])
    return data

data = json.loads(string, object_hook=fn)

##

data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}

string = json.dumps(data)

fn = lambda data: namedtuple("Data", data.keys())(*data.values())

data = json.loads(string, object_hook=fn)

data.b.d.e


##

data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}

string = json.dumps(data)

def _json_object_hook(data):
    return namedtuple('X', data.keys())(*data.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

data = json2obj(string)
