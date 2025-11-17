<div align="center">
<h1>Keepr 🗝️</h1>
<br/>
<a href="https://pypi.org/project/Keepr"><img src="https://img.shields.io/pypi/v/keepr.svg" alt="PyPI Version"></a>
<a href="https://pepy.tech/projects/keepr"><img src="https://static.pepy.tech/personalized-badge/keepr?period=total&units=ABBREVIATION&left_color=GREY&right_color=MAGENTA&left_text=downloads" alt="PyPI Downloads"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built_with-python3-green.svg" alt="Built with Python3"></a>
<a href="LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-orange.svg" alt="License badge"></a>
<a href="https://github.com/bsamarji/Keepr"><img src="https://img.shields.io/github/stars/bsamarji/Keepr?style=social" alt="GitHub stars"></a>
<h3>A lightweight, end-to-end encrypted password manager for developers - built for the terminal.</h3>
</div>

Keepr is a secure, cross-platform command-line password manager designed for software developers.  
It stores your credentials in a fully encrypted [SQLCipher](https://www.zetetic.net/sqlcipher/) database that lives **entirely on your local machine**, ensuring complete control over your data. 
No servers, no cloud syncing — just strong, local encryption.

The vault is protected by a **Master Password** derived into a strong encryption key using industry-standard PBKDF2-HMAC (SHA256, 1.2M iterations).
Your data remains safe even if the database or key files are compromised.

---

## 🧠 Why Keepr?

As a developer, you constantly handle sensitive data — API keys, repository tokens, SSH passwords, and configuration secrets. 
Keepr was built to simplify that workflow by letting you **store, search, and retrieve secrets directly from the terminal**, without switching tools or exposing plaintext data.

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

---

## 🧩 Features at a Glance

* 🔒 End-to-End Encryption — AES-256 via SQLCipher and Fernet.
* 🔑 Master Password — Derives a Key Encryption Key (KEK) with PBKDF2-HMAC.
* 🕒 Timed Sessions — Stay logged in for convenience, auto-lock after expiry.
* 🧭 Vault Management — Add, update, list, search, or delete credentials.
* 🧰 Password Generator — Cryptographically secure, configurable length.
* 🧼 Clipboard Copy — Automatically copy passwords to the clipboard when viewing an entry.
* 🎨 Custom Color Scheme — Clear, high-contrast terminal output.
* ⚙️ User configuration — Configure the session length, the terminal output color scheme and password generator settings. 

---

## 📦 Installation

You can install Keepr either via **PyPI (recommended)** or as a **standalone binary** if you can’t install Python.

---

### 🐍 Option 1: Install from PyPI (Recommended)

Keepr supports **macOS**, **Linux**, and **Windows**.

```bash
pip install keepr
```

Once installed, verify your installation:

```bash
keepr --help
```

### 💻 Option 2: Download a Prebuilt Binary

If you prefer not to install Python, Keepr provides precompiled binaries built with PyInstaller, which bundle Python and all dependencies.

👉 Download the latest binary for your OS from the [GitHub Releases page](https://github.com/bsamarji/Keepr/releases).

#### Steps

1. Download the correct archive for your OS.
2. Extract the contents to a permanent folder (e.g. `~/tools/keepr` on macOS/Linux, or `C:\Tools\Keepr` on Windows).
3. Add that folder to your system’s PATH so keepr can be run from anywhere.

<details> <summary>macOS & Linux Setup</summary>

On macOS and Linux, you'll update your shell's configuration file (usually `.zshrc` or `.bashrc`).

1.  **Move the Directory:** Move the extracted `keepr` folder (containing the executable) to a clean, permanent location, like a new `tools` directory in your home folder:
    ```bash
    # Example: Move the extracted 'keepr' folder into a 'tools' directory
    mv /path/to/downloaded/keepr ~/tools/
    ```

2.  **Edit Shell Configuration:** Open the configuration file for your shell (`.zshrc` for modern macOS, `.bashrc` for most Linux systems) using a text editor like `vim`:
    ```bash
    # For modern macOS (Zsh):
    vim ~/.zshrc

    # For most Linux systems (Bash):
    vim ~/.bashrc
    ```

3.  **Add to PATH:** Add the following line to the **very end** of the file, replacing the path with your chosen directory:
    ```bash
    export PATH="$HOME/tools/keepr:$PATH"
    ```

4.  **Apply Changes:** Save the file and apply the new configuration by running:
    ```bash
    source ~/.zshrc  # or source ~/.bashrc
    ```

5.  **Verify:** Open a **new terminal window** and run `keepr --help`.

</details>

<details> <summary>Windows (PowerShell) Setup</summary>

On Windows, you need to update your systems environment variables. This can be done through the GUI, but below I've posted instructions for doing this through the command line.
Please ensure you're running Powershell in **Administrator Mode**.

1. Ensure you have moved the extracted `keepr` folder to a permanent, simple location, for example: `C:\Tools\Keepr`.

2. **Define the Path:** Open a new **Windows Terminal** window running PowerShell. First, set the path to your `keepr` folder as a variable for easier use.
    ```powershell
    # Set the variable to the exact path where the 'keepr' executable is located
    $KeeprPath = "C:\Tools\Keepr"
   ```

3. **Add the Path Permanently:** Use the built-in .NET class method to append the new directory to your User-level PATH variable. The third argument "User" ensures the change is permanent.
    ```powershell
   [System.Environment]::SetEnvironmentVariable(
    "Path",
    "$env:Path;$KeeprPath",
    "User"
    )
   ```

4. **Exclude the Dir From Windows Defender:** Windows defender massively hampers performance of this executable as it scans the directory everytime which can take minutes. To avoid this, please exclude it from defender scans:
    ```powershell
   Add-MpPreference -ExclusionPath $KeeprPath
   ```
   
5. **Verify:** **Close and reopen** any active Command Prompt or PowerShell windows, and then run `keepr --help`.

</details>

---

## 🧠 Usage Overview

Keepr is designed to feel natural for developers — everything happens directly in your terminal. 

**Note:** You may have to resize your terminal so the outputs from keepr can be displayed without breaking up.

All commands follow the format:

```bash
keepr <command> [arguments]
```

If you ever get lost, use:

```bash
keepr --help
```

### 🔐 First-Time Setup

Before using keepr, you must create your master password. 
This password is the only way to unlock your vault — it cannot be recovered if lost.
To do this run:

```bash
keepr login
```

Keepr will guide you through the initial setup, generating encryption keys and a secure vault on your local machine.
Once logged in, your vault remains unlocked for a timed session of 1 hour to support a smooth workflow.

### ⚙️ Core Commands

All commands follow the structure: `$ keepr <command> [arguments]`

| Command         | Description                                                             | Example                   |
|:----------------|:------------------------------------------------------------------------|:--------------------------|
| `login`         | Logs in and unlocks your vault (creates or renews your session).        | `$ keepr login`         |
| `logout`        | Instantly locks the vault and clears any active session.                | `$ keepr logout`        |
| `change-master` | Safely change your Master Password.                                                                        | `$ keepr change-master` |

### 🔑 Vault Management

You can only run the vault management commands once you've logged in and created an active session.

| Command | Description                                                  | Example |
| :--- |:-------------------------------------------------------------| :--- |
| `add` | Creates a new entry in the vault, prompting for details.     | `$ keepr add github` |
| `view` | Displays a specific entry's details, including the password. | `$ keepr view example_site` |
| `list` | Shows all entries in a clean table (passwords hidden).       | `$ keepr list` |
| `search` | Finds entries matching a given keyword.                      | `$ keepr search work` |
| `update` | Updates the password for an existing entry.                  | `$ keepr update old_site` |
| `delete` | **Permanently deletes** an entry after confirmation.         | `$ keepr delete test_account` |

### 🧩 Session Management

Keepr uses a temporary session file to keep your vault unlocked during your work session. 
Sessions last 1 hour.
You can logout manually anytime using keepr logout. 
After expiration, Keepr requires your Master Password again.

---

## ⚙️ Configuration

You'll find a `.keepr` hidden directory in your `home` directory. 
In the `.keepr` directory you'll find a `config.ini` file. 
Open the config.ini file in a text editor of your choice and change the values for the settings you want to change.

### 🎨 Color Options

There are 8 colors supported:

* `black`
* `red`
* `green`
* `yellow`
* `blue`
* `magenta`
* `cyan`
* `white`

### Default configuration

The default configuration file is below. 
If you want to restore the default values, then you can replace your modified config.ini with the text below.

```ini
[SESSION_CONFIG]
session_timeout_seconds = 3600

[PASSWORD_CONFIG]
password_generator_length = 20
password_generator_special_chars = !@#$^&*

[COLOR_SCHEME_CONFIG]
color_error = red
color_success = green
color_prompt = cyan
color_warning = yellow
color_header = magenta
color_sensitive_data = green
color_non_sensitive_data = white
```

---

## 🛡️ Security Model

Keepr follows a two-tier encryption model for maximum protection of your secrets.

### 1. 🔑 Master Key Derivation (KEK)
   * Input: Master Password + random Salt
   * Algorithm: PBKDF2-HMAC (SHA256, 1,200,000 iterations)
   * Output: Key Encryption Key (KEK)
   * The KEK is never stored — it’s derived at runtime from your Master Password.

---

### 2. 🧠 Primary Encryption Key (PEK)
   * The PEK is the actual key that encrypts your vault (keepr.db) using SQLCipher.
   * It’s stored encrypted on disk (.keepr/.security/keepr.key) — wrapped with your KEK via cryptography.Fernet.

---

### 3. 🧭 Unlocking Flow
   1. You enter your Master Password.
   2. Keepr derives the KEK from it.
   3. The KEK decrypts your encrypted PEK.
   4. The PEK opens your SQLCipher database.
   5. A temporary session file keeps the vault open until timeout or logout.

Even if an attacker steals both your vault and key files, your data remains secure — without your Master Password, decryption is computationally infeasible.

---

### 🏰 Local-Only Security

Keepr is 100% offline — no network requests, telemetry, or remote storage. 
Everything (database, keys, and session) resides in your home directory under:

```bash
~/.keepr/
```

This ensures full data ownership and an extremely small attack surface.

---

### 💡 Pro Tips

* Use short, memorable entry names (e.g., aws, github, prod-db).
* Rotate your Master Password occasionally with `keepr change-master`.
* Always lock the vault when leaving your machine:

```bash
keepr logout 
```

---

## 🤝 Contributing

Contributions are welcome — whether it's bug reports, new ideas, or pull requests.

If you're planning a substantial change, please open an issue first so we can discuss the approach.

### How to Contribute

1. **Fork** the repository  
2. **Create a branch** for your feature or fix  
3. **Commit** your changes with clear messages  
4. **Open a Pull Request**  
5. Wait for review and feedback

---

## 🛠 Support

If you run into problems, the best way to get help is through the GitHub issue tracker.

- 🐛 **Bug Reports:**  
  Tag the issue with the `bug` label and include steps to reproduce.

- 💡 **Feature Requests:**  
  Use the `enhancement` label and describe what you’d like to see added or improved.

- ❓ **General Questions:**  
  Feel free to open an issue or reach out directly to the maintainers.

---

## 🗺 Roadmap

Planned future features and improvements:

- ⌨️ Shell autocompletion for Keepr commands and arguments.
- 🧪 Password strength checks.
- 🧵 Bulk import/export of entries.
- 🔄 A copy command, which copies a password for an entry to the clipboard, without displaying any info on screen.
- 🧩 A generate command, which just generates a password and displays it on screen (separate to the -g option for the add command).
- 🛡️ Optional Two-factor authentication.

If you want to help shape the roadmap, feel free to open an issue or submit proposals.

---

## 👤 Authors

- **Ben Samarji** — Active Maintainer  
  📧 bensamarji5637@gmail.com

---

## 📜 License

Keepr is offered under the **MIT License**.
See `LICENSE.md` for full details.

You are free to use, modify, and distribute the software as long as the license terms are respected.

---

## 🚀 Project Status

**Active development**

New features, performance improvements, and security enhancements are added regularly. 
Community feedback is always appreciated, and contributions are welcome!
