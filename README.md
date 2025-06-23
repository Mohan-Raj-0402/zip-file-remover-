# zip-file-remover

Brute-forcing a zip file password becomes very slow as you increase:

* the number of characters in charset

* the max_length

Even max_length=5 with len(charset)=94 can take billions of attempts:

* `94^5 ≈ 7.3 billion combinations`


inspired by:
https://github.com/shridarpatil/zip_password_cracker/tree/master

download this file link:⬇️
https://codeload.github.com/shridarpatil/zip_password_cracker/zip/refs/heads/master

## Installation
```bash
pip install pyzipper
