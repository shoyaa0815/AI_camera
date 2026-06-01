radio.setGroup(24)
radio.setTransmitPower(7)
PlanetX_AILens.initModule()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.Color)
let count_item = 0
basic.showLeds(`
    . # # # .
    # . . . .
    . # # # .
    . . . . #
    . # # # .
    `)
basic.forever(function () {
    basic.showIcon(IconNames.Yes)
    PlanetX_AILens.cameraImage()
    basic.pause(100)
    if (PlanetX_AILens.colorCheck(PlanetX_AILens.ColorLs.red)) {
        radio.sendString("red")
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # # .
            # . . # .
            # . . . #
            `)
        count_item += 1
        basic.pause(2000)
        basic.clearScreen()
    } else if (PlanetX_AILens.colorCheck(PlanetX_AILens.ColorLs.blue)) {
        radio.sendString("blue")
        basic.showLeds(`
            # # # . .
            # . . # .
            # # # . .
            # . . # .
            # # # . .
            `)
        count_item += 1
        basic.pause(2000)
        basic.clearScreen()
    } else if (PlanetX_AILens.colorCheck(PlanetX_AILens.ColorLs.green)) {
        radio.sendString("green")
        basic.showLeds(`
            # # # # #
            # . . . .
            # . # # #
            # . . . #
            # # # # #
            `)
        count_item += 1
        basic.pause(2000)
        basic.clearScreen()
    }
})
