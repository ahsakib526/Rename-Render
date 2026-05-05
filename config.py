# Don't Remove Credit @AHSakib1
# Subscribe Telegram Channel For Amazing Bot @SakibMovieCollection
# Ask Doubt on telegram @AHSakib1


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "1701363")

API_HASH = os.environ.get("API_HASH", "df8beceb7a16ccc6d128522b30845a20")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7967050798:AAHh_MTm8J0eh3k-eLGSl3qK1NW-AIiQu8E") 

FORCE_SUB = os.environ.get("FORCE_SUB", "AHSakib1") 

             # Don't Remove Credit @AHSakib1
             # Subscribe Telegram Channel For Amazing Bot @SakibMovieCollection
             # Ask Doubt on telegram @AHSakib1

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ahsakib526_db_user:juGP2xl00Xn5poJW@cluster0.3ljksgg.mongodb.net/?appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @AHSakib1
# Subscribe Telegram Channel For Amazing Bot @SakibMovieCollection
# Ask Doubt on telegram @AHSakib1
