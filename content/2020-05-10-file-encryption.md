---
layout: post
title: File Encryption
slug: file-encryption
author: Martin Thoma
date: 2020-05-10 20:00
category: Code
tags: Python, Security, file-encryption
featured_image: logos/python.png
---
I recently wondered how difficult it is to encrypt a file. In this article I
will show you two ways to do it. I use a text file `content.txt` with the
content

```text
This is a top secret message!
Don't show it to others!
```

## Applications

> [GNU Privacy Guard](https://en.wikipedia.org/wiki/GNU_Privacy_Guard) (GnuPG
> or GPG) is a free-software replacement for Symantec's PGP cryptographic
> software suite, and is compliant with RFC 4880, the IETF standards-track
> specification of OpenPGP.

Check with `gpg --list-secret-keys` if you already have keys. If not, run

```bash
gpg –-gen-key
```

Encrypt file:

```bash
gpg -e -r info@martin-thoma.de content.txt
```

Decrypt file:

```bash
gpg -d -o out.decrypted.txt content.txt.gpg
```

## Python

In order to generate an encrypted file with Python, I use the [fernet](https://cryptography.io/en/latest/fernet/) module of [cryptography](https://pypi.org/project/cryptography/).
It's not part of the standard library ([source](https://docs.python.org/3/library/crypto.html)), but
it is super wide spread.

It uses AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding. Initialization vectors are generated using os.urandom().


```python
from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
with open("keyfile", "wb") as fp:
    fp.write(key)

# Get bytes to encrypt
message = "This is secret!"
encoded = message.encode()

# Encrypt the bytes
fernet = Fernet(key)
encrypted = fernet.encrypt(encoded)

# Write encrypted file
with open("encrypted-file", "wb") as fp:
    fp.write(encrypted)

# Decrypt the bytes
fernet = Fernet(key)
decrypted = fernet.decrypt(encrypted)
print(decrypted.decode())
```

You can also generate the key from a password like this:

```python
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = "something I can remember"

# Set this in the application as a constant
# Generate one for yourself with
# >>> import os; os.urandom(16)
salt = b"\xd8\x85\xd3`|\xa2\x82w\x11!\xcc\x8d\xa4\x8a:\xb4"

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100_000,
    backend=default_backend(),
)
key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
```


## Attacker Scenarios

### Lost Device

Alice was sitting in a taxi, using her laptop and her phone at the same time.
She just quickly put her laptop next to her and had a look at her phone.
Thinking about the flight she needed to catch, she forgot the laptop. The
taxidriver sold the laptop on ebay and Bob bought it. He wants to see if there
is valuable information on it and tries to get access.

**Asessment**: To protect agains this, Alice should use full disk encryption
(FDE). If Alice doesn't have FDE, encrypting a single file might help for that
single file. But as it only protects one file, it's certainly worse than FDE.

### Root Access

Alice catched a virus! No, not COVID-19, but one on her computer. Bob now has
remote access to her machine.

**Asessment**: In this case, I would say all hope is lost. The attacker can
install a keylogger and will get the result he wants. Or a crypto trojan which
prevents Alice from using her computer. Encrypting a single file might help if
Alice doesn't access that file while the attacker has control. FDE would not
help here at all.

### User Access

Bob has access to the computer of Alice, but just normal user permissions. He
cannot install new software. He can just run installed software under the
account of Alice.

**Asessment**: Encrypting a single file helps as long as Alice doesn't access
the file.


### Man in the Middle: E-Mail

Alice sends data to Charlie. Bob

Bob is here the [Man in the Middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)
and makes a Man in the Middle (MitM) attack.


## See also

* PyTutorials: [How to Encrypt Strings and Files in Python](https://www.youtube.com/watch?v=H8t4DJ3Tdrg), 2018.
* Isuru Perera: [Encrypting disks on Ubuntu 19.04](https://medium.com/@chrishantha/encrypting-disks-on-ubuntu-19-04-b50bfc65182a) on Medium, 2019.
* Wikipedia:
    * [List of cryptographic file systems](https://en.wikipedia.org/wiki/List_of_cryptographic_file_systems)
* StackExchange:
    * [Defence Against Keyboard Keylogger](https://security.stackexchange.com/q/44268/3286)
    * [Full disk encryption vs targetted partition encryption for security experts?](https://security.stackexchange.com/q/197131/3286)
    * [What is the attack scenario against which encrypted files provide protection?](https://security.stackexchange.com/q/231408/3286)
