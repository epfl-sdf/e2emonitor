#!/bin/bash

case "$(pidof firefox | wc -w)" in

0)	;;
*) 	killall -9 firefox
	;;
esac

case "$(pidof Xvfb | wc -w)" in

0)	;;
*) 	killall -9 Xvfb
	;;
esac
