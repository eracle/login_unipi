#!/bin/bash

# Insert here private username and password:
username='username'
password='password'

# Wireless ip is retrived:
myip=$(ifconfig wlan0 | grep "inet:" | awk -F: '{print $2}' | awk '{print $1}')

curl -v -POST --data "reqFrom=perfigo_login.jsp&uri=&cm=&userip=$myip&session=&pm=Linux%20x86_64&index=3&pageid=-1&compact=false&egisterGuest=NO&userNameLabel=Username&passwordLabel=Password&guestUserNameLabel=Guest%20ID&guestPasswordLabel=Password&username=$username&password=$password&provider=LDAP%20UniPi" https://auth3.unipi.it/auth/perfigo_cm_validate.jsp
