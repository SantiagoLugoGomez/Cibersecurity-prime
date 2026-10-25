# Phase 0 exercises

Three small scripts that use only the Python standard library. They work as they are; the tasks below ask you to extend them. Run them only against machines you own or are explicitly allowed to test, such as the VMs in your [home lab](../../../homelab/README.md).

| Script | What it does | Concepts |
|---|---|---|
| [`port_check.py`](port_check.py) | Tries a TCP connection to each port in a list | Sockets, timeouts, the TCP handshake |
| [`http_headers.py`](http_headers.py) | Reports which common security headers a URL returns | HTTP, TLS, response headers |
| [`failed_logins.py`](failed_logins.py) | Counts failed SSH logins per source IP and user in an `auth.log` file | Regex, counters, log analysis |

```bash
python3 port_check.py 192.168.56.10 -p 20-25,80,443
python3 http_headers.py https://example.com
python3 failed_logins.py sample-auth.log --top 5
```

`sample-auth.log` contains invented entries that use the documentation address ranges from RFC 5737, so it is safe to share.

## Tasks

1. `port_check.py`: add concurrency with `concurrent.futures.ThreadPoolExecutor`, then measure the speed difference on a /24 in your lab. Explain in your notes why a closed port answers quickly and a filtered port times out.
2. `http_headers.py`: print the TLS version and cipher negotiated (hint: `ssl.SSLSocket.version()` and `cipher()`), and flag a `Strict-Transport-Security` header whose `max-age` is shorter than one year.
3. `failed_logins.py`: add a `--since` option that filters by timestamp, and output JSON when `--json` is passed. Then write the same logic as a one-line pipeline with `grep`, `awk`, `sort` and `uniq -c`, and compare.
