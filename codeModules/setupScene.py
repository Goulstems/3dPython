from ursina import *

def setupScene():
    app = Ursina(size=(800, 600), borderless=False)     #Starts Ursina application
    #hot-reload v --
    # application.hot_reloader._original_source_code_content = application.hot_reloader.get_source_code()
    # application.hot_reloader.hotreload = True
    #- - - - - - ---
    EditorCamera(rotation_x=35, rotation_y=-45) #CAMERA
    setupLighting()
    return app

def setupLighting():
    Sky()
    AmbientLight(color=color.rgba(160, 160, 180, 255))
    sun = DirectionalLight(
        shadows=True,
        color=color.rgb(255, 240, 210), #light pink hue
        y=10,
        z=-5,
        rotation=(45, -30, 0)
    )
    return sun