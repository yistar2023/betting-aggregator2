import pandas as pd
from scraper import get_all_predictions

# Get scraped data
all_preds = get_all_predictions()

# DEBUG: show scraped results
print("\n🔍 Raw scraped predictions:")
print(all_preds.head())

# Check if data is usable
if all_preds.empty:
    print("❌ No prediction data found. Please check the scraper sources.")
    exit()

required_columns = {"Match", "Pick", "Confidence", "Source"}
if not required_columns.issubset(all_preds.columns):
    print(f"❌ Missing required columns: {required_columns - set(all_preds.columns)}")
    exit()

# Group and aggregate
grouped = all_preds.groupby(["Match", "Pick"]).agg({
    "Confidence": "mean",
    "Source": "count"
}).reset_index()

# Filter: only show strong picks (70%+ confidence)
final = grouped[grouped["Confidence"] >= 70].sort_values(by="Confidence", ascending=False)

# Save to CSV
final.to_csv("predictions.csv", index=False)
print("✅ predictions.csv created with", len(final), "entries.")