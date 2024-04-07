# cipher-flex

cipher-flex is a Python package for medium-level encryption and decryption.

## Installation

You can install the package using pip:

```bash
pip install git+https://github.com/your-username/cipher-flex.git
```

## Usage

1. Import the `CipherFlex` class from the package:

```python
from cipher_flex import CipherFlex
```

2. Create an instance of `CipherFlex`:

```python
encryption = CipherFlex()
```

3. Encrypt data:

```python
key, encrypted_data = encryption.encrypt("your-password")
```

4. Decrypt data:

```python
key, decrypted_data = encryption.decrypt(encrypted_data)
```

Replace `"your-password"` with the actual data you want to encrypt.

## Example

Here's a complete example of using `CipherFlex` for encryption and decryption:

```python
from cipher_flex import CipherFlex

encryption = CipherFlex()
key, encrypted_data = encryption.encrypt("your-password")
print("Encrypted data:", encrypted_data)

key, decrypted_data = encryption.decrypt(encrypted_data)
print("Decrypted data:", decrypted_data)
```

Make sure to replace `"your-password"` with the actual data you want to encrypt.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
