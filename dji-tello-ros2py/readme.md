# General Info
- DJITelloPy API Reference: https://djitellopy.readthedocs.io/en/latest/tello/
- Tello Specs: https://www.ryzerobotics.com/tello/specs

```
                               ____      _ ___   _____    _ _                             
                              |  _ \    | |_ _| |_   _|__| | | ___   
                              | | | |_  | || |    | |/ _ \ | |/ _ \ 
                              | |_| | |_| || |    | |  __/ | | (_) |
                              |____/ \___/|___|   |_|\___|_|_|\___/ 
                                                                                             
                 _ __________ ____ __,▄▄⌐______________.▄▄,___________________
              _ ________    ______.▄▓▓▌╨ _______________╙▀▓▌▄_______  _ __________
               ______ _ _______╓▄▓▓▓▌╨____________________╙▀▓▓▌▄µ_________________
             ___  _  _______,▄▓▓▓▓▌╨________________________╙▓▓▓▓▓▄⌂_______     ___
             ___ __________╟▓▓▓▓▓▀____________________________╙▓▓▓▓▓▄___________ __
              __________▄Φ╜▓▓▓▌▀─.......'.......''.'''.........,Å▀▓▓▓▀Φ▄._________
             ________.''▓▄▓▓▀▌Φ▄¿:::::::::::;¡≥æææ;::::::::::::|▄▄╣▀▓▓▄▓''_________
             __ _____,▄▓▓▓▓Φ▌░»»╜▀Φ▄p»»»»»"'''''''''─"»»»»»╓▄Φ▀É»»░▓▄▓▓▓▓▄_________
             ______.▄▓▓▓▓▓Ñ»╜▀▄⌂»»»»╙▀Φ▄░»`.`_...___``:»▒Φ▀Ü»»»»;▄▌É»╜▓▓▓▓▓▄_______
             _____▄▓▓▓▓▓▀»::»»╙▀▒p»»nn░█H─'```````````:░█░»»»»╓╣▀░:::─└▀▓▓▓▓▓▄_____
             ___▄▓▓▓▀▀``'''─::»»┴▀▌▄un░█H─````````````:»█M░░╖╣▀░:::──''```╙▀▓▓▓▄___
             _▄▓▓▀╙_____`'''':»»»»»▀▓▄░█░~````````````:»█M▄▓▀|»;:───''``_____╙▀▓▓▄_
             `▀▀_________`''''─:»»»»»║▓▓░~`'``````````:»▓▌▀»»»»::──'````_______ ╙▀`
             _____________``'''::»»»»»n╢▌"````````'```:╣▌»»»»»:─:'`'``_____________
             ______________``'':─»»»»»n║▓"````````````:▓▒»»»»»:───''``_____________
             ______________``''─::»»»»»║▓»````````````;▓▒»»»»;:──'```______________
             ______________```''::»»»»»▐▓"```````'````;▓H»»»»»::──'```_____________
             ___________`__```'::»»»»»╠╣▓;````````````;▓▌▄»»»»:──'`''`_____________
             ⁿ▓▌▄_________`.'.:::»»»▄▓▀╢▀»``'µ;»∩:»'`';╢▒▀▓▄»»»::─'''._________▄▓▓H
             _ ▀▓▓▌▄_____`.''::::»▄▓▀░░▐Ñ»`.'└─└└`┘:.'»▐M░n║▓▄»::::'''`____,╓▄▓▓▀ _
             ___ ▀▓▓▓▓▄p..'─:::¡▄▀Ö»»n░░▒»::▄▄▄▄▄▄▄▄::»║M░░»»╜▀▄¿:::─`'`╓▄▓▓▓▓▀____
             _____`▀▓▓▓▓▓▄::─╓▄▀░»»»»░╔▄▌φφ╢▓▓▓▓▓▓▓▓▌φφ╣▄U░»»»»╙▀▄µ:::▄▓▓▓▓▓▀`___ _
             _______└▀▓▓▓▓▌╓▒▀┴»»»╓▄Φ▀Ö╙»»n░░░░░░░░░░»n»░Å▀Φ▄p»»»»▀▒@╢▓▓▓▓▀└_______
             ________.`▀▓▓▓▄╝▄5▄Φ▀╨»»»»»»»»»»»»»»»»»»»»»»»»»»╜▀Φ▄φ╗╝▄▓▓▓▀┘`________
             ___  __``''▓▄▀█▓▓▄»»»»»»»»»»»:──::::::»»:»»»»»»»»»»»╠▓▓█▀╠▓'``___ ____
             ____ __````'╙▀▓▓▓▓▓▄───'''────'''''''''''─'''────:╥▓▓▓▓▓▀╜```___ _____
             ______   _ _`'"▓▓▓▓▓▓φ''```````````'``````'``''`╓▓▓▓▓▓▓H```____ ______
             _______ ________└▀▓▓▓▓▌p______________________╓▓▓▓▓▓▀⌡`__ _ __________
             _  _________  _____ ╙▀▓▓▌µ________         `╓▄▓▓▀▀`____  _________ ___
             __________________ _   ╙▀▓▌⌐  ______      .▓▓▌╨_   ______________  ___
   
      ~ A python wrapper to interact with the Ryze Tello drone using the official Tello API ~
                  [Developed by João R. Cioffi at Centro Espacial ITA - 2023]
```

