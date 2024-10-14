import shlex

def Tokenize_Input(InputString):
    """Tokenizes an input string into a format suitable for subprocess.
    Args:
        input_string: The input string to tokenize.
    Returns:
        A list of tokens.
    """
    try:
        tokens = shlex.split(InputString)
        return tokens
    except ValueError as e:
        print(f"Error Tokenizing Input: {e}")
        return None