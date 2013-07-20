VIM: minibufexpl Performance Issues
###################################
:date: 2011-10-21 12:53
:author: admin
:category: VIM
:tags: editor, vim
:slug: vim-minibufexpl

I work in consulting, and this means that I frequently am asked to work
on clients' machines. As part of my most recent engagement, I've done a
bit of quick Python scripting to take care of some straightforward
tasks. I initially installed my default VIM setup on this machine, but
have run into some issues with it that I haven't experienced elsewhere.

One of the biggest is an overall slowness when opening, closing, saving,
or even editing files. Sometimes it would take up to ten seconds to
enter insert mode--totally unacceptable, and strange for an editor like
VIM that was originally built to work over paltry network connections
20+ years ago.

As it turns out, like many corporate environments, very little is
actually stored on the local machine. Almost every location that a user
has write access to is a network drive that has been mapped to a drive
letter. Also like many corporate networks and SAN setups, this one was
overtaxed and slow. This, combined with one of the plugins I was using,
the otherwise excellent minibufexpl, turned out to be causing the bulk
of my issues, which I discovered after deactivating all of my plugins
and reactivating them one by one. It seems that minibufexpl was
traversing all of the open buffers every time a user performed an
action. I found some chatter about this, and some proposed patches, but
even after updating to the most recent version, the issue persisted.

In order to solve it, I unfortunately had to move away from minibufexpl
for this machine, and replace it with BufExplorer. BufExplorer is not
ideal for me--I can see how it would be helpful for editing dozens of
files at once, but I rarely have more than ten or so open at a time, so
minibufexpl's visual buffer representation is much better for me.
However, this new setup does fix my issues and after remapping some keys
in my vimrc--primarily binding ``<leader>b`` to ``:BufExplorer``, it's
almost as nice.

Hopefully, minibufexpl will fix this at some point in the future. Until
then, its BufExplorer for me.
