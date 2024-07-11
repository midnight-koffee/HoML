# Chapter 2: Exploring the Housing Data
<blockquote style="background-color: #f7f7f7; border-left: 10px solid #ccc; padding: 0.5em 10px; margin: 0 0 10px;">
    <p style="font-style: italic; color: #666;">Here the name of the dataframe is "housing"</p>
</blockquote>



## Getting a Feel for the Data

### Methods Used:

1. **head() Method**:
   - **Description**: Displays the first few rows of the dataset.
   - **Usage**: Quickly inspect the structure and contents of the dataset.
   - **Syntax**: `housing.head()`

2. **info() Method**:
   - **Description**: Provides a concise summary of the dataset, including the number of entries and data types of each column.
   - **Usage**: Useful for checking missing values and understanding the overall dataset characteristics.
   - **Syntax**: `housing.info()`

3. **describe() Method**:
   - **Description**: Generates descriptive statistics of numerical attributes, such as mean, standard deviation, min, max, etc.
   - **Usage**: Offers insights into the distribution and range of numerical data.
   - **Syntax**: `housing.describe()`

### Visualizing Data Distribution:

To visualize the distribution of numerical attributes, we used the following code to plot histograms:

```python
import matplotlib.pyplot as plt

# Plot histograms of the dataset
housing.hist(bins=50, figsize=(20,15))
plt.show()
```
1. **(bins = 50)**
- Specifies that each histogram should be divided into 50 bins (or bars).

2. **figsize=(20,15)**
- Sets the figure size of the plot to be 20 units wide and 15 units high.
3. **hist()**
  - `housing.hist()`: This function generates histograms for all numerical columns in the housing dataset
