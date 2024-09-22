# hackuncensoreUtube
A little hack to by pass the censure of Utube.

# How does it work

Please install a good environement for python ( virtualenv ... ) 

python videosplit2.py [yourvideo]

.This split the video in two part, and mute on each video one second , with an offset of one second for the second one. 

. This will produce two video, left_video, and right_video

![sounds muted](2024-09-22_17-45.png)

. After in other html page , display the two video together , like behind

![two video](2024-09-22_17-41.png)

So change in the merge2video.html the correct ID. 

To play video click on the button play video. 

Then the sound will be synchronise ( you should have a good connection ).

The Voice to text of utube will to lost.

# Result 

![In dashboard](2024-09-22_18-06.png)

# Todo 
* upload automitcly the two video on your utube account
* add in comment the id of the other video
* make a server which can displau correctly the video. *

# Ethics

¨Please respect a minimal of ethic using this, and please don't make a commercial service for that or contact me. Thank's

contact me if you want to help me twitter/x zebulon75018 


# Dependencies

* argparse
* moviepy
