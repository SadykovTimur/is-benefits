from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.start_map_page.components.map import Map

__all__ = ['StartMapPage']


class StartMapPage(Page):
    header = Component(id="header")
    map = Map(id="map")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.visible
                assert self.map.title.visible
                assert self.map.dropdown.visible
                assert self.map.map.visible

                return self.map.menu.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
