text = """Python is one of the most popular programming languages. Due to how beginner-friendly its syntax can be, it has become an incredibly versatile utility used for various purposes — including Artificial Intelligence (AI), web scraping, and even game development."""
words = text.split()

x = ""
for letter in words:
    if len(x) + len(letter) + 1 <= 40:
        x += letter + " "
    else:
        print(x.strip())
        x = letter + " "
if x:
    print(x.strip())




