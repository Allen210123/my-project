# -*- coding: utf-8 -*-
import os
from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('相同內容.ini',encoding="utf-8")
from elasticsearch import Elasticsearch

import json
dsl = {
    'query': {
       'bool':{ 'must':[{'term': {   'id': ('btm978952')      }} ]
               
              }
    },'size': 3000
}
es = Elasticsearch()
result = es.search(index='erica', doc_type='politics',body=dsl,filter_path=["hits.hits._source.content"])
print(json.dumps(result, indent=2, ensure_ascii=False))
with open(cfg['path'].get('content_file'),"w+",encoding="utf-8") as f:
    f.write(json.dumps(result, indent=2, ensure_ascii=False))
    