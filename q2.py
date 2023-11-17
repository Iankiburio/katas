def sort_strings_by_length(strings):
    return sorted(strings, key=len)
    
# Example usage:
strings = ["Ian", "Outside", "Unforgettable", "Queue"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)
