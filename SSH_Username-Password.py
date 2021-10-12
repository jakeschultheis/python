#!/usr/bin/python3
#SSH_Username-Password.py
#Quick script to SSH into Server using username & password and run a command
import paramiko

cmd='$command'

ip_address='$ip_address'
port=22
username='$username'
password='$password'

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip_address,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
stdout.channel.set_combine_stderr(True)

outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
