cdef _floatconstants()

cpdef linecol(char *doc, int pos)

cpdef errmsg(char *msg, char *doc, int pos, end)

cpdef py_scanstring(s, int end, bint strict, dict _b, _m)

cpdef JSONObject(s_and_end, bint strict, scan_once, object_hook, object_pairs_hook, dict memo, _w, _ws)

cpdef JSONArray(s_and_end, scan_once, _w, _ws)

cdef class JSONDecoder(object):
    cdef public bint strict
    cdef public object object_hook
    cdef public object parse_float
    cdef public object parse_int
    cdef public object parse_constant
    cdef public object object_pairs_hook
    cdef public object parse_object
    cdef public object parse_array
    cdef public object parse_string
    cdef public dict memo
    cdef public object scan_once

    cpdef decode(self, char *s, _w)

    cpdef raw_decode(self, char *s, int idx)
