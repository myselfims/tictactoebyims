import json
from ntpath import join
from tabnanny import check
from time import sleep
# from traceback import print_tb
from channels.consumer import SyncConsumer,StopConsumer,AsyncConsumer
from channels.consumer import async_to_sync,database_sync_to_async
import random
from django.contrib import messages
from .models import Game
from asgiref.sync import sync_to_async
# import pywhatkit

from game.views import idgenerator


def idgenerator():
        code = ""
        for i in range(8):
            number = random.randint(1,9)
            code = code + str(number)
        return code

class ForCreatingRoom(AsyncConsumer):
    
    async def websocket_connect(self,event):
        print('websocket connected...',event)
        print(self.channel_name)
        await self.send({
            'type': 'websocket.accept'
        })
    async def websocket_receive(self,event):
        print('messages received...',event['text'])
        hoster = json.loads(event['text'])
        joiner = json.loads(event['text'])
        hall = json.loads(event['text'])
        print(hall)
        # print(hall['roomcode'])
        room_code = ''
        if hoster['mode'] == 'create':
            room_code = room_code + idgenerator()
            await self.channel_layer.group_add(room_code,self.channel_name)
            game = Game(room_code = room_code, host = hoster['hostername'])
            # pywhatkit.sendwhatmsg('Hello World')
            await database_sync_to_async(game.save)()
            await self.channel_layer.group_send(room_code,{
                'type': "chat.message",
                'message': json.dumps({'roomcode':room_code,'hostername':hoster['hostername'],'mode':'create'})
            })
        elif hall['mode'] == 'hall':
            print('hall connected to roomcode...',hall['roomcode'])
            await self.channel_layer.group_add(hall['roomcode'],self.channel_name)

            second = 5
            # for i in range(5):
            #     # sleep(1)    
            #     await self.channel_layer.group_send(hall['roomcode'],{
            #         'type':'timer.message',
            #         'message': json.dumps({'countdown':'true','timer':second - i})
            #     })
            await self.channel_layer.group_send(hall['roomcode'],{
                    'type':'chat.message',
                    'message': json.dumps({'channelname': str(self.channel_name),'timer':second})
                })
            
        elif hall['mode'] == 'hallevent':
            print('hall connected to roomcode...',hall['roomcode'])
            # await self.channel_layer.group_add(hall['roomcode'],self.channel_name)
            
            await self.channel_layer.group_send(hall['roomcode'],{
                'type':'chat.message',
                'message': json.dumps({'clicked':hall['clicked'],'btn':'true','btnnum':hall['name']})
            })
        elif hall['mode'] == 'playagain':
            print('hall connected to roomcode...',hall['roomcode'])
            # await self.channel_layer.group_add(hall['roomcode'],self.channel_name)
            
            await self.channel_layer.group_send(hall['roomcode'],{
                'type':'chat.message',
                'message': json.dumps({'clicked':hall['clicked'],'btn':hall['player'],'btnnum':hall['mode']})
            })
        else:
            checkroom = await database_sync_to_async(list)(Game.objects.filter(room_code=joiner['roomcode']))
            print(checkroom)
          
            
            for code in checkroom:
                print('database code...',type(code))
                print('room code...',type(joiner['roomcode']))
                if str(code) == joiner['roomcode']:
                    print('opponent is...',code.join)
                    if code.join == '' or code.join == None:
                        code.join = joiner['name']
                        await database_sync_to_async(code.save)()
                        print('opponent is...',type(code.join))
                        print('room code match hora')
                        await self.channel_layer.group_add(str(code),self.channel_name)
                        await self.channel_layer.group_send(joiner['roomcode'],{
                        'type': "chat.message",
                        'message': json.dumps({'joinername':joiner['name'],'mode':'joined','roomcode':joiner['roomcode']})
                    
                })
                        break
                        
                    
                    else:
                        print('yaha par ara')
                        await self.send({
                        'type': "websocket.send",
                        'text': json.dumps({'message':'Room is full!','mode':'roomfull'})})
                        
                        
                    
                else:
                    await self.channel_layer.group_send(joiner['roomcode'],{
                    'type': "chat.message",
                    'message': json.dumps({'msg':'room code not exist'})
                    
                })
                    
                    
        
    async def chat_message(self,event):
        print(event['message'])
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })
        
        
    async def timer_message(self,event):
        print(event['message'])
        await self.send({
            'type':'websocket.send',
            'text': event['message']
        })
        sleep(1)
        


        
# class ForJoiningRoom(AsyncConsumer):
    
#     def websocket_connect(self,event):
#         print('websocket connected...',event)
#         self.send({
#             'type': 'websocket.accept'
#         })
#     def websocket_receive(self,event):
#         print('messages received...',event['text'])
        
#     def websocket_disconnet(self,event):
#         print('websocket disconnected')