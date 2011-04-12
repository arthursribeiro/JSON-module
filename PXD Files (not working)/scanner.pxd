cimport cython

@cython.locals(string=object, idx=int, nextchar=char)
cdef _scan_once(object string, int idx)

@cython.locals(string=char*, idx=int)
cpdef scan_once(char *string, int idx)

cpdef py_make_scanner(object context)

cpdef object make_scanner
