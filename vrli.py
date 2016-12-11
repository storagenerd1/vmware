#!/bin/env python
# Script tot check if vRealize Log Insight is installed
# Storagenerd 28112016

url = 'http://reposerver/loginsight/'
vrli = 'VMware-Log-Insight-Agent-4.0.0-4549831.noarch_10.212.113.3.rpm'

pkg = 'VMware-Log-Insight-Agent'

def ostype():
    import platform
    dist = platform.dist()
    if dist[0] == 'redhat':
        return dist
    elif dist[0] == 'centos':
        return dist
    elif dist[0] == 'SuSe':
        return dist
    else:
        print 'Unknown OS'

def checkpkg(pkg):
    os = ostype()
    if os[0] == 'redhat':
        import commands
        if commands.getstatusoutput("rpm -q " +pkg)[0] == 0:
            print 'Installed, nothing to do!'
        else:
            print 'Not Installed, Installing Agent'
            commands.getstatusoutput("rpm -ivh " +url +vrli)
    elif os[0] == 'centos':
        print 'Needs Work'
    else:
        print 'Unknown OS, nothing to do!'

checkpkg(pkg)
