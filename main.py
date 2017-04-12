class OnlyMirrorScreen():
    def __init__(self,**kwargs):
        pass

    def change_screen(self,obj):
        self.keep_on=False
        self.manager.current = "mainpage"

    def sensor_in_mirror(self):
        self.keep_on=True
        obj_sensor = StartSensor()
        self.thread = threading.Thread(target=self.sensor_fun, args=(obj_sensor,)).start()
    
    def sensor_fun(self):
        while True:
            if self.keep_on:
                print "here in mirror"
                response = obj_sensor.start_sensor()
                time.sleep(0.1)
                if response==1:
                    self.change_screen(self.back_button)
            if not self.keep_on:
                print "stopping mirror thread"
                # self.thread.clear()
                break
                