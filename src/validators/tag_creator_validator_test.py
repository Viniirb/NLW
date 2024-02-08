from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRquest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validor():
    req = MockRquest(json={"product_code": "12345"})
    tag_creator_validator(req)

def test_tag_creator_validor_with_error():
    req = MockRquest(json={"product_code": 112345})

    try:
        tag_creator_validator(req)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)