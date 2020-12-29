import json
import pathlib

import cherrypy

import cards

currentDir = str(pathlib.Path().absolute())


class Root(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"


class CardServer(object):

    def __init__(self):
        self.game = cards.Two_Player_Stich_Jass('livio', 'toni')

    @cherrypy.expose
    def index(self, **params):
        game = self.game
        me = params.get('player')
        me = 'livio' if me == None else me

        players = game.players()
        if me != players[0] and me != players[0]:
            return json.dumps({'exception': 'you are not a player'})

        player_status = {}
        player_status['me'] = me
        player_status['players'] = game.players()
        player_status['player_cards'] = game.player_cards(me)
        player_status['playable_cards'] = game.playable_cards(me)
        player_status['round'] = game.round()
        player_status['score'] = game.score()
        player_status['current_player'] = game.current_player()

        result = json.dumps(player_status)

        return result


cherrypy.tree.mount(CardServer(), '/api')
cherrypy.tree.mount(Root(), '/', {'/': {
    'tools.staticdir.on': True,
    'tools.staticdir.dir': currentDir + "/html",
    'tools.staticdir.index': "index.html"}})
cherrypy.engine.start()
cherrypy.engine.block()
