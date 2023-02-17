import pytest
from calculator import Calculator

calculator = Calculator()
@pytest.mark.parametrize("num1, num2, result", [(2,7,9), (-2,-7,-9), (-2,7,5), (2.3,7.1,9.4), (2,0,2)])
def test_sum_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1,num2)
    res = round(res, 1)
    assert res == result

@pytest.mark.parametrize("nums, result", [([], 0),([1, 2, 3,4,5,6,7,8,9,5], 5)])
def test_avg_list(nums, result):
    calculator = Calculator()
    res = calculator.avg(nums)
    assert res == result
    
def test_div_pozitive_nums():
    calculator = Calculator()
    res = calculator.div(12, 3)
    assert res == 4

def test_div_zero_nums():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(12, 0)




