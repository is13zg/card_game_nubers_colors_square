# importing image object from PIL
import math
from PIL import Image, ImageDraw, ImageFont, ImageCms
from io import BytesIO
import random

#colors = {"red": "#fe0000", "yellow": "#ffcc00", "green": "#019934", "blue": "#3401cc", "violet": "#990099","orange": "#ff7513"}





def remove_icc(image: Image.Image) -> Image.Image:
    """
    Убирает у картинки ICC-профиль и ставит обычный sRGB, который не имеет
    проблем с отображением на разных устройствах. Возвращает копию картинки
    с убранным профилем.
    """

    icc_bytes = image.info.get("icc_profile") or b""
    if not icc_bytes:
        # Если ICC-профиля нет, то просто возвращаем копию картинки
        return image.copy()

    # Читаем ICC-профиль из картинки
    orig_icc = ImageCms.getOpenProfile(BytesIO(icc_bytes)).profile
    # Получаем обычный профиль sRGB, в который будем конвертировать
    srgb_icc = ImageCms.createProfile("sRGB")

    # Помогаем Pillow выполнить преобразование цветовых режимов там, где он сам
    # не справляется (из-за необходимости этого преобразования использовать
    # inPlace=True в общем случае не получится)
    mode = image.mode
    tmp_image = None
    if mode == "CMYK":
        mode = "RGB"
    elif mode == "P":
        mode = "RGBA"
        tmp_image = image.convert("RGBA")

    # Создаём сконвертированную копию картинки
    try:
        result = ImageCms.profileToProfile(
            tmp_image or image, orig_icc, srgb_icc, outputMode=mode
        )
    finally:
        if tmp_image is not None:
            tmp_image.close()

    # Удаляем информацию о профиле sRGB, чтобы всякие гимпы
    # не предлагали сконвертировать sRGB в sRGB
    result.info.pop("icc_profile")

    # Имейте в виду, что profileToProfile при создании копии картинки
    # не переносит мета-информацию вроде EXIF. Если она вам нужна, придётся
    # позаботиться о её копировании самостоятельно
    if image.info.get("exif"):
        result.info["exif"] = image.info["exif"]

    return result

def mega_draw(numbers, cls, name):
    colors = {"1": "#fe2712", "2": "#3e01a4", "3": "#68ae34", "4": "#f9bc02"}

    w, h = 587, 587
    border = round(w / 100 * 4)
    line_w = round(w / 100 * 2)
    xw, xh = round(w / 2), round(h / 2)
    border = round(w / 100 * 2.5)
    line_w = round(w / 100 * 2)

    # creating new Image object
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # create rectangle image
    img1 = ImageDraw.Draw(img)

    # draw triangles
    img1.polygon([0, 0, w, 0, xw, xh], fill=colors[cls[0]])
    img1.polygon([0, 0, 0, h, xw, xh], fill=colors[cls[1]])
    img1.polygon([w, h, w, 0, xw, xh], fill=colors[cls[2]])
    img1.polygon([w, h, 0, h, xw, xh], fill=colors[cls[3]])

    # draw diag
    img1.line([(0, 0), (w, h)], fill=(255, 255, 255), width=line_w)
    img1.line([(0, w), (h, 0)], fill=(255, 255, 255), width=line_w)

    # draw border
    img1.rectangle([0, 0, w, border], fill=(255, 255, 255))
    img1.rectangle([0, 0, border, h], fill=(255, 255, 255))
    img1.rectangle([0, h - border, w, h], fill=(255, 255, 255))
    img1.rectangle([w - border, 0, w, h], fill=(255, 255, 255))

    num_size = round(w / 100 * 35)

    # draw number 1
    text_mask = Image.new('RGBA', (num_size, num_size), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", num_size)
    text.text((0, 0), str(numbers[0]), (255, 255, 255), font=font)

    img.paste(text_mask, (xw - round(num_size / 4), xh + round(num_size / 2.5)), text_mask)

    # draw number 2
    text_mask = Image.new('RGBA', (num_size, num_size), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", num_size)
    text.text((0, 0), str(numbers[1]), (255, 255, 255), font=font)
    text_mask2 = text_mask.rotate(-90, expand=True)

    img.paste(text_mask2, (xw - round(num_size / 0.7), xh - round(num_size / 3.1)), text_mask2)

    # draw number 3
    text_mask = Image.new('RGBA', (num_size, num_size), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", num_size)
    text.text((0, 0), str(numbers[2]), (255, 255, 255), font=font)
    text_mask3 = text_mask.rotate(180, expand=True)

    img.paste(text_mask3, (xw - round(num_size / 1.4), xh - round(num_size / 0.7)), text_mask3)

    # draw number 4
    text_mask = Image.new('RGBA', (num_size, num_size), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", num_size)
    text.text((0, 0), str(numbers[3]), (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)

    img.paste(text_mask1, (xw + round(num_size / 2), xh - round(num_size / 1.4)), text_mask1)

    #img = remove_icc(img)
    #2

    img.save(f"res2//{name}.png")

main_ls = [('1', '3', '4', '2'), ('1', '4', '3', '2'), ('1', '4', '2', '3'), ('1', '2', '4', '3'), ('1', '3', '2', '4'), ('1', '2', '3', '4')]

for x in main_ls:
    for y in main_ls:
        mega_draw(x,y,str(x)+str(y))