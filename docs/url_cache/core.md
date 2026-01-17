Module url_cache.core
=====================
Core functionality for url_cache, switches on the URLs to request different types of information
saves that to cache. If something has already been requested, returns it from cache.

Functions
---------

`preprocess_url(url: str) ‑> str`
:   Shorthand to expose default preprocess url steps as a function

Classes
-------

`URLCache(*, cache_dir: str | pathlib.Path | None = None, loglevel: int = 30, sleep_time: int = 5, additional_extractors: list[typing.Any] | None = None, file_parsers: list[url_cache.summary_cache.FileParser[~T]] | None = None, options: dict[str, typing.Any] | None = None)`
:   Main interface to the library
    
    sleep_time: time to wait between HTTP requests
    cache_dir: location the store cached data
               uses default user cache directory if not provided

    ### Instance variables

    `logpath: str`
    :   Returns the path to the url_cache logfile

    ### Methods

    `get(self, url: str) ‑> url_cache.model.Summary`
    :   Gets metadata/summary for a URL
        Save the parsed information in a local data directory
        If the URL already has cached data locally, returns that instead

    `get_cache_dir(self, url: str) ‑> str | None`
    :   If this URL is in cache, returns the location of the cache directory
        Returns None if it couldn't find a matching directory

    `in_cache(self, url: str) ‑> bool`
    :   Returns True if the URL already has cached information

    `preprocess_url(self, url: str) ‑> str`
    :   Runs each preprocess_url function from each enabled extractor,
        along with the default unquoting/strip

    `request_data(self, url: str, preprocess_url: bool = True) ‑> url_cache.model.Summary`
    :   Given a URL:
        
        Uses lassie to grab metadata
        Parses/minifies the HTML text with readablity/lxml
        
        Calls each enabled 'site' extractor, to extract additional information if a site matches the URL
        e.g. If this is a youtube URL, this requests youtube subtitles
        
        returns all the requested/parsed info as a models.Summary object

    `sleep(self) ‑> None`
    :