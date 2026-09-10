from algoritms.arithmetic.is_valid_brackets import  is_valid_brackets

def test_valid_cases(valid_string):
    assert is_valid_brackets(valid_string) is True

def test_invalid_cases(invalid_string):
    assert is_valid_brackets(invalid_string) is False

def test_string_without_brackets():
    text_without_brackets = "Тут только текст"
    assert is_valid_brackets(text_without_brackets) is True
