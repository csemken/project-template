LATEX_ESCAPE_CHARS_TEXT = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
    "\\": r"\textbackslash{}",
}
LATEX_ESCAPE_CHARS_MATH = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "{": r"\{",
    "}": r"\}",
    "~": r"\sim",
    "\\": r"\backslash",
}
LATEX_ESCAPE_SPACE = {" ": r"\ "}
LATEX_PROP_ENTRY = "\\prop_put:Nnn \\{prop_name} {{ {key} }} {{ {value} }}\n"


def escape_latex(
    string: str, escape_mode: str = "text", escape_spaces: bool = True
) -> str:
    if escape_mode == "text":
        escape_dict = LATEX_ESCAPE_CHARS_TEXT
    elif escape_mode == "math":
        escape_dict = LATEX_ESCAPE_CHARS_MATH
    elif escape_mode == "none":
        escape_dict = {}
    else:
        raise ValueError('escape_mode has to be "text", "math" or "none"')

    if escape_spaces:
        escape_dict = escape_dict | LATEX_ESCAPE_SPACE

    return "".join(escape_dict.get(c, c) for c in string)


def dict_to_autofilling_values(
    values: dict,
    prop_name: str = "varProp",
    escape_mode: str = "text",
    escape_spaces: bool = True,
) -> str:
    r"""Save autofilling values for usage in LaTeX.

    Parameters
    ----------
    values : Dictionary of values to be saved.
    prop_name : LaTeX3 prop name. Needs to be a valid macro name
        (letters only).
    escape_mode : {"text", "math", "none"}
        How to escape characters. Possible values are:
        - "text": Escape characters for text mode.
        - "math": Escape characters for math mode.
        - "none": Do not escape characters.
    escape_spaces : If `True`, escape spaces " " to "\ "

    Returns
    -------
    LaTeX3 code that can be used in a tex or lyx file, after
    `\prop_new:N \varProp`, where `varProp` is the value of the
    `prop_name` parameter above.

    Examples
    --------
    >>> dict_to_autofilling_values(
    ...     {
    ...         "int-example": 3,
    ...         "pct-example": f"{1/3:.2%}",
    ...         "txt-example": "This is a test sentence.",
    ...     }
    ... )
    \prop_put:Nnn \varProp { int-example } { 3 }
    \prop_put:Nnn \varProp { pct-example } { 33.33\% }
    \prop_put:Nnn \varProp { txt-example } { This\ is\ a\ test\ sentence. }

    """
    assert prop_name.isalpha()

    output = ""
    for key, value in values.items():
        value = escape_latex(str(value), escape_mode, escape_spaces)
        output += LATEX_PROP_ENTRY.format(
            prop_name=prop_name,
            key=key,
            value=value,
        )

    return output
