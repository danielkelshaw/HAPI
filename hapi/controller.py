import json
from typing import Tuple, NoReturn, Optional

import requests
from requests.models import Response

from .user import User


class Controller:

    def __init__(self, user: User) -> None:

        """Hue Controller.

        Parameters
        ----------
        user : User
            User object for relevant API URL.
        """

        self.user = user

    def get_lights(self, light_id: Optional[int] = None) -> dict:

        """Gets information on all lights.

        Parameters
        ----------
        light_id : Optional[int]
            ID of a single Hue light.

        Returns
        -------
        dict
            Requested information for lights.
        """

        if not light_id:
            req = requests.get(url=self.user.url + '/lights/')
        else:
            req = requests.get(url=self.user.url + f'/lights/{light_id}/')

        return req.json()

    def switch(self, light_id: int) -> None:

        """Switches the status of a given light.

        Parameters
        ----------
        light_id : int
            ID of single Hue light.
        """

        curr_state = self.get_lights(light_id)['state']['on']
        switch_state = not curr_state

        req = requests.put(
            url=self.user.url + f'/lights/{light_id}/state',
            data=json.dumps({'on': switch_state})
        )

    def pulse(self, light_id: int) -> None:

        """Pulses a given light.

        Parameters
        ----------
        light_id : int
            ID of a single Hue light.
        """

        pulse_data = {'on': True, 'transitiontime': 40, 'alert': 'select'}
        req = self._set_state(light_id=light_id, data=pulse_data)

    def set_ct(self, light_id: int, ct: int) -> None:

        """Set colour temperature of a given light.

        Parameters
        ----------
        light_id : int
            ID of a single Hue light.
        ct : int
            Colour temperature to set the light to.
        """

        req = self._set_state(light_id=light_id, data={'ct': ct})

    def set_colour(self, light_id: int, hsb: Tuple[int, int, int]) -> None:

        """Sets the colour of a given light.

        Parameters
        ----------
        light_id : int
            ID of a single Hue light.
        hsb : Tuple[int, int, int]
            Tuple giving the required (Hue, Saturation, Brightness).
        """

        hsb_data = {k: v for k, v in zip('hsb', hsb)}
        self._set_state(light_id=light_id, data=hsb_data)

    def all_off(self) -> NoReturn:
        raise NotImplementedError('Controller::all_off()')

    def all_on(self) -> NoReturn:
        raise NotImplementedError('Controller::all_on()')

    def _set_state(self, light_id: int, data: dict) -> Response:

        """Method to change state of a given Hue light.

        Parameters
        ----------
        light_id : int
            ID of a single Hue light.
        data : dict
            Data for PUT request.

        Returns
        -------
        req : Response
            Response code object from the request.
        """

        req = requests.put(
            url=self.user.url + f'/lights/{light_id}/state',
            data=json.dumps(data)
        )

        return req
