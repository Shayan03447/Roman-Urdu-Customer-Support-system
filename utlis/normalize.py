import re

def normalize_text(text: str)-> str:

    if not isinstance(text, str):
        raise TypeError("normalize_text: input must be a string")
    try:
        text=text.lower()
        text=text.strip()
        text=re.sub(r"\s+", " ", text)
        return text
    except Exception as e:
        raise ValueError(f"Text normalization error : {e}")


