Postmortem: Outage on User Login Service
Issue Summary:

Duration: 2024-08-16 10:00 AM UTC to 2024-08-16 11:30 AM UTC (1 hour 30 minutes)
Impact: User login services were completely down during the outage. As a result, 85% of users were unable to log into the platform, affecting user access to core services like dashboard interaction and data processing. Approximately 10,000 users reported being locked out of their accounts during this period.
Root Cause: A misconfigured database query during a code deployment caused a deadlock situation, which exhausted database connection resources and prevented the user login service from functioning.
Timeline:
10:00 AM: Issue detected via monitoring alerts indicating database connection timeouts.
10:05 AM: Engineers notified by automatic alert system.
10:10 AM: Initial investigation focused on the authentication server; database queries were running slower than expected.
10:20 AM: Engineers suspected a sudden traffic spike, causing increased load on the authentication service.
10:30 AM: Realized the assumption about the traffic spike was incorrect; shifted focus to database behavior.
10:40 AM: Database logs showed a significant number of deadlock errors.
10:50 AM: Incident escalated to the database team after deadlock suspicions.
11:00 AM: Root cause identified—a query in the latest deployment update was locking multiple rows in a way that led to resource exhaustion.
11:20 AM: Deployment rollback initiated, reverting the database changes and clearing locked queries.
11:30 AM: Full recovery confirmed, user login services restored.
Root Cause and Resolution:
The issue was caused by a recently deployed feature that introduced an inefficient database query. The query inadvertently locked multiple rows in the database, causing a deadlock condition where no further queries could be processed. As the database resources were exhausted by these locks, all login requests were queued indefinitely, effectively halting user authentication.

Once identified, the team rolled back the deployment, which eliminated the problematic query from the system. They also manually cleared the deadlocks and restarted the database connections. After rollback and clearing the locks, normal operation was restored, and users were able to log in again.

Corrective and Preventative Measures:
Improvements:
A more thorough review of database query changes will be implemented before deployment, especially for any queries affecting user-facing services.
Regular stress testing of the database under different query scenarios will be conducted to identify potential deadlocks in development.
Improved monitoring alerts specific to deadlock and database lock conditions will be added to catch these issues faster.
Tasks:
 Patch the authentication service to avoid locking queries in the future.
 Add monitoring for deadlocks and other DB errors.
 Automate rollback procedures for database-related deployments.
 Improve database query review process before deployment.
