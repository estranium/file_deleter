# file_deleter ![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
This python package provide possibility to delete that was created before defined time.

##### Install
```
pip3 install file_deleter
```

##### Use
```
import datetime
import file_deleter

file_deleter.delete(pattern='/tmp/*.txt', timepoint=datetime.datetime.now())
```
