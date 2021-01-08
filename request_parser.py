import abc
import json

from haralyzer import HarParser


def get_http_parser(filepath):
    return HttpArchiveParser(filepath)


class RequestParser(abc.ABC):
    """An abstract request parser class"""

    def __init__(self, filepath):
        self.filepath = filepath

    @abc.abstractmethod
    def load_requests(self):
        pass


class HttpArchiveParser(RequestParser):
    """An implementation of for Http Archive """

    def __init__(self, filepath):
        super(HttpArchiveParser, self).__init__(filepath)

    def load_requests(self):
        with open(self.filepath, 'r', encoding='utf-8-sig') as f:
            har_parser = HarParser(json.loads(f.read()))

        # Need to collect all entries for all pages and return as a single array.
        return har_parser.pages[0].entries
