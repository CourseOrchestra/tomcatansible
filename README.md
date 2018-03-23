Tomcat
=========

[![Build Status](https://ci.corchestra.ru/buildStatus/icon?job=tomcatansible/master)](https://ci.corchestra.ru/job/tomcatansible/job/master/)

Installation of [Apache Tomcat](http://tomcat.apache.org/) service bound to localhost. This role is prerequisite for Showcase and Mellophone installations.


Requirements
------------

Java 8 (Oracle)

Role Variables
--------------

* tomcat_version: Tomcat version to install
* tomcat_group: the group for tomcat service user (default valute is tomcat)


Example Playbook
----------------

    - hosts: servers
      vars:
         oracle_java_version: 8
         oracle_java_version_update: 131
      roles:
         - role: ansiblebit.oracle-java
         - role: CourseOrchestra.tomcat

License
-------

MIT

Author Information
------------------

https://corchestra.ru/en
