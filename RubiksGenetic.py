from Rubik2x2 import *
import random

shuffle_num=10

cube=Rubik()
cube.reset()

rev_dictionary={0:1,1:0,2:3,3:2,4:5,5:4,6:7,7:6,8:9,9:8,10:11,11:10}
print cube.shuffle(shuffle_num)


gene_size=shuffle_num
pop_size=100

mut_rate=1
num_child=10


def fitness(member):
    global cube
    Test_cube=Rubik()
    Test_cube.reset()
    for i in member:
        Test_cube.move(i)
    a=Test_cube.get_int_cube()
    b=cube.get_int_cube()
    correct=0
    for i in range(len(a)):
        if a[i]==b[i]:
            correct+=1

    return (float(correct)/len(a))*100



def gen_population():
    global pop_size,gene_size
    pop=[]
    for i in range(pop_size):
        a=[]
        for j in range(gene_size):
            k=random.randint(0,11)
            a.append(k)
        pop.append(a)
    return pop


def crossover(po):
    global pop_size,num_child,gene_size
    pop=[]
    #topp=int(pop_size*cr_rate)
    i=0
    #top = [po[x][0] for x in range(0, topp)]
    while i<pop_size:
        a=po[i]
        b=po[i+1]
        i=i+2
        children=[]
        t=random.randint(1,gene_size-1)
        c=a[:gene_size/2]+b[gene_size/2:]
        d=b[:gene_size/2]+a[gene_size/2:]
        e=a[:t]+b[t:]
        f=b[:t]+a[t:]
        g=[]
        h=[]
        sw=0
        for j in range(len(a)):
            if sw==0:
                g.append(a[j])
                h.append(b[j])
                sw=1
            else:
                g.append(b[j])
                h.append(a[j])
                sw=0
        children.append(a)
        children.append(b)
        children.append(c)
        children.append(d)
        children.append(e)
        children.append(f)
        children.append(g)
        children.append(h)
        for j in range(2):
            a = []
            for j in range(gene_size):
                k = random.randint(0, 11)
                a.append(k)
            children.append(a)
        each=[]
        for j in range(num_child):
            each.append([children[j],fitness(children[j])])
        pro=sorted(each,key=lambda x:x[1])
        pro=pro[::-1]
        pop.append(pro[0][0])
        pop.append(pro[1][0])
    return pop

def mutation(po):
    global mut_rate
    pop=[]
    for i in range(len(po)):
        c = po[i]
        for j in range(len(c)):
            if mut_rate > random.randint(0, 150):
                c[j] = random.randint(0,11)
        pop.append(c)
                #print "Mutated"
    return pop

f=raw_input()
gen=0
pop=gen_population()
while True:
    gen+=1
    n_pop=[]
    for i in range(pop_size):
        cand=pop[i]
        n_pop.append([cand,fitness(cand)])

    n_pop=sorted(n_pop,key=lambda x:x[1])
    n_pop=n_pop[::-1]
    best=n_pop[0][1]
    best_c=n_pop[0][0]

    avg=0
    for i in range(pop_size):
        avg+=n_pop[i][1]
    avg=avg/float(pop_size)
    pop=crossover(pop)
    pop=mutation(pop)
    print gen,best,avg,best_c
    if best>=100:
        #print best_c
        break
print "Done Learning!"
best_c=best_c[::-1]
moves=[]
for i in range(len(best_c)):
    moves.append(rev_dictionary[best_c[i]])

print moves
i=0
j=0
while cube.get_reward()<100:
   print cube.get_cube()
   cube.move(moves[j])
   j+=1
   i+=1

print cube.get_cube()
print "Solved in",i






