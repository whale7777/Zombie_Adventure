from re import S, U
from turtle import Screen
import pygame
import pygame
import time as t
from math import *
from pygame import mixer
FPS_Timer = 0

ending = False

ending_timer = 0

name = "" 


import os

s_ypos = 500

main = True
game_level = 1

pygame.init()

zombie = []
zombies = []

z_hp = []

guns = []
bullets = []

gun_xpos = 0
gun_ypos =0


is_selected = 1

store = False
path = os.getcwd()
#path = path + "\\Project"
print("Path : "+path)
box_path = os.path.join(path, "bg.png")
font_bold = os.path.join(path, "Maplestory Bold.ttf")
font_light = os.path.join(path, "Maplestory Light.ttf")
bg = pygame.image.load(box_path)
gun = pygame.image.load(os.path.join(path, "gun.png"))
bullet = pygame.image.load(os.path.join(path, "bullet.png"))
zombie_ch = pygame.image.load(os.path.join(path, "zombie.png"))
fence = pygame.image.load(os.path.join(path, "Fence.png"))



z_start = True

clock = pygame.time.Clock()
width = 1400
height = 770
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("좀비 어드벤쳐 - Zombie Adventure - Win32 V1.0 - Korean")

game_font = pygame.font.Font(font_bold, 88)
subtext_font = pygame.font.Font(font_bold,50)
maple_font = pygame.font.Font(font_bold,50)
small_font = pygame.font.Font(font_bold,20)
lv_font = pygame.font.Font(font_bold,30)
Gold_font = pygame.font.Font(font_bold,40)

total_time = 120
a = 0

start_ticks = pygame.time.get_ticks()
elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

running = True
start = True

damage = 5


gun_cooltime = 30
coin = 0
lv = 0
xp = 0
required_coin = 0
강화비용 = 0
내구도 = 0
수리비용 = 0
데미지강화비용 = 0
cheat = 0
egg_cheat = 0

f = open(os.path.join(path,"Database.txt"), mode='r', encoding='utf-8')
f = next(f)
print(f)
coin, lv, xp, required_coin, 강화비용, 데미지강화비용, 수리비용, 내구도, cheat, egg_cheat, damage, gun_cooltime, 이름받음, name = f.split(":")

coin = int(coin)
lv = int(lv)
xp = int(xp)
required_coin = int(required_coin)
강화비용 = int(강화비용)
내구도 = int(내구도)
데미지강화비용 = int(데미지강화비용)
수리비용 = int(수리비용)
cheat = int(cheat)
egg_cheat = int(egg_cheat)
damage = float(damage)
gun_cooltime = float(gun_cooltime)
이름받음 = int(이름받음)

c=0
c_1 = 0
c_2 = 0
c_3 =0

ec = 0
ec_1 =0
ec_2 = 0
game_over = pygame.image.load(os.path.join(path,"Gameover.png"))



