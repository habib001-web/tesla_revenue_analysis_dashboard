import json
import urllib.request
from statistics import mean

# SEC API endpoint for Tesla Revenue data
CIK = "0001318605"
CONCEPT = "us-gaap/Revenues"
API_URL = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK}/{CONCEPT}.json"

# Set User-Agent as per SEC guidelines
headers = {
    'User-Agent': 'Tesla Revenue Analysis Tool contact@example.com',
    'Accept-Encoding': 'gzip, deflate'
}

# Fetch data from SEC API
req = urllib.request.Request(API_URL, headers=headers)
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode())

# Extract entity name
entity_name = data.get('entityName', '')

# Filter USD entries where fy >= "2018" and val exists and is numeric
usd_entries = data.get('units', {}).get('USD', [])
filtered_entries = []

for entry in usd_entries:
    if 'fy' in entry and 'val' in entry:
        fy = str(entry['fy'])
        val = entry['val']
        
        # Check if fy >= "2018" and val is numeric
        if fy >= "2018" and isinstance(val, (int, float)):
            filtered_entries.append({
                'fy': fy,
                'val': val
            })

# Calculate statistics
values = [entry['val'] for entry in filtered_entries]
average_revenue = round(mean(values), 2)

max_entry = max(filtered_entries, key=lambda x: x['val'])
min_entry = min(filtered_entries, key=lambda x: x['val'])

# Prepare output data
output_data = {
    "entityName": entity_name,
    "average_revenue": average_revenue,
    "max": {
        "val": max_entry['val'],
        "fy": max_entry['fy']
    },
    "min": {
        "val": min_entry['val'],
        "fy": min_entry['fy']
    }
}

# Save to data.json
with open('data.json', 'w') as f:
    json.dump(output_data, f, indent=2)

print(f"Data saved successfully for {entity_name}")
print(f"Average Revenue: ${average_revenue:,.2f}")
print(f"Max Revenue: ${max_entry['val']:,} (FY {max_entry['fy']})")
print(f"Min Revenue: ${min_entry['val']:,} (FY {min_entry['fy']})")