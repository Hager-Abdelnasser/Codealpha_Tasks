"""
CodeAlpha Internship - Task 3: Task Automation with Python Scripts
Automation idea: extract all email addresses from a .txt file and
save them to another file.
Concepts: os, re, file handling.

Usage:
    python email_extractor.py                      # uses input.txt -> emails.txt
    python email_extractor.py my_file.txt out.txt  # custom input / output
"""

import os
import re
import sys

EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

SAMPLE_TEXT = """Hello team,

Please contact hager@example.com or support@codealpha.tech for questions.
You can also reach the admin at admin@my-company.org.
Duplicate: hager@example.com
Not an email: hello@ and @world
Marketing: marketing.team+news@sub.domain.co.uk
"""


def create_sample_file(path):
    """Create a sample input file so the script can be tested right away."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(SAMPLE_TEXT)
    print(f"'{path}' was not found, so a sample file was created.")


def extract_emails(text):
    """Return a sorted list of unique emails found in the text."""
    found = EMAIL_PATTERN.findall(text)
    # Lowercase to treat Foo@x.com and foo@x.com as the same, then remove duplicates
    return sorted({email.lower() for email in found})


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "emails.txt"

    if not os.path.exists(input_path):
        create_sample_file(input_path)

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    emails = extract_emails(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")
    print(f"\nSaved to '{output_path}'")


if __name__ == "__main__":
    main()
