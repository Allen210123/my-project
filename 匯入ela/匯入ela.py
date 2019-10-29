from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('相同內容.ini',encoding="utf-8")
from elasticsearch import Elasticsearch
import json 
import os


es = Elasticsearch()
path = cfg['path'].get('h_folder')
files = os.listdir(path)
for i in range(0,len(files)):
    file = files[i]
    with open(path+'/'+file,'r', encoding='UTF-8') as fp:
        lines = fp.readlines()
        for j in range(0,len(lines)):
            es.index(index='erica', doc_type='politics', body=lines[j], ignore=400)
            print(lines[j])