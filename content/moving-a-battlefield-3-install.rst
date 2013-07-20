How to Move a Battlefield 3 Install Directory
#############################################
:date: 2011-11-14 11:11
:author: admin
:category: Uncategorized
:tags: battlefield, bf3, games, gaming, howto
:slug: moving-a-battlefield-3-install

I play the occasional PC game with my out-of-town friends--we all get on
a Vent server and play a few games once a week as a good way to stay in
touch. One of the games is Battlefield 3. I am in the middle of slowly
building a new machine, purchasing parts as they go on sale, and as part
of that, ended up with an SSD. I figured I'd go ahead and throw the SSD
in my old machine and move my games onto it to take advantage of it
until I finished the rest of the new machine.

Unfortunately, Battlefield 3 requires Origin, EA's terrible ripoff of
Steam, which seems to add no value to the experience and as far as I can
tell, does nothing but annoy anyone. One sign of its immaturity is that
it doesn't easily support moving game installation directories like
Steam does. However, I really didn't want to re-download all 10GB of
Battlefield 3, so I did some digging to see what I could do. Buried deep
in the EA forums, I found out how to move an install. It involves a
registry edit, so make sure you are comfortable with regedit, and/or
take a backup before doing this.

#. Copy the install directory to the new location. I used a copy manager
   (TeraCopy) to do this.
#. Run regedit.exe.
#. Navigate to [HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\EA
   Games\\Battlefield 3] in the registry.
#. Change the GDFBinary key to reflect the new location.
#. Change the Install Dir key to reflect the new location.
#. Navigate to [HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Wow6432Node\\Electronic
   Arts\\Battlefield 3] and update the directories in this
   location--needed to ensure the uninstall functionality works.
#. Update your desktop and/or start menu shortcuts to reflect the new
   location.

Way more work than it should be, but there it is. Hopefully EA will get
it together at some point, but I'm less than optimistic.

As another note, Origin uses a browser-based server browser. While this
isn't the worst thing in the world, it does mean you have to restart the
game every time you change servers. As such, the game really benefits
from an SSD--my time from clicking "Join" to being in-game went from 3+
minutes to about 30 seconds.
