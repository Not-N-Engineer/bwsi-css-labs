import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_all_positives():
    assert max_subarray_sum([4, 6, 2, 8]) == 20      
    assert max_subarray_sum([5, 19, 28, 4, 6, 13, 17, 12]) == 104

def test_all_negatives():
    assert max_subarray_sum([-4, -6, -2, -8]) == -20      
    assert max_subarray_sum([-5, -19, -28, -4, -6, -13, -17, -12]) == -104

def test_negatives_in_middle():
    assert max_subarray_sum([4, 6, -2, 8]) == 16      # Test for when max sum is full set even when one negative is present
    assert max_subarray_sum([5, 19, 28, -4, -6, -13, 17, 12]) == 58      # Test for when max sum is full set even when multiple negatives are present
    assert max_subarray_sum([5, 19, -28, -4, -6, -13, 17, 12]) == 29      # Test for when max sum is not full set when multiple negatives are present

def test_negatives_scattered():
    assert max_subarray_sum([-4, 6, 2, -8]) == 8      
    assert max_subarray_sum([-5, 19, -28, 4, 6, -13, 17, -12]) == 19

if __name__ == "__main__":
    pytest.main()