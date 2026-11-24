# The text in triple quotes is a "docstring": it describes this file.
"""Core functions for the project."""

# Import the libraries we use. "as np" and "as pd" are short nicknames.
import numpy as np  # numpy: fast maths (here, the logarithm)
import pandas as pd  # pandas: series and tables of data, like Excel columns


# "def" creates a function. Inside the brackets is the input (prices);
# after "->" is the type of result it gives back (also a pandas Series).
def log_returns(prices: pd.Series) -> pd.Series:
    """Compute log returns from a price series."""
    # Safety check: a log return needs prices above zero.
    # .any() is True if at least one price is zero or negative.
    if (prices <= 0).any():
        # Stop with a clear error message instead of giving a wrong result.
        raise ValueError("Prices must be strictly positive.")
    # prices.shift(1) moves every price down one row, so each row sees
    # the previous day's price. Formula: ln(P_t / P_t-1).
    # .dropna() removes the first row, which has no previous price.
    return np.log(prices / prices.shift(1)).dropna()
