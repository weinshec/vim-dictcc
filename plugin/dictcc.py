#!/usr/bin/env python
# encoding: utf-8

import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


class DictQuery(object):

    QUERY_URL = "https://www.dict.cc"
    QUERY_HEADER = {"user-agent": "Mozilla/5.0 (Linux) Gecko"}

    def __init__(self, target):
        self._target = target
        self._request = urllib.request.Request(
            self.QUERY_URL,
            urllib.parse.urlencode({"s": target}).encode("utf-8"),
            self.QUERY_HEADER,
        )

    @property
    def target(self):
        return self._target

    @property
    def translations(self):
        return self._parse_html()

    @property
    def response(self):
        if not hasattr(self, "_response"):
            try:
                response = urllib.request.urlopen(self._request)
                self._response = response.read().decode("utf-8")
            except urllib.error.URLError as e:
                print("Error during dict request: {}".format(e.reason))
                return None
        return self._response

    def as_lines(self):
        lines = ["Translations of \"{}\"".format(self.target)]
        for i, (left, right) in enumerate(self.translations):
            line = "{:>2}: {:<35} {}".format(i, left[:35], right[:35])
            lines.append(line)
        return lines

    def _parse_html(self):
        translations = list()

        if self.response is None:
            return translations

        soup = BeautifulSoup(self.response, "html.parser")

        def parse_table_col(td):
            w = str()
            for a in td.find_all("a"):
                w += " {}".format(a.text)
            return w.strip()

        # table rows containing translations are numbered tr[0-9]+
        for tr in soup.find_all("tr", {"id": re.compile("tr*")}):
            td_left, td_right = tr.find_all("td")[1:3]
            translations.append(
                (parse_table_col(td_left), parse_table_col(td_right)))

        return translations
