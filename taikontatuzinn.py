import pygame
import sys
import random
import time

pygame.init()

# --- 画面設定 ---
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taiko no Tatsujin Simple")

clock = pygame.time.Clock()

# --- 色 ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50) 
BLUE = (50, 80, 220)
GOLD = (255, 215, 0)

# --- ノーツ設定 ---
NOTE_SPEED = 5
NOTE_SIZE = 30
HIT_POSITION = 75   # 判定位置


REMOVE_SPEED=15

COMBO_SIZE=12

IMAGE_SIZE=150
IMG_X=WIDTH//2-75
IMG_Y=HEIGHT-170
combo=0

f_img=-1

img0=pygame.image.load("dontyan_0.png")
img1=pygame.image.load("dontyan_1.png")
background = pygame.image.load("T_haikei.jpg")
img0 = pygame.transform.scale(img0, (IMAGE_SIZE, IMAGE_SIZE))
img1 = pygame.transform.scale(img1, (IMAGE_SIZE, IMAGE_SIZE))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

don_sound = pygame.mixer.Sound("don.wav")
ka_sound = pygame.mixer.Sound("ka.wav")

dontyan=-1

hit_type="ka"

notes = []
rnotes = []
hits=[]

# --- スコア ---
score = 0
#font = pygame.font.SysFont(None, 40)
font = pygame.font.SysFont("msgothic", 40)

# --- 新規追加：タイトル用フォント ---
title_font = pygame.font.SysFont("msgothic", 80)
button_font = pygame.font.SysFont("msgothic", 50)

NOTE_SPEED = 5
time_span=6 #<10
music_s_time=60

fx=15
fy=29
time_count=0

music = [
    
    
    
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,2,0,0,0,1,0,1,0],

[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0],

[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],

[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0],
[1,0,0,1,1,0,1,0,1,0,0,0,1,0,1,0],

[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],#
[1,0,0,0,1,0,0,0,2,0,0,6,1,0,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,2,0,0,6,5,2,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,2,0,0,0,1,0,1,0],
[1,0,0,0,5,0,0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,2,0,0,0,0,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,0,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[1,0,0,1,1,0,1,0,1,0,1,0,2,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,2,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0],
[1,0,0,0,1,0,0,0,2,0,0,0,1,0,1,0],
[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1]
]

