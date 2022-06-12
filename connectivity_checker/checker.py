# connectivity_checker/checker.py

from http.client import HTTPConnection
from tkinter import E
from urllib.parse import urlparse

def site_is_online(url, timeout=2):
    """
    Return TRUE if the site at url is online.

    Otherwise, raise an exception.
    """
    error = Exception("unknown error")
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=timeout)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            error = e
        finally:
            connection.close()
    raise error
