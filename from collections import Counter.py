from collections import Counter

def min_operations(str1, str2):
    # Count frequency of each character in both strings
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # Initialize deletion and insertion counts
    deletions = 0
    insertions = 0
    
    # Calculate deletions and insertions
    for char in count1:
        if char in count2:
            if count1[char] > count2[char]:
                deletions += count1[char] - count2[char]
        else:
            deletions += count1[char]
    
    for char in count2:
        if char not in count1:
            insertions += count2[char]
        elif count2[char] > count1[char]:
            insertions += count2[char] - count1[char]
    
    return deletions, insertions

# Example usage
str1 = "heap"
str2 = "pea"
deletions, insertions = mi
