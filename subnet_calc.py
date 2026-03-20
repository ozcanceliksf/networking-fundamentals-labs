#!/usr/bin/env python3
# ============================================================
# subnet_calc.py — Subnet Calculator
# Author: Ozcan Celik | Networking Fundamentals Labs
# ============================================================

import ipaddress
import sys

def calculate_subnet(cidr):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
        print("=" * 50)
        print(f" SUBNET CALCULATOR — {cidr}")
        print("=" * 50)
        print(f"  Network Address  : {network.network_address}")
        print(f"  Broadcast        : {network.broadcast_address}")
        print(f"  Subnet Mask      : {network.netmask}")
        print(f"  Wildcard Mask    : {network.hostmask}")
        print(f"  CIDR Notation    : /{network.prefixlen}")
        print(f"  Usable Hosts     : {network.num_addresses - 2}")
        print(f"  First Host       : {list(network.hosts())[0]}")
        print(f"  Last Host        : {list(network.hosts())[-1]}")
        print(f"  IP Class         : {'A' if network.prefixlen <= 8 else 'B' if network.prefixlen <= 16 else 'C'}")
        print(f"  Is Private       : {network.is_private}")
        print("=" * 50)
    except ValueError as e:
        print(f"[!] Invalid input: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print("[!] Usage: python3 subnet_calc.py <CIDR>")
        print("    Example: python3 subnet_calc.py 192.168.1.0/24")
        sys.exit(1)

    calculate_subnet(sys.argv[1])

if __name__ == "__main__":
    main()
