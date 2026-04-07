---
id: BrainCAP
type: knowledge
owner: OA_Triage
---
# BrainCAP
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
BrainCAP_BrainSYNC
==================

This repo contains the code and documentation for a personalized neurofeedback system. There is an arduino sketch that needs to be run on the headgear that is pulling EEG samples from a Mindflex. The processing sketch is an Android application that receives the data via Bluetooth and stores it to the internal SD card on any android device.

It is based off of the hack originally done by the frontiernerds of ITP (http://frontiernerds.com/brain-hack). I encourage you to follow their tutorial before you begin trying to get this one working. The Arduino-side part ot he BrainSYNC system (BrainSYNC_Arduino.ino) uses the frontiernerds Arduino library, Brain.h. The arduino, which isn't absolutely necessary but good for data encrypting, acts as a midpoint between the mindflex and a bluetooth module that I got off of sparkfun.

The processing-based Android application (BrainSYNC_Android.pde) takes a lot of code directly from the tutorial documented here (http://webdelcire.com/wordpress/archives/1045#comment-21099). In order to get processing working for android I recommend following the steps that are thoroughly documented here: http://wiki.processing.org/w/Android

Feel free to contact me (conor dot russomanno at gmail dot com) if you have questions about setting up this system. But hopefully you can piece most of it together from the links above.

For more information on this hack, follow the tutorial I am in the process of making: http://braininterfacelab.wordpress.com/2012/06/01/braincap-brainsync-mindflex-android/

```

