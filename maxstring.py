def is_special(word):
    return len(set(word)) == max_word_distinct_count
words = input().split()
max_word = ""
max_word_distinct_count = 0
for word in words:
    distinct_count = len(set(word.lower()))
    if distinct_count > max_word_distinct_count or (distinct_count == max_word_distinct_count and word < max_word):
        max_word = word 
        max_word_distinct_count = distinct_count 
print(max_word)