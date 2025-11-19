# ⚙️ Configuration

Keepr lets you configure password generator seetings, session timeout duration and the color scheme for the terminal output.

Logging in for the first time and setting your master password will generate a user configuration file.
To access your user configuration file, navigate to a hidden `.keepr` directory in your `home` directory. 

```bash
cd ~/.keepr
```

In the `.keepr` directory you'll find a `config.ini` file. 
Open the config.ini file in a text editor of your choice and change the values for the settings you want to change.

## 🎨 Color Options

There are 8 colors supported:

* `black`
* `red`
* `green`
* `yellow`
* `blue`
* `magenta`
* `cyan`
* `white`

## 🚦 Default configuration

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

## 📝 Notes

* If you delete or move your configuration file, logging in again will generate a new one with the default values.
* Be careful about adding more special characters to the `password_generator_special_chars` variable, as some special characters might not be supported by your terminal or python.