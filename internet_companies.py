# Internet Companies

# Imports
import pandas as pd
import matplotlib.pyplot as plt


# Import data
internet_table = pd.read_html("https://en.wikipedia.org/wiki/List_of_largest_Internet_companies", header=0)
internet_data = internet_table[0]  # Konverter til pandas dataframe

print(internet_data)

# Export til CSV
internet_data.to_csv("internet_data.csv", index=False)

# Top 10 og Rank, Company, Revenue
top10_internet_data = internet_data.drop(["Refs", "F.Y.", "Employees", "Market cap. ($B)", "Headquarters", "Founded"], axis=1).head(10)

# Fjern $
top10_internet_data["Revenue ($B)"] = top10_internet_data["Revenue ($B)"].astype(str).str.replace("$", "")

print(top10_internet_data)
top10_internet_data.to_csv("top10_internet_data.csv", index=False)

# Plot - Donut Chart
labels = top10_internet_data.Company
sizes = top10_internet_data["Revenue ($B)"]
explode = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
fig1, ax1 = plt.subplots(figsize=(10, 8))
ax1.pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.85)

# Tegn cirkel
centre_circle = plt.Circle((0, 0), 0.70, fc="white")
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
fig.suptitle("Top10 Internet virksomheder", fontsize=20, y=1.1)
ax1.axis("equal")
plt.tight_layout()
plt.show()




