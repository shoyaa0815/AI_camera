def on_button_pressed_ab():
    for index in range(999999):
        if GigoSensor.sensor(GigoSensor.SensorChannel.P1) == 0 and GigoSensor.sensor(GigoSensor.SensorChannel.P16) == 0:
            GigoMotor.motor_control2(GigoMotor.MotorChannel.G,
                GigoMotor.MotorShaftDirection.LOW,
                43)
            GigoMotor.motor_control2(GigoMotor.MotorChannel.F,
                GigoMotor.MotorShaftDirection.HIGH,
                40)
            basic.pause(200)
            GigoMotor.motor_stop1(GigoMotor.MotorChannel.G)
            GigoMotor.motor_stop1(GigoMotor.MotorChannel.F)
            basic.pause(200)
        elif GigoSensor.sensor(GigoSensor.SensorChannel.P1) == 1:
            GigoMotor.motor_control2(GigoMotor.MotorChannel.G,
                GigoMotor.MotorShaftDirection.LOW,
                43)
            basic.pause(200)
            GigoMotor.motor_stop1(GigoMotor.MotorChannel.G)
            basic.pause(200)
        elif GigoSensor.sensor(GigoSensor.SensorChannel.P16) == 1:
            GigoMotor.motor_control2(GigoMotor.MotorChannel.F,
                GigoMotor.MotorShaftDirection.HIGH,
                40)
            basic.pause(200)
            GigoMotor.motor_stop1(GigoMotor.MotorChannel.F)
            basic.pause(200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

basic.show_string("พร้อม")