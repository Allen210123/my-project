from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('相同內容.ini',encoding="utf-8")

cou=1
i=0
with open(cfg['path'].get('content_file'),'r',encoding='UTF-8') as f:
 temp=""
 temp=f.read()
 print(temp)
 while temp.find("content",i)!=-1:
     head=temp.find("content",i)
     tail=temp.find("發信站",head)
     i=tail
     with open(cfg['path'].get('content_file'),"a",encoding="utf-8") as fa:
         fa.write(temp[head:tail])
     cou=cou+1
     print(temp[head:tail])