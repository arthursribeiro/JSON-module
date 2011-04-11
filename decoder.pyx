"""Implementation of JSONDecoder
"""
import binascii
import re
import sys
import struct

from scanner cimport make_scanner

try:
    from _json import scanstring as c_scanstring
except ImportError:
    c_scanstring = None

__all__ = ['JSONDecoder']

FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

cdef object _floatconstants():
    cdef bytes _BYTES = binascii.unhexlify(b'7FF80000000000007FF0000000000000')
    cdef double nan, inf
    if sys.byteorder != 'big':
        _BYTES = _BYTES[:8][::-1] + _BYTES[8:][::-1]
    nan, inf = struct.unpack('dd', _BYTES)
    return nan, inf, -inf

def linecol(char *doc, int pos):
    cdef bytes newline
    cdef int lineco, colno
    if isinstance(doc, bytes):
        newline = b'\n'
    else:
        newline = '\n'
    lineno = doc.count(newline, 0, pos) + 1
    if lineno == 1:
        colno = pos
    else:
        colno = pos - doc.rindex(newline, 0, pos)
    return lineno, colno

def errmsg(char *msg, char *doc, int pos, int end=None):
    # Note that this function is called from _json
    cdef int lineco, colno, endlineno, endcolno
    cdef char *fmt
    lineno, colno = linecol(doc, pos)
    if end is None:
        fmt = '{0}: line {1} column {2} (char {3})'
        return fmt.format(msg, lineno, colno, pos)
        #fmt = '%s: line %d column %d (char %d)'
        #return fmt % (msg, lineno, colno, pos)
    endlineno, endcolno = linecol(doc, end)
    fmt = '{0}: line {1} column {2} - line {3} column {4} (char {5} - {6})'
    return fmt.format(msg, lineno, colno, endlineno, endcolno, pos, end)
    #fmt = '%s: line %d column %d - line %d column %d (char %d - %d)'
    #return fmt % (msg, lineno, colno, endlineno, endcolno, pos, end)

_CONSTANTS = {
    '-Infinity': NegInf,
    'Infinity': PosInf,
    'NaN': NaN,
}


STRINGCHUNK = re.compile(r'(.*?)(["\\\x00-\x1f])', FLAGS)
BACKSLASH = {
    '"': '"', '\\': '\\', '/': '/',
    'b': '\b', 'f': '\f', 'n': '\n', 'r': '\r', 't': '\t',
}


