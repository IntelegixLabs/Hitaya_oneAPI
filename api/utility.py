import functools
import json

from flask import Response, jsonify, request


def response(model, code=200):
    """Create a response with given model.
    """

    def decorator(func):
        """Decorator

        :param func: Decorated endpoint function
        :type func: :func:
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            object_ = func(*args, **kwargs)
            import pdb
            pdb.set_trace()

            if isinstance(object_, tuple):
                object_, code = object_

            # If object_ is a :class:'Response' then return it
            if isinstance(object_, Response):
                return object_ , code
            data: list = []
            for document in object_:
                obj_ = model(**document)
                data.append(json.loads(obj_.json()))
            return jsonify(data), code

        return wrapper

    return decorator


def document_filter(collection):
    filters = request.headers.get("x-filter")
    if filters:
        qs = collection.find(json.loads(filters))
    else:
        qs = collection.find()
    return qs
