# 📦 Installation

You can install Keepr either via **PyPI (recommended)** or as a **standalone binary** if you can’t install Python.

---

## 🐍 Option 1: Install from PyPI (Recommended)

Keepr supports **macOS**, **Linux**, and **Windows**.

```bash
pip install keepr
```

Once installed, verify your installation:

```bash
keepr --help
```

## 💻 Option 2: Download a Prebuilt Binary

If you prefer not to install Python, Keepr provides precompiled binaries built with PyInstaller, which bundle Python and all dependencies.

👉 Download the latest binary for your OS from the [GitHub Releases page](https://github.com/bsamarji/Keepr/releases).

### Steps

1. Download the correct archive for your OS.
2. Extract the contents to a permanent folder (e.g. `~/tools/keepr` on macOS/Linux, or `C:\Tools\Keepr` on Windows).
3. Add that folder to your system’s PATH so keepr can be run from anywhere.

### 🍎 macOS & 🐧 Linux Shell Setup

On macOS and Linux, you'll update your shell's configuration file (usually `.zshrc` or `.bashrc`).

1.  **Move the Directory:** Move the extracted `keepr` folder (containing the executable) to a clean, permanent location, like a new `tools` directory in your home folder:

        # Example: Move the extracted 'keepr' folder into a 'tools' directory
        mv /path/to/downloaded/keepr ~/tools/

2.  **Edit Shell Configuration:** Open the configuration file for your shell (`.zshrc` for modern macOS, `.bashrc` for most Linux systems) using a text editor like `vim`:

        # For modern macOS (Zsh):
        vim ~/.zshrc

        # For most Linux systems (Bash):
        vim ~/.bashrc

3.  **Add to PATH:** Add the following line to the **very end** of the file, replacing the path with your chosen directory:

        export PATH="$HOME/tools/keepr:$PATH"

4.  **Apply Changes:** Save the file and apply the new configuration by running:

        source ~/.zshrc  # or source ~/.bashrc

5.  **Verify:** Open a **new terminal window** and run `keepr --help`.

---

### 🪟 Windows PowerShell Setup

On Windows, you need to update your systems environment variables. This can be done through the GUI, but below I've posted instructions for doing this through the command line.
Please ensure you're running Powershell in **Administrator Mode**.

1. Ensure you have moved the extracted `keepr` folder to a permanent, simple location, for example: `C:\Tools\Keepr`.

2. **Define the Path:** Open a new **Windows Terminal** window running PowerShell. First, set the path to your `keepr` folder as a variable for easier use.

        # Set the variable to the exact path where the 'keepr' executable is located
        $KeeprPath = "C:\Tools\Keepr"

3. **Add the Path Permanently:** Use the built-in .NET class method to append the new directory to your User-level PATH variable. The third argument "User" ensures the change is permanent.

        [System.Environment]::SetEnvironmentVariable(
        "Path",
        "$env:Path;$KeeprPath",
        "User"
        )

4. **Exclude the Dir From Windows Defender:** Windows defender massively hampers performance of this executable as it scans the directory everytime which can take minutes. To avoid this, please exclude it from defender scans:

        Add-MpPreference -ExclusionPath $KeeprPath
   
5. **Verify:** **Close and reopen** any active Command Prompt or PowerShell windows, and then run `keepr --help`.

## 🐾 Next Steps

Check out our user guides for: 

* [**Getting started**](user_guides/getting_started.md) 
* [**Configuration**](user_guides/configuration.md)