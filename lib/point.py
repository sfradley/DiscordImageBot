from PIL import Image, ImageFont, ImageDraw
import warnings

warnings.filterwarnings(action='ignore')


class Farquaad:
    def __init__(self, file, font):
        self.file = file
        self.font = font

    def add_text(self, s: str) -> Image:
        img = Image.open(self.file)

        img_fraction = 0.9
        fontsize = 1
        font = ImageFont.truetype(self.font, fontsize)

        while font.getsize(s)[0] < img_fraction * img.size[0] and fontsize <= 96:
            fontsize += 1
            font = ImageFont.truetype(self.font, fontsize)

        font = ImageFont.truetype(self.font, fontsize)

        draw = ImageDraw.Draw(img)

        draw.text((img.width // 2, img.height // 25),
                  s,
                  anchor='mt',
                  fill='white',
                  stroke_fill='black',
                  stroke_width=4,
                  font=font
                  )
        return img
