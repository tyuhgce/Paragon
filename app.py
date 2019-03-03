from sanic import Sanic
from sanic.response import json
from sanic.log import logger

from core.image_service.dto.ImageData import ImageData
from core.paragon_facade import ParagonCore


def get_file_bytes(request):
    key = next(iter(request.files))
    if len(request.files) > 0 and key is not None:
        return request.files[key][0][1]
    raise ValueError('error', "can't parse the file from request")


app = Sanic('app')
app.static('/', './index.html')
paragon = ParagonCore()


@app.route("/ping")
async def test(request):
    return json("pong")


@app.route('/image', methods=['OPTIONS', 'GET', 'POST'])
async def image(request):
    try:
        r = paragon.prepare_image(
            ImageData(
                get_file_bytes(request),
                int(request.form['naturalWidth'][0]),
                int(request.form['naturalHeight'][0])
            ))
        return json(
            {
                'code ': 200,
                'light ': r[0],
                'dark ': r[1],
                'decision ': r[2],
            }
        )
    except Exception as error:
        logger.error('image method fell with exception: %s' % error)
        return json({
            'error': 'something went wrong, please try again later!'
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
