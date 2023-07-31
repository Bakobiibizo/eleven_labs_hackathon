import asyncio

from image.generate_image import GenerateImage


def test():
    image = GenerateImage()
    image_data = image.generate_image("a hacker encountering a firewall in cyberspace")
    print(image_data)
    return image_data
    
test()
