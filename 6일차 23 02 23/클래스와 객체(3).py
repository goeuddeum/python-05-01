>>> class RCCar:
    def __init__(self):
        self.dir='stop'
        self.spd= 0
    def go_forward(self):
        self.dir='forward'
    def go_backward(self):
        self.dir = 'backward'
    def turn_left(self):
        self.dir = 'left'
    def turn_right(self):
        self.dir = 'right'
    def set_speed(self, spd):
        self.spd = spd
    def stop(self):
        self.dir = 'stop'
        self.spd = 0
    def show_state(self):
        self.dir, self.spd
        
>>> mycar = RCCar()
>>> mycar.go_forward()
>>> mycar.set_speed(30)
>>> mycar.show_state()
('forward', 30)
>>> class Remote:
    def __init__(self,car):
        self.car =car
    def gp_forward(self,spd):
        self.car.go_forward()
        self.car.set_speed(spd)
    def stop(self):
        self.car.stop()
    def show_screen(self):
        self.car.show_state()
        
>>> remot= Remote(mycar)
>>> remote = Remote(mycar)
>>> remote.go_forward(30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Remote' object has no attribute 'go_forward'
>>> remote.go_forward(30)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Remote' object has no attribute 'go_forward'
>>> remote.show_screen()
('forward', 30)
>>> remote.stop()
>>> remote.show_screen()
('stop', 0)

>>> class coffeeMachine:
    def __init__(self):
        self.menu = {}
        self.tatal_money = 0
    def set_menu(self,**menu):
        self.menu = menu
    def get_coffee(self, money_in, coffee_in):
        change, coffee_out = money_in, None
        if coffee_in in self.menu.keys():
            price = self.menu[coffee_in]
            if money_in>=price:
                change = money_in - price
                coffee_out = coffee_in
        return change, coffee_out
    
>>> cm= coffeeMachine()
>>> menu = {
    'americano':1500,
    'caffe latte':2500,
    'espresso':1500}
>>> cm.set_menu(**menu)
>>> print(cm.menu)
{'americano': 1500, 'caffe latte': 2500, 'espresso': 1500}
>>> change, coffee = cm.get_coffee(5000,'espresso')
>>> print(change,coffee)
3500 espresso
>>> 