# SecureConnect
This is a hackathon project to detect NSFW content in a video stream.

# Inspiration
With countries in lockdown and people in quarantine, Zoom has been one of the popular software at this time that has gained huge user base to have video conferences for work as well as for personal conversations. With many schools and businesses using Zoom as a meeting platform, there has been lot of “Zoombombing”.  This term used when uninvited participants join the meeting and harass by projecting derogatory and pornographic content. Zoombombing has become a serious issue especially with many incidents being reported where pornographic content was projected in school classroom sessions. This has led us to develop a bot which can detect nudity in Zoom meetings and remove the participant. 

The Zoombombing incidents are mainly due to the security flaws in the video conferencing tool. In other more secure platforms like webex or skype, there can be other incidents in which a meeting participant may not be aware of their actions. Our bot is designed to detect any unintended appearance like topless video stream of the participants and remove them thereby avoiding any embarrassments[1][2].

# Function
The bot is invited to the meeting just like a participant by sending an invite. The bot then joins the meeting and continuously monitors the video feed of the meeting to detect any nude content. If it finds something it will remove the participant if it has the host permission, else it will notify the host. The bot is created from machine learning algorithm and neural networks that has been trained to detect nudity. 

# Flow

<em>
The image below shows an example of classroom session in progress via zoom. This example considers a teacher and a couple of students.
 </em>
<p>
<img src=SHIELD_Demo/Pic1.png width=400 >
</p>

<em>
The second image shows a “Spammer” who is an uninvited guest joining the call and presenting his screen with inappropriate content.
</em>
<p>
<img src=SHIELD_Demo/pic2.png width=400 >
</p>

<em>
SHIELD bot which has the host permission immediately removes the participant named “Spammer” who shared inappropriate content. After SHIELD performed the action it notifies everybody about it via the chat box.
</em>
<p>
<img src=SHIELD_Demo/pic3.png width=400 >
</p>

# Future work

Our program is working modularly to detect both intentional or unintentional nudity. However, we have not yet integrated this algorithm on a standalone server to function as a fully operating bot given the time constraint. 
We will continue to build this into a standalone bot which is platform agnostic. 

# Installation
```
poetry install
```
Do note this does not install `opencv`, that has to be installed separately.

# Usage:
```
Usage:poetry run sfw [--tolerance=<tolerance>] [--debug]

>>>>>>> fix: merge conflicts
Options:
--tolerance=<tolerance>   Number of video frames to tolerate before issuing a warning.[default=4]
--debug                   Prints the inference logs.
```
This will throw an exception `UnsafeEnvironment` if more than `tolerance` number of frames contain NSFW content.


# Reference

1. https://nypost.com/2020/04/16/brazilian-judge-caught-shirtless-during-court-session-on-zoom/
2. https://www.ebaumsworld.com/videos/woman-drops-a-hot-deuce-forgetting-she-is-on-a-video-conference-on-quarentine/86228857/
3. https://www.reddit.com/r/MachineLearning/comments/b78j1q/p_nudity_detection_and_censoring_in_images_with/
4. https://devpost.com/software/zoogle-assistant

