// Ambos motores avanzan
// Ejecutar la función on_forever de forma continua
basic.forever(function () {
    // Medir la distancia con el sensor ultrasónico
    if (maqueen.Ultrasonic(PingUnit.Centimeters) < 10) {
        // Si hay un obstáculo cerca, retrocede
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        // Retrocede el motor izquierdo
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
        // Retrocede el motor derecho
        basic.pause(1000)
        // Pausar durante 1 segundo
        // Detener ambos motores
        maqueen.motorStop(maqueen.Motors.All)
        basic.pause(500)
        // Pausar durante 0.5 segundos
        // Girar hacia la derecha para esquivar el obstáculo
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        // Avanza el motor izquierdo
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
        // Retrocede el motor derecho
        basic.pause(1000)
        // Pausar durante 1 segundo
        // Detener ambos motores
        maqueen.motorStop(maqueen.Motors.All)
        basic.pause(500)
    } else {
        // Pausar durante 0.5 segundos
        // Si no hay obstáculo, avanzar
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 50)
    }
})
