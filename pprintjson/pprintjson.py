"""pprintjson module"""

from sys import stdout
from json import dumps
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from typing import Dict, IO


def pprintjson(obj: Dict, indent: int = 4, end: str = "\n", file: IO = stdout, flush: bool = False) -> None:
    json = dumps(obj, indent=indent)
    if file.isatty():
        json = highlight(json, JsonLexer(), TerminalFormatter())
    print(json, end=end, file=file, flush=flush)
