python query.py localhost:46257 put a/b=10
python query.py localhost:46257 put "a/c=get(a/b)"
python query.py localhost:46257 put "a/d=increment(a/c)"
python query.py localhost:46257 put "a/d=increment(a/c)###again"
python query.py localhost:46257 put "a/e=sum(a/c,a/d)"
python query.py localhost:46257 put "a/f=factorial(a/b)"
python query.py localhost:46257 put "c/asum=hiersum(a)"
python query.py localhost:46257 get a/e
python query.py localhost:46257 put "0-200:b/@1/@0=1"
python query.py localhost:46257 put "c/bsum=hiersum(b)"
