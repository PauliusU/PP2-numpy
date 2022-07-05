import numpy as np


def to_np_array(value: list) -> np.array:
    """ Converts Python list to NumPy array """
    return np.array(value)


def analyze_data(value: list) -> None:
    arr = to_np_array(value)
    average = np.average(arr)
    median = np.median(arr)
    standard_deviation = np.std(arr)
    higher_that_gdp_filter = arr[arr > 100]

    print()
    print(f"Debt-to-GDP ratio ranges from {np.min(arr)}% to {np.max(arr)}%")
    print(f"Average debt-to-GDP ratio: {average:.2f}%")
    print(f"Median debt-to-GDP ratio: {median:.2f}%")
    print(f"Standard deviation of debt-to-GDP ratio: {standard_deviation:.2f}%")
    print(f"Debt was higher that GDP on {np.count_nonzero(higher_that_gdp_filter)} occasions: {higher_that_gdp_filter}")