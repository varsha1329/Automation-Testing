def Search_Longest_String(string_List):
    string_Len = []
    for n in string_List:
        string_Len.append((len(n), n))
    string_Len.sort()
    return string_Len[-1][0], string_Len[-1][1]
result = Search_Longest_String(["Atombomb" , "Hiroshima" ,"America"])
print("\nLongest word:",result[1])
print("Length of the longest word:",result[0])


