class User:

    def __init__(self, ip: str, user_id: str) -> None:

        """User Class.

        Parameters
        ----------
        ip : str
            IP Address of the Hue Bridge.
        user_id : str
            User ID for API.
        """

        self.ip = ip
        self.user_id = user_id

    @property
    def url(self) -> str:
        return f'http://{self.ip}/api/{self.user_id}'
