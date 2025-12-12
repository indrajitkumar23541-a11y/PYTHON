lists = [1, 2, 1]
lists_copy = lists.copy()
lists_copy.reverse()

if(lists==lists_copy):
    print("Palindrom")
else:
    print("Not Palindrom")