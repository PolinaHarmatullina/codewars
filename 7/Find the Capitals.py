def capital(capitals): 
    return [f"The capital of " + (cptls['state'] if 'state' in cptls else cptls['country']) + f" is {cptls['capital']}" for cptls in capitals]