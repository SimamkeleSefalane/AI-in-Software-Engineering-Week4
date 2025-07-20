def sort_by_key(data, key):
    try:
        return sorted(data, key=lambda x: x[key])
    except KeyError as e:
        print(f"KeyError: {e}") 
        return data
