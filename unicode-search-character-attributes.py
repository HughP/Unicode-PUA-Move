# coding: utf-8

import icu
category = icu.UCharCategory
chartype = icu.Char.charType

# Find all the characters used in Latin script. That includes common and inherited characters

getscrn = lambda x: icu.Script.getShortName(icu.Script.getScript(x))
allchar = (unichr(x) for x in xrange(65536))
lchar = [x for x in allchar if getscrn(x) in ('Latn', 'Zyyy', 'Zinh')]
len(lchar)

# Find all the Sk characters

lskchar = [x for x in lchar if chartype(x) == category.MODIFIER_SYMBOL]
len(lskchar)

# Find all the Lo characters

llochar = [x for x in lchar if chartype(x) == category.OTHER_LETTER]
len(llochar)

# Find all the Lm characters

llmchar = [x for x in lchar if chartype(x) == category.MODIFIER_LETTER]
len(llmchar)
