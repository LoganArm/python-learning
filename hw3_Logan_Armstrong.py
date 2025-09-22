import re


# ================================
# Part 1: Advanced String Methods
# ================================

def format_receipt(items, prices, quantities):
    """
    Create a formatted receipt using string methods.
    """
    header = "=" * 40 + "\n"
    header += f"{'Item':<20}{'Qty':^5}{'Price':>15}\n"
    header += "=" * 40 + "\n"

    lines = ""
    total = 0
    for item, price, qty in zip(items, prices, quantities):
        line_total = price * qty
        total += line_total
        lines += f"{item:<20}{qty:^5}${line_total:>8.2f}\n"

    footer = "=" * 40 + "\n"
    footer += f"{'TOTAL':<25}${total:>8.2f}\n"
    footer += "=" * 40

    return header + lines + footer


def process_user_data(raw_data):
    """
    Clean and process user input data using string methods.
    """
    name = " ".join(raw_data.get("name", "").split()).title()
    email = raw_data.get("email", "").replace(" ", "").lower()
    phone = re.sub(r"\D", "", raw_data.get("phone", ""))
    address = " ".join(raw_data.get("address", "").split()).title()

    parts = name.split()
    username = f"{parts[0].lower()}_{parts[-1].lower()}" if parts else ""

    validation = {
        "email_valid": bool(re.match(r"^[\w._]+@[\w.-]+\.\w+$", email)),
        "phone_valid": len(phone) == 10,
        "name_valid": len(parts) >= 2,
    }

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "username": username,
        "validation": validation,
    }


def analyze_text(text):
    """
    Perform comprehensive text analysis using string methods.
    """
    lines = text.splitlines()
    words = re.findall(r"\w+", text)
    total_chars = len(text)
    total_words = len(words)
    total_lines = len(lines)
    avg_word_length = round(sum(len(w) for w in words) / total_words, 2) if total_words else 0

    # most common word
    word_counts = {}
    for w in words:
        lw = w.lower()
        word_counts[lw] = word_counts.get(lw, 0) + 1
    most_common_word = max(word_counts, key=word_counts.get) if word_counts else None

    longest_line = max(lines, key=len) if lines else ""
    words_per_line = [len(re.findall(r"\w+", line)) for line in lines]

    sentences = re.split(r"(?<=[.!?])\s+", text.strip())
    capitalized_sentences = sum(1 for s in sentences if s and s[0].isupper())
    questions = sum(1 for s in sentences if s.endswith("?"))
    exclamations = sum(1 for s in sentences if s.endswith("!"))

    return {
        "total_chars": total_chars,
        "total_words": total_words,
        "total_lines": total_lines,
        "avg_word_length": avg_word_length,
        "most_common_word": most_common_word,
        "longest_line": longest_line,
        "words_per_line": words_per_line,
        "capitalized_sentences": capitalized_sentences,
        "questions": questions,
        "exclamations": exclamations,
    }


# ================================
# Part 2: Regular Expressions
# ================================

def find_patterns(text):
    """
    Find basic patterns in text using regex.
    """
    patterns = {
        "integers": r"\b\d+\b",
        "decimals": r"\b\d+\.\d+\b",
        "words_with_digits": r"\b\w*\d\w*\b",
        "capitalized_words": r"\b[A-Z][a-z]+\b",
        "all_caps_words": r"\b[A-Z]{2,}\b",
        "repeated_chars": r"\b\w*(\w)\1\w*\b",
    }

    return {k: re.findall(v, text) if k != "repeated_chars" else re.findall(v, text) for k, v in patterns.items()}


def validate_format(input_string, format_type):
    """
    Validate if input matches specified format using regex.
    """
    patterns = {
        "phone": r"^(?:\((\d{3})\)\s*(\d{3})-(\d{4})|(\d{3})-(\d{3})-(\d{4}))$",
        "date": r"^(0[1-9]|1[0-2])/([0-2]\d|3[01])/(\d{4})$",
        "time": r"^(?:(\d{1,2}):(\d{2})\s*([AP]M)|([01]\d|2[0-3]):([0-5]\d))$",
        "email": r"^([\w._]+)@([\w.-]+)\.(\w+)$",
        "url": r"^(https?)://([\w.-]+)(?:/.*)?$",
        "ssn": r"^(\d{3})-(\d{2})-(\d{4})$",
    }

    pattern = patterns.get(format_type)
    if not pattern:
        return (False, None)

    match = re.match(pattern, input_string)
    if not match:
        return (False, None)

    parts = {}
    if format_type == "phone":
        if match.group(1):
            parts = {"area_code": match.group(1), "prefix": match.group(2), "line": match.group(3)}
        else:
            parts = {"area_code": match.group(4), "prefix": match.group(5), "line": match.group(6)}
    elif format_type == "date":
        parts = {"month": match.group(1), "day": match.group(2), "year": match.group(3)}
    elif format_type == "time":
        if match.group(1):
            parts = {"hour": match.group(1), "minute": match.group(2), "ampm": match.group(3)}
        else:
            parts = {"hour": match.group(4), "minute": match.group(5)}
    elif format_type == "email":
        parts = {"username": match.group(1), "domain": match.group(2), "ext": match.group(3)}
    elif format_type == "url":
        parts = {"protocol": match.group(1), "domain": match.group(2)}
    elif format_type == "ssn":
        parts = {"area": match.group(1), "group": match.group(2), "serial": match.group(3)}

    return (True, parts)


