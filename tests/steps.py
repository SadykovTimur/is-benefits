from typing import Callable
from uuid import uuid4

import allure
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.application_page import ApplicationPage
from dit.qa.pages.helpers.captcha_helper import resolve_captcha
from dit.qa.pages.operator_to_page import OperatorTOPage
from dit.qa.pages.start_map_page import StartMapPage
from dit.qa.pages.start_page import StartPage
from dit.qa.pages.subsidies_page import SubsidiesPage

__all__ = [
    'open_start_page',
    'sign_in',
    'open_operator_to_page',
    'open_map_page',
    'open_subsidies_page',
    'open_application',
    'logout_application',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def sign_in(app: Application, request: FixtureRequest, get_captcha_image: Callable[..., None]) -> None:
    login = request.config.option.username
    password = request.config.option.password
    url = request.config.option.captcha_url

    with allure.step(f'{login} signing in'):
        try:
            path = f'{uuid4().hex}.png'
            page = StartPage(app)

            page.login.send_keys(login)
            page.password.send_keys(password)

            get_captcha_image(path, page.captcha_image.webelement.screenshot_as_png)
            solution = resolve_captcha(path, url)
            page.captcha.send_keys(solution)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        page.submit.click()


def open_operator_to_page(app: Application) -> None:
    with allure.step('Opening OperatorTO page'):
        try:
            OperatorTOPage(app).wait_for_loading()

            screenshot_attach(app, 'operator_to_page')
        except Exception as e:
            screenshot_attach(app, 'operator_to_page_error')

            raise TimeoutError('OperatorTO page was not loaded') from e


def open_subsidies_page(app: Application) -> None:
    with allure.step('Opening Subsidies page'):
        try:
            OperatorTOPage(app).menu.subsidies.click()
            SubsidiesPage(app).wait_for_loading()

            screenshot_attach(app, 'subsidies_page')
        except Exception as e:
            screenshot_attach(app, 'subsidies_page_error')

            raise TimeoutError('Subsidies page was not loaded') from e


def open_application(app: Application) -> None:
    with allure.step('Opening Application'):
        try:
            field = SubsidiesPage(app).tasks[0].fields[2]
            field.wait_for_clickability()
            field.webelement.click()

            ApplicationPage(app).wait_for_loading()

            screenshot_attach(app, 'application')
        except Exception as e:
            screenshot_attach(app, 'application_error')

            raise TimeoutError('Application was not loaded') from e


def logout_application(app: Application) -> None:
    with allure.step('Logout Application'):
        try:
            ApplicationPage(app).exit_btn.click()
            SubsidiesPage(app).wait_for_loading()

            screenshot_attach(app, 'logout_application')
        except Exception as e:
            screenshot_attach(app, 'logout_application_error')

            raise TimeoutError('Application page was not closed') from e


def open_map_page(app: Application) -> None:
    with allure.step('Opening Map page'):
        try:
            page = StartMapPage(app)
            page.base_url = 'https://lgotato.mos.ru'
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'map_page')
        except Exception as e:
            screenshot_attach(app, 'map_page_error')

            raise TimeoutError('Map page was not loaded') from e
