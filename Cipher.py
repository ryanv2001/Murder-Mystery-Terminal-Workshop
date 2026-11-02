#!/usr/bin/env python3
"""Jacobson Manor Cryptographic Analysis Utility

Workshop CLI Tool for Terminal Operations & Cryptanalysis
"""

import argparse
import base64
import sys
from cryptography.fernet import Fernet, InvalidToken


def caesar(text: str, shift: int, decrypt: bool = False) -> str:
  if decrypt:
    shift = -shift
  output = []
  for char in text:
    if "a" <= char <= "z":
      base = ord("a")
      output.append(chr((ord(char) - base + shift) % 26 + base))
    elif "A" <= char <= "Z":
      base = ord("A")
      output.append(chr((ord(char) - base + shift) % 26 + base))
    else:
      output.append(char)
  return "".join(output)


def rot13(text: str) -> str:
  return caesar(text, 13)


def b64_decode(data: str) -> str:
  try:
    raw_bytes = base64.b64decode(data.strip())
    return raw_bytes.decode("utf-8", errors="replace")
  except Exception as e:
    return f"[-] Base64 decoding failed: {e}"


def decrypt_fernet(key_str: str, file_path: str) -> None:
  if not key_str:
    print("[-] Error: You must supply a Fernet key using --key")
    sys.exit(1)
  try:
    cipher = Fernet(key_str.encode("utf-8"))
  except Exception as e:
    print(f"[-] Invalid Fernet Key format: {e}")
    sys.exit(1)

  try:
    with open(file_path, "rb") as f:
      encrypted_data = f.read()
  except FileNotFoundError:
    print(f"[-] Error: Target file '{file_path}' not found.")
    sys.exit(1)

  try:
    decrypted = cipher.decrypt(encrypted_data)
    print("[+] Decryption Successful!\n")
    print(decrypted.decode("utf-8"))
  except InvalidToken:
    print("[-] Decryption failed: Invalid key or corrupted data.")
    sys.exit(1)


def main():
  parser = argparse.ArgumentParser(
      description="Jacobson Manor Cryptanalysis Tool"
  )
  parser.add_argument(
      "--mode",
      choices=["caesar", "rot13", "b64decode", "fernet"],
      required=True,
  )
  parser.add_argument(
      "--shift", type=int, default=3, help="Shift value for Caesar cipher"
  )
  parser.add_argument(
      "--decrypt", action="store_true", help="Flag to decrypt Caesar cipher"
  )
  parser.add_argument(
      "--key", type=str, help="Fernet key string for --mode fernet"
  )
  parser.add_argument("--text", type=str, help="Raw string to process")
  parser.add_argument("--file", type=str, help="Path to file to process")

  args = parser.parse_args()

  if args.mode == "fernet":
    decrypt_fernet(
        args.key, args.file if args.file else "Mansion/Attic/vault.enc"
    )
    return

  content = ""
  if args.text:
    content = args.text
  elif args.file:
    try:
      with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()
    except FileNotFoundError:
      print(f"[-] Error: File not found: {args.file}")
      sys.exit(1)
  else:
    print("[-] Error: Specify either --text or --file.")
    sys.exit(1)

  if args.mode == "rot13":
    print(rot13(content))
  elif args.mode == "caesar":
    print(caesar(content, args.shift, args.decrypt))
  elif args.mode == "b64decode":
    print(b64_decode(content))


if __name__ == "__main__":
  main()