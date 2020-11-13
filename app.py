from flask import Flask, request, Response

if __name__ == 'app':
    from cache_test import cache
else:
    cache = {0:0,1:1,2:1,3:2,4:3,5:5,6:8,7:13,8:21,9:34,10:55,}

app = Flask(__name__)


def recur_fibo_cache(n):
    if n < len(cache):
        return cache[n]    
    else:
        cache_keys = list(cache.keys())
        last_cache_key = cache_keys[-1]
        for i in range(last_cache_key, n+1):
            i += 1
            cache[i] = cache[i-1] + cache[i-2]
        return recur_fibo_cache(n)

@app.route('/fib')
def fibo_route():
    try:
        number = request.args.get('n', default=1, type=int)
        response = recur_fibo_cache(number)        
        return str(response)
    
    except Exception as e:
        return f'[Exception] ({type(e)}): {format(e)}\n'


if __name__ == "__main__":
    app.run(
        debug=False,
        port=8000,
        host='0.0.0.0'
        )


# > curl http://localhost:8000/fib?n=1
# 1

# > curl http://localhost:8000/fib?n=10
# 55

# > curl http://localhost:8000/fib?n=72
# 498454011879264