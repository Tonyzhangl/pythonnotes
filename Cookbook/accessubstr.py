#coding=utf-8
import struct

def fields(baseformat, theline, lastfield=False, _cache={ }):
    key = baseformat, theline, lastfield
    format = _cache.get(key)
    if format is None:
        numremain = len(theline) - struct.calcsize(baseformat)
        _cache[key] = format = "%s %d%s" % (
            baseformat, numremain, lastfield and "s" or "x"
        )
    return struct.unpack(format, theline)
