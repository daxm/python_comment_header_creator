import typing

MAXWIDTH = 120
EXPANDER = "=-"


def _generate_line(
    title: str = "", max_width: int = MAXWIDTH, expander: str = EXPANDER,
) -> typing.Tuple[str, bool]:
    if title:
        title = f" {title.upper()} {expander[-1]}"
    else:
        title = expander
    beginning = f"# {expander[-1]}"
    ending = f" #"
    remaining = max_width - len(beginning) - len(ending) - len(title)
    if remaining > 0:
        multiplier = int(remaining / 2 / len(expander))
        filler = expander * multiplier

        output = f"{beginning}{filler}{title}{filler}{ending}"
        return output, True
    else:
        max_length = max_width - len(beginning) - len(ending) - 2
        print(
            f"Length of string is too long.  Max possible string length: {max_length}."
        )
        print(
            f"Either increase 'max_width' value or decrease 'title', or 'expander' lengths."
        )
        return "", False


def uniline(
    title: str = "", max_width: int = MAXWIDTH, expander: str = EXPANDER,
) -> str:
    output = ""
    _title = ""
    valid_title = False

    if title:
        _title = title

    while not valid_title:
        if not title:
            _title = input("Enter Title: ")
        output, valid_title = _generate_line(
            title=_title, max_width=max_width, expander=expander,
        )
    return output


def multiline(
    title: str = "", max_width: int = MAXWIDTH, expander: str = EXPANDER,
) -> str:
    no_title, status = _generate_line(max_width=max_width, expander=expander)
    title_line = uniline(title=title, max_width=max_width, expander=expander)
    return f"{no_title}\n{title_line}\n{no_title}"


if __name__ == "__main__":
    pass
