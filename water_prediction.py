import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the water dataset
data = pd.read_csv("water_data.csv")

# Calculate water shortage
data["shortage"] = data["water_demand_m3"] - data["water_supply_m3"]

# Features used by the AI
features = [
    "rainfall_mm",
    "temperature_c",
    "population",
    "water_supply_m3",
    "water_demand_m3"
]

X = data[features]
y = data["shortage"]

# Create the AI model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X, y)

print("AI model trained successfully! 💧🤖")

# Test prediction
new_data = pd.DataFrame({
    "rainfall_mm": [10],
    "temperature_c": [42],
    "population": [1000000],
    "water_supply_m3": [450000],
    "water_demand_m3": [650000]
})

prediction = model.predict(new_data)[0]

print(f"Predicted water shortage: {prediction:.0f} m³")