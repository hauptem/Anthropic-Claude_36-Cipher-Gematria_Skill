![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Claude](https://img.shields.io/badge/Claude-Skill-orange)

# 36-Cipher Gematria - Claude Skill

A skill for Anthropic's Claude that enables gematria calculations across 36 different cipher systems directly within Claude conversations as a prebuilt skill.

## What This Skill Does

This skill extends Claude's capabilities by providing instant gematria calculations for any phrase across 36 cipher systems. 
- Calculate gematria values on demand during conversation
- Show detailed letter-by-letter breakdowns for any cipher

## Supported Ciphers (36 Total)

**Standard English**
- English Ordinal, Reverse Ordinal
- Full Reduction, Reverse Full Reduction
- Single Reduction, Reverse Single Reduction
- English Extended, Reverse Extended
- English Sumerian, Reverse English Sumerian

**Reduction Variants**
- Full Reduction KV, Reverse Full Reduction EP
- Single Reduction KV, Reverse Single Reduction EP

**Bacon Ciphers**
- Francis Bacon, Reverse Francis Bacon
- Franc Baconis, Reverse Franc Baconis

**Square-Based**
- Perfectsquare, Reverse Perfectsquare
- Squares, Reverse Squares

**Jewish/Hebrew**
- Jewish, Jewish Ordinal, Jewish Reduction

**Kabbalah**
- ALW Kabbalah, KFW Kabbalah, LCH Kabbalah

**Prime & Triangular**
- Primes, Reverse Primes
- Trigonal, Reverse Trigonal

**Traditional Systems**
- Septenary, Chaldean, Keypad, Fibonacci

## Installing as a Claude Skill

1. Download both files: `SKILL.md` and `36-cipher-gematria.py`
2. Create a zip file containing both files (or use the pre-zipped file):
   ```bash
   zip 36-cipher-gematria.zip SKILL.md 36-cipher-gematria.py
   ```
3. Go to [claude.ai](https://claude.ai) → Settings → Skills
4. Click "Create Skill" or "Upload Skill"
5. Upload the `36-cipher-gematria.zip` file
6. Enable the skill in your conversation

## How to Use with Claude

Simply ask Claude to calculate gematria values:

<img width="936" height="964" alt="Image" src="https://github.com/user-attachments/assets/296e4a22-dcf8-4865-a63a-737fe0cf66d6" />

Claude will automatically use this skill when you ask for gematria calculations.

---

## Standalone Python Calculator

Don't use Claude? You can use the Python script directly on your command line.

### Installation

```bash
# Download the script
wget https://raw.githubusercontent.com/hauptem/Anthropic-Claude_36-Cipher-Gematria_Skill/main/36-cipher-gematria.py

# Make it executable (optional)
chmod +x 36-cipher-gematria.py
```

**Requirements:** Python 3.x (no additional packages needed)

### Usage

```bash
# Calculate all ciphers
python3 36-cipher-gematria.py "your phrase here"

# Verbose breakdown for specific cipher
python3 36-cipher-gematria.py "your phrase here" -v "english ordinal"

# Verbose breakdown for all ciphers
python3 36-cipher-gematria.py "your phrase here" -v
```

### Example Output

```bash
$ python3 36-cipher-gematria.py "This is gematria!" -v "english ordinal"

=== ENGLISH ORDINAL BREAKDOWN ===

This: T=20 + H=8 + I=9 + S=19 = 56
is: I=9 + S=19 = 28
gematria!: G=7 + E=5 + M=13 + A=1 + T=20 + R=18 + I=9 + A=1 = 74

========================================
TOTAL: 158
========================================
```

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Disclaimer

- This solution is **NOT** officially endorsed, supported, or maintained by Anthropic.
- Anthropic retains all rights to their trademarks, including but not limited to "Anthropic", "Claude", and related marks
- This is an independent, community-developed solution that utilizes Anthropic products but is not affiliated with Anthropic.
- For official Claude support and solutions, please contact Anthropic directly

**Technical Disclaimer**

- This software is provided "AS IS" without warranty of any kind
- The authors and contributors are not responsible for any damages or issues that may arise from its use

MIT License - feel free to use and modify as needed.