while running:


    ##########Start Scene#######################
    while start:
        dt = clock.tick(5)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        
                    if event.key == pygame.K_SPACE:
                        start = False

        
        if a == 0:
            s_ypos = 1500
            a = 1
        elif a == 1:
            s_ypos = 500
            a=0
        
        

        

        

        screen.fill((176,20,50))
        timer = game_font.render("좀비 어드벤쳐!! [KOREAN]", True, (0,0,0))
        sub_text = subtext_font.render("[SPACE]로 게임 시작하기", True, (0,0,0))
        

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]


        sub_size = sub_text.get_rect().size
        s_width = sub_size[0]
        s_height = sub_size[1]
        

        screen.blit(bg,(0,0))
        
        w = round((width - s_width) / 2)

        print(w)

        screen.blit(timer, ((width - t_width) / 2 ,100))
        screen.blit(sub_text,(w,s_ypos))
        

        
        pygame.display.update()

    while 이름받음 == 0:

        

        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP_ENTER:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False

                    if event.key == pygame.K_a:
                        if len(name) <= 10:name += "a"
                    if event.key == pygame.K_b:
                        if len(name) <= 10:name += "b"
                    if event.key == pygame.K_c:
                        if len(name) <= 10:name += "c"
                    if event.key == pygame.K_d:
                        if len(name) <= 10:name += "d"
                    if event.key == pygame.K_e:
                        if len(name) <= 10:name += "e"
                    if event.key == pygame.K_f:
                        if len(name) <= 10:name += "f"
                    if event.key == pygame.K_g:
                        if len(name) <= 10:name += "g"
                    if event.key == pygame.K_h:
                        if len(name) <= 10:name += "h"
                    if event.key == pygame.K_i:
                        if len(name) <= 10:name += "i"
                    if event.key == pygame.K_j:
                        if len(name) <= 10:name += "j"
                    if event.key == pygame.K_k:
                        if len(name) <= 10:name += "k"
                    if event.key == pygame.K_l:
                        if len(name) <= 10:name += "l"
                    if event.key == pygame.K_m:
                        if len(name) <= 10:name += "m"
                    if event.key == pygame.K_n:
                        if len(name) <= 10:name += "n"
                    if event.key == pygame.K_o:
                        if len(name) <= 10:name += "o"
                    if event.key == pygame.K_p:
                        if len(name) <= 10:name += "p"
                    if event.key == pygame.K_q:
                        if len(name) <= 10:name += "q"
                    if event.key == pygame.K_r:
                        if len(name) <= 10:name += "r"
                    if event.key == pygame.K_s:
                        if len(name) <= 10:name += "s"
                    if event.key == pygame.K_t:
                        if len(name) <= 10:name += "t"
                    if event.key == pygame.K_u:
                        if len(name) <= 10:name += "u"
                    if event.key == pygame.K_v:
                        if len(name) <= 10:name += "v"
                    if event.key == pygame.K_w:
                        if len(name) <= 10:name += "w"
                    if event.key == pygame.K_x:
                        if len(name) <= 10:name += "x"
                    if event.key == pygame.K_y:
                        if len(name) <= 10:name += "y"
                    if event.key == pygame.K_z:
                        if len(name) <= 10:name += "z"
                    
                    if event.key == pygame.K_RETURN:
                        이름받음 = 1

                    if event.key == pygame.K_BACKSPACE:
                        name = ""

                    

        
        if a == 0:
            s_ypos = 1500
            a = 1
        elif a == 1:
            s_ypos = 500
            a=0
        
        

        

        

        screen.fill((176,20,50))
        timer = subtext_font.render("이름을 입력하시고 [ENTER]을 누르십시오]", True, (0,0,0))
        sub_text = subtext_font.render(f": {name}", True, (0,0,0))
        

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]


        sub_size = sub_text.get_rect().size
        s_width = sub_size[0]
        s_height = sub_size[1]
        

        
        
        w = round((width - s_width) / 2)

        

        screen.blit(timer, ((width - t_width) / 2 ,100))
        screen.blit(sub_text,(w,500))
        

        
        pygame.display.update()




    while is_selected:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        c = 0
                        c_1 = 0
                        c_2 = 0
                        c_3 = 0
                        ec = 0
                        ec_1 = 0
                        ec_2 = 0
                    if event.key == pygame.K_z:
                        if coin >= required_coin and 내구도 > 0:
                            coin -= required_coin
                            is_selected = False
                            z_start = True
                        c = 0
                        c_1 = 0
                        c_2 = 0
                        c_3 = 0
                        ec = 0
                        ec_1 = 0
                        ec_2 = 0
                    if event.key == pygame.K_s:
                        is_selected = False
                        z_start = False
                        store = True
                        main = False
                        c = 0
                        c_1 = 0
                        c_2 = 0
                        c_3 = 0
                        ec = 0
                        ec_1 = 0
                        ec_2 = 0
                    if event.key == pygame.K_c:
                        
                        ec = 0
                        ec_1 = 0
                        ec_2 = 0
                        if cheat ==0:
                            c = 1
                    if event.key == pygame.K_o:
                        if c ==1:
                            c_1 = 1
                        else:
                            c = 0
                            c_1 = 0
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                    if event.key == pygame.K_i:
                        if c_1 == 1 and c ==1:
                            c_2 = 1
                        else:
                            c = 0
                            c_1 = 0
                            c_2 = 0
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                            
                    if event.key == pygame.K_n:
                        if c_1 == 1 and c == 1 and c_2 == 1:
                            coin += 5000
                            cheat = 1
                            c = 0
                            c_1 = 0
                            c_2 = 0
                            c_3 = 0
                        else:
                            c = 0
                            c_1 = 0
                            c_2 = 0
                            c_3 = 0
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                    if event.key == pygame.K_e:
                        if egg_cheat == 0:
                            ec =1
                        else:
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                    if event.key == pygame.K_g:
                        if ec == 1 and ec_1 == 0:
                            ec_1 = 1
                        elif ec== 1 and ec_1 == 1:
                            coin += 50000
                            gun_cooltime = 0.5
                            damage = 40
                            lv = 10
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                            egg_cheat = 1
                        elif ec == 0:
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0
                        else:
                            ec = 0
                            ec_1 = 0
                            ec_2 = 0


                    
                    

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]
        
        

        

        screen.fill((176,20,50))
        timer = game_font.render("기지", True, (0,0,0))
        inf_g = subtext_font.render(f"G : {coin}", True, (0,0,0))
        inf_l = subtext_font.render(f"Lv : {lv}", True, (0,0,0))
        inf_e = subtext_font.render(f"xp : {xp}", True, (0,0,0))
        inf_n = subtext_font.render(f"내구도 : {내구도}", True, (0,0,0))
        inf = subtext_font.render(f"damage | {damage}", True, (0,0,0))
        inf_s = subtext_font.render(f"speed | {gun_cooltime}", True, (0,0,0))
        g_text = subtext_font.render("강화소  |  [S]", True, (0,0,0))
        z_text = subtext_font.render(f"전투  |  [Z]  | 필요 [{required_coin}G]", True, (0,0,0))

        
        

        screen.blit(timer, ((width - t_width) / 2,100))


        screen.blit(g_text, (100, 400))
        screen.blit(inf_g, (1000, 200))
        screen.blit(inf_l, (1000, 300))
        screen.blit(inf, (1000, 700))
        screen.blit(inf_s, (1000, 600))
        screen.blit(inf_e, (1000, 400))
        screen.blit(inf_n, (1000, 500))
        screen.blit(z_text, (100, 500))
        pygame.display.update()
        

    while z_start:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        main = False
                    if event.key == pygame.K_a:  # 학교
                        game_level = 1
                        z_start = False
                        main = True
                    if event.key == pygame.K_s: # 경찰서
                        game_level = 2
                        z_start = False
                        main = True
                    if event.key == pygame.K_d: # 버려진 도시
                        game_level = 3
                        z_start = False
                        main = True
                    if event.key == pygame.K_b: # 버려진 도시
                        if lv >= 10:
                            game_level = 5
                            z_start = False
                            main = True
                    if event.key == pygame.K_h:
                        start = False
                        
                        main = False
                        is_selected = True
                        z_start = False
                        main = False
                    

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]
        
        

        

        screen.fill((176,20,50))
        timer = game_font.render("전쟁터 선택", True, (0,0,0))


        sub_text = subtext_font.render("학교 {쉬움} |  [A]", True, (0,0,0)) # lv 1
        g_text = subtext_font.render("경찰서  {보통}|  [S]", True, (0,0,0)) # lv 2
        z_text = subtext_font.render("버려진 도시  {어려움}|  [D]", True, (0,0,0)) # lv 3
        if lv >= 10:
            c_text = subtext_font.render("백신 연구소  {매우 어려움}|  [B] ", True, (0,0,0)) # lv 3
        else: 
            c_text = subtext_font.render("백신 연구소  {매우 어려움}|  [잠김] ", True, (0,0,0)) # lv 3
        h_text = subtext_font.render("후퇴  |  [H]", True, (0,0,0))
        

        screen.blit(timer, ((width - t_width) / 2,100))
        screen.blit(sub_text, (200,300))

        screen.blit(g_text, (200, 400))

        screen.blit(z_text, (200, 500))

        screen.blit(c_text, (200,600))

        screen.blit(h_text, (40,30))
        pygame.display.update()

    from random import *


    global vaa
    vaa = 0
    global cooltime
    cooltime = 180 / game_level
    

    def zombie_spawn():

        a = randint(1,10)
        global vaa
        global cooltime
        if vaa != cooltime:
            vaa +=1
        elif vaa == cooltime:
            zombie.append(randint(120, 1200)) # 좀비 xpos
            zombies.append(randint(400,610))  # 좀비 ypos
            
            if game_level == 5:
                if a == 2:
                    z_hp.append(200)
                else:
                    z_hp.append(40)
            else:
                z_hp.append(20)
            vaa = 0
    
    
    global s
    s = 0
    def gun_spawn():

        bullets.append(gun_xpos+ 27)
        guns.append(100)  # 좀비 xpos

    game_over_ = False

    # 메인

    a = 0
    global uns
    uns = 0

    is발사허용 = 1

    while main:
        
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        main = False
                    if event.key == pygame.K_h:
                        zombie = []
                        zombies = []
                        guns = []
                        bullets = []
                        z_hp = []
                        어라 = 0
                        # gun_xpos = 0
                        start = False
                        running = True
                        main = False
                        is_selected = True
                        z_start = False
                        main = False
                    
                       
                    
        try:
            for i in range(len(bullets)):  # 충돌처리
                for j in range(len(zombies)):
                    if bullets[i] >= zombie[j] and bullets[i] < zombie[j] +  62 and guns[i] >= zombies[j]:
                        print("충돌!!")
                        # print(bullets,zombies,guns,zombie)
                        del bullets[i]
                        # del zombies[j]
                        del guns[i]
                        # del zombie[j]

                        # coin += randint(3,10)
                        # xp += randint(2,7)
                        # break   
                        z_hp[j] -= damage
                        z_hp[j] = round(z_hp[j],2)
                        if z_hp[j] <= 0:
                            del zombie[j] 
                            del zombies[j]
                            del z_hp[j] 
                            coin += randint(20 * game_level,45 * game_level)
                            xp += randint(2,7)
                            
                        break
            for i in range(len(bullets)):
                if guns[i] > 1000:
                    del guns[i]
                    del bullets[i]
        except IndexError:
            pass

        for i in range(len(zombies)):
            if zombies[i] <= 130 or 내구도 <= 0:
                print("으아아앙아ㅏㄱ 후퇴다! 하지만 다음부턴 봐주지 않아!!")
                zombie = []
                zombies = []
                guns = []
                bullets = []
                z_hp = []
                어라 = 0
                # gun_xpos = 0
                start = False
                running = True
                main = False
                is_selected = False
                game_over_ = True
                z_start = False
                main = False
                break

                    
        # for i in range():
        #     print()

        if is발사허용 == 0: 
            s += 0.1
            s = round(s, 2)
            print(s)
        if s >= gun_cooltime:
            is발사허용 = 1
            s = 0
        
        if is발사허용 == 1:
            내구도 -= 1
            if xp >= 100:
                lv += 1
                xp = 0
            gun_spawn()
            is발사허용 = 0

        if 내구도 == 0:
            zombie = []
            zombies = []
            guns = []
            bullets = []
            # gun_xpos = 0
            start = False
            running = True
            main = False
            is_selected = True
            z_start = False
            main = False     

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]
        
        ending_timer += 1
        
        spawn = zombie_spawn()
        

        screen.fill((176,20,50))
        timer = subtext_font.render("후퇴  |  [H]", True, (0,0,0))
        내구도_txts = small_font.render(f"{내구도}", True, (0,0,0))
        ending_t = subtext_font.render(f"{round(ending_timer / 60, 2)}", True, (0,0,0))
        
        
        

        

    
        
        for i in range(len(zombie)):  # 좀비 이동            
            if zombie[i] >= 1338:
                zombie[i] = 1338
            
                
            elif zombie[i] <= 0:
                zombie[i] = 0
            
            if game_level == 5:
                zombies[i] -= uniform(0.3, 0.6)
            else:
                zombies[i] -= uniform(0.1, 0.2)
            m = randint(1,20)

            if m < 3:
                p_or_m = randint(1,2)
                if p_or_m == 1:
                    zombie[i] += uniform(13,15)
                elif p_or_m == 2:
                    zombie[i] -= uniform(13,15)

        gun_xpos, _ = pygame.mouse.get_pos()
        uns = 0
        for i in range(len(guns)):     # 총알 표시
            screen.blit(bullet, (bullets[i], guns[i]))
        for i in range(len(zombie)):     # 좀비 표시
            screen.blit(zombie_ch, (zombie[i], zombies[i]))
            hp = small_font.render(f"{z_hp[i]}", True, (0,0,0))
            screen.blit(hp, (zombie[i] + 15, zombies[i] + 165))

        
        
        
        for i in range(len(guns)):  # 좀비 이동      
            
            guns[i] += 4
            #if guns[f"{i}"] > 1500:
                # del guns[f"{i}"]   
                # del bullets[f"{i}"]
                # print(guns)
                # print(bullets)
                # uns += 1
                
            #62


        



                # if len(guns) > 0:
                #     for j in range(len(guns)):
                #         guns[f"{j}"] = guns[f"{j+1}"]
                #         bullets[f"{j}"] = bullets[f"{j+1}"]
                        

        if round(ending_timer / 60, 2) >= 100:
            start = False
            running = True
            main = False
            is_selected = False
            z_start = False
            main = False
            ending = True

        if gun_xpos > 1320:
            gun_xpos = 1320

        # sub_text = subtext_font.render("학교 {쉬움} |  [A]", True, (0,0,0)) # lv 1
        # g_text = subtext_font.render("경찰서  {보통}|  [S]", True, (0,0,0)) # lv 2
        # z_text = subtext_font.render("버려진 도시  {어려움}|  [D]", True, (0,0,0)) # lv 3
        # c_text = subtext_font.render("백신 연구소  {매우 어려움}|  [잠김]", True, (0,0,0)) # lv 3
        # h_text = subtext_font.render("후퇴", True, (0,0,0))
        
        if game_level == 5:
            screen.blit(ending_t,(1200,0))
        screen.blit(gun,(gun_xpos, 0))
        screen.blit(내구도_txts,(gun_xpos, 20))
        screen.blit(timer, (30,40))
        screen.blit(fence, (0,100))
        # screen.blit(sub_text, (200,300))
   
        # screen.blit(g_text, (200, 400))

        # screen.blit(z_text, (200, 500))

        # screen.blit(c_text, (200,600))

        # screen.blit(h_text, (40,30))
        pygame.display.update()
    while store:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        main = False
                        store = False
                    
                    if event.key == pygame.K_k:
                        if coin >= 강화비용:
                            if gun_cooltime <= 5:
                                coin -= 강화비용
                                gun_cooltime -= 0.1
                                gun_cooltime = round(gun_cooltime, 2)
                                강화비용 *= 1.45
                                강화비용 = round(강화비용)
                    if event.key == pygame.K_d:
                        if coin >= 데미지강화비용:
                            coin -= 데미지강화비용
                            damage += 0.1
                            damage = round(damage,2)
                            데미지강화비용 *= 1.35
                            데미지강화비용 = round(데미지강화비용)
                    
                    if event.key == pygame.K_s:
                        if coin >= 수리비용:
                            coin -= 수리비용
                            내구도 = 12000
                            수리비용 *= 3
                            수리비용 = round(데미지강화비용)
                            

                    if event.key == pygame.K_n:
                        start = False
                        main = False
                        is_selected = True
                        z_start = False
                        main = False
                        store = False
                    

        timer_size = timer.get_rect().size
        t_width = timer_size[0]
        t_height = timer_size[1]
        
        

        

        screen.fill((176,20,50))
        timer = game_font.render("강화 / 수리소", True, (0,0,0))


        sub_text = subtext_font.render(f"데미지 강화 | {데미지강화비용}G필요 [D]", True, (0,0,0)) # lv 1
        s_text = subtext_font.render(f"공격속도 강화 | {강화비용}G필요 [K]", True, (0,0,0)) # lv 1
        su_text = subtext_font.render(f"돈 | {coin}G", True, (0,0,0)) # lv 1
        g_text = subtext_font.render(f"수리  | {수리비용}G 필요 [S]", True, (0,0,0)) # lv 2
        z_text = subtext_font.render("나가기 |  [N]", True, (0,0,0)) # lv 3

        

        screen.blit(timer, ((width - t_width) / 2,100))
        screen.blit(sub_text, (100,300))
        screen.blit(su_text, (50,100))
        screen.blit(s_text, (100,400))

        screen.blit(g_text, (100, 500))

        screen.blit(z_text, (50, 50))


        pygame.display.update()
    #게임오버씬

    c_time = 0

    while game_over_:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        main = False
                        store = False
                        game_over_ = False
                    if event.key == pygame.K_h:
                        if c_time >= 180:
                            start = False
                            running = True 
                            main = False
                            is_selected = True
                            z_start = False
                            main = False
                            store = False
                            game_over_ = False
        c_time += 1
        screen.fill((176,20,50))
        screen.blit(game_over,(0,0))

        pygame.display.update()

    ypos = 800

    c = 0

    while ending:   
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        start = False
                        running = False
                        main = False
                        is_selected = False
                        z_start = False
                        main = False
                        store = False 
                        ending = False      

        screen.fill((176,20,50))

        ypos -= 0.3
        c += 1

        e1_text = subtext_font.render(f"제작 : 신민혁", True, (0,0,0)) # lv 1

        e1_size = e1_text.get_rect().size
        e1_width = e1_size[0]

        screen.blit(e1_text, ((width - e1_width) / 2, ypos))
        e2_text = subtext_font.render(f"기획 : 신민혁", True, (0,0,0)) # lv 1

        e2_size = e2_text.get_rect().size
        e2_width = e2_size[0]

        screen.blit(e2_text, ((width - e2_width) / 2, ypos + 50))
        e3_text = subtext_font.render(f"투자 : 신민혁", True, (0,0,0)) # lv 1

        e3_size = e3_text.get_rect().size
        e3_width = e3_size[0]

        screen.blit(e3_text, ((width - e3_width) / 2, ypos + 100))
        e4_text = subtext_font.render(f"제작사 : 고래와 사자 스튜디오", True, (0,0,0)) # lv 1

        e4_size = e4_text.get_rect().size
        e4_width = e4_size[0]

        screen.blit(e4_text, ((width - e4_width) / 2, ypos + 150))


        e5_text = subtext_font.render(f"THANKS FOR {name}", True, (0,0,0)) # lv 1

        e5_size = e5_text.get_rect().size
        e5_width = e5_size[0]

        screen.blit(e5_text, ((width - e5_width) / 2, ypos + 200))

        # if c >= 12000:
        #     start = False
        #     running = False
        #     main = False
        #     is_selected = False
        #     z_start = False
        #     main = False

        pygame.display.update()


with open(os.path.join(path,"Database.txt"),'w',encoding = 'utf-8') as f:
   f.write(f"{coin}:{lv}:{xp}:{required_coin}:{강화비용}:{데미지강화비용}:{수리비용}:{내구도}:{cheat}:{egg_cheat}:{damage}:{gun_cooltime}:{이름받음}:{name}")
   

pygame.quit()