# Frequently Asked Questions (FAQ)

Below is a collection of the most common questions developers have when getting started with **Keepr**.

---

## 🔐 Security & Encryption

### **Is Keepr cloud-based?**
No. Keepr stores all data **locally only**, in an encrypted SQLCipher database.  
Nothing is ever synced or uploaded anywhere.

---

### **What happens if I forget my Master Password?**
Your vault **cannot** be recovered.  
Keepr uses strong, irreversible key derivation — without the Master Password, the encryption key cannot be recreated.

---

### **Is my decrypted key ever stored on disk?**
No.  
The decrypted PEK (Primary Encryption Key) only exists **in RAM** during a command execution.
The session file stores only a **Fernet-wrapped key**, not the plaintext version.

---

### **Could a memory-scrape attack extract my vault key?**
In theory, yes — if an attacker has full access to your machine while Keepr is unlocked and executing a command, they could attempt a RAM scrape. 
Command executions take a fractions of a second, so the vector for extracting the primary key is extremely low.

This is a limitation of all local password managers (including GUI ones).  
When Keepr is locked, this attack vector is eliminated.

---

### **What encryption algorithms does Keepr use?**
- **PBKDF2-HMAC-SHA256** for key derivation  
- **SQLCipher** AES-256 database encryption  
- **Fernet (AES-128 in CBC + HMAC-SHA256)** for wrapping the PEK  
- 1,200,000+ iterations for Master Password stretching

---

## 🧰 Usage & Workflow

### **Do I need Python installed?**
No, if using the packaged binary distribution.  
Yes, if installing from PyPI.

---

### **Where does Keepr store its data?**
All Keepr data is stored in:

```shell
~/.keepr
├── .security
│   ├── keepr.key
│   ├── keepr.session
│   └── keepr.salt
├── config.ini
└── keepr.db
```

This location is created automatically.

---

### **What happens when my session expires?**
You must re-enter your Master Password.  
Your vault is instantly locked again until you authenticate.

---

### **Can I change my Master Password later?**
Yes — using:

```bash
keepr change-master
```

This securely re-wraps the encryption key to your new master password.

---

## 📦 Installation & Compatibility

### **Which operating systems are supported?**
✔ macOS  
✔ Linux  
✔ Windows  

Keepr works anywhere Python 3.13+ is available, or via standalone binaries for each OS.

---

### **How do I uninstall Keepr?**
**If installed via pip:**

```bash
pip uninstall keepr
```

**If installed via a binary:**

Go to the location where you placed the keepr binary and delete the binary directory.

**To fully remove local encrypted data:**

**Be absolutely sure before doing this — it deletes your vault!**

```bash
rm -rf ~/.keepr
```

---

## 🛡️ Vault Management

### **What if I want to export my vault?**
Export functionality is planned for a future release.  
For now, backups require manually copying: `~/.keepr`

Do not modify the `.db` file manually as it is encrypted.

---

### **Can Keepr generate passwords automatically?**
Yes, with the `--generate` flag for the `add` abd `update` commands.

Keepr uses cryptographically secure randomness.

---

### **Can I store API keys and tokens?**
Yes. Keepr is designed for developers and supports arbitrary secret fields like:

- API keys  
- tokens  
- OAuth client secrets  
- SSH passwords  
- service keys  

---

## ☄️ Troubleshooting

### **Keepr is slow on Windows — why?**
Windows Defender can aggressively scan standalone binaries.  
You can fix this by adding your Keepr folder to Defender's exclusion list (see the [Installation guide](installation.md) for more details).

---

### **I get “vault locked” even after logging in.**
Check your session timeout settings in the `~/.keepr/config.ini` file.

If the session file was corrupted or expired, a fresh login fixes it.

---

### **My CLI colors look weird.**
Your custom terminal theme may interfere with some of the colors being displayed by Keepr.
Try configuring the Keepr color scheme in the `~/.keepr/config.ini` file.
More details on user configuration can be found in the [configuration guide](user_guides/configuration.md).

---

## ❓ Still stuck?

Open an Issue on GitHub:  
https://github.com/bsamarji/keepr/issues

Or reach out via the [**Support**](about/support.md) section of the docs.