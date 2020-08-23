import jsonschema
from jsonschema import validate

"""
This is the method written to validate the API schemas
this method expect two input, Actual and Expected on. Expected one mentioned in "ApiSchemas" class
Actual one can fe fetched from the response of API
"""

def validateJson(jsonData, validateSchema):
    try:
        validate(instance=jsonData, schema=validateSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True
