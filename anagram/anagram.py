def find_anagrams(word, candidates):
    anagrams = []
    for candidate_word in candidates:
        for character in candidate_word.lower():
            if character not in word.lower():
                break
            if candidate_word.lower().count(character) != word.lower().count(character):
                break
            if candidate_word.lower() == word.lower():
                break
        else:
            anagrams.append(candidate_word)
    return anagrams
