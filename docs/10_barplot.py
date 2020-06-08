# Simpel - Bar plot
# Import af CSV fil
import pandas as pd

house_data = pd.read_csv("https://github.com/hellstern/python_seminar/raw/master/california_housing_train.csv", sep=",")
print(house_data.head())

# Plot
import matplotlib.pyplot as plt

house_data["median_income"].hist()
plt.show()




