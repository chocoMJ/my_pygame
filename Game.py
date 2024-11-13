import pygame
import random
import sys
from pygame.locals import *
from Ground import *
from Player import *
from Mushroom import *
from Goblin import *
from Flying_eye import *
from Skeleton import *
from Collider import *
from Stone import *
from Fireball import *

# Initialize pygame
pygame.init()

FPS = 60
CLOCK = pygame.time.Clock()

#display
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Surviving from Death_Forest')

def MainMenu():
    menu_open = True
    while menu_open:
        render_ground(dis)  # 배경 색 설정
        font = pygame.font.Font(None, 36)  # 기본 폰트와 크기 설정
        title_text = font.render("Surviving from Death_Forest", True, (255, 255, 255))
        prompt_text = font.render("Press 1 to Start, 2 to Quit", True, (255, 255, 255))
        
        # 설명서
        controls_text = font.render("Arrow keys to move", True, (255, 255, 255))
        attack_text = font.render("SPACE to attack", True, (255, 255, 255))
        objective_text = font.render("Survive by breaking stones with UP key!", True, (255, 255, 255))

        dis.blit(title_text, (display_width // 2 - title_text.get_width() // 2, display_height // 4 - 50))
        dis.blit(prompt_text, (display_width // 2 - prompt_text.get_width() // 2, display_height // 2 - 50))

        dis.blit(controls_text, (display_width // 2 - controls_text.get_width() // 2, display_height // 2))
        dis.blit(attack_text, (display_width // 2 - attack_text.get_width() // 2, display_height // 2 + 40))
        dis.blit(objective_text, (display_width // 2 - objective_text.get_width() // 2, display_height // 2 + 80))

        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # 1번 키로 게임 시작
                    menu_open = False
                elif event.key == pygame.K_2:  # 2번 키로 종료
                    pygame.quit()
                    sys.exit()

def GameOverScreen(score):
    game_over = True
    font = pygame.font.Font(None, 36)

    while game_over:
        render_ground(dis)
        
        game_over_text = font.render("Game Over!", True, (255, 0, 0))
        score_display_text = font.render(f"Your score: {score}", True, (255, 255, 255))
        restart_text = font.render("Press 1 to Restart, 2 to Quit", True, (255, 255, 255))

        dis.blit(game_over_text, (display_width // 2 - game_over_text.get_width() // 2, display_height // 3))
        dis.blit(score_display_text, (display_width // 2 - score_display_text.get_width() // 2, display_height // 3 + 50))
        dis.blit(restart_text, (display_width // 2 - restart_text.get_width() // 2, display_height // 2))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:  # 1번키로 재시작
                    return  
                elif event.key == pygame.K_2:  # 2번 키로 나가기
                    pygame.quit()
                    sys.exit()

def GameLoop():
    difficulty = 0
    game_over = False
    score = 0  # 점수 초기화

    player = Player.Player()
    mushrooms = []
    goblins = []
    flying_eyes = []
    skeletons = []
    fireballs = []
    stones = []

    font = pygame.font.Font(None, 36)  # 점수 텍스트를 위한 폰트 설정

    while not game_over:
        if player.is_death:
            GameOverScreen(score)
            return

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        render_ground(dis)

        mushroom_hit = []
        goblin_hit = []
        skeleton_hit = []
        flying_eye_hit = []
        
        # 적을 일정 확률로 스폰
        spawn_chance = 0.003
        if random.random() < spawn_chance:
            mushrooms.append(Mushroom(spawn_point=random.randint(0, 1)))
        if random.random() < spawn_chance:
            goblins.append(Goblin(spawn_point=random.randint(0, 1)))
        if random.random() < spawn_chance:
            skeletons.append(Skeleton(spawn_point=random.randint(0, 1)))
        if random.random() < spawn_chance:
            flying_eyes.append(Flying_eye(spawn_point=random.randint(0, 1)))
        if random.random() < spawn_chance:
            stones.append(Stone(spawn_point=random.randint(0, 1), y=random.random() * 150))

        # ATTACK 상태일 때 근처 적을 타격
        if player.state == "ATTACK":
            mushroom_hit = check_player_attack_collision(player, mushrooms)
            goblin_hit = check_player_attack_collision(player, goblins)
            skeleton_hit = check_player_attack_collision(player, skeletons)
            flying_eye_hit = check_player_attack_collision(player, flying_eyes)
        
        #타격당한 적의 is_hit값을 True로 설정
        for index in mushroom_hit:
            mushrooms[index].is_hit = True
        for index in goblin_hit:
            goblins[index].is_hit = True
        for index in skeleton_hit:
            skeletons[index].is_hit = True
        for index in flying_eye_hit:
            flying_eyes[index].is_hit = True

        # 상태 업데이트
        player.update()

        #파이어볼 사용 시 파이어볼 생성
        if player.is_use_fireball:
            player.is_use_fireball = False
            fireballs.append(Fireball(player.rect.centerx, player.rect.centery - 32))

        #플레이어와 적의 충돌 체크
        check_player_enemy_collision(player, mushrooms)
        check_player_enemy_collision(player, goblins)
        check_player_enemy_collision(player, skeletons)
        check_player_enemy_collision(player, flying_eyes)
        check_player_stone_collision(player, stones)

        #파이어볼과 돌덩이 충돌 체크
        for i in range(len(fireballs)):
            for j in range(len(stones)):
                if check_stone_fireball_collision(stones[j], fireballs[i]):
                    stones[j].is_destroy = True
                    score += 1  # 점수 증가

        # 적 및 파이어볼 업데이트
        for i in sorted(range(len(mushrooms)), reverse=True):
            mushrooms[i].update()
            if mushrooms[i].is_death:
                mushrooms.pop(i)
                score += 1  

        for i in sorted(range(len(goblins)), reverse=True):
            goblins[i].update()
            if goblins[i].is_death:
                goblins.pop(i)
                score += 1  

        for i in sorted(range(len(skeletons)), reverse=True):
            skeletons[i].update()
            if skeletons[i].is_death:
                skeletons.pop(i)
                score += 1  

        for i in sorted(range(len(flying_eyes)), reverse=True):
            flying_eyes[i].update()
            if flying_eyes[i].is_death:
                flying_eyes.pop(i)
                score += 1 
            elif flying_eyes[i].rect.x < 0 or flying_eyes[i].rect.x > 550 :
                flying_eyes.pop(i)
                score -= 1

        for i in sorted(range(len(fireballs)), reverse=True):
            fireballs[i].update()
            if fireballs[i].is_destroy:
                fireballs.pop(i)

        for i in sorted(range(len(stones)), reverse=True):
            stones[i].update()
            if stones[i].is_destroy:
                stones.pop(i)

        # 점수 표시
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))  # 검은 글자
        dis.blit(score_text, (display_width - score_text.get_width() - 10, 10))  # 우측 상단에 표시

        # display 업데이트
        dis.blit(player.image, player.rect)
        for i in range(len(mushrooms)):
            dis.blit(mushrooms[i].image, mushrooms[i].rect)
        for i in range(len(goblins)):
            dis.blit(goblins[i].image, goblins[i].rect)
        for i in range(len(skeletons)):
            dis.blit(skeletons[i].image, skeletons[i].rect)
        for i in range(len(flying_eyes)):
            dis.blit(flying_eyes[i].image, flying_eyes[i].rect)
        for i in range(len(fireballs)):
            dis.blit(fireballs[i].image, fireballs[i].rect)
        for i in range(len(stones)):
            dis.blit(stones[i].image, stones[i].rect)
        
        pygame.display.update()
        CLOCK.tick(FPS)

        while game_over:
            render_ground(dis)
        
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            score_display_text = font.render(f"Your score: {score}", True, (255, 255, 255))
            restart_text = font.render("Press 1 to Restart, 2 to Quit", True, (255, 255, 255))

            dis.blit(game_over_text, (display_width // 2 - game_over_text.get_width() // 2, display_height // 3))
            dis.blit(score_display_text, (display_width // 2 - score_display_text.get_width() // 2, display_height // 3 + 50))
            dis.blit(restart_text, (display_width // 2 - restart_text.get_width() // 2, display_height // 2))

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:  # 1번 키로 게임 재시작
                        return  # 게임 루프 탈출하여 MainMenu로 복귀
                    elif event.key == pygame.K_2:  # 2번 키로 종료
                        pygame.quit()
                        sys.exit()

while True:
    MainMenu()
    GameLoop()