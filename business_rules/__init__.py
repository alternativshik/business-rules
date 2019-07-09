__version__ = '1.0.2'

from .engine import run_all

# Appease pyflakes by "using" these exports
assert run_all
