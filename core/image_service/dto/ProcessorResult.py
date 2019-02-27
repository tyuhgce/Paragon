class ProcessorResult:
    def __init__(self, light_pixels, dark_pixels):
        self.light_pixels = light_pixels
        self.dark_pixels = dark_pixels
        self.is_image_brightness = self.light_pixels >= self.dark_pixels

    light_pixels = 0
    dark_pixels = 0
    is_image_brightness = False
