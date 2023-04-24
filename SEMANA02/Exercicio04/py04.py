#courses.append('Art') adiciona o couses_2 como um bloco
#courses.insert(0,'Art')
#courses.extend(courses_2) adiciona cada item do couses_2 individualmente
#courses.remove('Math')
#courses.pop() retira o último valor

#popped=courses.pop()
#print(popped)            Mostra o item retirado

#courses.reverse() Inverte a sequência

#courses.sort()     Deixa na ordem alfabética
#nums.sort()        Deixa na ordem numérica
#courses.sort(reverse=True) Deixa na ordem alfabética ao contrário
#nums.sort(reverse=True)    Deixa na ordem numérica  ao contrário

#print(min(nums))     Mostra valor mínimo
#print(max(nums))     Mostra o valor máximo
#print(sum(nums))     Mostra a soma dos valores

#print(courses.index('CompSci')) Diz a posição da palavra na string
#print ('CompSci' in courses) Checa se está na string

#tuple = ('History', 'Math', 'Physics', 'CompSci') É imutavel
#list =['History', 'Math', 'Physics', 'CompSci'] É mutavel
#cs_courses = {'History', 'Math', 'Physics', 'CompSci'}  Imprime em ordem aleatória (sets)



courses=['History', 'Math', 'Physics', 'CompSci']

course_str = ' - '.join(courses)
new_list=course_str.split(' - ')

print(course_str)
print(new_list)


#nums = [1, 5, 2, 4, 3]
#sorted_courses=sorted(courses)

#print(min(nums))
