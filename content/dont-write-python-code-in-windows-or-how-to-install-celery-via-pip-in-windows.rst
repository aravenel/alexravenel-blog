Don't write Python code in Windows (or, how to install Celery via pip in Windows).
##################################################################################
:date: 2012-07-23 14:52
:author: admin
:category: Linux, Python
:tags: celery, coding, pip, programming, python, windows
:slug: dont-write-python-code-in-windows-or-how-to-install-celery-via-pip-in-windows

Seriously, just don't.

I love Python. I got my start writing it at work to automate simple but
tedious tasks ("rename these 4,000 files according to their author and
timestamp"), but quickly started tinkering with it for all sorts of
other uses. One of the things I love about it most is that it is
(usually) clean, clear, and concise. You know exactly what the code is
doing.

However, writing Python code in Windows is a colossal PITA. Whereas in
Linux (and presumably Mac) the Python binaries and libraries are a
simple package manager call away, in Windows, there is no shortage of
the hoops you have to jump through.

Most recently, I was trying to install the most recent version of Celery
on Windows 7 using pip. This however failed with cryptic
``Unable to find vcvarsall.bat`` errors.

Turns out, this was related to the Python distutils being unable to find
a compiler. To resolve this, do the following:

#. Download and install the MinGW compiler from \ http://www.mingw.org/.
   Make sure to select the c and c++ compilers when installing.
#. Add C:\\MinGW\\bin (or wherever you installed MinGW) to the system
   path.
#. Open (create if it doesn't exist) the
   file PYTHONPATH\\Lib\\distutils\\distutils.cfg (for me, this was
   in C:\\Python27\\Lib\\distutils).
#. Add the below lines to the file:

``[build]``

| compiler=mingw32
| 

This resolved the first error. However, that didn't fix everything--now
I was getting
``gcc: error: unrecognized command line option '-mno-cygwin'`` errors.
Turns out that this is related to a deprecated gcc flag that the version
of distutils included in my version of Python (2.7.2) was using.

To fix this, I went into C:\\Python27\\Lib\\distutils\\distutils.py and
found all places where it was calling gcc with this deprecated flag.
There was a cluster of them around line 322. I then removed the
-mno-cygwin flag from these gcc calls.

After this, everything installed successfully. What a pain.

Oh, and once it's running, you can't run ``celeryd`` as all the
documentation would have it--you need to run
``python -m celery.bin.celeryd`` in Windows. Sigh.

Seriously, don't write Python code on Windows--if you can avoid it. I'm
considering installing VirtualBox on the machines on which I have to run
Windows just to avoid having to deal with these headaches.
