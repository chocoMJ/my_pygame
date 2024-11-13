import pygame

sprite_sheet = pygame.image.load("img/char_blue.png")

#캐릭터 프레임
player_frame_width = 56  # 각 프레임의 너비
player_frame_height = 56  # 각 프레임의 높이

idle_frames = [] #가만히 서있는 경우, 이번 게임은 1개의 프레임 만을 사용
walk_frames = []
attack_frames = []
death_frames = []

rect = pygame.Rect(0,0,player_frame_width,player_frame_height)
frame = sprite_sheet.subsurface(rect)
idle_frames.append(frame)

for i in range(0, 6) :
    rect = pygame.Rect(i * player_frame_width, player_frame_height * 1, player_frame_width, player_frame_height)  # x 위치를 반복적으로 증가
    frame = sprite_sheet.subsurface(rect)
    attack_frames.append(frame)

for i in range(0,8):
    rect = pygame.Rect(i * player_frame_width, player_frame_height * 2, player_frame_width, player_frame_height)  # x 위치를 반복적으로 증가
    frame = sprite_sheet.subsurface(rect)
    walk_frames.append(frame)

for i in range(0,8):
    rect = pygame.Rect(i * player_frame_width, player_frame_height * 5, player_frame_width, player_frame_height)  # x 위치를 반복적으로 증가
    frame = sprite_sheet.subsurface(rect)
    death_frames.append(frame)

for i in range(0,4):
    rect = pygame.Rect(i * player_frame_width, player_frame_height * 6, player_frame_width, player_frame_height)  # x 위치를 반복적으로 증가
    frame = sprite_sheet.subsurface(rect)
    death_frames.append(frame)

idle_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in idle_frames]
attack_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in attack_frames]
walk_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in walk_frames]
death_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in death_frames]


#Mushroom Enemy Run 처리
sprite_sheet = pygame.image.load("img/mushroom/Mushroom_Run.png")

#Mushroom 프레임
enemy_frame_width = 50  # 각 프레임의 너비
enemy_frame_height = 50  # 각 프레임의 높이

mushroom_walk_frames = [] #8개
mushroom_death_frames = [] #4개

for i in range(0,24) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        mushroom_walk_frames.append(frame)

#Mushroom Enemy Death 처리
sprite_sheet = pygame.image.load("img/mushroom/Mushroom_Death.png")

for i in range(0,12) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        mushroom_death_frames.append(frame)

mushroom_walk_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in mushroom_walk_frames]
mushroom_death_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in mushroom_death_frames]

#Skeleton Enemy Run 처리
sprite_sheet = pygame.image.load("img/Skeleton/Walk.png")

skeleton_walk_frames = [] 
skeleton_death_frames = []
skeleton_shield_frames = [] #한개의 프레임만 사용할 예정

for i in range(0,12) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        skeleton_walk_frames.append(frame)

#Skeleton Enemy Death 처리
sprite_sheet = pygame.image.load("img/Skeleton/Death.png")

for i in range(0,12) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        skeleton_death_frames.append(frame)

#skeleton Enemy Shield 처리
frame = pygame.image.load("img/Skeleton/Shield[0].png")
skeleton_shield_frames.append(frame)

skeleton_walk_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in skeleton_walk_frames]
skeleton_death_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in skeleton_death_frames]
skeleton_shield_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in skeleton_shield_frames]


#Goblin Enemy Run 처리
sprite_sheet = pygame.image.load("img/Goblin/Run.png")

Goblin_Run_frames = [] 
Goblin_Death_frames = []

for i in range(0,24) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        Goblin_Run_frames.append(frame)

#Goblin Enemy Death 처리
sprite_sheet = pygame.image.load("img/Goblin/Death.png")

for i in range(0,12) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        Goblin_Death_frames.append(frame)

Goblin_Run_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in Goblin_Run_frames]
Goblin_Death_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in Goblin_Death_frames]


#Flying_eye 처리 시작

Flying_eye_Flight_frames = [] 
Flying_eye_Death_frames = []

#Flying_eye Flight 처리
sprite_sheet = pygame.image.load("img/Flying_eye/Flight.png")

for i in range(0,24) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        Flying_eye_Flight_frames.append(frame)

#Flying_eye Enemy Death 처리
sprite_sheet = pygame.image.load("img/Flying_eye/Death.png")

for i in range(0,12) :
    if i % 3 == 1:
        rect = pygame.Rect(i * enemy_frame_width, 50, enemy_frame_width, enemy_frame_height)
        frame = sprite_sheet.subsurface(rect)
        Flying_eye_Death_frames.append(frame)

Flying_eye_Flight_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in Flying_eye_Flight_frames]
Flying_eye_Death_frames_flipped = [pygame.transform.flip(frame, True, False) for frame in Flying_eye_Death_frames]

#Fireball 발사 스프라이트 처리

fireball_frames = []
for i in range(0,5):
    frame = pygame.image.load("img/fireball/FB500-" + str(i + 1) + ".png")
    scaled_frame = pygame.transform.scale(frame, (56, 56))
    fireball_frames.append(scaled_frame)

#Fireball 피격 스프라이트 처리

fireball_boom_frames = []
for i in range(0,3):
    frame = pygame.image.load("img/fireball/B500-" + str(i + 2) + ".png")
    scaled_frame = pygame.transform.scale(frame, (56, 56))
    fireball_boom_frames.append(scaled_frame)

#Stone image 처리
stone_width = 32
stone_height = 32
stone_image = pygame.image.load("img/stone.png")
stone_image = pygame.transform.scale(stone_image, (stone_width,stone_height))