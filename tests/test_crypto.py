import unittest
from ix_ghostprotocol.crypto import (
    generate_keypair,
    encrypt_message,
    decrypt_message,
    sign_message,
    verify_signature,
)

class TestCryptoFunctions(unittest.TestCase):

    def setUp(self):
        self.public_key, self.private_key = generate_keypair()
        self.message = b"Test message for crypto functions."

    def test_encrypt_decrypt(self):
        ciphertext = encrypt_message(self.public_key, self.message)
        plaintext = decrypt_message(self.private_key, ciphertext)
        self.assertEqual(plaintext, self.message)

    def test_sign_verify(self):
        signature = sign_message(self.private_key, self.message)
        verified = verify_signature(self.public_key, self.message, signature)
        self.assertTrue(verified)

    def test_invalid_signature(self):
        signature = sign_message(self.private_key, self.message)
        tampered_message = b"Tampered message"
        verified = verify_signature(self.public_key, tampered_message, signature)
        self.assertFalse(verified)

if __name__ == "__main__":
    unittest.main()
