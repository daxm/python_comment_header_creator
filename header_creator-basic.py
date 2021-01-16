max_width = 80
beginning = "# -"
expander = "=-"
ending = " #"

output = ""
valid_title = False
while not valid_title:
    title = input("Enter Title: ")
    title = f" {title.upper()} -"
    remaining = max_width - len(beginning) - len(ending) - len(title)
    if remaining > 0:
        valid_title = True
        multiplier = int(remaining / 2)
        filler = expander * multiplier

        output = f"{beginning}{filler}{title}{filler}{ending}"
    else:
        max_length = max_width - len(beginning) - len(ending) - 2
        print(f"Tile is too long.  Max possible title length: {max_length}")

print(output)
