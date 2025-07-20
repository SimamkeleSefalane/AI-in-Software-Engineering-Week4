def sort_by_key(data, key):
    return sorted(data, key=lambda d: d.get(key, 0))

# Sample data
sample_data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 95},
    {"name": "Charlie", "score": 75}
]

# Sort by 'score'
sorted_data = sort_by_key(sample_data, "score")

# Output result
print("Sorted Data by Score:")
for item in sorted_data:
    print(item)
