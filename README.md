ICE Technical Exercise – Kamran Dehghan



##########################################################################
#                        #     Overview     #                            #
##########################################################################
    

This project is a simple REST API built with FastAPI.
The API exposes a single endpoint /maiuscola_inversa which calls an internal library function to apply a transformation to the input string.

##########################################################################
#                       #    Setup & Run    #                            #
##########################################################################

-Clone repository

git clone 
cd ice_exercise


-Create virtual environment

python3 -m venv venv
source venv/bin/activate


-Install dependencies

pip install -r requirements.txt


-Run the API

uvicorn app.main:app --reload


-Test the API
Open your browser or Postman and visit:
👉 http://127.0.0.1:8000/transform?input=hello

##########################################################################
#                      #   Example Response   #                          #
##########################################################################
{
  "original": "hello",
  "transformed": "OLLEH"
}
