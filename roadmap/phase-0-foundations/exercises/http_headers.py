"""Show which common security headers a URL returns."""

import argparse
import urllib.error
import urllib.request

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]


def fetch_headers(url, timeout):
    request = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.headers
    except urllib.error.HTTPError as error:
        return error.code, error.headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("-t", "--timeout", type=float, default=10)
    args = parser.parse_args()

    try:
        status, headers = fetch_headers(args.url, args.timeout)
    except (urllib.error.URLError, ValueError) as error:
        raise SystemExit(f"Request failed: {error}")

    print(f"HTTP {status} {args.url}")
    for name in SECURITY_HEADERS:
        value = headers.get(name)
        print(f"  [{'+' if value else '-'}] {name}: {value or 'missing'}")


if __name__ == "__main__":
    main()
