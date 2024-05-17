from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    subsidies = Button(xpath="//div[text()='СУБСИДИИ']")
    control = Button(xpath="//div[text()='КОНТРОЛЬ']")
    report = Button(xpath="//div[text()='ОТЧЕТЫ']")
    operator_to = Component(xpath="//div[text()='ОПЕРАТОРЫ ТО']")
    conduct_to = Component(xpath="//div[text()='ПРОВЕДЕННЫЕ ТО']")
    payment = Component(xpath="//div[text()='ПЛАТЕЖНЫЕ РЕКВИЗИТЫ']")
    management = Component(xpath="//div[text()='РУКОВОДСТВО']")
    change_password = Component(xpath="//div[text()='СМЕНА ПАРОЛЯ'] ")


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
