from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    logo = Component(css='[src="/common/img/procto/logo.png"]')
    title = Component(xpath="//div[contains(text(),'Авторизация')]")
    login = TextField(id="login_id")
    password = TextField(id="pass_id")
    submit = Button(id="arm_oto_id")
    capcha = Component(id="checkKap")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title.visible
                assert self.login.visible
                assert self.password.visible
                assert self.capcha.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
