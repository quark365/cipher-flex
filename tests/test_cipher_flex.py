# test_cipher_flex.py
import random

import pytest
from CipherFlex import CipherFlex 

def test_encrypt_decrypt():
    encryption = CipherFlex()
    key, encrypted_data = encryption.encrypt("password123")
    _, decrypted_data = encryption.decrypt(encrypted_data)
    assert decrypted_data == "password123"
