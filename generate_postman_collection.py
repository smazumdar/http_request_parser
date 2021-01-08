import argparse

from request_parser import get_http_parser
from postman_collection import PostmanCollection

# Parse arguments.
parser = argparse.ArgumentParser()
parser.add_argument('path', help='The path to the file to HTTP archive file')

args = parser.parse_args()
http_requests = get_http_parser(args.path).load_requests()

collection = PostmanCollection()

for http_request in http_requests:
    collection.add_request(http_request)

collection.save()
