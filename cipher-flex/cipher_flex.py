import random

class CipherFlex:
    """
    CipherFlex - Python package for medium encryption and decryption.

    This module provides the CipherFlex class, which allows for medium-level encryption and decryption of data.

    Usage:
        from cipher_flex import CipherFlex

        # Create an instance of CipherFlex
        encryption = CipherFlex()

        # Encrypt data
        key, encrypted_data = encryption.encrypt("your-password")

        # Decrypt data
        key, decrypted_data = encryption.decrypt(encrypted_data)
    """
    def encrypt(self, psd):
        def randomize_list(original_list, seed_value):
            random.seed(seed_value)
            randomized_list = original_list[:]
            random.shuffle(randomized_list)
            return randomized_list

        a = [ord(i) for i in psd]
        k = int(input("Enter the order in [4,32]: "))
        qr = [i // k for i in a] + [i % k for i in a]
        l = random.randint(0, k - 1)
        qr = randomize_list(qr, l)
        n = max(len(bin(i).replace("0b", "")) for i in (l, k))
        key = (k << (n)) | l
        psd = bytes(qr)
        return key, psd

    def decrypt(self, psd):
        def retrieve_original_list(randomized_list, seed_value):
            random.seed(seed_value)
            indices = list(range(len(randomized_list)))
            random.shuffle(indices)
            original_list = [value for _, value in sorted(zip(indices, randomized_list))]
            return original_list

        qr = [byte for byte in psd]
        key = int(input("Enter Secret Key : "))
        m = len(bin(key).replace("0b", "")) // 2
        l = key & ((1 << m) - 1)
        qr = retrieve_original_list(qr, l)
        k = (key >> m) & ((1 << m) - 1)
        s = len(qr) // 2
        qr = [i for i in zip(qr[:s], qr[s:])]
        a = [chr(k * i[0] + i[1]) for i in qr]
        psd = ''.join(a)
        return key, psd
