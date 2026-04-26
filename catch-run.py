import pygame 
import sys
import numpy 
import moderngl
import random #Avin dunyaya gelmesi

pygame.init()
pygame.mixer.init()

bomb_voice = pygame.mixer.Sound("catchRun_bomb_point.wav")
safe_voice = pygame.mixer.Sound("catchRun_safe_point.wav")
bomb_voice.set_volume(0.8)
safe_voice.set_volume(0.8)

pygame.mixer.music.load("catchRun_melody.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1) #hep calsin, sarki bittikce basa sarsin.

pygame.display.set_mode((800,800), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("CATCH-RUN PROJESI")

ctx = moderngl.create_context()

v_shader = """
#version 330
in vec2 konumVeri;
out vec4 vertexColor;
uniform vec2 u_pos;    //ucgenin pozisyonunu aldik.
uniform vec3 u_color;

void main()
{
   gl_Position = vec4(konumVeri + u_pos,0.0,1.0);
   vertexColor = vec4(u_color, 1.0);
}
"""

f_shader = """
#version 330
in vec4 vertexColor;
out vec4 fragColor;

void main()
{
   fragColor = vertexColor;
}
"""

prog = ctx.program(vertex_shader=v_shader ,fragment_shader=f_shader)

vertices = numpy.array([
    0.0 , 0.1443376,        #ust kose     a
    -0.125 , -0.0721687,   #sol alt kose b
    0.125 , -0.0721687,    #sag alt kose c
],dtype='f4')
vbo = ctx.buffer(vertices.tobytes())
vao = ctx.vertex_array(prog,[(vbo,'2f','konumVeri')])


target_vertices = numpy.array([
    0.0 , 0.0
],dtype='f4')
target_vbo = ctx.buffer(target_vertices.tobytes())
target_vao = ctx.vertex_array(prog,[(target_vbo,'2f','konumVeri')])





pos_x = 0.0   #ucgenin agırlık merkezı G
pos_y = 0.0

up_line = 1.0 - vertices[1]
left_line = -1.0 - vertices[2]
down_line = -1.0 - vertices[3]
right_line = 1.0 - vertices[4]

health_bar=5
puan=0
status_message = "the game has started!"
starting_speed = 0.012  #min speed
max_speed = 0.06
current_speed = starting_speed


fps_saati = pygame.time.Clock()


active_points = []               #dinamik olarak point_sum miktarına göre dolacak.
start_time = 0

while True: #OYUN BASLANGIC
    x1,y1 = vertices[0]+pos_x , vertices[1]+pos_y
    x2,y2 = vertices[2]+pos_x , vertices[3]+pos_y
    x3,y3 = vertices[4]+pos_x , vertices[5]+pos_y

    #KLAVYE ETKİNLİKLERİ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        pos_y += current_speed
        if pos_y >= up_line:
            pos_y = up_line        
    if keys[pygame.K_a]:
        pos_x -= current_speed  
        if pos_x <= left_line:
            pos_x = left_line
    if keys[pygame.K_s]:
        pos_y -= current_speed
        if pos_y <= down_line:
            pos_y = down_line
    if keys[pygame.K_d]:
        pos_x += current_speed 
        if pos_x >= right_line:
            pos_x = right_line
    # if keys[pygame.K_SPACE]:
    #         pos_x ,pos_y = 0.0 ,0.0

    #ZAMANA BAGLI DOGUM
    current_time = pygame.time.get_ticks() #oyun basladıgı andan itibaren ms cinsinden bir sayac gibi süreyi tutar.
    if current_time - start_time > 1700 :
        active_points.clear()
        start_time = current_time
        
        point_sum = random.randint(5,15)  #point miktarını random seçtik.

        for i in range(point_sum):
            while True:
                temp_x = random.uniform(left_line,right_line)
                temp_y = random.uniform(down_line,up_line)
                mesafe_sqrt = (pos_x-temp_x)**2 + (pos_y-temp_y)**2 
                r_sqrt = vertices[5]**2+0.02
                if mesafe_sqrt> r_sqrt:
                    is_this_bomb = random.random() < 0.20 #0-1 arasından ürettiği sayi 0.20den kucukse (%20 şansla), is_bomb degiskeni true olur
                    point_character= {"x": temp_x,  #sozluk
                                    "y": temp_y,    #uniform:float
                                    "r": 0.0 if is_this_bomb else random.uniform(0.2,1.0), #rengi 0.0 yap eger is_this_bomb true ise, degilse rastgele renk 
                                    "g": 0.0 if is_this_bomb else random.uniform(0.2,1.0), 
                                    "b": 0.0 if is_this_bomb else random.uniform(0.2,1.0),
                                    "size": 30.0 if is_this_bomb else random.randint(15,20),
                                    "point_type_is_bomb": is_this_bomb #point bombaysa true,false 
                                    }
                    active_points.append(point_character)
                    print(active_points)
                    break


    #POINTLER VE UCGENIN CARPISMASI

    for point in active_points[:]:
        triangle_edge=abs(x3-x2)
        triangle_area=((3**0.5)/4 * triangle_edge**2)

        px=point["x"]
        py=point["y"]
        newTri_area1= abs(x1*y2+x2*py+px*y1-y1*x2-y2*px-py*x1)/2
        newTri_area2= abs(x1*y3+x3*py+px*y1-y1*x3-y3*px-py*x1)/2
        newTri_area3= abs(x2*y3+x3*py+px*y2-y2*x3-y3*px-py*x2)/2
        newTri_areaTotal = newTri_area1 + newTri_area2 + newTri_area3

        if abs(newTri_areaTotal-triangle_area)<0.0001:
            if point["r"]==0.0:
                health_bar-=1
                puan-=200   #hız---

                current_speed -= 0.008
                current_speed = max(starting_speed,current_speed) #hız sıfırlanmaması için
                status_message = "WARNING: Bomb Damage!"

                bomb_voice.play()
                
                for i in range(10):
                    ctx.clear(0.690,0.878,0.901,1.0)
                    if i%2==0:
                        prog['u_color'].value= (1.0,0.0,0.0)
                    else:
                        #prog['u_color'].value= (0.098,0.098,0.439)
                        prog['u_color'].value= (0.0,0.0,0.0)
                    prog['u_pos'].value=(pos_x,pos_y)
                    vao.render()
                    pygame.display.flip() 
                    pygame.time.wait(100)
                pos_x,pos_y=0,0
                
                if health_bar <= 0:
                    print("GAME OVER! Healt depleted.")  #terminal icin
                    status_message = "GAME OVER! Healt depleted."
                    pygame.display.set_caption(f"Catch-Run Game        |         Puan: {puan}        |        Health: {health_bar}      |       {status_message}    ")

                    pygame.time.wait(3000)
                    pygame.quit()
                    sys.exit()
            else:
                puan+=100    #hız++
                current_speed += 0.001

                current_time = min(max_speed,current_speed)
                messages =["COOL!","GREAT!","FANTASTİC!","GREAT!","GORGEOUS!",
                           "YUMMY!","GOOD!","UNBELIEVABLE!","INCREDİBLE!"]  
                message = random.choice(messages)

                safe_voice.play()

                print(f"{message}")  #terminal icin
                status_message = random.choice(messages)

            active_points.remove(point)
            
        

    pygame.display.set_caption(f"Catch-Run Game        |         Puan: {puan}        |        Health: {health_bar}      |       {status_message}    ")
            
    #CİZİM VE GPU EMRİ
    ctx.clear(0.690,0.878,0.901,1.0)  #eski ucgenler arkasında ız bırakır. ekranı temızle.
    prog['u_color'].value= (0.098,0.098,0.439) #ucgenın rengını dısarıdan bıldırdık
    prog['u_pos'].value=(pos_x,pos_y) #klavye hareketlerini prog ile u_pos'a aktarmalıyım. 
    vao.render()                #GPU'ya uzgenı cız emrı ver

    for point in active_points:
        prog['u_color'].value = (point["r"],point["g"],point["b"])
        prog['u_pos'].value = (point["x"],point["y"])
        ctx.point_size = point["size"]
        target_vao.render(moderngl.POINTS)

    
    pygame.display.flip()       #ekranı yenıle, doublebuf kullanmıstık.
    #pygame.time.wait(10)       #(CPU) o kadar güçlü ki cok hızlı ılerlemesın dıye döngüyü 10 milisaniye uyuttuk
    fps_saati.tick(60)              #60FPSyi tutturmak ıcın ne kadar gerekıyorsa o kadar uyu.
