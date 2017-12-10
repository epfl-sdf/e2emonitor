#!/bin/bash
virtFold="venv"

source ../$virtFold/bin/activate
python3 sn_storeDatasIncidents_influxDB.py
python3 sn_storeDatasKnowledge_influxDB.py
python3 sn_storeDatasPoseidon_influxDB.py
deactivate

# kill if some process still active
# firefox process
case "(pidof firefox | wc -w)" in

0)	;;
*)	killall -9 firefox
	;;
esac

# Xvfb process
case "(pidof Xvfb | wc -w)" in

0)	;;
*)	killall -9 Xvfb
	;;
esac
