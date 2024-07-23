import sys

N = int(sys.stdin.readline())

words = set()
for _ in range(N):
    words.add(sys.stdin.readline().rstrip())

letters = list(words)
letters.sort(key = lambda x : (len(x), x))

print(*letters, sep='\n')



# for _ in range(N-1):
#     letter = sys.stdin.readline()
#     if letter in words == True:
#         continue
#     else:
#         if len(words[-1]) < len(letter):
#             words.append(letter)
#         elif len(words[0]) > len(letter):
#             words.insert(0, letter)
#         else:
#             head = 0
#             tail = 0
#             for i in range(len(words)):
#                 if len(words[i]) == len(letter):
#                     head = i
#                     break
#             for i in range(len(words)-1, -1, -1):
#                 if len(words[i]) == len(letter):
#                     tail = i
#                     break
#             splitted_list = words[head:tail+1]
#             splitted_list.append(letter)
#             splitted_list.sort()
#             words  = words[:head] + splitted_list + words[tail:]
