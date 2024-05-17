from typing import List

from coms.qa.frontend.pages.component import Components, ComponentWrapper

__all__ = ['Tasks']


class TaskWrapper(ComponentWrapper):
    fields = Components(tag="td")


class Tasks(Components):
    def __get__(self, instance, owner):
        ret: List[TaskWrapper] = []

        for webelement in self.finds(instance):
            ret.append(TaskWrapper(instance.app, webelement, self._locator))

        return ret
