#!/usr/bin/env python3
import sys
from cryptography.fernet import Fernet, InvalidToken


def main():
  print("=====================================================")
  print("       JACOBSON ESTATE MASTER ARCHIVE TERMINAL       ")
  print("=====================================================")
  print("Assemble and enter the reconstructed 44-character Fernet master key.")
  try:
    user_key = input("Enter Key: ").strip()
  except (KeyboardInterrupt, EOFError):
    sys.exit(0)

  try:
    cipher = Fernet(user_key.encode("utf-8"))
  except Exception:
    print(
        "\n[-] Error: Malformed Fernet key. Must be 44 characters ending in =."
    )
    sys.exit(1)

  try:
    with open("vault.enc", "rb") as f:
      enc = f.read()
  except FileNotFoundError:
    print("[-] Error: vault.enc not found in current directory.")
    sys.exit(1)

  try:
    dec = cipher.decrypt(enc)
    print("[+] Vault decrypted successfully!\n")
    print("------------------ VAULT CONTENTS ------------------")
    print(dec.decode("utf-8"))
    print("----------------------------------------------------")
  except InvalidToken:
    print("\n[-] Decryption Failed: Invalid Key.")
    sys.exit(1)


if __name__ == "__main__":
  main()