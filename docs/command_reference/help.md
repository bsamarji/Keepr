# `keepr help`

Display Keepr’s built-in help text and command overview.

## Usage

```bash
keepr --help
```

## Description

The `--help` flag provides an overview of all available Keepr commands or detailed help for a specific command.

Running `keepr --help` without arguments lists every supported command with a short description.

Running `keepr <command> --help` shows the usage, options, and summary for that specific command.

## Examples

Show global help:

```bash
keepr --help
```

Show help for a specific command:

```bash
keepr add --help
```

Output (example):

```bash
Usage: keepr [OPTIONS] COMMAND [ARGS]...

  Keepr - Secure Command-Line Password Manager

  Manages passwords and sensitive data locally using an encrypted SQLite
  vault.

Options:
  -h, --help  Show this message and exit.

Commands:
  add            Creates a new entry in the vault, prompting for details.
  change-master  Safely change your Master Password.
  delete         Permanently deletes an entry from the vault after a...
  list           Shows all entries in a clean table (passwords and...
  login          Logs in and unlocks your vault (creates or renews your...
  logout         Instantly locks the vault and clears any active session.
  search         Finds entries matching a given keyword.
  update         Updates the password for an existing entry in the vault.
  view           Displays a specific entry's details, including the...

  Use 'keepr <command> --help' for command-specific usage and examples.
```

## Notes

- This command does not require an unlocked session.