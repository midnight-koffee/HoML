
# Data Splitting Methods for Machine Learning

## General Methods for Splitting Data

### 1. Random Sampling
- **Method:** Randomly select a portion of the dataset.
- **Problem:** Different test sets on each run, leading to potential data leakage.

```python
import numpy as np

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

train_set, test_set = split_train_test(housing, 0.2)
```

### 2. Fixed Random Seed
- **Method:** Initialize the random number generator with a fixed seed.
- **Problem:** Works only if the dataset is static. Adding new data or deleting rows alters the results.

```python
np.random.seed(42)
train_set, test_set = split_train_test(housing, 0.2)
```

### 3. Saving the Test Set
- **Method:** Save the test set and reload it for consistency.
- **Problem:** Not scalable when the dataset is updated.

## Using Identifiers for Stable Splits

### 4. `crc32` Hashing
- **Method:** Use a hash of unique and immutable identifiers to split the data. `crc32` is a function which takes some input and spits out a number between 1 and 2**32, and in each instance each number is equally likely to occur.
- **Advantage:** Maintains consistent splits even when the dataset is updated.

```python
from zlib import crc32

def test_set_check(identifier, test_ratio):
    return crc32(np.int64(identifier)) & 0xffffffff < test_ratio * 2**32

def split_train_test_by_id(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio))
    return data.loc[~in_test_set], data.loc[in_test_set]

housing_with_id = housing.reset_index()
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")
```

## Handling Missing Identifiers

### Using Feature-Based Identifiers
- **Method:** Combine stable features (e.g., latitude and longitude) to create unique identifiers.

```python
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
```

## Stratified Sampling for Representativeness

### Stratified Sampling Based on Median Income
- **Method:** Ensure the test set is representative by splitting based on income categories.

```python
housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# Remove the income_cat attribute to revert to original data
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)
```

This summary covers the primary methods for splitting data into training and test sets, addressing the issues and solutions associated with each method.
