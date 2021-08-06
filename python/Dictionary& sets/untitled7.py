myDict={
        "fast":"In a quick manner",
        "harry":"A coder",
        "marks":[1,2,5],
        "anotherdict":{'harry':'player'}
        }
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict={
    "Lovish":"friend",
    "Divya":"Friend",
    "Shubham":"Friend",
    "harry":"A Dancer"
    }
myDict.update(updateDict)
print(myDict)
print(myDict.get("harry"))
print(myDict["harry"])
print(myDict.get("harry2"))
#print(myDict["harry2"])