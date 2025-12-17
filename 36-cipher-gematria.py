#!/usr/bin/env python3
"""
36-Cipher Gematria Calculator
Calculates gematria values across all 36 cipher systems.
Usage: python3 36-cipher-gematria.py "phrase to calculate"
       python3 36-cipher-gematria.py "phrase" -v "CIPHER NAME"  # verbose breakdown for specific cipher
       python3 36-cipher-gematria.py "phrase" -v                # verbose breakdown for all ciphers
"""

import sys

# Define all 36 cipher systems
CIPHERS = {
    'ENGLISH ORDINAL': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26},
    'REVERSE ORDINAL': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':10,'P':11,'O':12,'N':13,'M':14,'L':15,'K':16,'J':17,'I':18,'H':19,'G':20,'F':21,'E':22,'D':23,'C':24,'B':25,'A':26},
    'FULL REDUCTION': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,'S':1,'T':2,'U':3,'V':4,'W':5,'X':6,'Y':7,'Z':8},
    'REVERSE FULL REDUCTION': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':1,'P':2,'O':3,'N':4,'M':5,'L':6,'K':7,'J':8,'I':9,'H':1,'G':2,'F':3,'E':4,'D':5,'C':6,'B':7,'A':8},
    'SINGLE REDUCTION': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,'S':10,'T':2,'U':3,'V':4,'W':5,'X':6,'Y':7,'Z':8},
    'REVERSE SINGLE REDUCTION': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':1,'P':2,'O':3,'N':4,'M':5,'L':6,'K':7,'J':8,'I':9,'H':10,'G':2,'F':3,'E':4,'D':5,'C':6,'B':7,'A':8},
    'FULL REDUCTION KV': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':1,'K':11,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,'S':1,'T':2,'U':3,'V':22,'W':5,'X':6,'Y':7,'Z':8},
    'REVERSE FULL REDUCTION EP': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':1,'P':11,'O':3,'N':4,'M':5,'L':6,'K':7,'J':8,'I':9,'H':1,'G':2,'F':3,'E':22,'D':5,'C':6,'B':7,'A':8},
    'SINGLE REDUCTION KV': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':1,'K':11,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,'S':10,'T':2,'U':3,'V':22,'W':5,'X':6,'Y':7,'Z':8},
    'REVERSE SINGLE REDUCTION EP': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':1,'P':11,'O':3,'N':4,'M':5,'L':6,'K':7,'J':8,'I':9,'H':10,'G':2,'F':3,'E':22,'D':5,'C':6,'B':7,'A':8},
    'ENGLISH EXTENDED': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':20,'L':30,'M':40,'N':50,'O':60,'P':70,'Q':80,'R':90,'S':100,'T':200,'U':300,'V':400,'W':500,'X':600,'Y':700,'Z':800},
    'REVERSE EXTENDED': {'Z':1,'Y':2,'X':3,'W':4,'V':5,'U':6,'T':7,'S':8,'R':9,'Q':10,'P':20,'O':30,'N':40,'M':50,'L':60,'K':70,'J':80,'I':90,'H':100,'G':200,'F':300,'E':400,'D':500,'C':600,'B':700,'A':800},
    'FRANCIS BACON': {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52},
    'REVERSE FRANCIS BACON': {'z':1,'y':2,'x':3,'w':4,'v':5,'u':6,'t':7,'s':8,'r':9,'q':10,'p':11,'o':12,'n':13,'m':14,'l':15,'k':16,'j':17,'i':18,'h':19,'g':20,'f':21,'e':22,'d':23,'c':24,'b':25,'a':26,'Z':27,'Y':28,'X':29,'W':30,'V':31,'U':32,'T':33,'S':34,'R':35,'Q':36,'P':37,'O':38,'N':39,'M':40,'L':41,'K':42,'J':43,'I':44,'H':45,'G':46,'F':47,'E':48,'D':49,'C':50,'B':51,'A':52},
    'FRANC BACONIS': {'A':1,'a':2,'B':3,'b':4,'C':5,'c':6,'D':7,'d':8,'E':9,'e':10,'F':11,'f':12,'G':13,'g':14,'H':15,'h':16,'I':17,'i':18,'J':19,'j':20,'K':21,'k':22,'L':23,'l':24,'M':25,'m':26,'N':27,'n':28,'O':29,'o':30,'P':31,'p':32,'Q':33,'q':34,'R':35,'r':36,'S':37,'s':38,'T':39,'t':40,'U':41,'u':42,'V':43,'v':44,'W':45,'w':46,'X':47,'x':48,'Y':49,'y':50,'Z':51,'z':52},
    'REVERSE FRANC BACONIS': {'Z':1,'z':2,'Y':3,'y':4,'X':5,'x':6,'W':7,'w':8,'V':9,'v':10,'U':11,'u':12,'T':13,'t':14,'S':15,'s':16,'R':17,'r':18,'Q':19,'q':20,'P':21,'p':22,'O':23,'o':24,'N':25,'n':26,'M':27,'m':28,'L':29,'l':30,'K':31,'k':32,'J':33,'j':34,'I':35,'i':36,'H':37,'h':38,'G':39,'g':40,'F':41,'f':42,'E':43,'e':44,'D':45,'d':46,'C':47,'c':48,'B':49,'b':50,'A':51,'a':52},
    'PERFECTSQUARE': {'A':36,'B':37,'C':38,'D':39,'E':40,'F':41,'G':42,'H':43,'I':44,'J':45,'K':46,'L':47,'M':48,'N':49,'O':50,'P':51,'Q':52,'R':53,'S':54,'T':55,'U':56,'V':57,'W':58,'X':59,'Y':60,'Z':61},
    'REVERSE PERFECTSQUARE': {'Z':36,'Y':37,'X':38,'W':39,'V':40,'U':41,'T':42,'S':43,'R':44,'Q':45,'P':46,'O':47,'N':48,'M':49,'L':50,'K':51,'J':52,'I':53,'H':54,'G':55,'F':56,'E':57,'D':58,'C':59,'B':60,'A':61},
    'JEWISH REDUCTION': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'K':1,'L':2,'M':3,'N':4,'O':5,'P':6,'Q':7,'R':8,'S':9,'T':1,'U':2,'X':3,'Y':4,'Z':5,'J':6,'V':7,'&':8,'W':9},
    'JEWISH ORDINAL': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'X':21,'Y':22,'Z':23,'J':24,'V':25,'&':26,'W':27},
    'JEWISH': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'K':10,'L':20,'M':30,'N':40,'O':50,'P':60,'Q':70,'R':80,'S':90,'T':100,'U':200,'X':300,'Y':400,'Z':500,'J':600,'V':700,'&':800,'W':900},
    'ALW KABBALAH': {'A':1,'L':2,'W':3,'H':4,'S':5,'D':6,'O':7,'Z':8,'K':9,'V':10,'G':11,'R':12,'C':13,'N':14,'Y':15,'J':16,'U':17,'F':18,'Q':19,'B':20,'M':21,'X':22,'I':23,'T':24,'E':25,'P':26},
    'KFW KABBALAH': {'K':1,'F':2,'W':3,'R':4,'M':5,'D':6,'Y':7,'T':8,'A':9,'V':10,'Q':11,'H':12,'C':13,'X':14,'O':15,'J':16,'E':17,'L':18,'G':19,'B':20,'S':21,'N':22,'I':23,'Z':24,'U':25,'P':26},
    'LCH KABBALAH': {'I':0,'L':1,'C':2,'H':3,'P':4,'A':5,'X':6,'J':7,'W':8,'T':9,'O':10,'G':11,'F':12,'E':13,'R':14,'S':15,'Q':16,'K':17,'Y':18,'Z':19,'B':20,'M':21,'V':22,'D':23,'N':24,'U':25},
    'ENGLISH SUMERIAN': {'A':6,'B':12,'C':18,'D':24,'E':30,'F':36,'G':42,'H':48,'I':54,'J':60,'K':66,'L':72,'M':78,'N':84,'O':90,'P':96,'Q':102,'R':108,'S':114,'T':120,'U':126,'V':132,'W':138,'X':144,'Y':150,'Z':156},
    'REVERSE ENGLISH SUMERIAN': {'Z':6,'Y':12,'X':18,'W':24,'V':30,'U':36,'T':42,'S':48,'R':54,'Q':60,'P':66,'O':72,'N':78,'M':84,'L':90,'K':96,'J':102,'I':108,'H':114,'G':120,'F':126,'E':132,'D':138,'C':144,'B':150,'A':156},
    'PRIMES': {'A':2,'B':3,'C':5,'D':7,'E':11,'F':13,'G':17,'H':19,'I':23,'J':29,'K':31,'L':37,'M':41,'N':43,'O':47,'P':53,'Q':59,'R':61,'S':67,'T':71,'U':73,'V':79,'W':83,'X':89,'Y':97,'Z':101},
    'REVERSE PRIMES': {'Z':2,'Y':3,'X':5,'W':7,'V':11,'U':13,'T':17,'S':19,'R':23,'Q':29,'P':31,'O':37,'N':41,'M':43,'L':47,'K':53,'J':59,'I':61,'H':67,'G':71,'F':73,'E':79,'D':83,'C':89,'B':97,'A':101},
    'TRIGONAL': {'A':1,'B':3,'C':6,'D':10,'E':15,'F':21,'G':28,'H':36,'I':45,'J':55,'K':66,'L':78,'M':91,'N':105,'O':120,'P':136,'Q':153,'R':171,'S':190,'T':210,'U':231,'V':253,'W':276,'X':300,'Y':325,'Z':351},
    'REVERSE TRIGONAL': {'Z':1,'Y':3,'X':6,'W':10,'V':15,'U':21,'T':28,'S':36,'R':45,'Q':55,'P':66,'O':78,'N':91,'M':105,'L':120,'K':136,'J':153,'I':171,'H':190,'G':210,'F':231,'E':253,'D':276,'C':300,'B':325,'A':351},
    'SQUARES': {'A':1,'B':4,'C':9,'D':16,'E':25,'F':36,'G':49,'H':64,'I':81,'J':100,'K':121,'L':144,'M':169,'N':196,'O':225,'P':256,'Q':289,'R':324,'S':361,'T':400,'U':441,'V':484,'W':529,'X':576,'Y':625,'Z':676},
    'REVERSE SQUARES': {'Z':1,'Y':4,'X':9,'W':16,'V':25,'U':36,'T':49,'S':64,'R':81,'Q':100,'P':121,'O':144,'N':169,'M':196,'L':225,'K':256,'J':289,'I':324,'H':361,'G':400,'F':441,'E':484,'D':529,'C':576,'B':625,'A':676},
    'SEPTENARY': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':6,'I':5,'J':4,'K':3,'L':2,'M':1,'N':1,'O':2,'P':3,'Q':4,'R':5,'S':6,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1},
    'CHALDEAN': {'A':1,'B':2,'C':3,'D':4,'E':5,'F':8,'G':3,'H':5,'I':1,'J':1,'K':2,'L':3,'M':4,'N':5,'O':7,'P':8,'Q':1,'R':2,'S':3,'T':4,'U':6,'V':6,'W':6,'X':5,'Y':1,'Z':7},
    'KEYPAD': {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M':6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9},
    'FIBONACCI': {'A':1,'B':1,'C':2,'D':3,'E':5,'F':8,'G':13,'H':21,'I':34,'J':55,'K':89,'L':144,'M':233,'N':233,'O':144,'P':89,'Q':55,'R':34,'S':21,'T':13,'U':8,'V':5,'W':3,'X':2,'Y':1,'Z':1}
}

