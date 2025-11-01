```markdown
## Business Objective
To enhance the security of user accounts by implementing Multi-Factor Authentication (MFA) during the login process, ensuring that only authorized users can access their accounts.

## Functional Requirements
- Users must be able to log in using their email and password.
- If MFA is enabled for the account, users must receive a one-time code via SMS after entering their email and password.
- Users must be able to enter the received one-time code to complete the login process.
- The system must lock the account for 15 minutes after three failed login attempts.
- The one-time SMS code must expire after 2 minutes.
- The system must log all login attempts for audit purposes.
- If the SMS code fails to send, the system must provide a single option to resend the code.

## Implicit Business Rules
- User accounts must be secured against brute-force attacks by locking after three failed login attempts.
- The one-time code must be time-sensitive, ensuring that it cannot be used after 2 minutes.
- All login attempts must be recorded to comply with security auditing requirements.
- The system must handle SMS sending failures gracefully by allowing users to request a resend.
```