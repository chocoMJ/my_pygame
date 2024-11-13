import pygame
from vector import Vector2D
from Sprite import enemy_frame_width, enemy_frame_height, player_frame_height, player_frame_width, stone_height, stone_width


player_half_width = player_frame_width / 2
enemy_half_width = enemy_frame_width / 2
player_half_height = player_frame_height / 2
enemy_half_height = enemy_frame_height / 2

#circle로부터 가장 가까운 정점 찾기
def find_closest_point_on_polygon(circle_center: Vector2D, vertices: list[Vector2D]):
    # Initialize values for closest point search
    result = -1
    min_distance = float('inf')

    for i, v in enumerate(vertices):
        dist = Vector2D.distance(v, circle_center)  # 벡터 간의 거리 계산

        # Update closest distance and index if a nearer point is found
        if dist < min_distance:
            min_distance = dist
            result = i

    # Return index of the closest vertex
    return result

#공격이 적에게 닿았는지 체크, 그리고 공격에 맞은 적의 객체를 담은 list반환
def check_player_attack_collision(player, enemies):
    hit_list = []
    player_centerx = player.rect.centerx
    player_centery = player.rect.centery

    for index, enemy in enumerate(enemies) :
        enemy_centerx = enemy.rect.centerx
        enemy_centery = enemy.rect.centery
        if player.facing_right == True : #플레이어가 바라보는 방향에 따라 공격 범위가 달라야 함
            if 0 < enemy_centerx - player_centerx < player_half_width + enemy_half_width :
                if abs(player_centery - enemy_centery) < player_half_height + enemy_half_height :
                    if enemy.state != 'DEATH' :
                        hit_list.append(index)
        else :
            if 0 < player_centerx - enemy_centerx < player_half_width + enemy_half_width :
                if abs(player_centery - enemy_centery) < player_half_height + enemy_half_height :
                    if enemy.state != 'DEATH' :
                        hit_list.append(index)
    
    return hit_list


#적과 플레이어의 콜리전 체크
def check_player_enemy_collision(player, enemies):
    player_centerx = player.rect.centerx
    player_centery = player.rect.centery

    for index, enemy in enumerate(enemies) :
        if enemy.state == 'DEATH' : continue
        enemy_centerx = enemy.rect.centerx
        enemy_centery = enemy.rect.centery

        #player가 적에게 맞는 판정은, 적이 player의 공격에 맞는 판정보다 작게한다.
        if abs(player_centerx - enemy_centerx) < player_half_width + enemy_half_width - 30 : 
            if abs(player_centery - enemy_centery) < player_half_height + enemy_half_height - 30 :
                player.state = 'DEATH'

#플레이어와 돌덩이의 충돌 체크
def check_player_stone_collision(player, stones) :
    player_centerx = player.rect.centerx
    player_centery = player.rect.centery

    for index, stone in enumerate(stones) :
        stone_centerx = stone.rect.centerx
        stone_centery = stone.rect.centery

        #player가 적에게 맞는 판정은, 적이 player의 공격에 맞는 판정보다 작게한다.
        if abs(player_centerx - stone_centerx) < player_half_width + enemy_half_width - 30 : 
            if abs(player_centery - stone_centery) < player_half_height + enemy_half_height - 30 :
                player.state = 'DEATH'

#stone과 fireball 충돌체크
def check_stone_fireball_collision(stone, fireball): #return 값은 bool값
    if abs(stone.rect.centerx - fireball.rect.centerx) > fireball.radius + stone_width :
        return False
    elif abs(stone.rect.centery - fireball.rect.centery) > fireball.radius + stone_height : 
        return False #X축과 y축에 대해 먼저 확인

    vertices = [
        pygame.math.Vector2(stone.rect.topleft),
        pygame.math.Vector2(stone.rect.topright),
        pygame.math.Vector2(stone.rect.bottomright),
        pygame.math.Vector2(stone.rect.bottomleft)
    ]
    
    cp_index = find_closest_point_on_polygon(pygame.math.Vector2(fireball.rect.center), vertices)
    
    cp = vertices[cp_index]

    axis = (cp-fireball.rect.center).normalize()

    min_a, max_a = project_circle(fireball.rect.center, fireball.radius, axis)
    min_b, max_b = project_vertices(vertices, axis)

    if(max_a <= min_b or max_b <= min_a) :
        return False

    return True

def project_circle(center, radius, axis):
    # Normalize the axis and apply the circle's radius
    direction = axis.normalize()  # 축을 정규화
    direction_and_radius = direction * radius  # 축에 반지름을 곱하여 투영 길이 설정

    # Calculate boundary points on the circle along the axis
    p1 = center + direction_and_radius
    p2 = center - direction_and_radius

    # Calculate projections of the boundary points onto the axis
    min_proj = p1.dot(axis)
    max_proj = p2.dot(axis)

    # Ensure min_proj and max_proj are correctly ordered
    if min_proj > max_proj:
        min_proj, max_proj = max_proj, min_proj

    return min_proj, max_proj

def project_vertices(vertices, axis):
    # Set initial min/max projection values
    min_proj = float('inf')
    max_proj = float('-inf')

    for v in vertices:
        # Calculate projection of vertex on the axis
        proj = v.dot(axis)  # 벡터의 dot product를 사용하여 축에 대한 투영 계산

        # Update min/max projection values
        if proj < min_proj:
            min_proj = proj
        if proj > max_proj:
            max_proj = proj

    # Return the min and max projections
    return min_proj, max_proj