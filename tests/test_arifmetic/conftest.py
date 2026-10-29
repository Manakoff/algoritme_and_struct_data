import pytest


@pytest.fixture(
    params=["", "()", "[](){}", "{[()]}", "а(б[в]г)д", "((((()))))", "[{()}](){[]}"]
)
def valid_string(request):
    return request.param


@pytest.fixture(params=["(", ")", "([)]", "(((()))", "(())))", "}{", "{[(])}"])
def invalid_string(request):
    return request.param
