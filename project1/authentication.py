#coding:utf-8
#!/usr/bin/env python

"""This module provides functions for authenticating users."""

def login(username,password):
    try:
        user_file = open('/etc/users.txt')
        user_buf = user_file.read()
        users = [line.split("|") for line in user_buf.split("\n")]
        if [username,password] in users:
            return True
        else:
            return False
    except Exception, exc:
        print "I can't authenticate you."
        return False

def logout():
    print '这一行不会被测试用例覆盖到'
    print '这一行也不会被测试用例覆盖到'