# Introduction
The Tello SDK connects to the aircraft through a Wi-Fi UDP port, allowing users to control the aircraft with text commands. After downloading and installing Python, download the Tello3.py file via the link: https://dl-cdn.ryzerobotics.com/downloads/tello/20180222/Tello3.py.

Tello3.py is a sample program based on python that establish a UPD communication port, which can implement simple interaction with Tello, including sending SDK instructions to Tello and receiving Tello information. Tello3.py is for reference only and user can develop more.

# Architecture
Use Wi-Fi to establish a connection between the Tello and PC, Mac, or mobile device.

## Send Command & Receive Response
Tello IP: 192.168.10.1 UDP PORT: 8889 <<- ->> PC/Mac/Mobile

- Step 1: Set up a UDP client on the PC, Mac, or mobile device to send and receive messages from the Tello via the same port.

- Step 2: Before sending any other commands, send “command” to the Tello via UDP PORT 8889 to initiate SDK mode.

## Receive Tello State
Tello IP: 192.168.10.1 ->> PC/Mac/Mobile UDP Server: 0.0.0.0 UDP PORT: 8890

- Step 3: Set up a UDP server on the PC, Mac, or mobile device and check the message from IP 0.0.0.0 via UDP PORT 8890. Steps 1 and 2 must be completed before attempting step 3. For more
details, refer to the Tello State section.

## Receive Tello Video Stream
Tello IP: 192.168.10.1 ->> PC/Mac/Mobile UDP Server: 0.0.0.0 UDP PORT: 11111

- Step 4: Set up a UDP server on the PC, Mac, or mobile device and check the message from IP 0.0.0.0 via UDP PORT 11111.

- Step 5: Send “streamon” to the Tello via UDP PORT 8889 to start streaming. Steps 1 and 2 must be completed before attempting step 5.

# Tello Command Types and Results:
The Tello SDK includes three basic command types.

## Control Commands (xxx)
- Returns “ok” if the command was successful.
- Returns “error” or an informational result code if the command failed.

## Set Command (xxx a) to set new sub-parameter values
- Returns “ok” if the command was successful.
- Returns “error” or an informational result code if the command failed.

## Read Commands (xxx?)
- Returns the current value of the sub-parameters.

# Tello Commands

## Control Commands

| Command  | Description | Possible Response |
| ------------- | ------------- | ------------- |
| Command | Enter SDK Mode | ok/error |
| takeoff | Auto takeoff | ok/error |
| land | Auto landing | ok/error |
| streamon | Enable video stream | ok/error |
| streamoff | Disable video stream | ok/error |
| emergency | Stops motors immediately | ok/error |
| up x | Ascend to "x" cm (x=20–500) | ok/error |
| down x | Descend to "x" cm (x=20–500) | ok/error |
| left x | Fly left for "x" cm (x=20-500) | ok/error |
| right x | Fly right for "x" cm (x=20–500) | ok/error |
| forward x | Fly forward for "x" cm (x=20–500) | ok/error |
| back x | Fly backward for "x" cm (x=20–500) | ok/error |
| cw x | rotates "x" degrees clockwise (x=1–360) | ok/error |
| ccw x | rotates "x" degrees counterclockwise (x=1–360) | ok/error |
| flip x | flip in "x" direction -> "l"=left,"r"=right,"f"=forward,"b"=backward | ok/error |
| go x y z speed | go to "x" "y" "z" at "speed" (cm/s) -> "x"=-500–500, "y"=-500–500, "z"=-500–500, "speed"=10–100. Note: "x", "y" and "z" values can't be set between -20-20 simultaneously | ok/error |
| stop | Hovers in the air. Note: works at any time | ok/error |
| curve x1 y1 z1 x2 y2 z2 speed | Fly at a curve according to the two given coordinates at "speed" (cm/s). If the arc radius is not within a range of 0.5–10 meters, it will respond with an error. "x1,"x2"=-500–500; "y1","y2"=-500–500; "z1","z2"=-500–500; "speed"=10–60. Note: "x", "y" and "z" values can't be set between -20-20 simutaneously | ok/error |
| go x y z speed mid | Fly to the "x", "y" and "z" coordinates of the Mission Pad. "mid"=m1–m8, "x"=-500–500, "y"=-500–500, "z"=-500–500, "speed"=10–100 (cm/s). Note: "x", "y" and "z" values can't be set between -20–20 simutaneously | ok/error |
| curve x1 y1 z1 x2 y2 z2 speed mid | Fly at a curve accoding to the two given coordinates of the Mission Pad ID at "speed" (cm/s). If the arc radius is not within a range of 0.5–19 meters, it will respond with an error. "x1","x2"=-500–500; "y1","y2"=-500–500; "z1","z2"=-500–500; "speed"=10–60. Note: "x", "y" and "z" values can't be set between -20–20 simutaneously | ok/error |
| jump x y z speed yaw mid1 mid2 | Fly to coordinates “x”, “y”, and “z” of Mission Pad 1, and recognize coordinates 0, 0, “z” of Mission Pad 2 and rotate to the yaw value. “mid” = m1-m8; “x” = -500-500; “y” = -500-500; “z” = -500-500; “speed” = 10-100 (cm/s). Note: “x”, “y”, and “z” values can’t be set between -20 – 20 simultaneously | ok/error |

