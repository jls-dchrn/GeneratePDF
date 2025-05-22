import random

def generate_paragraph_text(lines: int, characters_per_line: int) -> str:
    """Generate placeholder text for a given number of lines and characters per line."""
    total_chars = int(lines * characters_per_line)
    words = []
    while sum(len(w) + 1 for w in words) < total_chars:
        word_length = random.randint(3, 10)
        word = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=word_length))
        words.append(word)
    return ' '.join(words)