def get_char_value(char, cipher_dict):
    """Get the value of a character in a cipher."""
    if char == ' ':
        return None
    elif char.isdigit():
        return int(char)
    elif char in cipher_dict:
        return cipher_dict[char]
    elif char.upper() in cipher_dict:
        return cipher_dict[char.upper()]
    return None

def calculate_gematria(phrase):
    """Calculate gematria for a phrase across all 36 ciphers."""
    results = {}
    
    for cipher_name, cipher_dict in CIPHERS.items():
        total = 0
        for char in phrase:
            val = get_char_value(char, cipher_dict)
            if val is not None:
                total += val
        results[cipher_name] = total
    
    return results

def verbose_breakdown(phrase, cipher_name):
    """Show letter-by-letter breakdown for a specific cipher."""
    cipher_name_upper = cipher_name.upper()
    
    if cipher_name_upper not in CIPHERS:
        print(f"Unknown cipher: {cipher_name}")
        print(f"Available ciphers: {', '.join(CIPHERS.keys())}")
        return
    
    cipher_dict = CIPHERS[cipher_name_upper]
    
    # Remove punctuation for word splitting but keep original for display
    import re
    words = re.split(r'\s+', phrase)
    
    print(f"\n=== {cipher_name_upper} BREAKDOWN ===\n")
    
    grand_total = 0
    
    for word in words:
        if not word:
            continue
        word_total = 0
        breakdown = []
        
        for char in word:
            val = get_char_value(char, cipher_dict)
            if val is not None:
                # Display character (preserve case for case-sensitive ciphers)
                display_char = char if char in cipher_dict else char.upper()
                breakdown.append(f"{display_char}={val}")
                word_total += val
        
        if breakdown:
            print(f"{word}: {' + '.join(breakdown)} = {word_total}")
            grand_total += word_total
    
    print(f"\n{'='*40}")
    print(f"TOTAL: {grand_total}")
    print(f"{'='*40}\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 36-cipher-gematria.py \"phrase to calculate\"")
        print("       python3 36-cipher-gematria.py \"phrase\" -c \"CIPHER NAME\"  # specific cipher(s)")
        print("       python3 36-cipher-gematria.py \"phrase\" -v \"CIPHER NAME\"  # verbose breakdown")
        print("       python3 36-cipher-gematria.py \"phrase\" -v                 # verbose all ciphers")
        sys.exit(1)
    
    # Check for flags
    verbose = False
    verbose_cipher = None
    selected_ciphers = []
    args = sys.argv[1:]
    
    # Check for cipher selection flag
    if '-c' in args or '--cipher' in args:
        flag_idx = args.index('-c') if '-c' in args else args.index('--cipher')
        
        # Collect all cipher names following the flag
        cipher_start = flag_idx + 1
        cipher_end = cipher_start
        while cipher_end < len(args) and not args[cipher_end].startswith('-'):
            selected_ciphers.append(args[cipher_end].upper())
            cipher_end += 1
        
        args = args[:flag_idx] + args[cipher_end:]
    
    # Check for verbose flag
    if '-v' in args or '--verbose' in args:
        verbose = True
        flag_idx = args.index('-v') if '-v' in args else args.index('--verbose')
        
        # Check if a cipher name follows the flag
        if flag_idx + 1 < len(args) and not args[flag_idx + 1].startswith('-'):
            verbose_cipher = args[flag_idx + 1]
            args = args[:flag_idx] + args[flag_idx + 2:]
        else:
            args = args[:flag_idx] + args[flag_idx + 1:]
    
    phrase = ' '.join(args)
    
    if verbose:
        if verbose_cipher:
            # Show breakdown for specific cipher
            verbose_breakdown(phrase, verbose_cipher)
        else:
            # Show breakdown for all ciphers
            for cipher_name in CIPHERS.keys():
                verbose_breakdown(phrase, cipher_name)
    elif selected_ciphers:
        # Output only selected ciphers
        results = calculate_gematria(phrase)
        for cipher_name in selected_ciphers:
            if cipher_name in results:
                print(f"{cipher_name}: {results[cipher_name]}")
            else:
                print(f"Unknown cipher: {cipher_name}")
                print(f"Available ciphers: {', '.join(CIPHERS.keys())}")
    else:
        # Standard output - all ciphers
        results = calculate_gematria(phrase)
        for cipher, value in results.items():
            print(f"{cipher}: {value}")

if __name__ == "__main__":
    main()
