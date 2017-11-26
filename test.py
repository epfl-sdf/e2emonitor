#!/usr/bin/env python
#-*-coding:Utf-8 -*

import credFinder

(user, password)=credFinder.returnCred()

print("{0}\n{1}".format(user, password))
