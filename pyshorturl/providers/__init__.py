'''pyShortUrl: URL Shortening lib written in Python.

Copyright (c) 2012 Parth Bhatt

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from .base import BaseShortener, ShortenerServiceError

from .bit_ly import Bitly, BitlyError
from .bit_ly_v2 import Bitly as BitlyV2, BitlyError as BitlyV2Error
from .gim_ie import Gimie, GimieError
from .git_io import Gitio, GitioError
from .goo_gl import Googl, GooglError
from .is_gd import Isgd
from .v_gd import Vgd, VgdError
from .tinyurl_com import TinyUrlcom, TinyUrlcomError
