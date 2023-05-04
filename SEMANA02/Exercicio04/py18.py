
#import builtins

#print(dir(builtins))

#def min():
 #   pass

#m =min ([5, 1, 3, 4, 2])

#print(m)

#x = 'global x'

#def test(z):
 #   global x
  #  x='local x'
   # y='local y '
    #print (y)
    #print (x)
 #   print (z)

#test('local z')
#print (x)

def outer():
    x= 'outer x'

    def inner():
        #nonlocal x
        x='inner x'

    inner()
    print(x)

outer()
print(x)
