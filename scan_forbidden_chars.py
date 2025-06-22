


def scan_forbidden_chars(forbidden_keywords, text):
    # This function can be used to scan for forbidden characters in the text
    # For now, we will just return an empty list
    lowered_text = text.lower()
    return any(keyword in lowered_text for keyword in forbidden_keywords)

