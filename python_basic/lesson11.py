phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 94766281
}

phonebook.update(Jake=938273443)
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")