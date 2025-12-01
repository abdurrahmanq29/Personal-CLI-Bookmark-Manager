import json

def list_bookmarks():
    file.seek(0)
    try:
        bookmarks = json.load(file)
        if not bookmarks:
            print("No bookmarks found.")
        else:
            print("Existing bookmarks:")
            for name, url in bookmarks.items():
                print(f"{name}: {url}")
    except json.JSONDecodeError:
        print("No bookmarks found.")

bookmark_or_create = input("Would you like to access an existing bookmark(a) or\ncreate a new bookmark(b) or\nremove an existing bookmark(c)? (a/b/c): ").strip().lower()
with open("bookmarks.json", "a+") as file:
    if bookmark_or_create == 'a':
        list_bookmarks()

    elif bookmark_or_create == 'b':
        name = input("Enter the name for the bookmark: ").strip()
        url = input("Enter the URL for the bookmark: ").strip()
        try:
            file.seek(0)
            bookmarks = json.load(file)
        except json.JSONDecodeError:
            bookmarks = {}
        bookmarks[name] = url
        file.seek(0)
        file.truncate()
        json.dump(bookmarks, file)
        print(f"Bookmark '{name}' added.")
    elif bookmark_or_create == 'c':
        list_bookmarks()
        name = input("Enter the name of the bookmark to remove: ").strip()
        try:
            file.seek(0)
            bookmarks = json.load(file)
            if name in bookmarks:
                del bookmarks[name]
                file.seek(0)
                file.truncate()
                json.dump(bookmarks, file)
                print(f"Bookmark '{name}' removed.")
            else:
                print(f"No bookmark found with the name '{name}'.")
        except json.JSONDecodeError:
            print("No bookmarks found.")

