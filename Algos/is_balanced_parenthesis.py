def is_balanced_parentheses(inp):
    open_paran = []
    closed_paran = []
    for i in inp:
        if i == '(':
            open_paran.append(i)
        elif i == ')':
    if len(open_paran) == 0:
        print("Found ')' {open parentesis} in begenning given string is\nalready not in correct manner.")
        return False
    else:
        open_paran.pop()
        return True if len(open_paran) == 0 else False

if __name__ == "__main__":
print(is_balanced_parentheses("Check if this is balanced )
(()())"))
