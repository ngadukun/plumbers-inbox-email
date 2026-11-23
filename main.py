"""The Plumber's Inbox: a 120-word cold email.

Writes one cold email -- from a bookkeeping service to a busy plumber --
to /output/entry.txt and prints it. The email, subject line included,
is exactly 120 words and under 800 characters.
"""

import os

EMAIL = """Subject: Your invoices, done by Friday

Hi,

If your day starts at six, jumps from a burst pipe to a boiler call-out, and ends with invoices on the kitchen table at ten, I can take that last part off you.

I do the books for small plumbing firms. Send me your invoices, receipts and bank feed once a week. I chase late payers, sort your VAT, and send you one short list every Friday: who owes you, what you owe, and what is left.

It costs £140 a month, no contract. First step is smaller: send me last month's invoices and I will tidy them free, so you can judge the work.

Worth a quick try?

Tom Ellis, ClearLedger Books"""


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(EMAIL)
    print(EMAIL)


if __name__ == "__main__":
    main()
