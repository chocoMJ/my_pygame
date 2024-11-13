import pygame
from pygame.locals import *

# 변수 설정
display_width = 600
display_height = 480
tile_width = 24
tile_height = 24

# 배경 이미지 로드 및 크기 조정
def load_and_scale_background(path):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, (display_width, display_height))

background1 = load_and_scale_background("img/background_layer_1.png")
background2 = load_and_scale_background("img/background_layer_2.png")
background3 = load_and_scale_background("img/background_layer_3.png")
tileset_image = pygame.image.load('img/oak_woods_tileset.png')

# 타일을 얻는 함수
def get_tile(x, y):
    rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
    return tileset_image.subsurface(rect)

def render_ground(dis):
    #background 그리기
    dis.blit(background1, (0, 0))
    dis.blit(background2, (0, 0))
    dis.blit(background3, (0, 0))

    # 타일 가져와서 그리기
    y_offsets = [4, 3, 2, 1]
    tile_y_values = [0, 1, 1, 3]
    
    for y_offset, tile_y in zip(y_offsets, tile_y_values): #4층에 걸쳐 바닥 생성 예정
        y = display_height - (y_offset * tile_height)
        dis.blit(get_tile(0, tile_y), (0, y))
        for i in range(1, int(display_width / tile_width) - 1):
            dis.blit(get_tile(1, tile_y), (i * tile_width, y))
        dis.blit(get_tile(3, tile_y), (display_width - tile_width, y))
