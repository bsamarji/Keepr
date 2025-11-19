# `keepr search`

Search for entries in your vault using fuzzy or partial matching.

## Usage

```bash
keepr search <search term>
```

## Description

Displays a clean table of all entry names matching to the search term.

Useful for quickly seeing what you have stored, or before running update or delete commands.

## Example

```bash
keepr search git
```

Would match:

* GitHub
* gitea
* Gitlab

## Notes

- Matching is case-insensitive.
- Does not display any sensitive information.