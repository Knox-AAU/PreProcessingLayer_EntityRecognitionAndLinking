from Levenshtein import distance;

def test_OneReplace():
    assert distance("Drake", "Brake") == 1

def test_OneInsertion():
    assert distance("Drake", "Drakes") == 1

def test_OneDeletion():
    assert distance("Drake", "Drak") == 1

def test_ReplaceAndInsert():
    assert distance("kitten", "sitting") == 3

# Test for an empty string
def test_empty_string():
    assert distance("", "") == 0

# Test for identical strings
def test_identical_strings():
    assert distance("hello", "hello") == 0

# Test for strings with one character difference
def test_one_char_difference():
    assert distance("kitten", "sitten") == 1

# Test for strings with different lengths
def test_different_lengths():
    assert distance("kitten", "kittens") == 1

# Test for completely different strings
def test_completely_different_strings():
    assert distance("hello", "world") == 4

# Test with special characters and case sensitivity
def test_special_characters_and_case():
    assert distance("CaSe", "cAsE") == 4

# Test with non-ASCII characters
def test_non_ascii_characters():
    assert distance("café", "coffee") == 4

# Test with long strings
def test_long_strings():
    assert distance("a" * 100, "b" * 100) == 100