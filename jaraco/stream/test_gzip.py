import json
import threading

from six.moves import urllib, map, BaseHTTPServer

import pkg_resources
import pytest
from more_itertools.recipes import flatten, consume

from jaraco.stream import gzip


@pytest.fixture
def gzipped_json():
	"""
	A gzipped json doc created by gzipping this file:
	[
		{"id": 1, "data": "foo"},
		{"id": 2, "data": "bar"}
	]
	"""
	strm = pkg_resources.resource_stream('jaraco.stream', 'somefile.json.gz')
	return strm.read()


@pytest.yield_fixture
def gzip_server(gzipped_json):
	class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
		def do_GET(s):
			s.send_response(200)
			s.send_header("Content-type", "application/octet-stream")
			s.end_headers()
			s.wfile.write(gzipped_json)

	host = ''
	port = 8080
	addr = host, port
	httpd = BaseHTTPServer.HTTPServer(addr, MyHandler)
	url = 'http://localhost:{port}/'.format(**locals())
	try:
		threading.Thread(target=httpd.serve_forever).start()
		yield url
	finally:
		httpd.shutdown()
		httpd.server_close()


@pytest.fixture
def gzip_stream(gzip_server):
	return urllib.request.urlopen(gzip_server)


def test_lines_from_stream(gzip_stream):
	chunks = gzip.read_chunks(gzip_stream)
	streams = gzip.load_streams(chunks)
	lines = flatten(map(gzip.lines_from_stream, streams))
	first_line = next(lines)
	assert first_line == '['
	second_line = next(lines)
	result = json.loads(second_line.rstrip('\n,'))
	assert isinstance(result, dict)
	assert 'id' in result


def test_lines_completes(gzip_stream):
	"""
	When reading lines from a gzip stream, the operation should complete
	when the stream is exhausted.
	"""
	chunks = gzip.read_chunks(gzip_stream)
	streams = gzip.load_streams(chunks)
	lines = flatten(map(gzip.lines_from_stream, streams))
	consume(lines)
