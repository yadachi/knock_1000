string1 = "パトカー"
string2 = "タクシー" 
string3 = list(map(lambda x,y:x+y, string1, string2))
print("".join(string3))
