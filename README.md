# HAPI

Python Library for Interacting with Hue API.

- [x] Python 3.6+
- [x] MIT License

### **Example:**

The code below demonstrates the ability to switch the *'on'* state of
any lights given their respective IDs:

```python
import hapi

user = hapi.User(ip='***.***.***.***', user_id='****************')
controller = hapi.Controller(user)

controller.switch([1, 2, 3])
```

###### Made by Daniel Kelshaw
