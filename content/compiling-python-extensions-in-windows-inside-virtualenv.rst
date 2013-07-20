Compiling Python Extensions in Windows Inside Virtualenv
########################################################
:date: 2012-08-23 11:53
:author: admin
:category: Python
:tags: coding, programming, python, virtualenv, windows
:slug: compiling-python-extensions-in-windows-inside-virtualenv

If you are writing much Python code, there is a good chance you are
using Virtualenv. If you are doing this under Windows, you may have had
any number of problems (see `previous rant`_).

My most recent issue came with trying to install Celery inside a
virtualenv. My installation was failing when compiling the Billiard
dependency with the following error:

    ``C:\MinGW\bin\gcc.exe -shared -s build\temp.win32-2.7\Release\modules\_billiard\multiprocessing.o build\temp.win32-2.7\Re lease\modules\_billiard\semaphore.o build\temp.win32-2.7\Release\modules\_billiard\pipe_connection.o build\temp.win32-2. 7\Release\modules\_billiard\socket_connection.o build\temp.win32-2.7\Release\modules\_billiard\win32_functions.o build\t emp.win32-2.7\Release\modules\_billiard\_billiard.def -LC:\Users\aravenel\code\WeeklyMenus\venv\libs -LC:\Users\aravenel \code\WeeklyMenus\venv\PCbuild -lws2_32 -lpython27 -lmsvcr90 -o build\lib.win32-2.7\_billiard.pyd``

    c:/mingw/bin/../lib/gcc/mingw32/4.6.2/../../../../mingw32/bin/ld.exe:
    cannot find -lpython27

    collect2: ld returned 1 exit status

    error: command 'gcc' failed with exit status 1

This as it turns out is an issue with the Virtualenv not correctly
knowing the location of the Python libraries upon which it depends
(notably libpython27.a). To fix this, simply edit the activate.bat
script in your venv/Scripts folder to add the following line:

    ``set LIBRARY_PATH=c:\python27\libs``

Voila. No more compiler errors.

Answer found (as usual!) on `StackOverflow`_

.. _previous rant: http://www.alexravenel.com/?p=82
.. _StackOverflow: http://stackoverflow.com/questions/1015605/how-do-i-compile-python-c-extensions-using-mingw-inside-a-virtualenv
