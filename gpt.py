from PIL import Image, ImageDraw, ImageFont

# Создаем изображение и контекст для рисования
width, height = 400, 400
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Функция для рисования треугольника определенного цвета с числом в центре
def draw_triangle(color, number, x, y):
    draw.polygon([(x, y), (x + 50, y), (x + 25, y + 43)], fill=color)
    font = ImageFont.truetype("arial.ttf", 20)
    text = str(number)
    text_size = draw.textsize(text, font)
    text_width, text_height = text_size
    text_x = x + (50 - text_width) / 2
    text_y = y + (43 - text_height) / 2
    draw.text((text_x, text_y), text, fill="black", font=font)

# Рисуем квадрат с треугольниками
for i in range(1, 5):
    x = 100 * (i % 2)
    y = 100 * (i // 3)
    if i == 1:
        draw_triangle("red", i, x + 10, y + 10)
    elif i == 2:
        draw_triangle("blue", i, x + 10, y + 10)
    elif i == 3:
        draw_triangle("green", i, x + 10, y + 10)
    else:
        draw_triangle("yellow", i, x + 10, y + 10)

# Сохраняем изображение
image.save("output.png")
