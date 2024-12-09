# Maintain shedule
> My friend highly maintains a schedule and takes regular actions. However, sometimes he forgets to do certain tasks. As a good friend, I want to help him by finding out about his work. Can you please assist me to find his today's work?

> Flag Format: BDSEC{FLAG}

## About the Challenge
As you can see the title is `Maintain shedule`. So we need to find the flag in `Task Scheduling` feature

## How to Solve?
If you the `Task Scheduling` feature, there is 1 task that's suspicious


[Image extracted text: Pmsiam_taskz
Ready
General
Triggers
Actions
Conditions
Settings
History (disabled)
Name:
Pmsian_task2
Location:
{Event Viewer Task:
Author:
bdsec-PCIbdsec
Description:
Tamjust thinking
Security
ptions]


Run the task and you will obtain the flag


[Image extracted text: Task Scheduler {Local)
Name
Status
Task Scheduler Library
Event Viewer Tasks
PMSIAM TA
Disabled
On event
Log: Systen; Source: Service Control M
Microzcft
Pmziam_taskz
Running
WPD
Yeah
Genen
Nant
This is most Important for hacker Because this is the
flag:BDSEC{You_Are_L3g3nd_Fproved}
Loca
Auth
Desc
OK
Triggers]


```
BDSEC{You_Are_L3g3nd_#proved}
```