# `keepr login`

Authenticate with your Keepr vault and unlock access to all stored credentials.

## Usage

```bash
keepr login
```

## Description

The `login` command prompts you for your master password, verifies it against the vault, and decrypts the session key required for all further operations.  
Once logged in, a temporary session file is created to keep your session active until you log out or until the session timeout duration is reached.

## Behavior

- Prompts securely for your master password.
- Loads and decrypts the vault.
- Creates a session file containing an encrypted session key.
- If a session is already active, it will refresh the session and reset the session timeout duration.

## Notes

- This is the only command that can be run without an active session (apart from `--help`).
- The vault remains encrypted on disk at all times.

