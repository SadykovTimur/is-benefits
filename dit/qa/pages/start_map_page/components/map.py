from coms.qa.frontend.pages.component import Component, ComponentWrapper

__all__ = ['Map']


class MapWrapper(ComponentWrapper):
    title = Component(xpath="//ymaps[text()='Список пунктов ТО']")
    dropdown = Component(class_name="dropdown")
    menu = Component(id="menu")
    map = Component(css="[class*='events-pane']")


class Map(Component):
    def __get__(self, instance, owner) -> MapWrapper:
        return MapWrapper(instance.app, self.find(instance), self._locator)
