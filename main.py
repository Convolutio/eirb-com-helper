from os import getenv
from dotenv_vault import load_dotenv
load_dotenv()

from eirb_com_helper.server import app 

HOST = getenv("HOST", "0.0.0.0")
PORT = int(getenv("PORT", 5000))

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
