n = int(input())
dictionary = set()
dictionary_s = set()
for i in range(n):
    dictionary.add(input())
for item in dictionary:
    dictionary_s.add(item.lower())
text = input().split()
errors = 0
for word in text:
    if word in dictionary:
        continue
    let_s = 0
    for let in word:
        if 'a' <= let <= 'z':
            let_s += 1
    if let_s == len(word) - 1:
        if word.lower() in dictionary_s:
            errors += 1
        continue
    if (let_s == len(word) or
        let_s <= len(word) - 2):
        errors += 1
        continue
print(errors)
