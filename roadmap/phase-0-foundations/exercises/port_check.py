"""Report open TCP ports on a host you own or are authorized to test."""

import argparse
import socket


def parse_ports(spec):
    ports = set()
    for part in spec.split(","):
        if "-" in part:
            start, end = part.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)


def is_open(host, port, timeout):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host")
    parser.add_argument("-p", "--ports", default="22,80,443", help="e.g. 22,80,8000-8010")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="seconds per port")
    args = parser.parse_args()

    try:
        ports = parse_ports(args.ports)
    except ValueError:
        parser.error(f"invalid port list: {args.ports}")

    for port in ports:
        if is_open(args.host, port, args.timeout):
            print(f"{port}/tcp open")


if __name__ == "__main__":
    main()
