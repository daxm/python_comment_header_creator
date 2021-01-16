import typing

MAXWIDTH = 120
BEGINNING = "# -"
EXPANDER = "=-"
ENDING = " #"


def generate_line(
        title: str = "",
        max_width: int = MAXWIDTH,
        beginning: str = BEGINNING,
        ending: str = ENDING,
        expander: str = EXPANDER,
) -> typing.Tuple[str, bool]:
    if title:
        title = f" {title.upper()} -"
    else:
        title = expander
    remaining = max_width - len(beginning) - len(ending) - len(title)
    if remaining > 0:
        valid_title = True
        multiplier = int(remaining / 2 / len(expander))
        filler = expander * multiplier

        output = f"{beginning}{filler}{title}{filler}{ending}"
        return output, True
    else:
        max_length = max_width - len(beginning) - len(ending) - 2
        print(f"Tile is too long.  Max possible title length: {max_length}")
        return "", False


def uniline(
        title: str = "",
        max_width: int = MAXWIDTH,
        beginning: str = BEGINNING,
        ending: str = ENDING,
        expander: str = EXPANDER,
) -> str:
    output = ""
    _title = ""
    valid_title = False

    if title:
        _title = title

    while not valid_title:
        if not title:
            _title = input("Enter Title: ")
        output, valid_title = generate_line(
            title=_title,
            max_width=max_width,
            beginning=beginning,
            ending=ending,
            expander=expander,
        )
    return output


def multiline(
        title: str = "",
        max_width: int = MAXWIDTH,
        beginning: str = BEGINNING,
        ending: str = ENDING,
        expander: str = EXPANDER,
) -> str:
    no_title, status = generate_line(max_width=max_width, beginning=beginning, ending=ending, expander=expander)
    title_line = uniline(title=title,max_width=max_width, beginning=beginning, ending=ending, expander=expander)
    return f"{no_title}\n{title_line}\n{no_title}"


if __name__ == "__main__":
    pass
