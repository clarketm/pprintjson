"""pprintjson module"""

from json import dumps, loads
from sys import stdout, argv
from typing import Dict, IO, List, Union

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer


def pprintjson(
    obj: Union[Dict, List],
    indent: int = 4,
    end: str = "\n",
    file: IO = None,
    flush: bool = False,
) -> None:
    file = stdout if file is None else file
    json = dumps(obj, indent=indent)
    if file.isatty():
        json = highlight(json, JsonLexer(), TerminalFormatter())
    print(json, end=end, file=file, flush=flush)


if __name__ == "__main__":
    pprintjson(loads(argv[1]))
