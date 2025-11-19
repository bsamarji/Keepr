# 🏠 Home

![Keepr Logo](assets/keepr_logo.png)

Welcome to the official documentation for Keepr, a lightweight and intuitive password manager designed for developers and command-line users.

Keepr helps you store, search, edit, and manage credentials securely from your terminal — without the complexity and overhead of heavy password manager apps.

---

## 🧩 Features

* 🫧 Simple Interface — Clean commands, minimal setup.
* 🔑 Industry Standard Encryption — Only the master password will unlock your vault.
* 💾 Local-First Storage — Your vault stays on your machine.
* 🕒 Timed Sessions — Stay logged in for convenience, auto-lock after expiry.
* 🧭 Vault Management — Add, update, list, search, or delete credentials.
* 🧰 Password Generator — Cryptographically secure, configurable length.
* 🧼 Clipboard Copy — Automatically copy passwords to the clipboard when viewing an entry.
* 🎨 Custom Color Scheme — Clear, high-contrast terminal output.
* ⚙️ User Configuration — Configure the session length, the terminal output color scheme and password generator settings. 

---

## ⚡ Quick Start

Install Keepr from [PyPI](https://pypi.org/project/keepr/):

```bash
pip install keepr

keepr login # Set or unlock the master password

keepr add github # Add a credential

keepr view github # Retrieve entry securely
```

That’s it — your credentials are stored locally, fully encrypted, and accessible only through your master key.

Head over to the **Getting Started** section for more details on installation, setup and first steps.

---

## 🎥 Demo

<script src="https://asciinema.org/a/dpz0mO8AKUnlCOrqVwOb2UEkx.js" id="asciicast-dpz0mO8AKUnlCOrqVwOb2UEkx" async="true"></script>

---

## 📚 Docs Overview

* **[Getting Started](user_guides/getting_started.md)** — installation, setup, first steps
* **[Command Reference](command_reference/index.md)** — detailed reference for every keepr subcommand
* **[Vault Encryption Architecture](encryption.md)** — how and where Keepr stores encrypted data
* **[FAQs](FAQs.md)** — common issues, troubleshooting, tips
* **[Contributing](about/contributing.md)** — guidelines for contributors

---

## 🔗 Useful Links

* [**GitHub Repo**](https://github.com/bsamarji/Keepr)
* [**PyPI**](https://pypi.org/project/Keepr/)
* [**Issues**](https://github.com/bsamarji/Keepr/issues)

---

## ❤️ Contributing

Contributions, ideas, and suggestions are welcome!

Check out the [**Contributions page**](about/contributing.md) if you'd like to help improve Keepr!
