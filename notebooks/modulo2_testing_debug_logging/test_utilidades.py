import pytest
from utilidades import es_par

@pytest.mark.parametrize("n, esperado", [
    (0, True),
    (2, True),
    (5, False),
    (100, True)
])
def test_es_par(n, esperado):
    assert es_par(n) == esperado
