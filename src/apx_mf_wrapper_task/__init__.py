"""
Wrapper for mf CLI application to convert .tif files to .png
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("apx-mf-wrapper-task")
except PackageNotFoundError:
    __version__ = "uninstalled"