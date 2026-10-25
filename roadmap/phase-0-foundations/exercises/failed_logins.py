"""Count failed SSH password attempts per source IP and per user in an auth.log file."""

import argparse
import re
from collections import Counter

FAILED = re.compile(r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)")


def parse(path):
    by_ip, by_user = Counter(), Counter()
    with open(path, encoding="utf-8", errors="replace") as log:
        for line in log:
            match = FAILED.search(line)
            if match:
                by_ip[match["ip"]] += 1
                by_user[match["user"]] += 1
    return by_ip, by_user


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("logfile")
    parser.add_argument("--top", type=int, default=10)
    args = parser.parse_args()

    try:
        by_ip, by_user = parse(args.logfile)
    except OSError as error:
        raise SystemExit(f"Cannot read {args.logfile}: {error}")

    print("Top source IPs:")
    for ip, count in by_ip.most_common(args.top):
        print(f"  {count:>5}  {ip}")
    print("Top targeted users:")
    for user, count in by_user.most_common(args.top):
        print(f"  {count:>5}  {user}")


if __name__ == "__main__":
    main()
