# Ambos motores avanzan
# Ejecutar la función on_forever de forma continua

def on_forever():
    # Medir la distancia con el sensor ultrasónico
    if maqueen.ultrasonic(PingUnit.CENTIMETERS) < 10:
        # Si hay un obstáculo cerca, retrocede
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
        # Retrocede el motor izquierdo
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
        # Retrocede el motor derecho
        basic.pause(1000)
        # Pausar durante 1 segundo
        # Detener ambos motores
        maqueen.motor_stop(maqueen.Motors.ALL)
        basic.pause(500)
        # Pausar durante 0.5 segundos
        # Girar hacia la derecha para esquivar el obstáculo
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
        # Avanza el motor izquierdo
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
        # Retrocede el motor derecho
        basic.pause(1000)
        # Pausar durante 1 segundo
        # Detener ambos motores
        maqueen.motor_stop(maqueen.Motors.ALL)
        basic.pause(500)
    else:
        # Pausar durante 0.5 segundos
        # Si no hay obstáculo, avanzar
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
basic.forever(on_forever)
