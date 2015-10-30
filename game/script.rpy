#Init Python Section
#Description:

#Custom Audio Channels
#Ambience Audio Channel
init python:
    renpy.music.register_channel("ambience", "sfx", True)

#Custom Transitions
init python:
# eyewarp Function
#Description: Perform some "blinking" effects
  def eyewarp(x):
    return x**1.33
 
  #eye Pyton Variables:
  eye_open = ImageDissolve("fx/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
  eye_shut = ImageDissolve("fx/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
  
# Circlewipe Transition
#Description: Perform a circular wipe effect
init python:
    circlewipe = ImageDissolve("fx/Id_circlewipe.png", 1.0, 8)
    
#DelayBlinds Transition
#Description:
init python:
    delayblinds = ImageDissolve("fx/tr-delayblinds.png", 1.0, 8)

#Backgrounds
image black = '#000000'
image white = '#FFFFFF'
image class 1 = "Classroom_01_day.jpg"
image front gate = "school_gate_2.jpg"
image school grounds 1 = "school_grounds_1.jpg"

#Background Animations
image walking_crowd:
    "crowds/crowd1.png" with Dissolve(.06, alpha=True) #shows the image with a transition
    0.6 #A pause of 0.6 sec before the next image
    "crowds/crowd2.png" with Dissolve(0.6, alpha = True) #alpha=True to preserve transparency
    0.6
    "crowds/crowd3.png" with Dissolve(0.6, alpha = True)
    0.6
    repeat #creates a loop

#Characters used by the Game
#Kyoko
#Description:
define k = Character('Kyoko', color="#008000")

#Hisashi Unidentified
#Description:
define hu = Character( '???', color="#8B4513")

#Hisashi
#Description:
define h = Character('Hisashi', color="#8B4513")

#Teacher
define teach = Character('Teacher', color="#FFFFFF")

#None: display text
define n = Character(None, kind=nvl)

#Game splashscreen
label splashscreen:

    scene black
    with Pause(1)
    
    show text "ViSwan Studios Presents..." with dissolve
    with Pause(2)
    
    hide text with dissolve
    with Pause(1)
    return

#Game Start   
label start:

#Starting Music
stop music 
play music "jingles/Pre-chapter Jingle.mp3" noloop fadein 2.0 fadeout 2.0

#First Scene of Prologue
scene black with dissolve
show text "Prologue" with Pause(4.2)
with dissolve
scene black with dissolve

#Starting Music of Prologue
play music "music/Beginnings (Prologue).mp3" loop fadein 2.0

#Introduction
n "I always knew I was different"
n "Ever since I was a child, I just knew SOMETHING was different"
n "Unfortunately, I couldn't quite put my finger on it until I was 13"
nvl clear
n "The term \"transgender\" comes to mind for many."
n "Although to me, it's just another thing to add on the pile of things that make up me as a person"
nvl clear
n "Let's see..."
n "I suffer from fairly bad social anxiety."
n "As a result, I could be considered \"shy\" by many."
n "This led to me being kind of a \"shut-in\"." 
nvl clear
n "However..."
nvl clear
n "This also gave me time to figure out what I like to do."
n "I dabbled quite a bit in the arts, and figured out that my \"thing\", so to speak, was music."
n "Before long, My parents took note of this, and figured the best course of action was to send me to a school for \"gifted\" individuals."
n "No, I don't mean mentally or physically disabled."
n "I mean, people who are talented in the arts and related topics."
nvl clear
n "Chiaharu Academy, it's called."
n "Located in a quaint little town in Northern Japan."
n "It would be there that I would spend two years of my life, improving my artistic skills, while at the same time hopefully improving my social skills."
n "This is my story"
nvl clear

#Change musice for next Scene
stop music
play music "jingles/Pre-chapter Jingle.mp3" noloop fadein 2.0 fadeout 2.0

#Scene 2 Act 1\nNew Beginnings
scene black with dissolve 
show text "Act 1\nNew Beginnings" with Pause(4.2)
with dissolve
label act1:
scene front gate with dissolve
#Change Music
play music "music/Excitement.mp3" loop fadein 2.0

#Kyoko get into the crowded school 
k "Well, here goes nothing. First day at Chiaharu Academy."
"I close my eyes, quickly reflecting on my existence."

scene black with eye_shut

n "I'd be lying if I said I wasn't at least a little nervous."
n "I've never exactly had good experiences with schooling, be it due to me being bullied all throughout school, or some other thing, I will never know."
n "Regardless, I've never exactly been the type to easily socialize."
n "I'm just hoping that my time here will change that."

nvl clear
scene white with eye_open
scene front gate

"I let out a fairly long sigh"
k "Let's do this."

scene school grounds 1 with dissolve
show walking_crowd
play ambience "ambience/school_outdoors.mp3"

"There is a surprisingly large amount of students milling about the school grounds."
k "Come on Kyoko, don't panic, don't panic, breathe...."

hide walking_crowd
scene black with eye_shut

#Lower Music Volume during Panic Attack
python:
    renpy.music.set_volume(0, delay=2, channel='music')
    renpy.music.set_volume(0, delay=2, channel='ambience')
    
#Play Heartbeat sfx
play sound "sfx/Heartbeat.mp3" loop 

n "I tend to have panic attacks when in areas with a lot of people."
n "As such, I tend to keep to myself."
n "Breathe in."
n "Breathe out."
nvl clear
"I repeat this a few more times until I feel adequately comfortable."

#Stop Heartbeat sfx
stop sound fadeout 2

#Raise Music Volume after Panic Attack
python:
    renpy.music.set_volume(1, delay=2, channel='music')
    renpy.music.set_volume(1, delay=2, channel='ambience')
scene white with eye_open
scene school grounds 1
show walking_crowd

#Introduce Hisashi 
hu "Hey, uh, are you ok?"
"I quickly realize that someone, a boy, is talking to me."
n "He appears to be about 5 foot 6, with dark glasses and short brown hair."
nvl clear
k "Uh, yeah, sorry. I'm ok. Just kinda zoned out for a second there."
h "Hey, it's ok! Happens to me every so often. My name's Hisashi, what's your name?"
k "Kyoko. Kyoko Ashitaru"
h "Well, nice to meet you, Kyoko! Is this your first day at Chiaharu?"
k "Yeah, I guess you could say that. I transferred here from my other school."
h "Where'd you transfer from?"
k "A public school in Kyoto. Never really liked the hustle and bustle of large cities."
h "I gotcha. I've always been more of a city person myself, but that's just me"

#Start of class, signaled by bells
python:
    renpy.music.set_volume(.5, delay=0, channel='music')
play sound "jingles/Class Start.mp3" fadein 2.0 fadeout 2.0
#Pause and hide text for 8.5 seconds, for duration of bell, or until the player clicks again
$ renpy.pause(8.5) 
python:
    renpy.music.set_volume(1, delay=2, channel='music')
k "?"
#Stop Bell
stop sound fadeout 2

h "Well, there's the bell. Gotta get to class. Catch you later, ok?"
k "Alright. I should probably get to class myself, if I can find it, that is."
#Clock tick sound effect to symbolize time passing
play sound "sfx/Clock Ticking.mp3" fadein 1 fadeout 1.5
scene class 1 with delayblinds 
stop ambience fadeout 2
#Classroom day scene 1

n "I made it to class, albeit barely"
n "Much running and scrambling around was involved, but made it"
n "I'm REALLY hoping I'll get used to this sooner than later"
#Comment By Tanix Just to show some new functionality
#nvl clear

#  To be removed, just Idea how to jump labels Decisions during the Game, We can make also internal paths 
#  in the acts like make same flow PPT for each act to make paths inside it
menu:
    "Are you sure that you want to back?":
         jump backChoice

    "Let's Finish it":
         jump finishIt
         
label backChoice:
    k "DAMM you choose to back to beginning to Act 1"
    jump act1

label finishIt:
    k "OK let's finish it, I don't care Anymore"
    nvl clear
    scene white with eye_open
    with dissolve
    scene black
    #Play Heartbeat sfx
    play sound "sfx/Heartbeat.mp3" loop 
    
    h "K-chan clam Down!!!"
    nvl clear
    n "What is this? I dont fell anything else!!!!!"    
    #Stop Heartbeat sfx
    stop sound fadeout 2
    k "It`s Over"
    show text "GAME OVER" with Pause(4.2)
    nvl clear
