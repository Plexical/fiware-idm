import os

import fabric
from fabric.api import *
from fabric.colors import *

from plexical.shortcuts import t

# NB: `.setting` module variable injected by fabfile.py
setting = lambda name: settings.section('dev')[name]

role = 'dev'