# --- タイトル画面 ---
def title_screen():
    while True:
        screen.blit(background, (0, 0))

        # タイトル文字
        title_text = title_font.render("太鼓の達人", True, GOLD)
        screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 175))

        # スタートボタン
        button_rect = pygame.Rect(WIDTH//2 - 80, 300, 150, 80)
        pygame.draw.rect(screen, WHITE, button_rect)
        start_text = button_font.render("START", True, BLACK)
        screen.blit(start_text, (
            button_rect.centerx - start_text.get_width()//2,
            button_rect.centery - start_text.get_height()//2))

        pygame.display.update()


        # クリック待ち
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # ゲーム開始


# --- ノーツクラス ---
class Note:
    def __init__(self, type_):
        self.x = WIDTH
        self.type = type_
        self.color = RED if type_ == "don" else BLUE

    def move(self):
        self.x -= NOTE_SPEED
        pygame.draw.circle(screen, self.color, (int(self.x), HEIGHT // 2), NOTE_SIZE)
        pygame.draw.circle(screen, WHITE, (int(self.x), HEIGHT // 2), NOTE_SIZE,3)

    def is_miss(self):
        return self.x < 30

    def check_hit(self, type_):
        if self.type == type_ and abs(self.x - HIT_POSITION) < 20:
            global score, hits, combo, f_img
            score += (100+combo*10)
            timing = abs(self.x - HIT_POSITION)
            if timing < 15:
                grade = "良"
                score+=200
                combo+=1
                f_img*=-1
            else:
                grade = "可"
                score+=100
                combo+=1
                f_img*=-1
            #else:
                #grade = "不"
                #combo=0
            hits.append((grade, HIT_POSITION-20, HEIGHT//2 - 100, time.time() + 0.3))  # 1秒表示
            return True
        return False
    
class Rnote:
    def __init__(self,type_,x):
        self.x = x
        self.y=HEIGHT//2
        self.type = type_
        self.color = RED if type_ == "don" else BLUE

    def move(self):
        self.x +=REMOVE_SPEED+4
        self.y-=REMOVE_SPEED
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y) ), NOTE_SIZE)
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), NOTE_SIZE,3)



# --- 譜面生成 ---############################
def spawn_note():
    global time_count,fx,fy
    time_count+=1
    if time_count%time_span == 0 and music[fy][fx] != -1:
        if music[fy][fx] == 1:
            notes.append(Note("don"))
        elif music[fy][fx] == 2:
            notes.append(Note("ka"))
        fx+=1
        if fx == 16:
            fx=0
            fy+=1
    if music[fy][fx] == 4:
        music[fy][fx] = 0
        fx-=3
    if music[fy][fx] == 5:
        music[fy][fx] = 0
        fx-=2
    if music[fy][fx] == 6:
        music[fy][fx] = 0
        fx-=1

# ====== 追加：ゲーム開始前にタイトル画面を呼び出す ======
title_screen()

pygame.mixer.music.load("summer.mp3") 
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=0, start=music_s_time)  # 5秒地点から再生


# --- メインループ ---
running = True
while running:
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, WHITE, (0, HEIGHT//2-40, WIDTH, 2))
    pygame.draw.rect(screen, WHITE, (0, HEIGHT//2+38, WIDTH, 2))



    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # マウス入力
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                hit_type="don"
                don_sound.play()

            else:
                hit_type="ka"
                ka_sound.play()
            remove_list = []
            for note in notes:
                if note.check_hit(hit_type):
                    remove_list.append(note)
                    rnotes.append(Rnote(note.type,note.x))
            for note in remove_list:
                if note in notes:
                    notes.remove(note)
            
                    

        # キーボード入力
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                hit_type = "don"
                don_sound.play()
            elif event.key == pygame.K_j:
                hit_type = "ka"
                ka_sound.play()
            elif event.key == pygame.K_d:
                dontyan*=-1
            else:
                hit_type = None
            if hit_type:
                remove_list = []
                for note in notes:
                    if note.check_hit(hit_type):
                        remove_list.append(note)
                        rnotes.append(Rnote(note.type,note.x))
                for note in remove_list:
                    if note in notes:
                        notes.remove(note)
                        

    # ノーツ生成
    spawn_note()

    # ノーツ移動とMISS判定
    remove_list = []
    for note in notes:
        note.move()
        if note.is_miss():
            remove_list.append(note)
            combo=0
            
    for note in remove_list:
        if note in notes:
            notes.remove(note)

    if rnotes != []:
        for note in rnotes:
            note.move()

    # 判定枠描画
    pygame.draw.circle(screen, WHITE, (HIT_POSITION, HEIGHT // 2), NOTE_SIZE, 3)

    current_time = time.time()
    for h in hits[:]:
        text, x, y, end_time = h
        if current_time > end_time:
            hits.remove(h)
        else:
            if text == '良':
                grade_text = font.render(text, True, GOLD)
            else:
                grade_text = font.render(text, True, WHITE)
            screen.blit(grade_text, (x, y+10))
            


    # スコア表示
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, HEIGHT-60))

    combo_text = font.render(f"combo: {combo}", True, WHITE)
    screen.blit(combo_text, (WIDTH-200, HEIGHT-60))

    if dontyan == 1:
        don_x, don_y = pygame.mouse.get_pos()
        if f_img == -1:
            screen.blit(img0, (don_x-75, don_y-75))
        elif f_img == 1:
            screen.blit(img1, (don_x-75, don_y-75))
    else:
        if f_img == -1:
            screen.blit(img0, (IMG_X, IMG_Y))
        elif f_img == 1:
            screen.blit(img1, (IMG_X, IMG_Y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
