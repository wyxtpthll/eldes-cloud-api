#!/usr/bin/python3

import os
import eldes
import configparser


usr = None
psw = None
devid = None

usrDir = os.path.expanduser("~")
config = configparser.ConfigParser()
if os.path.exists("./config.txt"):
    config.read("./config.txt")
elif os.path.exists(usrDir + "/config.txt"):
    config.read(usrDir + "/config.txt")
else:
    raise FileExistsError('File not found: (./config.txt; ~/config.txt)')
usr = config.get("eldes", "username")
psw = config.get("eldes", "password")
devid  = config.get("eldes", "devid")


client = eldes.EldesClient(username=usr ,password=psw ,hostDeviceId=devid , refresh_token_file="refresh_token.txt")

#print(client.get_devices)
#print(client.is_partition_armed(location="Sodas", partition="SodoNamas"))
rez = client.get_temperatures(location="Sodas")
for x in rez["temperatureDetailsList"]:
    #print(x)
    #print(rez["temperatureDetailsList"][0]["temperature"])
    print("Name:", x["sensorName"], "Temperature:", x["temperature"])
#print(rez["temperatureDetailsList"][0]["temperature"])
#rez = client.get_events(location="Sodas")
#print(rez)
#print("ok")

