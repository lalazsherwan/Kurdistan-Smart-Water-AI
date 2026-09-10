import pandas as pd

# Sample water data
data = {
    "district": ["Erbil", "Sulaymaniyah", "Duhok", "Kirkuk"],
    "water_supply": [1000, 800, 900, 700],
    "water_demand": [850, 760, 950, 800]
}

df = pd.DataFrame(data)

# Calculate shortage
df["shortage"] = df["water_demand"] - df["water_supply"]

# Determine risk level
def risk_level(shortage):
    if shortage <= 0:
        return "Green"
    elif shortage <= 100:
        return "Yellow"
    else:
        return "Red"

df["risk_level"] = df["shortage"].apply(risk_level)

print(df)