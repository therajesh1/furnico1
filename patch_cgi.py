# patch_cgi.py
import sys
import types

# Mock the cgi module for Python 3.13 compatibility
cgi = types.ModuleType('cgi')
cgi.escape = lambda s, quote=None: s  # Replace escape with a simple passthrough
sys.modules['cgi'] = cgi
