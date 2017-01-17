#!flask/bin/python
from flask import Flask, jsonify, request, make_response
from connect4 import Game

app = Flask(__name__)

@app.route('/connect4/api/start', methods=['POST'])
def new_game():
    global g
    g = Game()
    color = request.json.get('color','black') #default color black : human goes second
    s = g.startGame(color)
    return jsonify({'gameId': s[0], 'board': s[1] }) #will send id and game board

@app.route('/connect4/api/play', methods=['POST'])
def play_game():
    gId = request.json.get('id',g.gameId)
    playerMove = request.json.get('position')
    s = g.playGame(playerMove)
    if s == "Invalid":
        return make_response(jsonify({ 'error': 'Illegal Move' }), 400)
    if s[0] == 1:
        gId = None
        return make_response(jsonify({'game': 'AI won!', 'board':s[1] }), 200)
    if s[0] == 2:
        gId = None
        return make_response(jsonify({'game': 'Human won!', 'board':s[1] }), 200)
    if s[0] == 0:
        gId = None
        return make_response(jsonify({'game': 'Draw!', 'board':s[1] }), 200)        
    else:
        return jsonify({'gameId':gId, 'AiMovePos':s[2], 'board':s[1] }) #will send computer position, status of game and board

if __name__ == '__main__':
    #g = Game()
    app.run(debug=True)
    
    
    
    
   #id=null (delete.game.id)