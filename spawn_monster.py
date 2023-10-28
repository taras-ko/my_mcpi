from mine import *
import time
from sys import argv

mc = Minecraft()
pos = mc.player.getTilePos()

mc.postToChat('Ready. Go')

mc.conn.send("events.setting","restrict_to_sword",0)
mc.conn.send("events.setting","detect_left_click",1)

book = '{Item: {id: "minecraft:written_book", Count:1, Damage:0}}'
torch = '{Item: {id: "minecraft:torch", Count:100, Damage:0}}'
bow = '{Item: {id: "minecraft:bow", Count:1, Damage:0}}'
arrow = '{Item: {id: "minecraft:arrow", Count:100, Damage:0}}'
aplle_ench = '{Item: {id: "minecraft:golden_apple", Count:64, Damage:0}}'
sword  = '{Item: {id: "minecraft:diamond_sword", Count:1, Damage:0}}'
arrow_2  = '{Item: {id: "minecraft:spectral_arrow", Count:64, Damage:0}}'

mc.postToChat(argv)
argv[1] # 1
argv[2] # 2
argv[3] # 3

argv.pop(0)

for item in argv:
    what_to_spawn = '{Item: {id: "minecraft:' + item + '", Count:64, Damage:0}}'
    mc.postToChat(what_to_spawn)
    #mc.spawnEntity('Item', pos, )


#mc.spawnEntity('Item', pos, sword)
#mc.spawnEntity('Item', pos, aplle_ench)
#mc.spawnEntity('Item', pos, arrow_2)

#while True:
    #hits = mc.events.pollBlockHits()
    #for hit in hits:
        #mc.postToChat(hit.pos)
        #time.sleep(1)
        #mc.spawnEntity("Creeper", hit.pos)
        
#time.sleep(0.2)
