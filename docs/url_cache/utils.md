Module url_cache.utils
======================

Functions
---------

`backoff_warn(details: dict[str, typing.Any]) ‑> None`
:   

`clean_url(urlstr: str) ‑> str`
:   unquotes and removes whitespace from URLs
    https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote

`fibo_backoff() ‑> Generator[float, None, None]`
:   Fibonacci backoff, with the first 6 elements consumed.
    In other words, this starts at 13, 21, ....

`normalize_path(p: str | pathlib.Path) ‑> pathlib.Path`
:   

`parse_timedelta_string(timedelta_str: str) ‑> datetime.timedelta`
:   This uses a syntax similar to the 'GNU sleep' command
    e.g.: 1w5d5h10m50s means '1 week, 5 days, 5 hours, 10 minutes, 50 seconds'