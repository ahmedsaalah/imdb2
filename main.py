from flask import Flask

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash


from flask import session as login_session


import requests
import platform
import json
import logging
import httpagentparser
from movies import movies ,db,app



''' Views  '''
@app.route('/')
def HomePage():
    db.create_all()
        
    return render_template('items.html' )


''' Views  '''
@app.route('/details')
def Details():
        
    return render_template('details.html' )




@app.route('/yes.html')
def Genre():
    

    
    
    return render_template('genre.html' )
@app.route('/movie_info/<int:id>', methods=['POST','GET'])
def movie_info(id):
     
    data ='     <div class="jtip-quality">HD</div>' 
    data +='<div class="jtip-top">' 
    data +=' <div class="jt-info jt-imdb">IMDb: 5.3</div>' 
    data +='    <div class="jt-info">2017</div>' 
    data +='    <div class="jt-info">94 min</div>' 
    data +=' <div class="clearfix"></div>' 
    data +='</div>' 
    data +='<p class="f-desc">This is an edgy, character-driven film with a positive Christian message. A suburban town is torn apart in the aftermath of an accidental teen drug overdose.</p>' 
    data +='<div class="pop-rating">' 
    data +=' <div class="dr-text"><span>0.0</span>0 rated</div>' 
    data +='<div class="d-rating">' 
    data +='<div class="dr-mark dr-0">' 
    data +='<div class="dr-show dr-stars"></div>' 
    data +='  </div>' 
    data +='<div class="dr-hide dr-stars"></div>' 
    data +=' </div>' 
    data +=' <div class="clearfix"></div>' 
    data +='</div>' 
    data +='<div class="block">Country: <a href="https://yesmovies.to/country/united-states.html" title="United States">United States</a></div>' 

    data +='  <div class="block">Genres: <a href="https://yesmovies.to/genre/drama.html" title="Drama">Drama</a></div>' 
    data +='<div class="jtip-bottom">' 
    data +='<a href="https://yesmovies.to/movie/the-unmiracle-22884/watching.html" class="btn btn-block btn-success"><i          class="fa fa-play-circle mr10"></i>Watch movie</a>' 
    data +='   <a onclick="favorite(22884,'+'cluetip'+')" href="javascript:void(0)" class="btn btn-block btn-default mt10 favorite-22884">Add to favorite</a>' 
    data +='</div>'
    return data

if __name__ == '__main__':
   app.run(debug = True)