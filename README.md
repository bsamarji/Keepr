# PassMan: Secure Command-Line Password Manager

## Description

**PassMan** is a secure command-line interface (CLI) password manager designed for software developers. 
Compatible with macOS, Linux and Windows, the data is stored in an encrypted SQLite database that resides exclusively on your local machine, 
ensuring full ownership and control of your sensitive information.

The vault is protected by industry-standard encryption, unlocked only through your unique Master Password. 
Since the encrypted SQLite database (`sqlcipher3`) is self-contained and serverless, the risk surface is minimized: 
the only vector for access is gaining physical access to your machine and either knowing your Master Password or 
successfully breaking the high-iteration encryption, which is computationally infeasible.

### Background

I built this app out of frustration for not having anywhere safe and convenient to store sensitive data at work. 
As a software developer, I'm constantly using credentials, repository access tokens, API keys, and other secrets.

**PassMan** solves this problem by enabling a secure, seamless workflow directly in the terminal, 
allowing developers to manage credentials without switching away from the command line.

## Features

**PassMan** is a feature-rich CLI with built-in support for:

* **Master Key Setup:** Secure creation and confirmation of your initial Master Password.
* **Authentication & Session:** Login with your Master Password creates an active, timed session (default: 1 hour) to keep the vault conveniently unlocked during your workflow.
* **Logout & Termination:** Explicitly clear the session file to instantly lock the vault.
* **Vault Management:** Add, Update, View, List, Search, and Delete entries.
* **Secure View:** View a specific entry, revealing sensitive data (like the password).
* **Clipboard Copy:** Copies the password to the clipboard when viewing an entry.
* **Master Password Change:** Functionality to safely update your Master Password.
* **Password Generation:** Integrated cryptographically secure password generator.
* **Colour Scheme:** High contrast colour scheme to create visually appealing and informative outputs.

## Installation

### Prerequisites

* Python 3.13 or newer.
* The `uv` tool for fast dependency resolution and installation (highly recommended).
* `git` for cloning the repository.

### Option 1: Local Development Install (Recommended for Developers/Contributors)

This option clones the repository and installs it in **editable mode** (`-e`), 
making it ideal if you plan to modify or contribute to the source code.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/bsamarji/PassMan.git](https://github.com/bsamarji/PassMan.git)
    cd PassMan
    ```

2.  **Install the project (Editable Mode) and Activate:**
    This installs all dependencies and creates the `passman` executable wrapper script within your virtual environment's path.
    ```bash
    # Create and activate the virtual environment
    python -m venv .venv
    source .venv/bin/activate
    
    # Install dependencies using uv
    uv pip install -e .
    ```

### Option 2: Direct Install (From GitHub)

If you only need to use the CLI and do not plan to make code changes, you can install directly from the GitHub repository URL.

1.  **Activate your desired environment** (or create one).
    ```bash
    # Example: create and activate a new venv
    python -m venv passman-cli-venv
    source passman-cli-venv/bin/activate
    ```

2.  **Install PassMan directly:**
    ```bash
    uv pip install git+[https://github.com/bsamarji/PassMan.git](https://github.com/bsamarji/PassMan.git)
    ```

3.  **Run the CLI:**
    The `passman` command is now available:
    ```bash
    $ passman --help
    ```

## Usage & Commands

The first time you run any `passman` command, you will be guided through the process of creating your **Master Password**. 
This password is the only key to your vault, so treat it as your most important secret.

All commands follow the structure: `$ passman <command> [arguments]`

### Core Commands

| Command         | Description                                                              | Example                   |
|:----------------|:-------------------------------------------------------------------------|:--------------------------|
| `login`         | Explicitly logs in and starts a new session (or updates an expired one). | `$ passman login`         |
| `logout`        | Clears the session file, locking the vault immediately.                  | `$ passman logout`        |
| `change-master` | Enables the user to change their master password.                        | `$ passman change-master` |

### Vault Management

| Command | Description                                                                | Example |
| :--- |:---------------------------------------------------------------------------| :--- |
| `add` | Creates a new entry in the vault, prompting for details.                   | `$ passman add github` |
| `view` | Retrieves and displays a specific entry's details, including the password. | `$ passman view example_site` |
| `list` | Displays a table of all entries in the vault (passwords are hidden).       | `$ passman list` |
| `search` | Searches entries that contain a given string.                              | `$ passman search work` |
| `update` | Updates the password for an existing entry.                                | `$ passman update old_site` |
| `delete` | **Permanently deletes** an entry after a confirmation prompt.              | `$ passman delete test_account` |

## Security Model

PassMan uses a robust, two-tier encryption system built on top of `sqlcipher3` (for the database) and `cryptography` (for key management) to protect your data. 

### 1. Master Key Derivation (KEK)

* **Input:** Your Master Password and a unique, randomly generated Salt (`.passman/.security/passman.salt`).
* **Function:** PBKDF2HMAC with SHA256, running through a high number of iterations (currently 1,200,000) to resist brute-force attacks.
* **Output:** The **Key Encryption Key (KEK)**. This key is *never* stored on disk; it is generated purely from your Master Password when you log in.

### 2. Primary Encryption Key (PEK)

* **Key Purpose:** The PEK is the actual 32-byte key used by `sqlcipher3` to encrypt and decrypt the entire vault file (`passman.db`).
* **Storage:** The PEK is initially generated and then **immediately encrypted** using the KEK (from step 1) via the `Fernet` symmetric encryption library.
* **Persistence:** This *encrypted* PEK is the only key material stored on your filesystem (`.passman/.security/passman.key`).

### How Unlocking Works

1.  **Authentication:** The user enters the Master Password.
2.  **KEK Generation:** The KEK is derived instantly from the Master Password and Salt.
3.  **PEK Decryption:** The KEK is used to decrypt the stored, locked PEK file.
4.  **Vault Access:** The now-unlocked PEK is temporarily used to open the `sqlcipher3` database connection.
5.  **Session:** For convenience, the unlocked PEK is stored in a time-limited session file (`.passman/.security/passman.session`). If the session expires, steps 1-4 must be repeated, requiring the Master Password again.

This layered architecture ensures that even if an attacker compromises your system and gains access to the database
file and the encrypted key file, the data remains protected without the knowledge of your Master Password.

## Support

* If you encounter any bugs or problems then please raise a ticket in the Issues tab with the `bug` label.
* If you would like to propose any changes then you can also raise a ticket in the Issues tab with the `enhancement` label.
* If you have any other questions then feel free to reach out to the active maintainers!

## Roadmap

* Option to update configuration settings of the CLI (like colour scheme, session duration and password generator length).
* Shell autocompletion on tab for passman and its commands and arguments.
* Downloadable binary for passman, so it can be installed and added into the user's path, without having to install python, uv or git.

## Authors

* Ben Samarji (bensamarji5637@gmail.com) - active maintainer

## License

MIT License (see LICENSE.md)

## Project status

Active development