#! C:\Users\Gherardelli\Documents\PortableApps\WinPython\python-2.7.10\python.exe
from UNCFS_auth import *

WORLD_WOE_ID = 1

world_trends = t.trends.place(_id = WORLD_WOE_ID)
print json.dumps(world_trends, indent=2)
