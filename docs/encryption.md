# 🫆 Vault Encryption Architecture

Keepr is built on a layered, security-first encryption model designed to keep your secrets safe even in the event of local system compromise.
This document explains how Keepr encrypts, stores, and protects your data.

---

## 🔐 Overview

Keepr uses a two-tier key system that separates:

* Your Master Password
* A Key Encryption Key (KEK)
* A Primary Encryption Key (PEK)
* An encrypted SQLCipher database

This decoupled architecture ensures that no sensitive key material—especially anything derived from your Master Password—is ever stored unencrypted on disk.

---

## 1. 🔑 Master Password → KEK Derivation

Your Master Password is the root of trust for your vault.

**How Keepr derives the KEK:**

* Your Master Password is combined with a cryptographically secure random salt
* Keepr runs this through PBKDF2-HMAC-SHA256
* Current iteration count: 1,200,000
* Output: a 32-byte Key Encryption Key (KEK)

**Notes:**

* The salt is stored at: `.keepr/.security/keepr.salt`
* The KEK itself is never stored, only derived in memory when you unlock the vault.
* High iteration counts dramatically slow down brute-force attacks.

---

## 2. 🔐 PEK: The Primary Encryption Key

The Primary Encryption Key (PEK) is the actual key used to encrypt the SQLite vault database.

**Properties:**

* 32-byte symmetric key
* Generated on first setup
* Used directly by sqlcipher3 to encrypt/decrypt keepr.db

**Storage Model**

The PEK is:

* Generated in memory
* Immediately encrypted using the KEK (via Fernet)
* Stored on disk at: `.keepr/.security/keepr.key`

If an attacker steals this file, it is useless without your Master Password.

---

## 3. 🗄️ SQLCipher Encrypted Vault

Keepr uses SQLCipher (via sqlcipher3) to encrypt the entire vault database.

**Security Properties:**

* Full-database AES-256-CBC encryption
* Integrates page-level encryption and metadata protection
* Database file stored at: `.keepr/keepr.db`
* Without the PEK, the database appears as random bytes

This means even filenames and table structure remain unreadable.

---

## 4. 🔓 Unlocking Process

When you run keepr login, the following happens:

1. User enters Master Password
2. Keepr re-derives the KEK using PBKDF2
3. Keepr decrypts the encrypted PEK file
4. The decrypted PEK is used to open the SQLCipher vault
5. A temporary session file stores the unlocked PEK for convenience

**Session File:**

* Located at: `.keepr/.security/keepr.session`
* Contains a **Fernet-encrypted, time-limited token**
* Default session duration: 1 hour
* When the session expires, the PEK is discarded and locked again

No plaintext keys are ever written to disk.

---

## 5. 🧯 Threat Model

Keepr is designed to withstand:

**✔ Local filesystem access**

Attackers reading your files cannot unlock your vault without your Master Password.

**✔ Theft of:**

* Vault database
* Encrypted PEK
* Salt

Each component alone is worthless.

**✔ Brute-force attempts**

High PBKDF2 iteration counts make password cracking computationally expensive.

**✔ Reverse-engineering the Keepr source**

Open source by design — no security through obscurity.

---

## 6. ⚠ Boundaries of Protection

Keepr does not protect against:

* Active malware/keyloggers on your system
* Memory-scraping attacks while Keepr is running (The opportunity for this window is a fraction of a second while a Keepr command executes)
* Shoulder-surfing or physical observation
* Weak Master Passwords (Use something strong and memorable!)

---

## 7. 🎯 Summary

Keepr’s encryption model is built to guarantee that:

* Your data is always encrypted at rest
* Your keys are always encrypted on disk
* Your Master Password is never stored
* Breaching your machine is not enough to unlock your vault

Your Master Password is the only key that can ever decrypt your vault — put simply:
> If you don’t know the Master Password, you can’t open the vault.
