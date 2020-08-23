# Describe what kind of json you expect.

class ApiSchemas:
    apiSchema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "userId": {"type": "number"},
                "id": {"type": "number"},
                "title": {"type": "string"},
                "body": {"type": "string"}}
        }
    }
    postAPISchema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"},
            "id": {"type": "number"},
        },
    }
    putAPISchema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "body": {"type": "string"},
            "userId": {"type": "number"},
            "id": {"type": "number"},
        },
    }