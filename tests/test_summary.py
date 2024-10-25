import json
import datetime

from url_cache.model import Summary, dumps


def test_summary_dumps() -> None:
    s = Summary(
        url="https://github.com/purarue",
        metadata={
            "videos": [],
            "site_name": "GitHub",
            "title": "purarue - Overview",
            "url": "https://github.com/purarue",
            "description": ":). purarue has 124 repositories available. Follow their code on GitHub.",
            "locale": "en_US",
            "status_code": 200,
        },
        timestamp=datetime.datetime(2021, 5, 11, 20, 0, 31, 724132),
    )
    assert json.loads(dumps(s))["url"] == "https://github.com/purarue"
