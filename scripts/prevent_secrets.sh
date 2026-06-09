#!/bin/bash
# SecureSphere Git Pre-Commit Hook
if git diff --cached | grep -iE "(password|secret|token|api_key)[ =]*['\"][a-zA-Z0-9_-]{10,}['\"]"; then
    echo "[!] HATA: Commit içinde gömülü şifre (hardcoded secret) tespit edildi! Lütfen .env kullanın."
    exit 1
fi
exit 0
