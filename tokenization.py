import torch
import re

def load_token_keys(key_loc="./basic_tokens.txt") -> dict[str, int]:
    token_keys = []
    with open(key_loc, 'r') as token_txt:
        while line := token_txt.readline():
            token_keys.append(line.strip())
    return {k : i for i, k in enumerate(token_keys)}

def tokenize_sequence(sequence: str, vocab: dict[str, int]) -> list[str]:
    sequence_list = re.findall(r"(?:<[^>]+>)|(?:.)", sequence)
    
    return [vocab[token_key] for token_key in sequence_list]
