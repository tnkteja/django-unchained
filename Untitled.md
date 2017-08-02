## Introduction
Sometimes a Web API is used interchangeably with a Web Service, 

## Background

### Web application
A web application is both a clientside by part and server-side by part application effort for a whole complete service.

### Web APIs
We have client-side Web API and server-side Web API. Client side Web API's usually refer to frameworks offering 
Application Programming interface, usually not the core browser engine APIs, unless they are publicly accesible.
Server-side web API is the request-response message system interfac, usually based off the obvious HTTP-based webserver. 

### Mashups vs Portals
Mashups are web applications that serve services from more than one web servers. Such services are often in complement to main r major 
web application server. More often these mashups are publich or open APIs offered by the various development communities.

###Webhooks
Web hooks are the event callbacks on the events that occur on a web appplication server. Usually tthesse callbacks are served by thrid party services or
the same web apllication but probably using a remote application server part the their mashup.

###Endpoints
Endpoints are the specific resource locations that offer each or a collection of web application servers services. Usually these are the **URI** on which HTTP req-resp are made.

### Web 1.0 vs Web 2.0


## Frameworks

### Frontend

#### Looks and Appeal

##### Angular-Material

##### Icons

|||
:-:|:-:
_http://google.github.io/material-design-icons/_| NA
_https://klarsys.github.io/angular-material-icons/_| NA

## Web Application Security
### Open Web Application Security Project

A community for security in web application development.

#### Top 10 Web Application Vulnerabilities
##### A1-Injection

Injection flaws, such as SQL, OS, XXE, and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile data can trick the interpreter into executing unintended commands or accessing data without proper authorization.
###### SQL Injection
##### A2-Broken Authentication and Session Management

Application functions related to authentication and session management are often implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens, or to exploit other implementation flaws to assume other users’ identities (temporarily or permanently).

##### A3-Cross-Site Scripting (XSS)

XSS flaws occur whenever an application includes untrusted data in a new web page without proper validation or escaping, or updates an existing web page with user supplied data using a browser API that can create JavaScript. XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.
##### A4-Broken Access Control

Restrictions on what authenticated users are allowed to do are not properly enforced. Attackers can exploit these flaws to access unauthorized functionality and/or data, such as access other users' accounts, view sensitive files, modify other users’ data, change access rights, etc.
##### A5-Security Misconfiguration

Good security requires having a secure configuration defined and deployed for the application, frameworks, application server, web server, database server, platform, etc. Secure settings should be defined, implemented, and maintained, as defaults are often insecure. Additionally, software should be kept up to date.
A6-Sensitive Data Exposure

Many web applications and APIs do not properly protect sensitive data, such as financial, healthcare, and PII. Attackers may steal or modify such weakly protected data to conduct credit card fraud, identity theft, or other crimes. Sensitive data deserves extra protection such as encryption at rest or in transit, as well as special precautions when exchanged with the browser.

##### A7-Insufficient Attack Protection

The majority of applications and APIs lack the basic ability to detect, prevent, and respond to both manual and automated attacks. Attack protection goes far beyond basic input validation and involves automatically detecting, logging, responding, and even blocking exploit attempts. Application owners also need to be able to deploy patches quickly to protect against attacks.

##### A8-Cross-Site Request Forgery (CSRF)

A CSRF attack forces a logged-on victim’s browser to send a forged HTTP request, including the victim’s session cookie and any other automatically included authentication information, to a vulnerable web application. Such an attack allows the attacker to force a victim’s browser to generate requests the vulnerable application thinks are legitimate requests from the victim.

##### A9-Using Components with Known Vulnerabilities

Components, such as libraries, frameworks, and other software modules, run with the same privileges as the application. If a vulnerable component is exploited, such an attack can facilitate serious data loss or server takeover. Applications and APIs using components with known vulnerabilities may undermine application defenses and enable various attacks and impacts.
A10-Underprotected APIs

Modern applications often involve rich client applications and APIs, such as JavaScript in the browser and mobile apps, that connect to an API of some kind (SOAP/XML, REST/JSON, 

## References
1. _https://www.owasp.org/index.php/Top_10_2017-Top_10_
