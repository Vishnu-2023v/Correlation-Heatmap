import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the COVID-19 dataset
df = pd.read_csv("covid_19_india.csv")

# Select numerical columns
data = df[["Confirmed", "Cured", "Deaths"]]

# Calculate correlation
correlation = data.corr()

# Create the heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("COVID-19 Correlation Heatmap", fontsize=16)
plt.tight_layout()

# Save the heatmap
plt.savefig("correlation_heatmap.png", dpi=300)

# Display the heatmap
plt.show()

print("Correlation Heatmap created successfully!")
print(correlation)