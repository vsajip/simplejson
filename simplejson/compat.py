import sys

if sys.version_info[0] < 3:
    PY3 = False

    def b(s):
        return s
    def u(s):
        return unicode(s, "unicode_escape")
    import cStringIO as StringIO
    StringIO = BytesIO = StringIO.StringIO
    text_type = unicode
    binary_type = str
    string_types = basestring,
    integer_types = (int, long)
    unichr = unichr
    
    def fromhex(s):
        return s.decode('hex')

else:
    PY3 = True

    def b(s):
        return s.encode("latin-1")
    def u(s):
        return s
    import io
    StringIO = io.StringIO
    BytesIO = io.BytesIO
    text_type = str
    binary_type = bytes
    string_types = str,
    integer_types = int,
    
    def unichr(s):
        return u(chr(s))

    def fromhex(s):
        return bytes.fromhex(s)

long_type = integer_types[-1]

