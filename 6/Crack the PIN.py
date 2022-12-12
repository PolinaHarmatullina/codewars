def crack(hash):
    import hashlib
    for x in range(99999):
        x=str(x)
        if len(x)==4:
            x="0"+x
        if len(x)==3:
            x="00"+x
        if len(x)==2:
            x="000"+x
        if len(x)==1:
            x="0000"+x
        if hash == hashlib.md5(x.encode()).hexdigest():
            return str(x)