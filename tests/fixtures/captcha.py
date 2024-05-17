import os
from typing import Callable

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture
def get_captcha_image(request: FixtureRequest) -> Callable[..., None]:
    def captcha(path: str, image: bytes) -> None:
        with open(path, 'wb') as file:
            file.write(image)

        def finalizer():
            os.remove(path)

        request.addfinalizer(finalizer)

    return captcha
