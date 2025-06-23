import zipfile
import itertools
import string
import time

# === Configuration ===
zip_path = r"C:\Users\robot\Downloads\zip_file_Name.zip"
max_length = 4  # You can increase this to 5 or more (but it will take much longer)

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
# === Characters to try (A-Z, a-z, 0-9), Punctuation/symbols (like !@#$%^&*()_+[]{}|;:'",.<>?/)===
charset = string.ascii_letters + string.digits + string.punctuation


# === Load ZIP file ===
zip_file = zipfile.ZipFile(zip_path)

start_time = time.time()
attempts = 0

for length in range(1, max_length + 1):
    for pwd_tuple in itertools.product(charset, repeat=length):
        pwd = ''.join(pwd_tuple)
        attempts += 1
        try:
            zip_file.extractall(pwd=bytes(pwd, 'utf-8'))
            elapsed = time.time() - start_time
            print(f"\n✅ Password found: {pwd}")
            print(f"🔢 Attempts: {attempts}")
            print(f"⏱️ Time elapsed: {elapsed:.2f} seconds")
            exit()
        except:
            print(f"❌ Tried: {pwd}", end='\r')

print("\n❌ Password not found.")
