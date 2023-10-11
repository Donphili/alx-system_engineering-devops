#0x19-postmortem


#MY FIRST POSTMORTEM:

#Step 1: INCIDENT:
#"Website Downtime Due to Database Failure"
 
Step 2:  Duration: 
 
The website was down for 4 hours on October 9th, 2021, from 2:00 PM to 6:00 PM (WAT).
Impact: The website became inaccessible during this time, affecting all users. Approximately 90% of users were unable to access the site.
Root Cause: The outage was caused by a database server failure.
 
Step 3: Timeline Events:
 
2:00 PM (WAT): Issue detected via monitoring alerts showing a spike in error rates.
2:15 PM (WAT): Engineers noticed the issue and began investigating.
2:30 PM (WAT): The initial assumption was that it might be a network issue. Network logs were checked.
3:00 PM (WAT): The network was ruled out as the issue. The investigation focused on the database.
4:00 PM (WAT): A database server failure was confirmed.
4:30 PM (WAT): The incident escalated to the database maintenance team.
6:00 PM (WAT): Issue resolved; database server restarted.

Step 4: Root Cause and Resolution:
 
The database server experienced a hardware failure in the storage subsystem, leading to data corruption and unavailability.
 
Resolution: The database maintenance team replaced the faulty hardware components and performed data recovery from backups. The server was restarted, and the website was operational.

Step 5: Corrective and Preventative Measures:
 
Improve database server monitoring to detect hardware failures early.
Implement a redundant database server for failover.
Regularly test database backups for reliability.
Document the incident response process for faster resolution.
