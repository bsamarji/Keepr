# `keepr view`

View the decrypted details of a stored entry.

## Usage

```bash
keepr view <service name>
```

## Description

Displays the stored username, password, URL, notes and timestamps for create and update dates in a clean table.

This is the only command which will display your usernames and passwords.

The password is copied to your clipboard for convenience.

## Example

```bash
keepr view github
```

## Notes

- Decrypted fields exist only briefly in RAM.
- Keepr clears the data after output.