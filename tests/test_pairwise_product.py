from algos_ds_python.pairwise_product import (
    compute_max_values,
    naive_max_pair_product,
    max_pair_product,
)
from hypothesis import given
from hypothesis import strategies as st


def test_compute_max_values():
    """Test with examples"""
    assert compute_max_values((3, 1), 2) == (3, 2)
    assert compute_max_values((3, 1), 4) == (4, 3)
    assert compute_max_values((-1, -1), 2) == (2, -1)
    assert compute_max_values((3, 1), 0) == (3, 1)


def test_naive_max_pair_product():
    """Tests with examples"""
    assert naive_max_pair_product([1, 2, 3]) == 6
    assert naive_max_pair_product([7, 5, 14, 2, 10, 8, 10, 21, 2, 3]) == 294
    assert naive_max_pair_product([1, 2, 1]) == 2
    assert naive_max_pair_product([7, 5, 14, 2, 8, 8, 10, 1, 2, 3]) == 140


def test_max_pair_product():
    """Tests with examples"""
    assert max_pair_product([1, 2, 3]) == 6
    assert max_pair_product([7, 5, 14, 2, 10, 8, 10, 21, 2, 3]) == 294
    assert max_pair_product([1, 2, 1]) == 2
    assert max_pair_product([7, 5, 14, 2, 8, 8, 10, 1, 2, 3]) == 140


test_cases = number_list = st.lists(
    st.integers(min_value=0, max_value=10000), min_size=2, max_size=1000
)


@given(test_cases)
def test_stress_test_pair_product(number_list):
    """Testin that naive = efficient"""
    assert max_pair_product(number_list) == naive_max_pair_product(number_list)
