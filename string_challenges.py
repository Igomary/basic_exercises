# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))

# Вывести количество гласных букв в слове
word = 'Архангельск'
word = word.lower
vowels = 'аяоёуюэеыи'
num_vowels = 0

for each in word:
    if each in vowels:
        num_vowels += 1

print(num_vowels)




# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
splitted_sentence =sentence.split(' ')
print(len(splitted_sentence))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
splitted_sentence =sentence.split(' ')
for each in splitted_sentence:
    print(each)
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
splitted_sentence =sentence.split(' ')
words = len(splitted_sentence)
print((len(sentence)-(words-1))/words)