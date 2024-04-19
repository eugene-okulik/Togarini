text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,"
        "dignissim vitae libero")
words = text.split()

result = []
for word in words:
    sep = ""
    if word[-1] in [',', '.']:
        sep = word[-1]
        word = word[:-1]

    new_word = word + "ing" + sep
    result.append(new_word)

new_text = " ".join(result)
print(new_text)
