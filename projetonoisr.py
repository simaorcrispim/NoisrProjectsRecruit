import numpy as np
import matplotlib . pyplot as plt
from matplotlib . animation import FuncAnimation
from dataclasses import dataclass
from random import uniform


@dataclass
class Particle:
    pos: float #posição
    v: float #velocidade
    m: float #massa

def initial_conditons(balls_x): #receber as condições iniciais
    box_size= uniform(0,b)
    for i in range(num_particles):
        x=uniform(1,box_size-1)
        #print(x)
        vel=uniform(-box_size/4,box_size/4)
        mass=uniform(0.1,10)
        balls_x[i][0]=Particle(pos=x,v=vel,m=mass)
    
    #balls_x[0][0]=Particle(pos=25,v=10,m=3)
    #balls_x[1][0]=Particle(pos=60,v=-5,m=4)


    simulate_collision(balls_x,box_size)

def simulate_collision(balls_x,box_size):

    special_frame=0 #falta ir modificando o special frame (o special frame são os frames no qual os dados vão sendo estabelecidos)
    while special_frame < num_frames-1:
        if special_frame<num_frames:
            calculations=trigger(balls_x,box_size,special_frame)
            special_frame = calculations[1]
            #print(calculations[1],"!!!")
            #print(special_frame,"!!")
            balls_x = calculations[0]
            #print(calculations[0],"debugging e fdd")
    for i in range(num_frames):
        for j in range(num_particles):
            if balls_x[j][i].m==0:
                balls_x[j][i].v=balls_x[j][i-1].v
                balls_x[j][i].pos=balls_x[j][i-1].pos + balls_x[j][i-1].v*(1/fps)
                balls_x[j][i].m=balls_x[j][0].m
            
        
    #print(balls_x)

    create_animation(balls_x,box_size)

def trigger(balls_x,box_size,special_frame):

    print(special_frame,"porque é que esta merda não atualiza??")
    mino=[num_frames,0,0,0] #no programa main será necessário dizer que se min[0]>=frames_restantes então não afetar o codigo

    for j in range (num_particles):
        frame2=(-(balls_x[j][special_frame].pos)/balls_x[j][special_frame].v)*fps 
        #print(frame2)
        frame3=((box_size-balls_x[j][special_frame].pos)/balls_x[j][special_frame].v)*fps 
        #print(frame3)
        for k in [x for x in range(num_particles) if x!=j]:
            if balls_x[j][special_frame].v-balls_x[k][special_frame].v!=0: #se as velocidades forem iguais não colidem
                frame1=((balls_x[k][special_frame].pos-balls_x[j][special_frame].pos)/(balls_x[j][special_frame].v-balls_x[k][special_frame].v))*fps
            else:
                frame1=num_frames
            #print (frame1)

            data=evaluate(frame1,frame2,frame3)
            data[0]=data[0]+special_frame
            data.append(j)
            data.append(k)
            if mino[0]>data[0]:
                mino=data
    #print(mino)
    balls_x = aftermath(mino[0],mino[1],mino[2],mino[3],balls_x,special_frame)

    novo_frame=(mino[0])
    novo_frame=int(novo_frame)

    if novo_frame+1>=num_frames:
        novo_frame=num_frames-1
    return [balls_x,novo_frame]

    #return(frame)
def evaluate(choque,origem,parede): #créditos para o Satisfação (Filipe)
    lista=[choque,origem,parede]
    mino=num_frames
    k=0
    for i in range(len(lista)):
        if origem//1== mino//1==parede//1:
            mino=lista[i]-1  #foi aqui
            k=4
        if lista[i]<mino and lista[i]>=1:
            mino=lista[i]-1 #foi aqui
            k=i+1

    return [mino,k]


