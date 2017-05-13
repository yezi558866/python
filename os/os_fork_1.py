#!/usr/bin/env python3
# -*- coding: utf-8 -*_

import os

pid = os.fork()

if pid:
	print('Child process id:',pid)
else:
	print('I am the child')