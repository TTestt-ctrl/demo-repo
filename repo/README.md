# BookIt (fixture — intentionally non-compliant)

A minimal ride-booking demo app used as a Preflight test fixture. This repo
intentionally contains PDPL gaps: no consent code anywhere, passwords stored
in plaintext, a foreign analytics SDK (Mixpanel), and a fixed non-KSA AWS
region. No password hashing, no retention/TTL fields, no data-subject-rights
endpoints (export/delete), no audit logging.

See `test_fixtures/repo_flawed/expected_output.json` (one level up) for the
scanner's expected output against this repo.
