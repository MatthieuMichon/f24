#!/usr/bin/python3

"""
extract.cache
~~~~~~~~~~~~~

This module implements a simple read cache.
"""

import hashlib
import os
import time
import json
import requests
from pathlib import Path


class Cache:

    CACHE_DIR = 'cache_db'
    CACHE_FILENAME_LEN = 40
    DEFAULT_TTL = 3600

    def __init__(self, verbose=False):
        p = Path('.')
        self.path = p / self.CACHE_DIR
        self.verbose = verbose

    def lookup(self, uri, ttl=None):
        """Perform a lookup for the given URI
        :param string uri: Target URI
        :param int ttl: Optional Time-to-live in seconds
        """
        sha1 = self.get_hash_str(uri)
        ttl = (ttl or self.DEFAULT_TTL)
        self.file_list = self.get_file_list(self.path)
        if any(x == sha1 for x in self.file_list) is False:
            # No file matches the given URI
            self.print_verbose('Cache miss: no file with sha1 {}'.format(sha1))
            return self.store(uri=uri)
        else:
            file_ = open(str(self.path / sha1))
            jfile = json.load(file_)
            file_ts = int(jfile['ts'])
            current_ts = int(time.time())
            if (current_ts < file_ts):
                self.print_verbose(
                    'Inconsistent timestamps: {} < {}'.format(
                        current_ts, file_ts))
                raise ValueError(
                    'File timestamp is newer than current timestamp',
                    file_ts, current_ts)
            if (current_ts - file_ts > int(ttl)):
                self.print_verbose('Cache file is too old: {}'.format(
                        current_ts - file_ts))
                # Cache file is present but outdated
                return self.store(uri=uri)
            else:
                # Cache file is present and is recent enough
                self.print_verbose('Cache hit: file with sha1 {}'.format(sha1))
                return json.loads(jfile['data'])

    def store(self, uri):
        """Retrieves the given URI in a cache file and returns its contents
        :param string uri: Target URI
        """
        ts = int(time.time())
        ts_data = {}
        ts_data['ts'] = ts
        ts_data['data'] = json.dumps(requests.get(uri).text)
        sha1 = self.get_hash_str(uri)
        with open(str(self.path / sha1), mode='w') as cache_file:
            self.print_verbose(
                'Storing contents of URI {} in cache file {}'.format(
                    uri, sha1))
            json.dump(ts_data, cache_file)
            return json.loads(ts_data['data'])

    def get_file_list(self, path):
        if not path.exists():
            self.print_verbose(
                'Creating missing directory cache: {}'.format(path))
            os.mkdir(str(path))
        return [str(x.name) for x in path.iterdir() if not x.is_dir()]

    def get_hash_str(self, data):
        s = hashlib.sha1()
        s.update(str.encode(data))
        return s.hexdigest()

    def print_verbose(self, text):
        """Print text if verbose mode is set"""
        if self.verbose:
            print(text)


def main():
    c = Cache()
    print(c.lookup(uri='example.com/path/filename?arg=lil'))
    print(c.lookup(uri='example.com/path/filename?arg=lol'))
    print(c.lookup(uri='example.com/path/filename?arg=luzl", ttl=3'))
    my_dict = {}
    my_dict['key1'] = 'arg1'
    my_dict['key2'] = 'arg2'
    c.store('example.com/path/filename?arg=lol', my_dict)


if __name__ == "__main__":
    main()
