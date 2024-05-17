from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ApplicationPage']


class ApplicationPage(Page):
    application = Component(xpath="//div[text()='Заявка']")
    notification = Component(xpath="//div[text()='Уведомление']")
    registry = Component(xpath="//div[text()='Реестр']")
    agreement = Component(xpath="//div[text()='Соглашение']")
    transfer = Component(xpath="//div[text()='Перечисление субсидий']")
    root = Component(id="root_action")
    table = Components(class_name='white_tbl_div')
    exit_btn = Button(css='input[value="Выйти"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.application.visible
                assert self.notification.visible
                assert self.registry.visible
                assert self.agreement.visible
                assert self.transfer.visible
                assert self.root.visible
                assert self.exit_btn.visible

                return self.table[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
