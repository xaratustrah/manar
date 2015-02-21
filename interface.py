from abc import ABCMeta, abstractmethod


class Interface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update_text_field(self, text):
        pass
