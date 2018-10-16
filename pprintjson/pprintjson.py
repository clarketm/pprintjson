"""pprintjson module"""

from sys import stdout, argv
from json import dumps, loads
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from typing import Dict, IO, List, Union


def pprintjson(obj: Union[Dict, List], indent: int = 4, end: str = "\n", file: IO = stdout, flush: bool = False) -> None:
    json = dumps(obj, indent=indent)
    if file.isatty():
        json = highlight(json, JsonLexer(), TerminalFormatter())
    print(json, end=end, file=file, flush=flush)


if __name__ == '__main__':
    pprintjson(loads(argv[1]))
