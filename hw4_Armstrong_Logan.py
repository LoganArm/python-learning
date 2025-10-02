import re
import time

# -------------------------
# Problem 1: Grouping and Capturing
# -------------------------
def problem1():
    # a) Extract ISO dates YYYY-MM-DD
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    pattern_iso = r"\b\d{4}-\d{2}-\d{2}\b"
    iso_dates = re.findall(pattern_iso, dates_text)

    # b) Extract username/domain from emails
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    pattern_email = r"(?P<username>[\w._-]+)@(?P<domain>[\w.-]+)"
    email_parts = [m.groupdict() for m in re.finditer(pattern_email, emails_text)]

    # c) Phone numbers with area code
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    pattern_phone = r"(?:\((\d{3})\)|(?:(\d{3})))[- ]?(\d{3}-\d{4})"
    phone_numbers = []
    for m in re.finditer(pattern_phone, phones_text):
        area = m.group(1) if m.group(1) else m.group(2)
        phone_numbers.append((area, m.group(3)))

    # d) Repeated words
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    pattern_repeated = r"\b(\w+)\s+\1\b"
    repeated_words = [m.group(1).lower() for m in re.finditer(pattern_repeated, repeated_text, re.IGNORECASE)]

    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }

# -------------------------
# Problem 2: Alternation
# -------------------------
def problem2():
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    pattern_images = r"\b\w+\.(?:jpg|jpeg|png|gif)\b"
    image_files = re.findall(pattern_images, files_text, re.IGNORECASE)

    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    pattern_dates = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\w+ \d{1,2}, \d{4}\b"
    all_dates = re.findall(pattern_dates, mixed_dates)

    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    pattern_prices = r"(?:\$\d+\.\d{2}|USD \d+\.\d{2}|\d+ dollars|€\d+\.\d{2}|£\d+\.\d{2})"
    prices = re.findall(pattern_prices, prices_text)

    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    pattern_langs = r"\b(?:Python|JavaScript|JS|Java|C\+\+|CPP)\b"
    languages = re.findall(pattern_langs, code_text)

    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }

# -------------------------
# Problem 3: findall vs finditer
# -------------------------
def problem3():
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
    pattern_timestamp = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"
    timestamps = re.findall(pattern_timestamp, log_text)

    pattern_log = r"\]\s(\w+): (.*)"
    log_entries = re.findall(pattern_log, log_text)

    pattern_ip = r"\b\d{1,3}(?:\.\d{1,3}){3}\b"
    ip_addresses = [{"ip": m.group(), "start": m.start(), "end": m.end()} for m in re.finditer(pattern_ip, log_text)]

    def highlight_errors(text):
        return re.sub(r"ERROR", r"**ERROR**", text)

    highlighted_log = highlight_errors(log_text)

    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }

# -------------------------
# Problem 4: re.sub() transformations
# -------------------------
def problem4():
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    def standardize_phones(text):
        pattern = r"\D*(\d{3})\D*(\d{3})\D*(\d{4})"
        return re.sub(pattern, r"(\1) \2-\3", text)
    cleaned_phones = standardize_phones(messy_phones)

    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    def redact_sensitive(text):
        text = re.sub(r"\d{3}-\d{2}-\d{4}", "XXX-XX-XXXX", text)
        text = re.sub(r"\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}", "XXXX-XXXX-XXXX-XXXX", text)
        return text
    redacted_text = redact_sensitive(sensitive_text)

    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    def markdown_to_html(text):
        return re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2">\1</a>', text)
    html_text = markdown_to_html(markdown_text)

    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {'name': 'John Smith', 'order_id': '12345', 'product': 'Python Book', 'tracking': 'TRK789XYZ'}
    def fill_template(template, values):
        return re.sub(r"{(\w+)}", lambda m: values.get(m.group(1), m.group(0)), template)
    filled_template = fill_template(template, values)

    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }

# -------------------------
# Problem 5: Compiled Patterns
# -------------------------
def problem5():
    class PatternLibrary:
        EMAIL = re.compile(r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$", re.IGNORECASE)
        URL = re.compile(r"^(https?://)?[\w.-]+\.[A-Za-z]{2,}(/[\w./-]*)?$")
        ZIP_CODE = re.compile(r"^\d{5}(-\d{4})?$")
        PASSWORD = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^\w]).{8,}$", re.VERBOSE)
        CREDIT_CARD = re.compile(r"^(?:\d{4}[- ]?){3}\d{4}$")

    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }

    validation_results = {
        'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']]
    }

    return validation_results

# -------------------------
# Problem 6: Log Analyzer
# -------------------------
def problem6():
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """

    # Regex for: IP, timestamp, method, path, status, size
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - '
        r'\[(?P<timestamp>[^\]]+)\] '
        r'"(?P<method>[A-Z]+) (?P<path>[^ ]+) [^"]+" '
        r'(?P<status>\d{3}) (?P<size>\d+)'
    )

    parsed_logs = []
    for m in log_pattern.finditer(log_data):
        entry = m.groupdict()
        entry['status'] = int(entry['status'])
        entry['size'] = int(entry['size'])
        parsed_logs.append(entry)

    # Analyze logs
    analysis = {
        'total_requests': len(parsed_logs),
        'unique_ips': sorted(set(e['ip'] for e in parsed_logs)),
        'error_count': sum(1 for e in parsed_logs if 400 <= e['status'] < 600),
        'total_bytes': sum(e['size'] for e in parsed_logs),
        'most_requested_path': max(
            set(e['path'] for e in parsed_logs),
            key=lambda p: sum(1 for e in parsed_logs if e['path'] == p)
        ),
        'methods_used': sorted(set(e['method'] for e in parsed_logs))
    }

    return {'parsed_logs': parsed_logs, 'analysis': analysis}


# -------------------------
# Main Runner
# -------------------------
if __name__ == "__main__":
    print("Problem 1 Results:", problem1())
    print("\nProblem 2 Results:", problem2())
    print("\nProblem 3 Results:", problem3())
    print("\nProblem 4 Results:", problem4())
    print("\nProblem 5 Results:", problem5())
    print("\nProblem 6 Results:", problem6())