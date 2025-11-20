# `keepr change-master`

Change your master password and re-encrypt the vault with a new key derived from it.

## Usage

```bash
keepr change-master
```

## Description

Prompts you for your current master password, then asks you to enter a new one. 
Keepr will derive a new encryption key from your new password and re-encrypt the entire vault.

## Behavior

- Verifies the current master password.
- Generates a new key from the new password.
- Re-encrypts all vault entries.
- Updates metadata and persists the updated vault.

## Notes

- Make sure to remember your new master password — it cannot be recovered.
- Re-encryption happens locally and does not require internet access.
