import os
import datetime
import glob

# delete - delete all files that match pattern and was created before timepoint.
def delete(pattern, timepoint=datetime.datetime.today()):
    for path in glob.glob(pattern):
        if datetime.datetime.fromtimestamp(os.path.getatime(path)) < timepoint:
            os.remove(path)


# delete('/tmp/*',(datetime.datetime.now()-datetime.timedelta(minutes=10)))
