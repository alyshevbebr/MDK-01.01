from my_scr.pow import PoW, find_fibonacci
import pytest

@pytest.mark.pow2
def test_pow2():
    assert PoW.pow2(5) == 25

@pytest.mark.pow2
def test_pow2_match():
    assert PoW.pow2_math(3) == 9

@pytest.mark.pow3
def test_pow3_math():
    assert PoW.pow3_math(5) == 125

@pytest.mark.fibonacci
def test_fibonacci():
    assert find_fibonacci(5) == 7


@pytest.mark.pow3
@pytest.mark.skip()
def test_notpow():
    assert 33 == 5




