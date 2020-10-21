thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["brand"] = "Chevy"
print(thisdict)

print(thisdict.values())

for i in thisdict.items():
    print(i)

thisdict["collectible"] = True
thisdict.pop("collectible")
thisdict.clear()
print(thisdict)
x = dict({"one": "two"})
print(x)
