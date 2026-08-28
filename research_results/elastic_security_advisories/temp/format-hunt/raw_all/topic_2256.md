warkolm | 2015-06-09 21:40:28 UTC | #1

**Summary:**
Elasticsearch versions 1.0.0 - 1.5.2 are vulnerable to an engineered attack on other applications on the system.  The snapshot API may be used indirectly to place snapshot metadata files into locations that are writeable by the user running the Elasticsearch process.  It is possible to create a file that another application could read and take action on, such as code execution.  

This vulnerability requires several conditions to be exploited.  There must be some other application running on the system that would read Lucene files and execute code from them.  That application must also be accessible to the attacker, e.g. over the network.  Lastly, the Java VM running the Elasticsearch process must be able to write into a location that the other application will read and potentially execute.

We have been assigned [CVE-2015-4165][1] for this issue.

**Fixed versions:**
[Version 1.6.0][2] address the vulnerability by adding configuration to limit the filesystem paths that the Java VM can write into.

**Remediation:**
Users should [upgrade to the 1.6.0 release][3]. Read the release blog post [here][4].

Users that do not want to upgrade can address the vulnerability in any of several ways:

 - Ensure that there are no other applications running on the Elasticsearch server
 - Ensure that the Elasticsearch JVM cannot write a directory that other applications read from
 - Use a firewall, reverse proxy, or Shield to prevent snapshot API calls from some or all users
 - Ensure that other applications running on the server are not accessible to attackers

  [1]: http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4165
  [2]: https://www.elastic.co/downloads/elasticsearch
  [3]: https://www.elastic.co/downloads/elasticsearch
  [4]: https://www.elastic.co/blog/elasticsearch-1-6-0-released

-------------------------

system | 2017-07-06 13:46:50 UTC | #2



-------------------------

