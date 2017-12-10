#!/usr/env python
# -*- coding: utf-8 -*-
#lm021217.1855

# File to store datas on influxDB database that we have already created

import sys
sys.path.insert(0, '/home/ubuntu/e2emonitor/service_now/')
from sn_scenario_poseidon import returnTimePoseidon

from influxdb import InfluxDBClient

def main(host='localhost', port=8086):
	# Import data to stock
	(timestamp, times_list) = returnTimePoseidon()
	sys.path.remove('/home/ubuntu/e2emonitor/service_now/')

	# Prepare data to stock
	"""Instantiate a connection to the InfluxDB."""
	dbname = "serviceNow_poseidon"
	json_body_totalTime = [
		{
			"measurement": "Total time",
			"time": timestamp,
			"fields": {
				"Int_value": times_list[0]
			}
		}
	]

	json_body_networkTime = [
		{
			"measurement": "Network time",
			"time": timestamp,
			"fields": {
				"Int_value": times_list[1]
			}
		}
	]

	json_body_serverTime = [
		{
			"measurement": "Server time",
			"time": timestamp,
			"fields": {
				"Int_value": times_list[2]
			}
		}
	]

	json_body_browserTime = [
		{
			"measurement": "Browser time",
			"time": timestamp,
			"fields": {
				"Int_value": times_list[3]
			}
		}
	]

	client = InfluxDBClient(host, port, database=dbname)
	client.write_points(json_body_totalTime)
	client.write_points(json_body_networkTime)
	client.write_points(json_body_serverTime)
	client.write_points(json_body_browserTime)

if __name__ == '__main__':
	main()
