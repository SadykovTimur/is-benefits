from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_operator_to_page, open_start_page, open_subsidies_page, sign_in


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('IS-BENEFITS')
@allure.story('Раздел "Субсидии"')
@allure.title('Переход в раздел "Субсидии"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_transition_subsidies(
    request: FixtureRequest,
    get_captcha_image: Callable[..., None],
    make_app: Callable[..., Application],
    browser: str,
    device_type: str,
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)

    sign_in(app, request, get_captcha_image)
    open_operator_to_page(app)

    open_subsidies_page(app)
