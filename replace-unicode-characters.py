#!/usr/bin/python

import sys, codecs, re

charmap = {
        u"\uF203": u"\u0234",
        u"\uF20C": u"\1D91",
# ...
}

charlist = u"|".join(charmap.keys())

with codecs.open(sys.argv[1], encoding="utf-8") as inf, codecs.open(sys.argv[2], "w", encoding="utf-8") as outf:
        for l in inf.readlines():
                outf.write(re.sub(charlist, lambda x:charmap[x.group(0)], l))
