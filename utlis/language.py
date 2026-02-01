def detect_language(text):
    if any("\u0600" <= c <= "\u06FF" for c in text):
        return "urdu"
    else:
        return "roman_urdu"
