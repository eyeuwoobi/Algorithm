import sys

L = int(sys.stdin.readline())
string = sys.stdin.readline()

hash_value = 0

for i in range(L):
    hash_value += (ord(string[i]) - 96) * (31 ** i)

print(hash_value)