from flask import Flask, render_template, request, redirect, session, flash, url_for
import requests

#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#session: armazena informações do usuário
#flash:mensagem de alerta exibida na tela
#url_for: vai para aonde o redirect indica

app = Flask(__name__)
app.secret_key = 'flask'
#chave secreta da sessão



#configuração da rota index.
@app.route('/', methods=['get', 'post'])
def index():
    return render_template('index.html') 


@app.route('/criaTibia', methods=['POST', 'GET'])
def criaTibia():

    name = request.form['name']

    nameCharacter = name
    
    url = 'https://api.tibiadata.com/v2/characters/{}.json'.format(nameCharacter)

    response = requests.get(url)

    char = response.json()['characters']

    level = (char['data']['level'])
    residence = (char['data']['residence'])
    sex = (char['data']['sex'])
    status = (char['data']['status'])
    title = (char['data']['title'])
    vocation = (char['data']['vocation'])
    world = (char['data']['world'])
   
    info = [level, residence, sex, title, vocation, world]

    return render_template('index.html', info=info, name=name)
    #return redirect(url_for('index'))


@app.route('/worldsTibia', methods=['POST','GET'])
def worldsTibia():

    world = request.form['world']


    url = 'https://api.tibiadata.com/v2/world/{}.json'.format(world)

    response = requests.get(url)

    charOnline = response.json()['world']

    Name=[]; Level=[]; Vocation=[]

    currentOnline = charOnline['world_information']['players_online']

    for oC in charOnline['players_online']:
        name = oC['name']
        level = oC['level']
        vocation = oC['vocation']
        Name.append(name)
        Level.append(level)
        Vocation.append(vocation)

    tam = len(Name)

    return render_template('index.html', currentOnline=currentOnline, name=Name, level=Level, vocation=Vocation, tam=tam)
    

app.run(debug=True)





