phrase = input().casefold()
vowels = ['a', 'o', 'u', 'i', 'e', 'y']
result = {i: phrase.count(i) for i in vowels}
print(result)