# USER STORY: Login with MFA

As a registered user,  
I want to log in using my email and password,  
and if Multi-Factor Authentication (MFA) is enabled for my account,  
I should receive a one-time code via SMS to complete the login.

Business Rules:
- Three failed login attempts lock the account for 15 minutes.
- The SMS code expires after 2 minutes.
- All login attempts must be logged for audit (security compliance).
- If the SMS fails to send, a single resend option should be offered.
