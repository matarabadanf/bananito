# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:02:26 2020

@author: matar
"""

# bot.py
import discord
import nest_asyncio

authorised_users = {'fermat': '6950', 'guillermoso999':7652}

nest_asyncio.apply()

class MyClient(discord.Client):

    # noinspection PyAttributeOutsideInit
    async def on_ready(self):
        self.speechless = False
        self.flame_warning_off = True
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content.lower() == 'e':
            print('iniciando esta mierda a ver que pasa')

        # COMANDOS DE ALTOS PRIVILEGIOS
        elif message.content.lower() == './purge':
            channel = message.channel
            if (message.author.name in authorised_users) and \
                    (message.author.discriminator == authorised_users[message.author.name]):
                print(message)
                self.speechless = True
                deleted = await channel.purge(limit=10000, check=None)
                self.speechless = False
            else:
                await channel.send('No tienes permiso para hacer esto, contacta con algun accionista para solucionarlo')

        # COMANDOS DE PRIVILEGIOS MEDIOS
        elif message.content.lower() == '!silenciate':
            if self.speechless:
                self.speechless = False
            else:
                self.speechless = True

        elif message.content.lower() == '!flame_warning':
            if self.flame_warning_off:
                self.flame_warning_off = False
            else:
                self.flame_warning_off = True

        # COMANDOS SIN REQUERIMIENTOS
        elif 'españa' in message.content.lower().lower():
            print('eee')
            print(message.channel.id)
            channel = self.get_channel(690292782224769124)
            if self.speechless:
                pass
            else:
                await channel.send('ARRRRRRIBA')

    async def on_typing(self, channel, user, when):
        print(self.flame_warning_off)
        print(self.speechless)
        if self.flame_warning_off or self.speechless:
            pass
        else:
            await channel.send('%s esta escribiendo, cuidadin con lo que mandas' % user)

    async def on_message_delete(self, messages):
        channel = self.get_channel(messages.channel.id)
        if self.speechless:
            pass
        else:
            await channel.send('Alguien ha intentado silenciar a %s' % messages.author.name)

'''
    async def on_raw_message_delete(self, messages):
        print(messages)
'''

client = MyClient()
client.run('Njg3MjA3NzI2MjI4NzAxMTg3.XnPSlw.CFt_Ehf9oInV-63KOhosVvA_WMs')
