import numpy as np

from student_rag.data.generate import make_students


def test_same_seed_gives_same_students():
    a, _ = make_students(np.random.default_rng(42), 2000)
    b, _ = make_students(np.random.default_rng(42), 2000)
    
    for col in a:
        assert np.array_equal(a[col],b[col]), col


def test_different_seed_gives_different_students():
    a, _ = make_students(np.random.default_rng(42), 2000)
    c, _ = make_students(np.random.default_rng(7), 2000)
    
    assert any(not np.array_equal(a[col],c[col]) for col in a)
