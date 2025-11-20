# Command Reference Overview

Welcome to the Keepr command reference. This section provides a detailed breakdown of every CLI command available in Keepr, along with examples, flags, and recommended usage patterns.

Keepr follows a simple and intuitive command structure designed to be easy to learn while still offering powerful security features. Each command below links to a dedicated page with detailed documentation.

---

## 🔐 Authentication Commands

### [`keepr login`](login.md)
Authenticate with an existing vault session and unlock your encrypted passwords.

### [`keepr logout`](logout.md)
Securely close the active session and remove the in-memory session key.

### [`keepr change-master`](change_master.md)
Change your vault’s master password and re-encrypt all contents.

---

## 📦 Vault Management Commands

### [`keepr add`](add.md)
Add a new credential entry to your vault.

### [`keepr update`](update.md)
Modify an existing password for an existing entry.

### [`keepr delete`](delete.md)
Remove an entry from the vault permanently.

---

## 🔍 Retrieval & Viewing Commands

### [`keepr view`](view.md)
View the decrypted details of a stored entry.

### [`keepr list`](list.md)
List all entries stored in your vault.

### [`keepr search`](search.md)
Search for entries using name-based fuzzy matching.

---

## 🔧 Utility Commands

### [`keepr --help`](help.md)
Show documentation for Keepr or a specific command.

---

## 📚 Notes

- All commands require an unlocked session except `login` and `--help`.
- Keepr securely wipes decrypted secrets from memory whenever possible.
- The vault file remains encrypted on disk at all times.
- See the [**Encryption Architecture**](../encryption.md) section for more details on encryption and threat models.

---

## 🧭 Next Steps

- New to Keepr? Start with the [Getting Started Guide](../user_guides/getting_started.md).
- Want to contribute? See the [Contributing Guide](../about/contributing.md).