## Set Commands
| Command  | Description | Possible Response |
| ------------- | ------------- | ------------- |
| speed x | Set speed to “x” cm/s; x = 10-100 | ok/error |
| rc a b c d | Set remote controller control via four channels. “a” = left/right (-100-100); “b” = forward/backward (-100-100); “c” = up/down (-100-100); “d” = yaw (-100-100) | ok/error |
| wifi ssid pass | Set Wi-Fi password. ssid = updated Wi-Fi name; pass = updated Wi-Fi password | ok/error |
| mon | Enable mission pad detection (both forward and downward detection) | ok/error |
| moff | Disable mission pad detection | ok/error |
| mdirection x | “x” = 0/1/2 (0 = Enable downward detection only,1 = Enable forward detection only,2 = Enable both forward and downward detection); Notes: \Perform “mon” command before performing this command. The detection frequency is 20 Hz if only the forward or downward detection is enabled. If both the forward and downward detection are enabled, the detection frequency is 10 Hz | ok/error |
| ap ssid pass | Set the Tello to station mode, and connect to a new access point with the access point’s ssid and password. ssid = updated Wi-Fi name; pass = updated Wi-Fi password | ok/error |

## Read Commands
| Command  | Description | Possible Response |
| ------------- | ------------- | ------------- |
| speed? | Obtain current speed (cm/s) | “x” = 10-100 |
| battery? | Obtain current battery percentage | “x” = 0-100 |
| time? | Obtain current flight time | “time” |
| wifi? | Obtain Wi-Fi SNR | “snr” |
| sdk? | Obtain the Tello SDK version | “sdk version” |
| sn? | Obtain the Tello serial number | “serial number” |

# Tello State

## Data type: String

- Data string received when the mission pad detection feature is enabled:
“ata string received when the mission pad detection feature is enabled:requency is 10 Hz.ltheof:%d;h:%d;bat:%d;baro:%f;\r\nm

- Data string received when the mission pad detection feature is disabled:
“pitch:%d;roll:%d;yaw:%d;vgx:%d;vgy%d;vgz:%d;templ:%d;temph:%d;tof:%d;h:%d;bat:%d;baro:%.2f; time:%d;agx:%.2f;agy:%.2f;agz:%.2f;\r\n”

- Description
1. “mid” = the ID of the Mission Pad detected. If no Mission Pad is detected, a “-1” message will be received instead.

2. “x” = the “x” coordinate detected on the Mission Pad. If there is no Mission Pad, a “0” message will be received instead.

3. “y” = the “y” coordinate detected on the Mission Pad. If there is no Mission Pad, a “0” message will be received instead.

4. “z” = the “z” coordinate detected on the Mission Pad. If there is no Mission Pad, a “0” message will be received instead.

5. pitch = the degree of the attitude pitch.

6. roll = the degree of the attitude roll.

7. yaw = the degree of the attitude yaw.

8. vgx = the speed of “x” axis.

9. vgy = the speed of the “y” axis.

10. vgz = the speed of the “z” axis.

11. templ = the lowest temperature in degree Celsius.

12. temph = the highest temperature in degree Celsius

13. tof = the time of flight distance in cm.

14. h = the height in cm.

15. bat = the percentage of the current battery level.

16. baro = the barometer measurement in cm.

17. time = the amount of time the motor has been used.

18. agx = the acceleration of the “x” axis.

19. agy = the acceleration of the “y” axis.

20. agz = the acceleration of the “z” axis.

## mid commands

mid commands are only used with a Mission Pad. mid commands include:
- mon
- moff
- mdirection “x”
- go “x” “y” “z” “speed” “mid”
- curve “x1” “y1” “z1” “x2” “y2” “z2” “speed” “mid”
- jump “x” “y” “z” “speed” “yaw” mid1 mid2

## Safety Feature

If there is no command for 15 seconds, the Tello will land automatically.

# Reset Tello Wi-Fi

Make sure the Tello is turned on and press and hold the power button for five seconds. The indicators will turn off and blink yellow slowly. When the Wi-Fi SSID and password is reset to the default settings, the indicator blinks yellow quickly. Note that in default there is no password set.
