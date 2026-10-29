import pytest

from src.timeout_utils import validate_timeout


def test_accepts_valid_timeout():
    assert validate_timeout(3) == 3


def test_rejects_negative_timeout():
    with pytest.raises(ValueError):
        validate_timeout(-1)
