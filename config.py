"""
This module contains configuration settings for the Money Manager application.

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>

"""

import os

MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://mmdb_admin:tiaNSKxzyO2NdXts@moneymanagerdb.s2bp9.mongodb.net/"
    "?retryWrites=true&w=majority&appName=MoneyManagerDB",
)

TOKEN_SECRET_KEY = "your_secret_key"
TOKEN_ALGORITHM = "HS256"

API_BIND_HOST = "0.0.0.0"
API_BIND_PORT = 9999

TELEGRAM_BOT_TOKEN = "7601886777:AAEqIw5gVUPBuDqVeWwR1GdG_Y8eiA0JKFA"
TELEGRAM_BOT_API_BASE_URL = "http://localhost:9999"
