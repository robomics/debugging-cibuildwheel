from ._mymodule import __doc__, call_me

try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version

__version__ = version("mymodule")
__all__ = ["__doc__", "__version__", "add", "subtract"]
