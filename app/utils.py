def transform_function(data:str) -> str:

    ##########################################################################
    #         Una semplice funziona che trasforma la parola ricevuta.        #
    #         Mettendo un inout per esempio "ciaone" restituisce             #
    #         "ENOAIC" (maiuscolo inverso).                                  #
    ##########################################################################

    if not data.isalpha():
        raise ValueError("Input must contain only alphabetic characters.")
    
    
    
    return data[::-1].upper()