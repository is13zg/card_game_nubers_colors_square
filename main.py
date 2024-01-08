# importing image object from PIL
import math
from PIL import Image, ImageDraw, ImageFont
import random


def mega_draw(numbers, cls, name):
    colors = {"red": "#fe0000", "yellow": "#ffcc00", "green": "#019934", "blue": "#3401cc", "violet": "#990099",
              "orange": "#ff7513"}

    cls = list(cls)
    random.shuffle(cls)
    w, h = 772, 772
    border = round(w / 100 * 4)
    line_w = round(w / 100 * 2)
    xw, xh = round(w / 2), round(h / 2)
    border = round(w / 100 * 3)
    line_w = round(w / 100 * 2)

    # creating new Image object
    img = Image.new("RGB", (w, h), (255, 255, 255))

    # create rectangle image
    img1 = ImageDraw.Draw(img)

    img1.rectangle([border, border, border + xw, border + xh], fill=colors[cls[0]])
    img1.rectangle([border * 3 + xw, border, border * 3 + xw * 2, border + xh], fill=colors[cls[1]])
    img1.rectangle([border, border * 3 + xh, border + xw, border * 3 + xh * 2], fill=colors[cls[2]])
    img1.rectangle([border * 3 + xw, border * 3 + xh, border * 3 + xw * 2, border * 3 + xh * 2], fill=colors[cls[3]])

    # draw numbers

    # draw number 1
    text_mask = Image.new('RGBA', (90, 130), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)
    text.text((0, 0), str(numbers[0]), (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste left_up
    img.paste(text_mask1, (237, 150), text_mask1)
    img.paste(text_mask2, (17, 140), text_mask2)
    img.paste(text_mask, (145, 235), text_mask)
    img.paste(text_mask3, (150, 18), text_mask3)

    # draw number 2
    text_mask = Image.new('RGBA', (90, 130), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)
    text.text((0, 0), str(numbers[2]), (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste right_up
    img.paste(text_mask1, (621, 150), text_mask1)
    img.paste(text_mask2, (401, 140), text_mask2)
    img.paste(text_mask, (529, 235), text_mask)
    img.paste(text_mask3, (534, 18), text_mask3)

    # draw number 3
    text_mask = Image.new('RGBA', (90, 130), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)
    text.text((0, 0), str(numbers[2]), (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste left_down
    img.paste(text_mask1, (237, 534), text_mask1)
    img.paste(text_mask2, (17, 524), text_mask2)
    img.paste(text_mask, (145, 619), text_mask)
    img.paste(text_mask3, (150, 402), text_mask3)

    # draw number 4
    text_mask = Image.new('RGBA', (90, 130), (0, 0, 0, 0))
    text = ImageDraw.Draw(text_mask)
    font = ImageFont.truetype("myraidpro.ttf", 150)
    text.text((0, 0), str(numbers[3]), (255, 255, 255), font=font)
    text_mask1 = text_mask.rotate(90, expand=True)
    text_mask2 = text_mask.rotate(-90, expand=True)
    text_mask3 = text_mask.rotate(180, expand=True)

    # paste right_down
    img.paste(text_mask1, (621, 534), text_mask1)
    img.paste(text_mask2, (401, 524), text_mask2)
    img.paste(text_mask, (529, 619), text_mask)
    img.paste(text_mask3, (534, 402), text_mask3)

    # draw web
    img1.line([(0, 0), (w, h)], fill=(255, 255, 255), width=2)
    img1.line([(0 - 6, w), (h - 6, 0)], fill=(255, 255, 255), width=2)

    img1.line([(0, h / 2 - 3), (w / 2, h - 3)], fill=(255, 255, 255), width=2)
    img1.line([(w / 2 - 3, 0), (w - 3, h / 2)], fill=(255, 255, 255), width=2)

    img1.line([(0, h / 2 - 3), (w / 2, 0 - 3)], fill=(255, 255, 255), width=2)
    img1.line([(w / 2, h - 9), (w, h / 2 - 9)], fill=(255, 255, 255), width=2)

    # Обрезка
    img = img.crop((0, 0, 768, 768))

    img.save(f"res\\{name}.png")


num_ls = [(0, 1, 2, 3),
          (1, 3, 2, 4),
          (4, 3, 2, 0),
          (2, 0, 1, 4),
          (1, 2, 3, 5),
          (7, 1, 0, 5),
          (6, 5, 0, 7),
          (6, 1, 4, 8),
          (9, 5, 3, 1),
          (7, 1, 4, 6),
          (3, 5, 2, 8),
          (6, 0, 2, 9),
          (4, 3, 2, 0),
          (2, 0, 1, 4),
          (0, 1, 2, 3),
          (1, 2, 3, 5),
          (1, 3, 2, 4),
          (1, 2, 1, 3),
          (2, 4, 2, 1),
          (2, 3, 1, 5),
          (4, 1, 2, 3),
          (5, 4, 2, 1),
          (4, 5, 3, 3),
          (4, 1, 2, 3),
          (5, 4, 2, 1),
          (4, 5, 3, 3),
          (1, 2, 3, 5),
          (7, 1, 4, 6),
          (2, 3, 1, 5),
          (2, 0, 1, 4),
          (4, 3, 2, 0),
          (7, 1, 2, 3),
          (1, 3, 2, 4),
          (1, 2, 1, 3),
          (4, 3, 2, 8),
          (2, 0, 1, 4),
          (4, 1, 2, 3),
          (1, 3, 2, 4),
          (1, 2, 3, 5),
          (4, 1, 2, 3),
          (2, 4, 2, 1),
          (7, 1, 9, 5),
          (0, 1, 2, 3),
          (6, 0, 2, 9),
          (9, 5, 3, 1),
          (6, 1, 4, 8),
          (6, 5, 6, 7),
          (3, 5, 2, 8)]
cls_ls = [("red", "orange", "yellow", "blue"),
          ("red", "orange", "yellow", "green"),
          ("red", "orange", "yellow", "violet"),
          ("red", "orange", "blue", "green"),
          ("red", "orange", "blue", "violet"),
          ("red", "orange", "green", "violet"),
          ("red", "yellow", "blue", "green"),
          ("red", "yellow", "blue", "violet"),
          ("red", "yellow", "green", "violet"),
          ("red", "blue", "green", "violet"),
          ("orange", "yellow", "blue", "green"),
          ("orange", "yellow", "blue", "violet"),
          ("orange", "yellow", "green", "violet"),
          ("orange", "blue", "green", "violet"),
          ("yellow", "blue", "green", "violet"),
          ("red", "orange", "yellow", "blue"),
          ("red", "orange", "yellow", "green"),
          ("red", "orange", "yellow", "violet"),
          ("red", "orange", "blue", "green"),
          ("red", "orange", "blue", "violet"),
          ("red", "orange", "green", "violet"),
          ("red", "yellow", "blue", "green"),
          ("red", "yellow", "blue", "violet"),
          ("red", "yellow", "green", "violet"),
          ("red", "blue", "green", "violet"),
          ("orange", "yellow", "blue", "green"),
          ("orange", "yellow", "blue", "violet"),
          ("orange", "yellow", "green", "violet"),
          ("orange", "blue", "green", "violet"),
          ("yellow", "blue", "green", "violet"),
          ("red", "orange", "yellow", "blue"),
          ("red", "orange", "yellow", "green"),
          ("red", "orange", "yellow", "violet"),
          ("red", "orange", "blue", "green"),
          ("red", "orange", "blue", "violet"),
          ("red", "orange", "green", "violet"),
          ("red", "yellow", "blue", "green"),
          ("red", "yellow", "blue", "violet"),
          ("red", "yellow", "green", "violet"),
          ("red", "blue", "green", "violet"),
          ("orange", "yellow", "blue", "green"),
          ("orange", "yellow", "blue", "violet"),
          ("orange", "yellow", "green", "violet"),
          ("orange", "blue", "green", "violet"),
          ("yellow", "blue", "green", "violet"),
          ("red", "orange", "green", "violet"),
          ("red", "yellow", "blue", "green"),
          ("red", "yellow", "blue", "violet")]

for x in range(48):
    mega_draw(num_ls[x], cls_ls[x], "card_" + str(x))
