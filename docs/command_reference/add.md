# `keepr add`

Add a new credential entry to your Keepr vault.

## Usage

```bash
keepr add <service name>
```

## Description

Creates a new vault entry with the given name and prompts you for:

- Username (optional)
- Password (you may generate one instead)
- URL / service address (optional)
- Notes (optional)

## Flags (optional)

- `--generate` — automatically generates a strong password.
- `without-special-chars` — can only be used with the `--generate` flag, it genrates a password without special characters.

## Examples

Add a new entry:

```bash
keepr add github
```

Add a new entry with a randomly generated password:

```bash
keepr add github -g
```

Add a new entry with a randomly generated password **without** special characters:

```bash
keepr add github -g -w
```

Keepr will guide you interactively through all the prompts.

## Notes

- Entries must have unique names.
- If you want a space in your service name then you must use quotation marks e.g. `keepr add "github repo"`.
