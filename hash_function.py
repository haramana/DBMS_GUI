import hashlib
def pass_to_hash(password):

    h= hashlib.new("SHA256") #scelgo l'algorimto da utulizzare per hashing
    pass_iniziale=password
    h.update(pass_iniziale.encode())
    pass_hash= h.hexdigest()
    return pass_hash
