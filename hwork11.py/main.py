# main.py

from tracker import create_record
from datetime import datetime
import json

# Step 1: Create list of travel records
records = [
    create_record("London", "Visited the London Eye", "05-06-2022"),
    create_record("Dubai", "Amazing skyline!", "12-11-2021"),
    create_record("Tokyo", "Loved the culture and food", "20-03-2023")
]

# Step 2: Convert date strings into readable format
for rec in records:
    date_obj = datetime.strptime(rec["date"], "%d-%m-%Y")  # convert string → datetime
    formatted_date = date_obj.strftime("%B %d, %Y")        # format date → "Month Day, Year"
    rec["date"] = formatted_date                           # replace original date

# Step 3: Convert list to JSON string
json_data = json.dumps(records, indent=4)
print("JSON Output:\n", json_data)

# Step 4: Parse JSON back to Python object
parsed_records = json.loads(json_data)

print("\nParsed Records:")
# Step 5: Print each record on a separate line
for record in parsed_records:
    print(record)
