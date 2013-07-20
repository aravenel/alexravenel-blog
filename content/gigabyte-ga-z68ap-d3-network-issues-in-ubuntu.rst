Gigabyte GA-Z68AP-D3 Network Issues in Ubuntu
#############################################
:date: 2012-01-02 09:30
:author: admin
:category: Uncategorized
:tags: linux, network, ubuntu
:slug: gigabyte-ga-z68ap-d3-network-issues-in-ubuntu

I recently purchased a Gigabyte GA-Z68AP-D3 motherboard as part of a new
PC build. When I went to install Ubuntu on it, my network connection was
horribly slow--time outs all over the place, slow downloads, and even
slow transfer speeds on the local network. A bit of research showed a
mind boggling amount of dropped packets as well. As it turns out, this
motherboard (and presumably other motherboards of the GA-Z68 series)
have a Realtek 8111E ethernet chipset, which has some known issues in
Ubuntu--namely that Ubuntu loads a slightly wrong driver for it. The
driver works, sort of, but people see lots of issues like mine--dropped
packets, slow speeds, etc.

Thankfully the fix is fairly easy. Realtek has the `proper Linux driver
available`_. Even though it says it is for kernels 2.4.x and 2.6.x, I
can confirm that it does indeed work in the 3.0.x kernels present in
Ubuntu 11.10.

There are some great instructions over at `Foxhop.net`_. Note that the
first step will be making sure that you have your kernel headers and
build-essential packages installed! After installing the proper driver,
everything is working just like it should.

In short, they are:

#. Get the updated driver:
    ``wget http://www.foxhop.net/attachment/r8168-8.023.00.tar.bz2``
#. Remove the offending kernel module:
    ``sudo rmmod r8169``
#. Install the new driver:
    ``cd r8168-8.023.00 sudo ./autorun.sh``

.. _proper Linux driver available: http://www.realtek.com/downloads/downloadsView.aspx?Langid=1&PNid=13&PFid=5&Level=5&Conn=4&DownTypeID=3&GetDown=false
.. _Foxhop.net: http://www.foxhop.net/realtek-dropping-packets-on-linux-ubuntu-and-fedora
