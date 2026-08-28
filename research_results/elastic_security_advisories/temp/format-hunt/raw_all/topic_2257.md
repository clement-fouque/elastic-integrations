warkolm | 2015-06-09 21:42:06 UTC | #1

**Summary:**
Logstash versions 1.4.2 and prior are vulnerable to a directory traversal attack that allows an attacker to over-write files on the server running Logstash. This vulnerability is not present in the initial installation of Logstash. The vulnerability is exposed when the file output plugin is configured for use. The files impacted must be writeable by the user that owns the Logstash process.

We have been assigned [CVE-2015-4152][1] for this issue.

**Fixed versions:**
Versions [1.5.0 and 1.4.3][2] have addressed the vulnerability. Read the release blog post [here][3].

**Remediation:**
Users that currently use the file output plugin or may use it in the future should [upgrade to 1.5.0 or 1.4.3][4]. This will address the vulnerability and preserve file output functionality.  

Users that do not want to upgrade can address the vulnerability by disabling the file output plugin.

**Credit:**
Colin Coghill reported this issue.


  [1]: http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4152
  [2]: https://www.elastic.co/downloads/logstash
  [3]: https://www.elastic.co/blog/logstash-1-4-3-released
  [4]: https://www.elastic.co/downloads/logstash

-------------------------

system | 2017-07-06 13:46:47 UTC | #2



-------------------------

