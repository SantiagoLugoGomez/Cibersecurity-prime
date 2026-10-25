#!/usr/bin/env bash
# Run inside a lab VM. Passes only if the VM cannot reach the internet.
set -u

reachable=0

if ping -c 2 -W 2 1.1.1.1 >/dev/null 2>&1; then
    echo "FAIL: ICMP to 1.1.1.1 succeeded"
    reachable=1
fi

if getent hosts example.com >/dev/null 2>&1; then
    echo "FAIL: public DNS name resolved"
    reachable=1
fi

if command -v curl >/dev/null && curl -s -m 5 -o /dev/null https://example.com; then
    echo "FAIL: HTTPS to example.com succeeded"
    reachable=1
fi

if [ "$reachable" -eq 0 ]; then
    echo "PASS: no internet access from this VM"
fi
exit "$reachable"
