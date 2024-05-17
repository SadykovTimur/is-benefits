from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.operator_to_page.components.menu import Menu
from dit.qa.pages.subsidies_page.components.tasks import Tasks

__all__ = ['SubsidiesPage']


class SubsidiesPage(Page):
    menu = Menu(css='div[class*="menu_top"]')
    table_subsidies = Component(xpath="//h1[text()='Субсидии ']")
    tasks = Tasks(css="[class*='td_white']")
    search = Component(id='search_form')

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

                assert self.search.visible
                assert self.tasks[0].visible

                return self.table_subsidies.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
