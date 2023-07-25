def longest_palindromic_substring(inp):
    possible_comb = set()
    palindroms = []
    for i in range(len(inp)):
        for j in range(i, len(inp)):
            for k in range(len(inp)):
                if len(inp[j:j+k]) in [0, 1]:
                    pass
                else:
                    possible_comb.add(inp[j:j+k])
    for j in possible_comb:
        if j == j[::-1]:
            palindroms.append(j)
    selected = palindroms[0]
    for k in range(len(palindroms)):
        if len(palindroms[k]) > len(selected):
            selected = palindroms[k]
    print(selected)
    print(possible_comb)
    print(palindroms)
if __name__ == '__main__':
    longest_palindromic_substring('abcdffdsfffffffs')
