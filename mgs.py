import pandas as pd

input_file = "mgsv emblem words.txt"   # your input file
output_file = "mgsoutput.csv" # will open in Excel fine

data = []

# Read and split each line by '-'
with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        # Strip whitespace and skip empty lines
        clean_line = line.strip()
        if not clean_line:
            continue

        parts = [item.strip() for item in line.strip().split("-")]
        data.append(parts)

# Convert to DataFrame
df = pd.DataFrame(data)

# Export to CSV instead of Excel
df.to_csv(output_file, index=False, header=False)

print(f"✅ Data successfully exported to {output_file}")
