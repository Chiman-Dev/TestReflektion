import logging
import requests
from APIDetails.APIHeader import ApiHeader
from APIDetails.APIPayload.API_Payload import ApiPayload
from APIDetails.APIURI import ApiDetails
import json
from validation.apiSchemas import ApiSchemas
from validation.validationSchema import validateJson


def test_get_API1():
    response = requests.get(ApiDetails.fetchRecords1, headers=ApiHeader.headers)
    print(response.status_code, type(response.json()), len(response.json()))
    print("Schema validation is ", validateJson(json.loads(response.text), ApiSchemas.apiSchema))
    assert (response.status_code == 200)
    assert (len(response.json()) == 100)


def test_get_API2():
    response = requests.get(ApiDetails.fetchRecords2, headers=ApiHeader.headers)
    print(response.status_code, type(response.json()), len(response.json()))
    print("Schema validation is ", validateJson(json.loads(response.text), ApiSchemas.apiSchema))
    assert (response.status_code == 200)
    assert len(response.json()) == 1, "Number of records are {}".format(len(response.json()))


def test_get_API3():
    response = requests.get(ApiDetails.fetchRecords3, headers=ApiHeader.headers)
    logging.basicConfig(level=logging.INFO)
    logging.info("Request is {} and the response is {}".format(ApiDetails.fetchRecords3, response.json()))
    assert response.status_code == 404, "The response code is {}".format(response.status_code)


def test_post_API():
    getResponse = requests.get(ApiDetails.postRecords, headers=ApiHeader.headers)
    count = len(getResponse.json())
    response = requests.post(ApiDetails.postRecords, json=ApiPayload.body, headers=ApiHeader.headers)
    print(response.json())
    assert (response.status_code == 201)
    print("Schema validation is ", validateJson(json.loads(response.text), ApiSchemas.postAPISchema))
    assert len(
        requests.get(ApiDetails.postRecords, headers=ApiHeader.headers).json()) == count + 1, "Record is not inserted"


def test_put_API():
    getResponse = requests.get(ApiDetails.fetchRecords1, headers=ApiHeader.headers)
    response = requests.put(ApiDetails.putRecords, json=ApiPayload.putBody, headers=ApiHeader.headers)
    print("Schema validation is ", validateJson(json.loads(response.text), ApiSchemas.putAPISchema))
    assert (response.status_code == 200)
    assert getResponse.json()[ApiPayload.putBody["id"] - 1] == response.json(), "Record is not updated"


def test_Delete_API():
    response = requests.delete(ApiDetails.putRecords, headers=ApiHeader.headers)
    print("Response is ", response.json())
    assert (response.status_code == 200)


