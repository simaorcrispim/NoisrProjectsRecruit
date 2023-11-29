
import random
from random import uniform
import matplotlib . pyplot as plt

def consideracao(prob):
    veredito=uniform(0,1)
    if veredito>prob:
        return -1
    else:
        return 1


def afetacao_matrix(particula,step,prob):
     particle_paths[particula][step]=particle_paths[particula][step-1]+consideracao(prob)

def random_walk(prob,num_particles,num_steps):
    particle_paths[0][0]=consideracao(prob)
    particle_paths[1][0]=consideracao(prob)
    for i in range(1,num_steps):  
        for j in range (num_particles):
            afetacao_matrix(j,i,prob)
    #print(len(particle_paths [0]))
    create_plot(num_particles,particle_paths)

def create_plot ( num_steps , particle_paths ):
    time = [x for x in range(len ( particle_paths [0]))]
    # Build the plot with all the particles for particle path in particle paths :
    for particle_path in particle_paths :
        plt.plot(particle_path ,time)

    plt.title( ' Random Walk - N particles' ) 
    plt.xlabel ( ' Position ')
    plt.ylabel(' Time ')
    plt.show()



num_particles=10
num_steps=100
prob=0.6
particle_paths=[]
for i in range(num_particles): #m (número de linhas)
    particle_paths.append([0]*num_steps) #n (número de colunas)

random_walk(prob,num_particles,num_steps)
#print(particle_paths)