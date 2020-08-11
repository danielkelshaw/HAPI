from typing import NoReturn, Tuple
from .user import User


class Controller:

    def __init__(self, user: User) -> None:
        self.user = user

    def get_lights(self) -> NoReturn:
        raise NotImplementedError('Controller::get_lights()')

    def get_groups(self) -> NoReturn:
        raise NotImplementedError('Controller::get_groups()')

    def switch(self, light_id: int) -> NoReturn:
        raise NotImplementedError('Controller::switch()')

    def pulse(self, light_id: int) -> NoReturn:
        raise NotImplementedError('Controller::pulse()')

    def set_ct(self, light_id: int) -> NoReturn:
        raise NotImplementedError('Controller::set_ct()')

    def set_colour(self, light_id: int, hsb: Tuple[int, int, int]) -> NoReturn:
        raise NotImplementedError('Controller::set_colour()')

    def all_off(self) -> NoReturn:
        raise NotImplementedError('Controller::all_off()')

    def all_on(self) -> NoReturn:
        raise NotImplementedError('Controller::all_on()')
