def rijec_unatrag(string):
    if string == "":
        return""
    return rijec_unatrag(string[1:])+string[0]
print(rijec_unatrag("Mostar"))
