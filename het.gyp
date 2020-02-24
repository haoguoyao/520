tuple =  ('a', True, False, 'Hello')
def func(b,*a):
    print (b)
    print(a)
    for i in a:
        print(i)

func(10,"a","b","c")