import json


SKIP_LIST = ['CONNECT']

REQUEST_HEADERS_TO_ADD = ['Authorization', 'Content-Type']

DEFAULT_COLLECTION_INFO = {"name": "Load Test",
                           "schema": ("https://schema.getpostman.com/json/"
                                      "collection/v2.1.0/collection.json")}


class PostmanCollection():
    """A class representing a postman collection"""

    def __init__(self):
        self.collection = {}
        self.collection["info"] = DEFAULT_COLLECTION_INFO
        self.collection["items"] = []

    def add_request(self, http_request):

        # Skip the request if this is a method, we aren't interested in.
        if any([http_request.request.method.upper() == method for method in SKIP_LIST]):
            return

        # Add request and request headers appropriately.
        item = {}
        item['name'] = http_request.url
        item['request'] = {"method": http_request.request.method,
                           "header":  [{'key': header['name'], 'value': header['value'], 'type': 'text'}
                                       for header in http_request.request.headers if header['name'] in
                                       REQUEST_HEADERS_TO_ADD],
                           "url": {"raw": http_request.url,
                                   "host": [http_request.request.host],
                                   "path": http_request.request.url.split('/')[3:],
                                   "query": [{"key": param['name'], "value": param['value']} for param in
                                             http_request.request.queryString]}}

        # if this is a put or post request, add the body.
        if http_request.request.bodySize > 0:
            item["request"]["url"]["body"] = {"mode": "raw",
                                              "raw": http_request.request["postData"]["text"]}

        self.collection['items'].append(item)

    def save(self):
        print(json.dumps(self.collection, indent=4))
