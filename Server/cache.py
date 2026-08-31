#Server/cache.py

cache: dict[tuple[int, int], dict] = {} 

#simple in-memory cache
#key is day and version tuple
# value is Json output dict
