from app import *


def test_validate_increasing_three_letters():
    validator = PasswordValidator()

    assert validator.validate_increasing_three_letters('hijklmmn') is True
    assert validator.validate_increasing_three_letters('abbceffg') is False


def test_validate_has_only_allowed_letters():
    validator = PasswordValidator()

    assert validator.validate_has_only_allowed_letters('hijklmmn') is False
    assert validator.validate_has_only_allowed_letters('abbceffg') is True


def test_validate_has_two_pairs_of_letters():
    validator = PasswordValidator()

    assert validator.validate_has_two_pairs_of_letters('abbceffg') is True
    assert validator.validate_has_two_pairs_of_letters('abbcegjk') is False


def test_validate():
    validator = PasswordValidator()

    assert validator.valid('bbccfgh') is False

    assert validator.valid('hijklmmn') is False
    assert validator.valid('abbceffg') is False
    assert validator.valid('abbcegjk') is False

    assert validator.valid('abbccfgh') is True


def test_generate_next():
    generator = PasswordGenerator()

    assert generator.generate_next('aaaaaaaa') == 'aaaaaaab'
    assert generator.generate_next('aaaaaaaz') == 'aaaaaaba'
    assert generator.generate_next('aaaaaazz') == 'aaaaabaa'
    assert generator.generate_next('azaaaazz') == 'azaaabaa'


def test_generate_next_valid():
    generator = PasswordGenerator()

    assert generator.generate_next_valid('abcdefgh') == 'abcdffaa'
    assert generator.generate_next_valid('ghijklmn') == 'ghjaabcc'
