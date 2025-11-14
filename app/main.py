from fastapi import FastAPI, Query
from .utils import transform_function

app = FastAPI(description="API di un esercizio che prende una parola e la trasforma in maiuscolo inverso.")


@app.get("/maiuscola_inversa")
def maiuscola_inversa_endpoint(param: str = Query(..., description="Input your string here and receive the transformed output.")):
    
    ##########################################################################
    #     ENDPOINT CHE  TRASFORMA param E RESTITUISCE MAIUSCOLO INVERSO.     #
    ##########################################################################
    
    transformed = transform_function(param)
    return {"original": param ,"result": transformed}