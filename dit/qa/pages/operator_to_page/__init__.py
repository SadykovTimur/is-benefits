from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.operator_to_page.components.menu import Menu

__all__ = ['OperatorTOPage']


class OperatorTOPage(Page):
    menu = Menu(css='div[class*="menu_top"]')
    exit = Component(xpath="//span[text()='Выйти']")
    operator_to = Component(xpath="//h1[text()='Операторы ТО']")
    filter = Component(id="filter_app")
    table = Component(class_name='white_tbl_div')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.subsidies.visible
                assert self.menu.control.visible
                assert self.menu.operator_to.visible
                assert self.menu.conduct_to.visible
                assert self.menu.report.visible
                assert self.menu.payment.visible
                assert self.menu.management.visible
                assert self.menu.change_password.visible

                assert self.operator_to.visible
                assert self.filter.visible
                assert self.table.visible

                return self.exit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
