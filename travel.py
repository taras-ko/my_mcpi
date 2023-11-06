from mine import *
import keyboard
import time

mc = Minecraft()

delta = 10000
delta_y = 10

while True:
    try:
        if keyboard.is_pressed('x'):
            print('teleporting x by ' + str(delta))
            pos = mc.player.getTilePos()
            pos.x += delta
            mc.player.setTilePos(pos.x, pos.y, pos.z)
            mc.setBlock(pos.x, pos.y - 1, pos.z, 1)
        elif keyboard.is_pressed('y'):
            print('teleporting y by -' + str(delta_y))
            pos = mc.player.getTilePos()
            pos.y -= delta_y
            mc.player.setTilePos(pos.x, pos.y, pos.z)
            mc.setBlock(pos.x, pos.y - 1, pos.z, 1)
        elif keyboard.is_pressed('shift+y'):
            print('teleporting y by +' + str(delta_y))
            pos = mc.player.getTilePos()
            pos.y += delta_y
            mc.player.setTilePos(pos.x, pos.y, pos.z)
            mc.setBlock(pos.x, pos.y - 1, pos.z, 1)
        elif keyboard.is_pressed('z'):
            print('teleporting z by ' + str(delta))
            pos = mc.player.getTilePos()
            pos.z += delta
            mc.player.setTilePos(pos.x, pos.y, pos.z)
            mc.setBlock(pos.x, pos.y - 1, pos.z, 1)
        elif keyboard.is_pressed('b'):
            pos = mc.player.getTilePos()
            mc.player.setPos(29999.984, pos.y, 29999.984)
            pos = mc.player.getPos()
            mc.setBlock(pos.x, pos.y - 1, pos.z, 1)
        else:
            pass
    except Exception as e:
        print('except ' + e)
        break
    time.sleep(0.2)
