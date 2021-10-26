basic.showIcon(IconNames.Cow)
basic.pause(1000)
basic.clearScreen()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.Sad)
})
// def scutura():
//     zar = randint(1, 6)
//     basic.show_number(zar)
// input.on_gesture(Gesture.SHAKE, scutura)
//  Automatul de decizie
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let alegere = randint(0, 3)
    if (alegere == 0) {
        basic.showString("Da")
    } else if (alegere == 1) {
        basic.showString("Nu")
    } else if (alegere == 2) {
        basic.showString("Poate")
    } else {
        basic.showString("Nu stiu")
    }
    
})
//  Prinde punctul
let x = 0
let y = 0
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let punct_x = randint(0, 4)
    let punct_y = randint(0, 4)
    led.plot(punct_x, punct_y)
})
input.onGesture(Gesture.TiltRight, function inclina_dreapta() {
    
    
    led.unplot(x, y)
    x = x + 1
    led.plot(x, y)
})
input.onGesture(Gesture.TiltLeft, function inclina_stanga() {
    
    
    led.unplot(x, y)
    x = x - 1
    led.plot(x, y)
})
input.onGesture(Gesture.LogoDown, function inclina_sus() {
    
    
    led.unplot(x, y)
    y = y - 1
    led.plot(x, y)
})
input.onGesture(Gesture.LogoUp, function inclina_jos() {
    
    
    led.unplot(x, y)
    y = y + 1
    led.plot(x, y)
})
