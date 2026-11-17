from PIL import Image

color_table = [
    (0,0,0),
    (0x55,0,0),
    (0xA4,0,0),
    (0xEF,0,0),
]

def extract(file, bytes, width):
    x_mult = 128/width
    y_rows = (((len(bytes)//2)//8)//16)*x_mult

    image = Image.new("RGBA", [width,int(y_rows*8)])

    pixels = []

    i = 0
    while i < len(bytes):
        s = int.from_bytes(bytes[i:i+2], 'little')

        bit = 0
        while bit < 8:
            pixels.append(s & 0b11)
            s >>= 2
            bit += 1

        i += 2

    i = 0
    for tile_y in range(image.size[1]//8):
        for tile_x in range(image.size[0]//8):
            for y in range(8):
                for x in range(8):
                    if i >= len(pixels):
                        break
                    image.putpixel(((tile_x*8)+x,(tile_y*8)+y), color_table[pixels[i]])
                    i += 1

    image.save(f'extract/{file}.png')