# -*- coding: utf-8 -*-

from pathlib import Path
import sys
import csv
import datetime

BASE_PATH=sys.argv[1]

# Pathオブジェクトを生成
p = Path(BASE_PATH)

# 再帰的な検索
file_list=list(p.glob("**/*"))

with open('file_list.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['full_path', 'file_name', 'suffix' ,'is_file', 'is_symlink', 'mtime']

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()

    for f in file_list:
         #print(f.stat())
         #print(datetime.datetime.fromtimestamp(f.stat().st_mtime).isoformat())
         #print(str(f.is_file())+":"+ str(f.is_symlink())+":"+f.suffix + ":"  + f.name + ":" + str(f))
         mtime=datetime.datetime.fromtimestamp(f.stat().st_mtime).isoformat()
         row = {'full_path':str(f), 'file_name':f.name, 'suffix':f.suffix ,'is_file':f.is_file(), 'is_symlink':f.is_symlink(), 'mtime':mtime}
         writer.writerow(row)
