## string split
#txt = "apple@banana@@cherry@ @Orange"
#print(txt.split("@"))
#print(txt.split("@" , 2))

## string join
#txt = "Jhon Peter Vicky"
#txtTuple = ("Jhon" , "Peter", "Vicky")
#txtDict = {"name":"John", "Country":"Norway"}
#print("_".join(txt))
#print(" & ".join(txtTuple))
#print("TEST".join(txtDict))
def split_and_join(line):
    return "-".join(line.split(" "))

line = input()
result = split_and_join(line)
print(result)

