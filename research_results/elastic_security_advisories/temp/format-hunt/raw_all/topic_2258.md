warkolm | 2015-06-09 21:43:31 UTC | #1

**Summary:**
Kibana versions 4.0.0, 4.0.1 and 4.0.2 are vulnerable to a cross-site scripting (XSS) attack. The attack allows execution of arbitrary JavaScript in the context of the user’s browser.

We have been assigned [CVE-2015-4093][1] for this issue.

**Fixed versions:**
[Version 4.0.3][2] has addressed the vulnerability. Read the release blog post [here][3].

**Remediation:**
Users running with Kibana 4.0.0-4.0.2 should [upgrade to 4.0.3][4]. This will address the vulnerability.


  [1]: http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4093
  [2]: https://www.elastic.co/downloads/kibana
  [3]: https://www.elastic.co/blog/kibana-4-0-3
  [4]: https://www.elastic.co/downloads/kibana

-------------------------

system | 2017-07-06 13:46:43 UTC | #2



-------------------------

