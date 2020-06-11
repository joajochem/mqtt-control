#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import os
import argparse
############

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-cmd', '-cmd', help='helpcmd', required=False)
parser.add_argument('-service', '-srv', help='service', required=False)
parser.print_help()

args = parser.parse_args()

broker_address="eyf-server"
print("creating new instance")
client = mqtt.Client("server1")
print("connecting to broker")
client.connect(broker_address)
#client.publish("commands/client2", "this is server")
arg_command = args.cmd
arg_service = args.service 

mqtt_command = "{} {}".format(arg_command,arg_service)
client.publish("commands/clients", mqtt_command)
print("message send")

