"""Print publish=true when this version isn't on PyPI yet."""
import json
import re
import urllib.error
import urllib.request

text = open("pyproject.toml").read()
name = re.search(r'^name = "([^"]+)"', text, re.M).group(1)
version = re.search(r'^version = "([^"]+)"', text, re.M).group(1)
try:
    urllib.request.urlopen("https://pypi.org/pypi/%s/%s/json" % (name, version), timeout=30)
    print("publish=false")
except urllib.error.HTTPError as e:
    if e.code != 404:
        raise
    print("publish=true")
