"""
A pretty-printing function for json.
"""

from json import dumps, loads, load
from sys import stdin, stdout
from typing import Dict, IO, List, Union

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import JsonLexer

from pprintjson import __version__


def pprintjson(
    *obj: Union[Dict, List],
    indent: int = 4,
    end: str = "\n",
    file: IO = None,
    flush: bool = False,
) -> None:
    file = stdout if file is None else file
    json = [dumps(o, indent=indent) for o in obj]
    try:
        if file.isatty():
            json = [highlight(j, JsonLexer(), TerminalFormatter()) for j in json]
    except AttributeError:
        pass
    print(*json, end=end, file=file, flush=flush)


def cli():
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=35, width=100
        ),
    )
    parser.add_argument(
        "-i",
        "--indent",
        type=int,
        default=4,
        metavar="num",
        help="indent <num> number of spaces at each level (default: %(default)s)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        metavar="file",
        help="write  output to <file> instead of stdout (default: stdout)",
    )
    parser.add_argument(
        "-c", "--command", type=str, metavar="cmd", help="json <str> to pretty-print"
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "file",
        nargs="?",
        type=argparse.FileType("r"),
        help="json <file> to pretty-print",
        default=stdin,
    )
    args = parser.parse_args()
    file = open(args.output, "w") if args.output else None

    if args.command is not None:
        pprintjson(loads(args.command), indent=args.indent, file=file)
    else:
        pprintjson(load(args.file), indent=args.indent, file=file)


if __name__ == "__main__":
    cli()
