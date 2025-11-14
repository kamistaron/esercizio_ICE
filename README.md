ICE Technical Exercise – Kamran Dehghan




#                             Overview                                 #

    

This project is a simple REST API built with FastAPI.
The API exposes a single endpoint /maiuscola_inversa which calls an internal library function to apply a transformation to the input string.


#                           Setup & Run                               #

    1. Clone repository

        git clone https://github.com/kamistaron/esercizio_ICE.git
        cd esercizio_ICE


    2. Create virtual environment

        python3 -m venv ICEvenv
        source ICEvenv/bin/activate


    3. Install dependencies

        pip install -r requirements.txt


    4. Run the API

        uvicorn app.main:app --reload


    5. Test the API
        Open your browser and visit:
        http://127.0.0.1:8000/maiuscola_inversa?param=hello
        or equally
        http://localhost:8000/maiuscola_inversa?param=hello

    Surely you could try the API with other words as well


#                         Example Response                             #


A JSON that looks like this:

{
  "original": "hello",
  "result": "OLLEH"
}
