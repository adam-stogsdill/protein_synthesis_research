import torch

def load_token_keys(key_loc="./basic_tokens.txt") -> dict[str, int]:
    token_keys = []
    with open(key_loc, 'r') as token_txt:
        while line := token_txt.readline():
            token_keys.append(line.strip())
    return {k : i for i, k in enumerate(token_keys)}