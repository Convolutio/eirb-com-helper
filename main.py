from dotenv_vault import load_dotenv
load_dotenv()

from eirb_com_helper.server import app 

if __name__ == "__main__":
    app.run(debug=True)
