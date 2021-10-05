import time
import datetime
import os
import sys

print(f"Your timezone: {time.timezone / 3600}")
print(f"Currently day: {datetime.date.today()}")
print(f"Dir path: {sys.path[0]}")
os.mkdir('test')
print("Empty dir test created")