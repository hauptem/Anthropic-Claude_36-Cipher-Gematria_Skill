---
name: 36-Cipher-Gematria
description: Calculate gematria values across 36 cipher systems
---

# Usage
Run the pre-built script:
```bash
# Standard output (all ciphers)
python3 /mnt/skills/user/36-cipher-gematria/36-cipher-gematria.py "phrase to calculate"

# Verbose breakdown for specific cipher
python3 /mnt/skills/user/36-cipher-gematria/36-cipher-gematria.py "phrase" -v "CIPHER NAME"

# Verbose breakdown for all ciphers
python3 /mnt/skills/user/36-cipher-gematria/36-cipher-gematria.py "phrase" -v
```

# Rules
- NEVER use memorized values. ALWAYS calculate fresh.
- Numbers: each digit sums individually (16 = 1+6 = 7)
