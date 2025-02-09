import pytest
def add(a, b):
	return a+b
def subtract(a, b):
	return a-b

@pytest.mark.calc
class TestCalculator:
	@pytest.mark.addition
	@pytest.mark.parametrize("test_input, expected", [("2+3", 5), ("2+2", 4), ("3+7", 10)])
	def test_add(self, test_input, expected):
		assert eval(test_input)==expected

	@pytest.mark.subtraction
	# @pytest.mark.xfail
	# @pytest.mark.skip(reason="Just checking out")
	def test_subtract(self, input):
		assert subtract(input,3)==36, "Subtraction failed"
