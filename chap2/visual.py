import numpy as np
import pandas as pd
from stratsplit import strat_train_set
import matplotlib.pyplot as plt

housing = strat_train_set.copy()
# Now you can use `housing` as needed in this file

#housing.plot(kind="scatter", x="longitude", y="latitude")
housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)



housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
s=housing["population"]/100, label="population", figsize=(10,7),
c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
)
plt.legend()
plt.show()