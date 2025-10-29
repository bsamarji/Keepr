import base64
import os
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from .config import DB_DIR_NAME, SECURITY_DIR_NAME, SALT_FILE_NAME, PEK_FILE_NAME
from .config import (COLOR_SENSITIVE_DATA, COLOR_PRIMARY_DATA, COLOR_WARNING, COLOR_ERROR,
                     COLOR_HEADER, COLOR_PROMPT_BOLD, COLOR_PROMPT_LIGHT, COLOR_SUCCESS)
import click

def initialise_security_dir():
    """
    Initialise the security directory.
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    Path.mkdir(security_dir, parents=True, exist_ok=True)

def generate_salt_file():
    """
    Generate a random salt and write it to a file, if a salt file doesn't exist.
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    salt_file = security_dir / SALT_FILE_NAME
    if not salt_file.exists():
        salt = os.urandom(16)
        with open(salt_file, "wb") as f:
            f.write(salt)

def retrieve_salt():
    """
    Retrieve the salt from the salt file.

    Returns:
         The salt.
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    salt_file = security_dir / SALT_FILE_NAME
    with open(salt_file, "rb") as f:
        salt = f.read()
    return salt

def key_derivation_function(salt):
    """
    Define a key derivation function that uses the salt from the salt file.

    Args:
        salt (bytes): The salt from the salt file

    Returns:
        The key derivation function
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1_200_000,
    )
    return kdf

def login():
    """
    Login to the password manager.

    Returns:
         The master password
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    pek_file = security_dir / PEK_FILE_NAME

    if not pek_file.exists():
        click.secho("Welcome to PassMan!", **COLOR_WARNING)
        master_password = click.prompt(
            click.style("Please create your master password", **COLOR_PROMPT_BOLD),
            hide_input=True,
            confirmation_prompt=True,
        )
        return master_password
    else:
        master_password = click.prompt(
            click.style("Please enter your master password", **COLOR_PROMPT_BOLD),
            hide_input=True,
            confirmation_prompt=True,
        )
        return master_password

def generate_derived_key(kdf, master_password):
    """
    Create derived key using the given kdf and master password.

    Args:
        kdf: The key derivation function to use
        master_password: The master password to use

    Returns:
        The derived key
    """
    key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
    return key


def generate_and_encrypt_pek(derived_key):
    """
    Generates a 32-byte Primary Encryption Key (PEK) and locks it
    by encrypting it with the derived_key (KEK) using Fernet.
    Stores the encrypted PEK to disk.

    Args:
        derived_key (bytes): The 44-byte base64url-encoded key from the KDF.

    Returns:
        The decrypted PEK (bytes)
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    pek_file = security_dir / PEK_FILE_NAME

    f = Fernet(derived_key)

    pek = os.urandom(32)
    encrypted_pek = f.encrypt(pek)
    with open(pek_file, "wb") as file:
        file.write(encrypted_pek)
    return pek


def retrieve_and_decrypt_pek(derived_key):
    """
    Retrieve the PEK and decrypt it using Fernet.

    Args:
        The derived key (KEK) to use

    Returns:
        The decrypted primary encryption key (PEK)
    """
    home_dir = Path.home()
    security_dir = home_dir / DB_DIR_NAME / SECURITY_DIR_NAME
    pek_file = security_dir / PEK_FILE_NAME

    with open(pek_file, "rb") as file:
        encrypted_pek = file.read()

    f = Fernet(derived_key)

    try:
        pek = f.decrypt(encrypted_pek)
        return pek
    except Exception:
        click.secho("The master password is incorrect. Please try again.", **COLOR_ERROR)