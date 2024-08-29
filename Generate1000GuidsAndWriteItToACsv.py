import uuid
import csv

def generate_uuids(count):
    uuids = set()
    while len(uuids) < count:
        uuids.add(uuid.uuid4())
    return uuids


unique_uuids = generate_uuids(995)
# Output file path
output = 'guids.csv'
with open(output, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Id']) # Header
    for uuid in unique_uuids: # Writes each data in a new row
        writer.writerow([uuid])

print(f"{len(unique_uuids)} UUIDs have been written to {output}.")
