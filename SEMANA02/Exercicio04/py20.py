try:
    f=open('testfile.txt')
    #var=bad_var
    if f,name == 'testfile.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error')
else:
    print(f.read())
    f.close()
finally:
    print ("Executint Finally...")
