# 🚀 Getting Started with Keepr

Welcome to Keepr, a secure and developer-friendly command-line password manager designed for speed, simplicity, and strong encryption.

This guide walks you through the basic setup, commands, and workflow you’ll use every day.

---

## 1. 📦 Install Keepr

If you haven’t already installed Keepr, the recommended method is:

```bash
pip install keepr
```

Once installed, verify your installation:

```bash
keepr --help
```

You should see Keepr’s command list and usage help.

---

## 2. 🔑 Create Your Vault (First Run)

The first thing you must do is set your Master Password.

Run:

```bash
keepr login
```

Because no vault exists yet, Keepr will automatically:

* Generate cryptographic salts and key material
* Ask you to create and confirm your Master Password
* Create an encrypted PEK (Primary Encryption Key)
* Initialize your SQLCipher-encrypted vault database
* Create your first authenticated session

You'll see a confirmation message once everything is set up correctly.

> ⚠️ Important:
Your Master Password is the only way to decrypt your vault.
There is no reset, no backup key, and no recovery mechanism.
Choose a strong password you can remember.

---

## 3. 🔓 Logging In (Subsequent Sessions)

Once your vault exists, simply run:

```bash
keepr login
```

This:

* Prompts for your Master Password
* Re-derives the KEK using PBKDF2
* Decrypts the stored PEK
* Starts a new session (default: 1 hour)

During an active session, you won’t be asked for your Master Password again.

---

## 4. 🗄️ Adding Your First Entry

To store a credential:

```bash
keepr add <service name>
```

Example:

```bash
keepr add github
```

Keepr will prompt for:

* Username
* Password
* URL (optional)
* Notes (optional)

Your password will be:

* Hidden during input
* Stored encrypted
* Never written in plaintext

You’ll get a success message once the entry is saved.

---

## 5. 🔍 Listing Entries

To see all stored items:

```bash
keepr list
```

This displays:

* Service names
* URLs
* Notes
* Entry creation timestamps
* Last updated timestamps

Usernames and passwords are **never** shown in the list view.

---

## 6. 👁️ Viewing an Entry

Retrieve a specific entry:

```bash
keepr view <service name>
```

Example:

```bash
keepr view github
```

This reveals:

* Service names
* Usernames
* Decrypted passwords
* URLs
* Notes
* Entry creation timestamps
* Last updated timestamps

It will also copy the password to your clipboard for convenience.

---

## 7. 🔎 Searching the Vault

Find entries matching a term:

```bash
keepr search <search term>
```

Example:

```bash
keepr view git
```

Keepr returns all entries whose service names contain the search term.

This displays:

* Service names
* URLs
* Notes
* Entry creation timestamps
* Last updated timestamps

Usernames and passwords are **never** shown in the search view.

## 8. 🔄 Updating an Entry’s Password

To update the password for an existing entry:

```bash
keepr update <service name>
```

Example:

```bash
keepr update github
```

Keepr prompts for the new password and replaces the old one securely.

---

## 9. ❌ Deleting Entries

Permanently delete an entry:

```bash
keepr delete <service name>
```

Example:

```bash
keepr delete github
```

You’ll be asked to confirm before deletion.

---

10. 🔐 Logging Out (Ending Your Session)

To lock the vault immediately:

```bash
keepr logout
```

This clears your session token, forcing Keepr to wait for you to login with your master password again.

---

## 🎯 Summary of Essential Commands

| Action                    | Command                       |
|:--------------------------|:------------------------------|
| Log in / unlock           | `keepr login`                 |
| Log out / lock            | `keepr logout`                |
| Add new entry             | `keepr add <service name>`    |
| View entry                | `keepr view <service name>`   |
| Update password for entry | `keepr update <service name>` |
| Delete entry              | `keepr delete <service name>` |
| List all entries          | `keepr list`                  |
| Search entries            | `keepr search <search term>`  |

---

## 🐾 Next Steps

Check out:

* [Command Reference](../command_reference/index.md) — full list of available subcommands
* [Vault Encryption Architecture](../encryption.md) — how Keepr encrypts and protects your data
* [FAQs](../FAQs.md) - frequently asked questions by users