import os
import sublime
import sys

_ROOT = None
_DEVELOPMENT = False

def setup_all():
    global _DEVELOPMENT
    _setup_path()
    if os.path.exists(os.path.join(_ROOT, 'DEVELOPMENT')):
        os.environ['SUBLIME_DEV'] = '1'
        _DEVELOPMENT = True

def is_development():
    return _DEVELOPMENT

def is_same_package(filename):
    return filename.startswith(_ROOT)

def _setup_path():
    global _ROOT
    _ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(os.path.join(_ROOT, 'vendor'))
