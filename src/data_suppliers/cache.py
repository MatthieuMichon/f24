#!/usr/bin/python3

"""
f24.data_suppliers.cache
~~~~~~~~~~~~~~~~~~~~~~~~

This module contains the class implementing a simple cache.
"""

import hashlib
import os
import time
import json
from pathlib import Path


class Cache:
    CACHE_DIR = 'cache_db'
    CACHE_FILENAME_LEN = 40

    def __init__(self):
        p = Path('.')
        self.path = p / self.CACHE_DIR
        self.file_list = self.get_file_list(self.path)

    def lookup(self, uri, ttl=None):
        """Perform a lookup for the given URI
        :param string uri: Target URI
        :param int ttl: Time-to-live in seconds
        """
        sha1 = self.get_hash_str(uri)
        # TDB: add TTL check
        file_present = any(x == sha1 for x in self.file_list)
        print("Result: {}; URI: {}; sha1: {}".format(file_present, uri, sha1))
        if file_present is True:
            with open(str(self.path / sha1)) as cache_file:
                ts_data = json.load(cache_file)
                return ts_data['data']
        else:
            return None

    def store(self, uri, data):
        """Perform a lookup for the given URI
        :param string uri: Target URI
        :param dict data: Time-to-live in seconds
        """
        ts = int(time.time())
        ts_data = {}
        ts_data["ts"] = ts
        ts_data["data"] = data
        sha1 = self.get_hash_str(uri)
        with open(str(self.path / sha1), mode='w') as cache_file:
            json.dump(ts_data, cache_file)

    def get_file_list(self, path):
        if not path.exists():
            print('Creating missing directory cache: {}'.format(path))
            os.mkdir(str(path))
        return [str(x.name) for x in path.iterdir() if not x.is_dir()]

    def get_hash_str(self, data):
        s = hashlib.sha1()
        s.update(str.encode(data))
        return s.hexdigest()


def main():
    c = Cache()
    c.lookup(uri='example.com/path/filename?arg=lil')
    c.lookup(uri='example.com/path/filename?arg=lol')
    c.lookup(uri='example.com/path/filename?arg=luzl", ttl=3')
    my_dict = {}
    my_dict['key1'] = 'arg1'
    my_dict['key2'] = 'arg2'
    c.store('example.com/path/filename?arg=lol', my_dict)


if __name__ == "__main__":
    main()
