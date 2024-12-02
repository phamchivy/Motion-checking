import pygame
from utils.button import Button  # Import Button từ utils
from utils.title import *
from utils.background import *
from utils.text import *
import sys

# Hàm hiển thị hướng dẫn
def show_instructions(screen):

    SCREEN_WIDTH = 800
    font_path="../assets/fonts/Gamefont.ttf"
    text_path="../assets/fonts/Text.ttf"
    title_font = pygame.font.Font(font_path, 40)
    back_font = pygame.font.Font(font_path, 30)

    # Màu sắc
    NAVY = (25, 25, 112)
    LIGHT_PINK = (255, 182, 193)
    HOVER= (245, 162, 173)

    # Tạo đối tượng Title
    instruction_title = Title(
        text="Instruction:", 
        font=title_font, 
        color=LIGHT_PINK, 
        position=(SCREEN_WIDTH // 4.5, 70), 
        glow=True, 
        glow_color=(255, 223, 0), 
        glow_radius=15
    )

    # Nội dung hướng dẫn
    instructions = [
        "1. Rehabilitation: Thực hiện các động tác tay theo yêu cầu để phục hồi chức năng tay. Game sẽ theo dõi các cử động và cung cấp phản hồi khi bạn thực hiện đúng động tác.",
        "2. Gym: Chỉnh sửa tư thế khi thực hiện các bài tập thể dục. Game giúp bạn duy trì tư thế đúng để tránh chấn thương và cải thiện hiệu quả tập luyện.",
        "3. Challenge: Thử thách High Knees vui vẻ cùng với mọi người và lưu lại kết quả nhé."
    ]

    while True:
        draw_gradient(screen, (173, 216, 230), (255, 240, 245))

        font = pygame.font.Font(font_path, 40)
        text_font=pygame.font.Font(text_path, 20)
        back_button = Button("Back", 650, 500, 100, 50, LIGHT_PINK, HOVER)

        instruction_title.draw(screen)
        # Vẽ hướng dẫn lên màn hình
        y_pos = 60  # Vị trí bắt đầu từ trên màn hình
        show_text(screen,y_pos,instructions,SCREEN_WIDTH)
        
        back_button.is_hovered()
        back_button.draw(screen, back_font)

        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if back_button.is_clicked(event):
                return  # Trở về menu chính khi nhấn nút Back

        # Cập nhật màn hình
        pygame.display.flip()
