from os import getenv
from dotenv_vault import load_dotenv
load_dotenv()

from eirb_com_helper.server import app 

HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", 5000))
IS_DEBUG = getenv("MODE", "PRODUCTION") == "DEBUG"

if __name__ == "__main__":
    app.run(debug=IS_DEBUG, host=HOST, port=PORT)
