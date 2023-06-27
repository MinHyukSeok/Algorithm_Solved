input_word = input()
length_word = len(input_word)
result_word_check = [200 for _ in range(length_word)]
result_word_list = []

for cut1 in range(length_word-1):
    for cut2 in range(length_word-1):
            if cut1 < cut2:
                cut_word1 = input_word[:cut1 + 1]
                cut_word2 = input_word[cut1 + 1:cut2 + 1]
                cut_word3 = input_word[cut2 + 1:]

                cut_word1 = ''.join(reversed(cut_word1))
                cut_word2 = ''.join(reversed(cut_word2))
                cut_word3 = ''.join(reversed(cut_word3))

                temp_word = cut_word1 + cut_word2 + cut_word3
                result_word_list.append(temp_word)

result_word_list.sort()
print(result_word_list[0])


