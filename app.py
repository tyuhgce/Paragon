from sanic import Sanic
from sanic.response import json

from core.paragon_facade import ParagonCore


def get_file_bytes(request):
    return request.files['fileToUpload'][0][1]


app = Sanic()
app.static('/index.html', './index.html')
paragon = ParagonCore()


@app.route("/ping")
async def test(request):
    return json("pong")


@app.route('/image', methods=['OPTIONS', 'GET', 'POST'])
async def image(request):
    image_data = get_file_bytes(request)
    r = paragon.prepare_image(image_data)
    return json(
        {
            'code ': 200,
            'decision ': r.is_image_brightness,
            'light ': r.light_pixels,
            'dark ': r.dark_pixels
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
