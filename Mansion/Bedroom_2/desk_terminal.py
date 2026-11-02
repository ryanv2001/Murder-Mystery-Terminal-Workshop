#!/usr/bin/env python3
import sys

def main():
    print("========================================")
    print("      BEDROOM 2 - SECONDARY TERMINAL    ")
    print("========================================")
    print("Authentication Required.")
    print("Enter the Balcony Emergency Override code (HHMMSS format):")

    try:
        user_input = input(">> ").strip()
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

    if user_input == "234105":
        print("\n[+] Authentication Granted.")
        print("[+] Decryption Key Fragment Recovered:")
        print("    KEY_PART_2: 6pK4g1dHMres6Aa3wjjHk=")
    else:
        print("\n[-] Invalid Override Code. Access Denied.")

if __name__ == '__main__':
    main()