def extract_information(text):
    """
    Extract specific information from unstructured text.
    """
    prices = re.findall(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?", text)
    percentages = re.findall(r"\d+(?:\.\d+)?%", text)
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    sentences = re.findall(r"[^.!?]+[.!?]", text)
    questions = [s for s in sentences if s.strip().endswith("?")]
    quoted_text = re.findall(r'"([^"]+)"', text)

    return {
        "prices": prices,
        "percentages": percentages,
        "years": years,
        "sentences": [s.strip() for s in sentences],
        "questions": questions,
        "quoted_text": quoted_text,
    }


# ================================
# Part 3: Combined
# ================================

def clean_text_pipeline(text, operations):
    """
    Apply a series of cleaning operations using both string methods and regex.
    """
    original = text
    steps = []

    for op in operations:
        if op == "trim":
            text = text.strip()
        elif op == "lowercase":
            text = text.lower()
        elif op == "remove_punctuation":
            text = re.sub(r"[^\w\s]", "", text)
        elif op == "remove_digits":
            text = re.sub(r"\d", "", text)
        elif op == "remove_extra_spaces":
            text = re.sub(r"\s+", " ", text)
        elif op == "remove_urls":
            text = re.sub(r"https?://\S+", "", text)
        elif op == "remove_emails":
            text = re.sub(r"[\w._]+@[\w.-]+\.\w+", "", text)
        elif op == "capitalize_sentences":
            sentences = re.split(r"(?<=[.!?])\s+", text)
            text = " ".join(s.strip().capitalize() for s in sentences if s)
        steps.append(text)

    return {"original": original, "cleaned": text, "steps": steps}


def smart_replace(text, replacements):
    """
    Perform intelligent text replacements using patterns.
    """
    contractions = {
        "don't": "do not",
        "won't": "will not",
        "can't": "cannot",
        "I'm": "I am",
        "you're": "you are",
        "it's": "it is",
        "he's": "he is",
        "she's": "she is",
        "we're": "we are",
        "they're": "they are",
        "I've": "I have",
        "you've": "you have",
        "we've": "we have",
        "they've": "they have",
    }

    if replacements.get("censor_phone"):
        text = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text)
    if replacements.get("censor_email"):
        text = re.sub(r"[\w._]+@[\w.-]+\.\w+", "[EMAIL]", text)
    if replacements.get("fix_spacing"):
        text = re.sub(r"\s*([,.!?;:])\s*", r"\1 ", text)
    if replacements.get("expand_contractions"):
        for c, exp in contractions.items():
            text = re.sub(rf"\b{re.escape(c)}\b", exp, text, flags=re.IGNORECASE)
    if replacements.get("number_to_word"):
        num_words = {
            "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
            "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
        }
        for d, w in num_words.items():
            text = re.sub(rf"\b{d}\b", w, text)

    return text


# ================================
# Part 4: Log File Analyzer
# ================================

def analyze_log_file(log_text):
    """
    Analyze a simplified log file format using string methods and regex.
    """
    entries = re.findall(r"\[(.*?) (.*?)\] (\w+): (.*)", log_text)
    total_entries = len(entries)
    error_count = sum(1 for e in entries if e[2] == "ERROR")
    warning_count = sum(1 for e in entries if e[2] == "WARNING")
    info_count = sum(1 for e in entries if e[2] == "INFO")
    dates = sorted(set(e[0] for e in entries))
    error_messages = [e[3] for e in entries if e[2] == "ERROR"]

    times = [e[1] for e in entries]
    time_range = (min(times), max(times)) if times else ("", "")

    hours = {}
    for t in times:
        h = int(t.split(":")[0])
        hours[h] = hours.get(h, 0) + 1
    most_active_hour = max(hours, key=hours.get) if hours else None

    return {
        "total_entries": total_entries,
        "error_count": error_count,
        "warning_count": warning_count,
        "info_count": info_count,
        "dates": dates,
        "error_messages": error_messages,
        "time_range": time_range,
        "most_active_hour": most_active_hour,
    }


# ================================
# Testing
# ================================

def run_tests():
    """Test all functions with sample data."""

    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)

    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)

    test_data = {
        "name": "  john DOE  ",
        "email": " JOHN@EXAMPLE.COM ",
        "phone": "(555) 123-4567",
        "address": "123  main  street"
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned['name']}")
    print(f"Cleaned email: {cleaned['email']}")

    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)

    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns['integers']}")
    print(f"Found decimals: {patterns['decimals']}")

    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}, Parts: {phone_parts}")

    info_text = 'The price is $19.99 (20% off). "Great deal!" she said.'
    info = extract_information(info_text)
    print(f"\nPrices found: {info['prices']}")
    print(f"Percentages found: {info['percentages']}")
    print(f"Quoted text: {info['quoted_text']}")

    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)

    dirty_text = "  Hello   WORLD!  "
    operations = ["trim", "lowercase", "remove_extra_spaces"]
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result['original']}'")
    print(f"Cleaned: '{cleaned_result['cleaned']}'")

    text = "Call me at 555-123-4567. I'm busy."
    rules = {"censor_phone": True, "expand_contractions": True}
    print(f"Smart replace: {smart_replace(text, rules)}")

    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)

    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:31:00] INFO: Retry attempt
[2024-01-15 10:32:00] WARNING: Timeout warning"""

    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis['total_entries']}")
    print(f"Error count: {log_analysis['error_count']}")
    print(f"Unique dates: {log_analysis['dates']}")

    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)


if __name__ == "__main__":
    run_tests()
