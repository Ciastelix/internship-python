from elasticsearch import Elasticsearch, ConnectionError
from json import load
from contextlib import contextmanager

class Elastic:
    
    def __init__(self, es_url: str, index_name: str, mapping_url: str) -> None:
        self.es_url = es_url
        self.index_name = index_name
        self.mapping_url = mapping_url
        self._es= Elasticsearch(self.es_url,request_timeout=60)
        if not self._es.indices.exists(index=self.index_name):
            self._es.indices.create(index=self.index_name, body=load(open(self.mapping_url)))
        

    @contextmanager
    def es_inst(self):
        _es: Elasticsearch = self._es
        try:
            yield _es
        except Exception:
            raise ConnectionError