def aftermath (canon_frame,canon_event,p1,p2,balls_x,special_frame): #particula 1 e 2 que age na colisão, igualar o special frame com o canon frame depois(+1)
    if  canon_frame<=num_frames:  

        novo_frame=int(canon_frame)
        if canon_event==2 or canon_event==3:
            balls_x[p1][novo_frame].m=balls_x[p1][0].m
            balls_x[p1][novo_frame].v=-balls_x[p1][special_frame].v
            balls_x[p1][novo_frame].pos=balls_x[p1][special_frame].pos + (balls_x[p1][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p1][novo_frame].v)*(novo_frame+1-canon_frame)/fps
            #é necessário definir uma função com o frame atual

            balls_x[p2][novo_frame].m=balls_x[p2][special_frame].m
            balls_x[p2][novo_frame].v=balls_x[p2][special_frame].v
            balls_x[p2][novo_frame].pos=balls_x[p2][special_frame].pos + (balls_x[p2][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p2][novo_frame].v)*(novo_frame+1-canon_frame)/fps
        #adicionar um for para multiplas particulas
        if canon_event==4:
            balls_x[p1][novo_frame].m=balls_x[p1][0].m
            balls_x[p1][novo_frame].v=-balls_x[p1][special_frame].v
            balls_x[p1][novo_frame].pos=balls_x[p1][special_frame].pos + (balls_x[p1][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p1][novo_frame].v)*(novo_frame+1-canon_frame)/fps

            balls_x[p2][novo_frame].m=balls_x[p2][0].m
            balls_x[p2][novo_frame].v=-balls_x[p2][special_frame].v
            balls_x[p2][novo_frame].pos=balls_x[p2][special_frame].pos + (balls_x[p2][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p2][novo_frame].v)*(novo_frame+1-canon_frame)/fps

        if canon_event==1:
            balls_x[p1][novo_frame].m=balls_x[p1][0].m
            balls_x[p2][novo_frame].m=balls_x[p2][0].m

            balls_x[p1][novo_frame].v=((balls_x[p1][special_frame].m -balls_x[p2][special_frame].m)*balls_x[p1][special_frame].v+2*balls_x[p2][special_frame].m*balls_x[p2][special_frame].v)/(balls_x[p1][special_frame].m +balls_x[p2][special_frame].m) #v1 = ((m1 – m2)u1 + 2m2u2) / (m1 + m2)
            balls_x[p2][novo_frame].v=((balls_x[p2][special_frame].m -balls_x[p1][special_frame].m)*balls_x[p2][special_frame].v+2*balls_x[p1][special_frame].m*balls_x[p1][special_frame].v)/(balls_x[p2][special_frame].m +balls_x[p1][special_frame].m) #v2 = ((m2 – m1)u2 + 2m1u1) / (m2 + m1)
        
            balls_x[p1][novo_frame].pos=balls_x[p1][special_frame].pos + (balls_x[p1][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p1][novo_frame].v)*(novo_frame+1-canon_frame)/fps
            balls_x[p2][novo_frame].pos=balls_x[p2][special_frame].pos + (balls_x[p2][special_frame].v)*(canon_frame-special_frame)/fps+ (balls_x[p2][novo_frame].v)*(novo_frame+1-canon_frame)/fps                                    

    return balls_x







def create_animation ( balls_x, box_size ):

    fig, ax=plt.subplots() 
    ax.set_xlim(0, box_size) 
    ax.set_ylim(-0.1, 0.1)

    ball1, = ax.plot(balls_x[0][0].pos, 0, 'bo', markersize=10) 
    ball2, = ax.plot(balls_x[1][0].pos, 0, 'ro', markersize=10)

    def update(frame):
        ball1.set_xdata(balls_x[0][frame].pos)
        ball2.set_xdata(balls_x[1][frame].pos) 
        return ball1 , ball2
    ani = FuncAnimation( fig , update , frames=num_frames , blit=True) 
    plt .show()
    plt.close(fig)
            
def main():
    initial_conditons(balls_x)

b=1000
 #dicionário com as características de cada partícula
num_particles=2
fps=30
tempo=int(input("escolha quanto tempo deseja que a sua animação dure (segs)"))
num_frames=tempo*fps
balls_x=[]
for i in range(num_particles):
    balls_x.append([0]*num_frames)
for i in range (num_particles):
    for j in range (num_frames):
        balls_x[i][j] = Particle(pos=0,v=0,m=0)
main()


#main()
#print(balls_x) 


