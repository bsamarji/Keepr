# `keepr update`

Update fields inside an existing vault entry.

## Usage

```bash
keepr update <service name>
```

## Description

Allows you to change the password for an entry:

Keepr will prompt for confirmation.

## Flags (optional)

- `--generate` — automatically generates a strong password.
- `without-special-chars` — can only be used with the `--generate` flag, it genrates a password without special characters.

## Examples

Keepr will prompt you to enter a new password:

```bash
keepr update github
```

Keepr will randomly generate a new password:
```bash
keepr update github -g
```

Keepr will randomly generate a new password without special characters:
```bash
keepr update github -g -w
```
