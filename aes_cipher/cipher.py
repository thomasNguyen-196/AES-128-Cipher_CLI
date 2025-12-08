"""
AES-128 cipher logic placeholder.
Implement encrypt/decrypt (ECB/CFB) here.
"""

from typing import Optional, Tuple


def encrypt(plaintext: str, key: str, mode: str = "ecb", iv: Optional[str] = None) -> Tuple[str, Optional[str]]:
    """
    Encrypt plaintext with AES-128.
    TODO: implement actual AES-128 encryption. Should return (cipher_hex, iv_hex).
    """
    raise NotImplementedError("AES-128 encrypt not implemented yet.")


def decrypt(ciphertext: str, key: str, mode: str = "ecb", iv: Optional[str] = None) -> str:
    """
    Decrypt ciphertext with AES-128.
    TODO: implement actual AES-128 decryption.
    """
    raise NotImplementedError("AES-128 decrypt not implemented yet.")
