from upstash_vector import Index

# Initialize the Index
index = Index(
    url="https://nice-asp-61208-us1-vector.upstash.io",
    token="ABIFMG5pY2UtYXNwLTYxMjA4LXVzMWFkbWluTmpWak5qRTFNemN0TVdJeE15MDBaVE14TFRnMU1XTXRORFZoWW1VNU9EUXhOR0U1",
)

# Fetch all data
cursor = "0"
results = []
while True:
    response = index.range(cursor=cursor, limit=100, include_metadata=True)
    results.extend(response.vectors)
    cursor = response.next_cursor
    if cursor == "":
        break

# Process the results
for vector in results:
    print(vector)
