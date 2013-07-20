Ubuntu 11.10 Font Sizes
#######################
:date: 2011-10-21 13:24
:author: admin
:category: Linux
:tags: 11.10, linux, ubuntu
:slug: ubuntu-11-10-font-sizes

I love Ubuntu. All of my personal machines run it, and I rarely use
anything else except at work. However, some decisions in the most recent
release, 11.10, remove some basic configurability options that annoy me.

One of these is the ability to change the system font sizes. I don't
want my windows to have giant size 16 titles--it's a waste of space, and
while big fonts are all the rage, I don't want them wasting my valuable
desktop real estate. However, there is no way to change this out of the
box--an annoying oversight in my book.

Luckily it's easy to fix with an additional configuration tool:

``sudo apt-get install gnome-tweak-tool``

After this, it's a simple matter of opening this tool (it will show up
under "Advanced Settings" in your menu) and changing the requisite
options under "Fonts."

I don't think a user should have to download software to do something so
basic, but there it is.
