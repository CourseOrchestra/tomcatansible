Tomcat
=========

Jenkins [![Build Status](https://ci.corchestra.ru/buildStatus/icon?job=tomcatansible/master)](https://ci.corchestra.ru/job/tomcatansible/job/master/)

Travis [![Build Status](https://travis-ci.org/CourseOrchestra/tomcatansible.svg?branch=master)](https://travis-ci.org/CourseOrchestra/tomcatansible)

Installation of [Apache Tomcat](http://tomcat.apache.org/) service bound to localhost. This role is prerequisite for Showcase and Mellophone installations.

Requirements
------------

Java 8 (Oracle)

Role Variables
--------------

| parameter           | default value | description            |
|---------------------|---------------|------------------------|
| tomcat_version      | 8.5.32        | version to install     |
| tomcat_user         | tomcat        | service user           |
| tomcat_group        | tomcat        | service user group     |
| tomcat_bind_address | 127.0.0.1     | HTTP connector address |

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
