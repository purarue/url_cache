Module url_cache.model
======================

Functions
---------

`dumps(data: Any) ‑> str`
:   Dump a Summary object to JSON

Classes
-------

`Summary(url: str, data: dict[str, typing.Any] = <factory>, metadata: dict[str, typing.Any] = <factory>, html_summary: str | None = None, timestamp: datetime.datetime | None = None)`
:   Represents all possible data for a URL
    
    URL
    Metadata (description, images, page metadata) - from Lassie
    HTML Summary (parsed with readability)
    Timestamp (when this information was scraped)
    Data (any other data extracted from this site)

    ### Instance variables

    `data: dict[str, typing.Any]`
    :   The type of the None singleton.

    `html_summary: str | None`
    :   The type of the None singleton.

    `metadata: dict[str, typing.Any]`
    :   The type of the None singleton.

    `timestamp: datetime.datetime | None`
    :   The type of the None singleton.

    `url: str`
    :   The type of the None singleton.