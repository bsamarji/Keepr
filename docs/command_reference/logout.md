# `keepr logout`

Log out of your Keepr session and securely erase the active session key.

## Usage

```bash
keepr logout
```

## Description

Ends the current session by deleting the session file and cleaning up any residual session data in memory.  
This prevents further access to the vault until you log in again.

## Behavior

- Removes the session file.
- Ensures decrypted session keys are wiped from RAM.
- Prevents accidental vault access.

## Notes

- Safe to run even if no session is active — Keepr will simply notify you.
