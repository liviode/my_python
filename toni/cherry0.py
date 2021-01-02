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
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def Two_Player_Stich_Game(self):
        game = self.game
        me = None
        player_status = {}
        if 'player' in cherrypy.request.json:
            me = cherrypy.request.json['player']

        if me == None:
            return json.dumps({'exception': 'no player'})

        players = game.players()
        if me != players[0] and me != players[1]:
            return json.dumps({'exception': 'you are not a player'})

        if 'action' in cherrypy.request.json:
            action = cherrypy.request.json['action']
            if action == 'play_card':
                player = cherrypy.request.json['player']
                card = cherrypy.request.json['card']
                player_status['winner_card'] = self.game.play_card(player, card)







        player_status['me'] = me
        player_status['players'] = game.players()
        player_status['player_cards'] = game.player_cards(game.current_player())
        player_status['playable_cards'] = game.playable_cards(me)
        player_status['round'] = game.round()
        player_status['score'] = game.score()
        player_status['current_player'] = game.current_player()
        player_status['cards_on_table'] = game.cards_on_table()
        player_status['trumpf_card'] = game.trumpf_card()

        return player_status


cherrypy.config.update({
    'server.socket_port': 8011
})
cherrypy.tree.mount(CardServer(), '/api')
cherrypy.tree.mount(Root(), '/', {'/': {
    'tools.staticdir.on': True,
    'tools.staticdir.dir': currentDir + "/html",
    'tools.staticdir.index': "index.html"}})
cherrypy.engine.start()
cherrypy.engine.block()
