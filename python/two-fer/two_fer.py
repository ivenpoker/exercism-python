
def two_fer(name=None) -> str:
    """
    Return specific formatted information string based on presence
    of parameter.
    :param name: String (name) to format new returned string with.
    :return: Formatted string.
    """
    return f"One for {name if name else 'you'}, one for me."
