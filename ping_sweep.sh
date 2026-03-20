#!/bin/bash
# ============================================================
# ping_sweep.sh — Network Host Discovery via Ping Sweep
# Author: Ozcan Celik | Networking Fundamentals Labs
# ============================================================

NETWORK=$1

if [ -z "$NETWORK" ]; then
  echo "[!] Usage: ./ping_sweep.sh <network_prefix>"
  echo "    Example: ./ping_sweep.sh 192.168.1"
  exit 1
fi

echo "============================================"
echo " PING SWEEP — $NETWORK.0/24"
echo " $(date)"
echo "============================================"
echo ""

LIVE_HOSTS=0

for i in $(seq 1 254); do
  IP="$NETWORK.$i"
  if ping -c 1 -W 1 "$IP" > /dev/null 2>&1; then
    echo "[+] HOST UP: $IP"
    LIVE_HOSTS=$((LIVE_HOSTS + 1))
  fi
done

echo ""
echo "============================================"
echo "[*] Sweep complete."
echo "[*] Live hosts found: $LIVE_HOSTS"
echo "============================================"
