# SMOKE (critical for release)
- Successful login with valid credentials and MFA
  - Core functional path. If this fails, no user can access the product.
- Failed login due to incorrect password
  - Verifies basic credential validation and user feedback.
- Account lockout after three failed login attempts
  - Critical security control against brute force. Release blocker if broken.

# REGRESSION (repeat each sprint)
- Expired one-time code
  - Ensures OTP expiration is enforced (2-minute TTL). Protects against token reuse.
- Successful login with valid credentials but expired one-time code
  - Confirms that expired codes are always rejected and properly logged.
- Successful resend of one-time code after SMS failure
  - Ensures resilience/usability in case of third-party SMS delivery issues.
- Brute-force attack prevention
  - Confirms locked accounts cannot be accessed until lockout period ends.

# NIGHTLY (extended coverage, non-blocking)
- Successful login with valid credentials and valid one-time code
  - Full happy-path with MFA + OTP + audit logging. Should be green nightly to detect silent regressions.
