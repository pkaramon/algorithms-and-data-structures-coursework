import random
import pytest
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from counting_sort import counting_sort_unstable
from insertion_sort import insertion_sort 
from quick_sort import quick_sort


@pytest.mark.parametrize("f", [bubble_sort, selection_sort, counting_sort_unstable, insertion_sort, quick_sort])
def test_sorting(f):
    for _ in range(100):
        size = random.randint(0, 100)
        A = [random.randint(0, 100) for _ in range(size)]
        B = A.copy()

        f(A)
        B.sort()

        assert A == B
