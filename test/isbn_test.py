import isbn_validator

def test_get_isbn10_():
  assert isbn_validator.get_isbn10("0-19-852663-6")

  def test_get_isbn13_():
    assert isbn_validator.get_isbn13("978-3-16-148410-0")
    assert not isbn_validator.get_isbn13("0-19-852663-6")

    def test_is_valid_isbn():
      assert isbn_validator.is_valid("978-3-16-148410-0")