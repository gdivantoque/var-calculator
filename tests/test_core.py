# Libraries needed for the tests.
import numpy as np
import pandas as pd
import pytest  # the testing tool

# Import the function we want to test from our own package.
from var_calculator.core import log_returns


# pytest automatically runs every function whose name starts with "test_".
def test_log_returns_values():
    # 1. Prepare: three prices whose answers we already know.
    prices = pd.Series([100.0, 110.0, 99.0])
    # 2. Run the function.
    result = log_returns(prices)
    # 3. Check: 3 prices give 2 returns (day 1 has no previous price).
    assert len(result) == 2
    # 100 -> 110 is +10%, so the first log return must be ln(1.1).
    # pytest.approx accepts tiny rounding differences in the decimals.
    assert result.iloc[0] == pytest.approx(np.log(1.1))


def test_log_returns_rejects_non_positive_prices():
    # This test passes only if the function raises a ValueError
    # when it receives a price of zero.
    with pytest.raises(ValueError):
        log_returns(pd.Series([100.0, 0.0]))
