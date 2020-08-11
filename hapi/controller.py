import json
from typing import List, Tuple, NoReturn, Optional, Sequence, Union

import requests
from requests.models import Response

from .user import User
from .utils.inputs import to_list


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

    @to_list
    def switch(self, light_id: Union[int, List[int]]) -> None:

        """Switches the status of given light/s.

        NB: If int is passed then it is converted to an Iterable.

        Parameters
        ----------
        light_id : Union[int, Sequence[int]]
            ID of Hue light/s to switch.
        """

        for light in light_id:
            curr_state = self.get_lights(light)['state']['on']
            switch_dict = {'on': not curr_state}
            req = self._set_state(light_id=light, data=switch_dict)

    @to_list
    def pulse(self, light_id: Union[int, List[int]]) -> None:

        """Pulses the given light/s.

        NB: If an int is passed then it is converted to an iterable.

        Parameters
        ----------
        light_id : int
            ID of Hue light/s to pulse.
        """

        pulse_data = {'on': True, 'transitiontime': 40, 'alert': 'select'}

        for light in light_id:
            req = self._set_state(light_id=light, data=pulse_data)

    @to_list
    def set_ct(self, light_id: Union[int, List[int]], ct: Union[int, List[int]]) -> None:

        """Set colour temperature of given light/s.

        NB: If an int is passed then it is converted to an iterable.

        Parameters
        ----------
        light_id : Union[int, Sequence[int]]
            ID of Hue light/s to switch.
        ct : int
            Colour temperature to set Hue light/s to.
        """

        for idx, light in enumerate(light_id):
            req = self._set_state(light_id=light, data={'ct': ct[idx]})

    @to_list
    def set_colour(self,
                   light_id: Union[int, List[int]],
                   hsb: Union[Tuple[int, int, int], List[Tuple[int, int, int]]]) -> None:

        """Sets the colour of given light/s.

        NB: If an int is passed then it is converted to an iterable.

        Parameters
        ----------
        light_id : int
            ID of Hue light/s to set colour.
        hsb : Union[Tuple[int, int, int], List[Tuple[int, int, int]]]
            Tuple/s giving the required (Hue, Saturation, Brightness).
        """

        for idx, light in enumerate(light_id):
            hsb_data = {k: v for k, v in zip('hsb', hsb[idx])}
            self._set_state(light_id=light, data=hsb_data)

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
