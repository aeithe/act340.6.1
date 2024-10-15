states1 = {
    "California": "Los Angeles",
    "New York": "Albany",
    "Hawaii" : "Honolulu",
    "Alaska" : "Juneau",
    "Texas" : "Austin"
}

states2 = dict([
    ("California", "Los Angeles"),
    ("New York","Albany"),
    ("Hawaii" , "Honolulu"),
    ("Alaska" , "Juneau"),
    ("Texas" , "Austin")
])

print(type(states1))
print(type(states2))
print(states1)
print(states2)


print(states1["California"])
states1["Florida"] = "Tallahassee"
states1["California"] = "Sacremento"
del states1["Alaska"]
print(states1)

playlist = {
    "Linkin Park" : "In The End",
    "Euro Trash" : "Dipped In Sugar",
    "Yellow Claw": "Crash This Party",
    "System Of A Down" : "BYOB",
    "KILLEDDY" : "STILLINTOU",
    "AREZRA" : "Goodbye"
}

for artist in playlist.keys():
    print(artist)

for song in playlist.values():
    print(song)

for artist, song in playlist.items():
    print(f"{song} by {artist} is in the current playlist")

playlist.popitem();
playlist["Taylor Swift"] = "Anti-Hero"

playlist["Euro Trash"] = "Remix " + playlist["Euro Trash"]

print(playlist)

def print_all(songlist):
    for artist, song in songlist.items():
        print(f"{song} by {artist}")


print_all(playlist)