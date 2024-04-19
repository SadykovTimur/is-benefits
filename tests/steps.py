import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach

from dit.qa.pages.start_map_page import StartMapPage
from dit.qa.pages.start_page import StartPage

__all__ = ['open_start_page', 'open_map_page']


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
