import time
import sys

def type_effect(text, char_delay=0.05, line_delay=0.6):
    """Types out text letter-by-letter with custom speed and pauses."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    print() 
    time.sleep(line_delay) 


beats = [

    ("Tanging panalangin, lubayan na sana", 0.15, 1.4),
    ("Dahil sa bawat tingin, mukha mo'y nakikita", 0.20, 0.30),
    ("Kahit sa'n man mapunta ay anino mo'y kumakapit sa 'king kamay", 0.10, 1.0),
    ("Ako ay dahan-dahang nililibing nang buhay pa", 0.11, 2.0),
    
    
    ("Dinadalaw mo 'ko bawat gabi", 0.10, 1.0), 
    ("Wala mang nakikita", 0.12, 1.0),  
    ("Haplos mo'y ramdam pa rin sa dilim",0.09, 1.5),  
    
    
    ("Hindi na nananaginip", 0.10, 0.8),  
    ("Hindi na ma-makagising",0.11, 1.0), 
    ("Pasindi na ng ilaw",0.14, 1.5), 
    ("Minumulto na 'ko ng damdamin ko", 0.15, 1.15),  
    ("Ng damdamin ko",0.15, 2.5),  
    
    ("Hindi mo ba ako lilisanin?", 0.14, 0.8),  
    ("Hindi pa ba sapat pagpapahirap sa 'kin?",0.07, 1.0),  
    ("Hindi na ba ma-mamamayapa?", 0.11, 1.2), 
    ("Hindi na ba ma-mamamayapa?", 0.13, 2.0),

    ("Hindi na, makalaya", 0.40, 2.0), 
     
]

print("\n🎵 Starting track: Multo - Cup of Joe\n")
time.sleep(1)

for lyric, letter_speed, line_pause in beats:
    type_effect(lyric, char_delay=letter_speed, line_delay=line_pause)

print("\n🎵 Track ended.\n")