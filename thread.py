import concurrent.futures
import modulo_mando
import main

def foo(bar):
    while True:
        main.command = modulo_mando.teclaMando()
        return main.command

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(foo)
    return_value = future.result()
    print(return_value)
