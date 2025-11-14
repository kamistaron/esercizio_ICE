def transform_function(data:str) -> str:

    ##########################################################################
    #         Una semplice funziona che trasforma la parola ricevuta.        #
    #         Mettendo un inout per esempio "ciaone" restituisce             #
    #         "ENOAIC" (maiuscolo inverso).                                  #
    ##########################################################################

    if not isinstance(data, str):
        raise ValueError("Wrong input type. Put a string as input")
    
    return data[::-1].upper()