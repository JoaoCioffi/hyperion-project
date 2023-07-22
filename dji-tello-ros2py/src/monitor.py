import subprocess
import env
import re

env=env.environment()

def screenContent():
    
    def decodeSubProc(cmd):
      output=subprocess.check_output(cmd,shell=True,text=False,stderr=subprocess.STDOUT)
      decoded=re.sub(b"\x1b\[2K\r|\\\'|\n", b"",output).decode("utf-8")
      return decoded
    
    # Function to test Tello connection
    def testTelloConnection():
      try:
         network_ssid=env['client-socket']['wifi-name']
         network_pw=env['client-socket']['wifi-pw']
         response=subprocess.check_output(f'nmcli device wifi connect {network_ssid} password {network_pw}',
                                          shell=True,
                                          text=False,
                                          stderr=subprocess.STDOUT)
         response=re.sub(b"\x1b\[2K\r|\\\'|\n", b"",response).decode("utf-8")
         return response
      except:
         return "Not connected"
        

    print(f"""

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
      
      .
      .   
      .
                
    [Info]
          
        HOST OS ............................ {decodeSubProc('cat /etc/issue')}
        ROS2 ............................... {decodeSubProc('which ros2')}
        PORT ............................... {env['client-socket']['port']}
        WIFI NAME .......................... {env['client-socket']['wifi-name']}
        CLIENT IP .......................... {env['client-socket']['tello-ip']}
        CONNECTION STATUS .................. {testTelloConnection()}

    """)

screenContent()