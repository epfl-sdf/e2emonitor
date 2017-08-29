#!/bin/bash
#copy jmeter test plan to remote and run command test plan then retrieve log
test_plan=jmeter_test.jmx
log_file=jmeter.log
remote_username=ubuntu
remote_ip=128.178.116.120
remote_port=31221
ssh_options='-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'

#copy
scp $ssh_options -P $remote_port $test_plan $remote_username@$remote_ip:~/
#run
ssh $ssh_options $remote_username@$remote_ip -p $remote_port -- jmeter -n -t /home/$remote_username/$test_plan -l $log_file
#retrieve
scp $ssh_options -P $remote_port $remote_username@$remote_ip:~/$log_file ./
