import os

#print(dir(os))
print(os.getcwd())

os.chdir('\Users\carlo\OneDrive\Documentos\UFU\8º Período\Sistemas Embarcado')
os.rename('test.txt', 'demo.txt')

print(os.stat('demo.txt').st_mtime)
pritn(os.listdir())
