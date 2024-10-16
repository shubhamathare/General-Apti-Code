def get_suggestions(search_history, query):
    # Use a list comprehension to filter suggestions
    suggestions = [item for item in search_history if item.startswith(query)]
    return suggestions

# Sample search history
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

# Get user input for the partial search query
query = input("Enter your partial search query: ").strip()

# Get suggestions based on the query
suggestions = get_suggestions(search_history, query)

# Print the suggestions
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
