def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def check(word, dictionary):
    return word in dictionary

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    previous_row = list(range(len(s2) + 1))
    
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            current_row.append(min(
                previous_row[j + 1] + 1,      # insertion
                current_row[j] + 1,           # deletion
                previous_row[j] + (c1 != c2)  # substitution
            ))
        previous_row = current_row
    
    return previous_row[-1]

def suggest(word, dictionary, max_distance=2):
    # Filter by length first, then calculate distance
    candidates = [(w, levenshtein_distance(word, w)) 
                 for w in dictionary 
                 if abs(len(w) - len(word)) <= max_distance]
    
    # Filter by distance and sort
    suggestions = [w for w, dist in sorted(
        [c for c in candidates if c[1] <= max_distance], 
        key=lambda x: x[1]
    )[:5]]
    
    return suggestions

# Load the dictionary
nepali_words = load_dictionary("lekhnus.dic")

# Example usage
word1, word2 = "नेपाल", "नेपल"
print(f"Is '{word1}' correct? {check(word1, nepali_words)}")
print(f"Is '{word2}' correct? {check(word2, nepali_words)}")
print(f"Suggestions for '{word2}': {suggest(word2, nepali_words)}")