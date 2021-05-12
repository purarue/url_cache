"""
Methods to parse HTML
"""

import readability  # type: ignore[import]
import lxml.html  # type: ignore[import]


# remove all attributes (e.g. id/class)
cleaner = lxml.html.clean.Cleaner()
cleaner.safe_attrs_only = True
cleaner.safe_attrs = frozenset([])


def summarize_html(html_text: str) -> str:
    """
    Uses readability to summarize the HTML response into a summary,
    then lxml to remove unnecessary attributes on all elements
    """
    doc: readability.Document = readability.Document(html_text)
    summary: str = doc.summary()
    # remove class/id attributes
    tree = lxml.html.fromstring(summary)
    ctree = cleaner.clean_html(tree)
    # clean_html replaces the top-level
    # element with html, set it back to HTML if possible
    if ctree.tag == "div":
        ctree.tag = "html"
    html_bytes: bytes = lxml.html.tostring(ctree)
    # should html.unescape be called here? Or should that be handled
    # elsewhere/when parsing into text
    return html_bytes.decode("utf-8")
