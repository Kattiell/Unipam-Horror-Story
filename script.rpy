init python:
    class Pessoa:
        def __init__(self, genero, nome):
            self.genero = genero
            self.nome = nome

        masculino="false" ##masculino=falso, logo fala feminina.##
        materia = 0 # 0 = undefined 1 = Direito 2 = Engenharia 3 = Sistemas de informações
        nivel = 0 # 0 = undefined 1 = Baixo 2 = Médio 3 = Alto

define v = Character("[nomeDoProtagonista]", color = "#0099ff") #Variavel global de nome##
define s = Character("....", color = "#ffffff")
define josh = Character("Joshua", color = "#ffffff")
define joshuabravo = Character("Joshua", color = "#ffffff")
define joshuamachucado = Character("Joshua", color = "#ffffff")
define joshuavirado = Character("Joshua", color = "#ffffff")
define moca = Character("Balconista", color = "#ffffff")
define mislene = Character("Mislene", color = "#ffffff")
define mislenecomraiva = Character("Mislene", color = "#ffffff")
define mislenefeliz = Character("Mislene", color = "#ffffff")
define mislenealgemada = Character("Mislene", color = "#ffffff")
define sandro = Character("Sandro", color = "#ffffff")
define Naomi = Character("Naomi", color = "#ffffff")
define naomiemchoque = Character("Naomi", color = "#ffffff")
define Geovane = Character("Geovane", color = "#ffffff")
define Geovanerosto = Character("Geovane", color = "#ffffff")
define Geovanerosto2 = Character ("Geovane", color = "#ffffff")
define altamir = Character("Altamir", color = "#ffffff")
define altamirrosto = Character("Altamir", color = "#ffffff")
define altamirrosto2 = Character("Altamir", color = "#ffffff")
define altamirtriste = Character("Altamir", color = "#ffffff")
define altamirpreocupado = Character("Altamir", color = "#ffffff")
define altamirdesesperado = Character("Altamir", color = "#ffffff")
define vsz = Character("Voz Misteriosa", color = "#ffffff")
define stef = Character("Stefány", color = "#ffffff")
define klaraa = Character("Klara", color = "#ffffff")
define krysller = Character("Krysller", color = "#ffffff")
define krysllerserio = Character("Krysller", color = "#ffffff")
define guilherme = Character("Guilherme", color = "#ffffff")
define guilhermebravo = Character("Guilherme", color = "#ffffff")
define lia = Character("Talia", color = "#ffffff")
define gabriel = Character("Gabriel", color = "#ffffff")
define gabrielbravo = Character("Gabriel", color = "#ffffff")
define criança = Character("Criança Desconhecida", color = "#ffffff")
define filhaaltamir = Character("Filha", color = "#ffffff")
define filhaaltamirchorando = Character("Filha", color = "#ffffff")
define r = Character("Reitor", color = "#ffffff")
define rrisada = Character("Reitor", color = "#ffffff")
define reitorcav = Character("Reitor", color = "#ffffff")

##cena1,capasempersonagens ##
##cena2,quartoprincipal ## obs ter um cenário do hall da casa e um telefone
###cena3,telefonefinal##
##cena4,aeroporto##
##cena5,balcaodoaeroporto ##
##cena6,ruacomuber ##
##cena7,quartodoap##
##cena8,praçaforadoap##
##cena9,corredorunipam##
##cena10,saladiretor##
##cena11,entradadasala##
##cena12,saladeaula##
##cena13,jornal##
##cena14,Mercado##
##cena15,BardaStef##
##cena16,FotoNaomi##
##cena17,terraço#
##cena18,biblioteca##
##cena19,PortaSecreta##
##cena20,LivroNegro##


label start:
    play music "audio/SomPrincipal.mp3"
    show cena1

    $ nomeDoProtagonista = renpy.input("Qual é o seu nome?")
    if nomeDoProtagonista == "":
        $ nomeDoProtagonista = "Você"
    menu escolherGenero:
        "Por favor, escolha o seu gênero."
        "Masculino":
            $masculino="true"
            s "Seja Bem-Vindo {color=#0099ff}'[nomeDoProtagonista]'{/color} !!"
        "Feminino":
            $masculino="false"
            s "Seja Bem-Vinda {color=#0099ff}'[nomeDoProtagonista]'{/color} !!"

    hide cena1
    show cena2:
    with fade
    v "Chega, me decidi!"

    v "Eu já não estava mais aguentando todo esse nervosismo de escolher qual faculdade ingressar."

    v "Minha decisão foi de adentrar no UNIPAM, uma faculdade bem conceituada, espero ter me decidido bem."

    s "Este é o seu quarto!"

    v "Eu irei cursar... "

    menu:
        "Direito":
            $materia = 1
            v "Me identifico muito com esse curso, acho que é o melhor para mim!"
        "Engenharia ":
            $materia = 2
            v "Me identifico muito com esse curso, acho que é o melhor para mim!"
        "Sistemas de informação ":
            $materia = 3
            v "Me identifico muito com esse curso, acho que é o melhor pra mim!"

    if masculino=="true":
        v "Estou precisando mudar minha vida, viver aqui nessa cidade não estava sendo bom. Mudar os hábitos as vezes faz bem, e estou disposto a novos desafios."
    elif masculino=="false":
        v "Estou precisando mudar minha vida, viver aqui nessa cidade não estava sendo bom. Mudar os hábitos as vezes faz bem, e estou disposta a novos desafios."

    v "Independente da cidade que for, sair daqui já será ótimo.\nAs pessoas daqui são umas piores que as outras, cidade pequena é insuportável lidar com certas situações."

    v "Mas, chega disso preciso me concentrar em arrumar minhas malas para enfim ir embora daqui."

    s "O que fazer agora?"

    menu:
        "Arrumar as malas bem organizadas e jogar algo até a hora da viagem.":

            v "Melhor deixar tudo organizado para não faltar nada, melhor me prevenir. Ainda bem que o meu apartamento é bem pertinho da faculdade lá vai ser mais fácil me localizar."

            v "Quando acabar aqui precisarei contar para o Joshua minha decisão, não sei como ele vai reagir."

            stop music
            play music "audio/porta.mp3"

            s "{color=#0099ff}'[nomeDoProtagonista]'{/color} arrumando as malas e escuta um barulho na porta."

            v "Acredito que seja minha mãe que veio se despedir, entre."
            stop music
            play music "audio/SomPrincipal.mp3"
            v "Quando me viro é o Josh que está na porta."

            hide cena1
            show cena2:
            with fade

            show menino2:
                zoom 1.50
                ease 0.3 zoom 1.60
            with dissolve

            josh "Hey... \nEai?"

            hide menino2

            v "Oi Josh, então, escolhi a universidade, só que ela fica em outra cidade."
            show menino2:
                zoom 1.50
                ease 0.3 zoom 1.60
            with dissolve
            josh "Você fez a melhor escolha para você, estou muito feliz só não esquece que vou sempre te apoiar."
            hide menino2
            v "Obrigado Josh você é de mais."

            v "Subimos para o meu quarto, contei a ele minha decisão parece que ele ficou bem triste, mas me apoiou."
            v "Ficamos jogando e conversando até a hora de ir viajar e ele foi comigo para o aeroporto."
            hide cena1

        "Jogar as roupas de qualquer jeito na mala e sair.":

            v "Não ligo muito para organizar essas tralhas. Vou arrumar isso de qualquer jeito e achar algo mais interessante pra me divertir."

            v "Me falaram que o novo ap é meio longe, mas tanto faz."

            if masculino=="true":
                v "Sair pra espairecer vai ser a melhor decisão a tomar, ainda estou meio receoso sobre essa decisão."
            elif masculino=="false":
                v "Sair pra espairecer vai ser a melhor decisão a tomar, ainda estou meio receosa sobre essa decisão."

            v "Vou andar um pouco até dar a hora de viajar, não quero ninguém chorando por mim já que eles nunca se importaram mesmo."

            hide cena1
            stop music
        "Mandar mensagem para Josh enquanto mando minha mãe arrumar minhas malas.":

            $ renpy.movie_cutscene("Timeline 1.webm")


    show cena4:
    with pixellate
    stop music
    play music "audio/Avião.mp3"
    v "Já sinto até um ar diferente, vou sentir muita falta do Josh, nos conhecemos desde que ambos tínhamos 4 anos e sempre fomos muito chegados, bom eramos muito próximos."

    if masculino=="true":
        v "Tento me mostrar confiante mas estou um pouco nervoso, não é fácil mudar dessa forma e deixar tudo pra trás."
    elif masculino=="false":
        v "Tento me mostrar confiante mas estou um pouco nervosa, não é fácil mudar dessa forma e deixar tudo pra trás."

    if masculino=="true":
        v "Quero começar logo estou muito ansioso pelos desafios que me aguarda!"
    elif masculino=="false":
        v "Quero começar logo estou muito ansiosa pelos desafios que me aguarda!"

    v "Não me importo de ficar nessa fila monstruosa, vendo um lado positivo vou ter tempo pra colocar as ideias no lugar."

    v "Em Florianópolis era tudo muito mais fácil, aqui em Patos as coisas parecem ser bem mais difíceis."

    if masculino=="true":
        v "Não posso negar que me sinto aliviado em ter saído de casa, uma família conservadora chega a ser insuportável quando cismam em querer impedir as coisas."
    elif masculino=="false":
        v "Não posso negar que me sinto aliviada em ter saído de casa, uma família conservadora chega a ser insuportável quando cismam em querer impedir as coisas."

    v "Eles me dão nos nervos, mas com o tempo se aprende a conviver."

    v "Minha vez!"

    show cena5:
     zoom 1.2
    with fade

    show menina1:
       zoom 0.8
       ease 0.5 zoom 0.9
    with dissolve

    moca "Poderia me entregar sua passagem para realizarmos o seu check out, por favor?"

    hide menina1
    v "Claro, aqui."


    if masculino=="true":
        show menina1:
            zoom 0.8
            ease 0.5 zoom 0.9
        with dissolve
        moca "Novo na cidade? Espero que goste daqui."
    elif masculino=="false":
        show menina1:
            zoom 0.8
            ease 0.5 zoom 0.9
        with dissolve
        moca "Nova na cidade? Espero que goste daqui."

    hide menina1

    menu:
        "A sim, estou me mudando para fazer faculdade por aqui, irei criar indepedência, pela primeira vez é bem diferente.":
            show menina1:
                zoom 0.8
                ease 0.5 zoom 0.9
            with dissolve
            moca "Te entendo bem, espero que encontre o que procura. Tome seus papeis e pegue esse doce, por conta da casa."

            stop music
            play music "audio/Vento.mp3"
            hide menina1
            hide cena5
            show cena6:
            with fade
            v "Ela entregou tudo com um singelo sorriso, saio puxando minhas malas em direção a rua em busca de algum táxi, para ir logo pra casa."

            v "A viagem foi exaustiva e quero descansar."

            hide menina1
            hide cena5
        "Como? Sim, cheguei agora. Pode me entregar meus documentos?":
            show menina1:
                zoom 0.7
                ease 0.5 zoom 0.8
            with dissolve
            moca "Tome. Próximo!"

            hide menina1

            v "Ela diz e eu rapidamente saio em direção a rua com minha mochila nas costas, trouxe pouca coisa o que eu precisar compro por aqui."

            v "Como olhei no mapa sei mais ou menos onde fica o meu novo apartamento."

            v "Então vou andando mesmo, uma caminhada faz bem."

            hide menina1
        "Seu chefe te paga para tomar conta da vida dos outros?":
            show menina1:
                zoom 0.8
            with dissolve
            moca "Espero que sua recepção seja tão boa quanto sua educação, suma daqui."
            hide menina1
            v "Percebi que deixei aquela moça bem brava, mas as coisas da minha vida não são da conta de ninguém."

            v "Fiquei triste, queria um daqueles doces que estavam no balcão."

            stop music
            play music "audio/Vento.mp3"
            show cena6:
            with pixellate

            v "Vou até a saída e lembro que não faço ideia de onde seja o meu apartamento e ligo pra minha mãe."
            hide menina1
            v "Já entro em um daqueles taxis que ficam na porta do aeroporto, não ligo se é mais caro não sou eu que vou pagar mesmo, meus gastos são no cartão dos meus pais então..."

            v "Coloco as malas exageradas que minha mãe arrumou no porta malas, já coloco o celular no viva-voz e peço para ela explicar ao motorista onde fica, vou cochilando no caminho."

    play music "audio/SomPrincipal.mp3"
    hide menina1
    hide cena4
    show cena7:
    with pixellate

    v "Cheguei."

    v "Pelo menos o aparamento já é mobilhado, só preciso colocar minhas coisas no lugar"

    s " O que fazer?"

    menu:
        "Arrumar as malas no local para ficar livre e descansar.":
            v "..."
        "Jogar tudo em qualquer lugar e me jogar na cama para dormir.":
            v "..."
        "Ver um pouco de tv e acabar cochilando no sofá.":
            v "..."

    stop music
    play music "audio/Despertador.mp3"

    hide cena6
    show quarto2prontoo:
    with pixellate

    v "Acordo as 8:00, estou bem contente e resolvo dar uma volta para conhecer a nova cidade antes de começar a faculdade."

    hide quarto2prontoo
    show cena7:
    with pixellate

    v "Até porque não quero perder nada no primeiro dia."
    stop music
    play music "audio/Vento.mp3"

    hide cena6
    hide cena7
    show cena8:
    with pixellate

    v "Andei por muito tempo conheci a cidade descobri vários locais legais."
    s "A praça tinha uma enegeria muita positiva e atraia várias pessoas, além de seu clima e o vento suave que tinha por lá."

    v "Está praça é o marco da cidade e daqui já consigo ver a universidade estou bem perto do meu futuro agora."
    v "Só não antes de provar esse tal sorvete gourmet que estão vendendo aqui."
    v "Espero que tudo ocorra bem nesse primeiro dia de aula."

    stop music
    play music "audio/SomPrincipal.mp3"

    hide cena8
    show cena9:
    with dissolve

    s "Chegando na universidade..."

    v "Me deparo com um cenário totalmente diferente do padrão das escolas."
    show cena10:
    with fade

    v "Entro na Reitoria da faculdade e me encontro com o que parece o Diretor geral da universidade."
    v "Ele me apresenta o Reitor geral da faculdade, e ambos conversam comigo."
    v "Como ganhei uma bolsa especial pelo que parece precisam ver se deram a bolsa para a pessoa certa."

    v "Fiquei muito tempo conversando com eles, as coisas aqui são bem rigorosas mesmo."
    hide cena10
    hide cena7
    hide cena8
    show cena11:
      zoom 1.1
    with pixellate

    v "Será que é essa sala?"

    v "Fiquei o dia todo resolvendo a negociação da bolsa, já foi bem cansativo, ainda bem que as aulas são noturnas."

    hide cena11

    show cena12:
    with fade
    stop music
    play music "audio/Conversa.mp3"
    v "Pelo que parece é aqui, sala lotada de gente e um pouco de barulho."

    s "O que fazer?"
    menu:
        "Vou me sentar na frente não quero que essa bagunça me atrapalhe.":
            s "..."
        "Vou me sentar em qualquer lugar e esperar algum professor chegar aqui.":
            s "..."
        "É melhor me sentar no fundo, é mais fácil de fazer amizades.":
            s "..."

    show mislene:
        zoom 1.33
        yalign 0.5
        ease 0.3 zoom 1.35
    with dissolve

    if materia==1:
        mislene "Boa noite alunos, me chamo Mislene, vou ser a professora de Linguagens de vocês."
    elif materia==2:
        mislene "Boa noite alunos, me chamo Mislene, vou ser a professora de Cálculo de vocês."
    elif materia==3:
        mislene "Boa noite alunos, me chamo Mislene, vou ser a professora de Sistemas de informações de vocês."

    mislene "Façam silêncio, irei explicar como funciona as coisas na faculdade e falar um pouco do que eu vou ensinar pra vocês."
    hide mislene

    stop music
    play music "audio/SomPrincipal.mp3"

    show mislenefeliz:
        zoom 1.33
    with dissolve
    mislene "Certo, minha ideia para o plano de ensino de vocês é:"

    if materia==1:
        mislene "{color=#0099ff}Literatura\nArtigos\nComunicação e Midias. {/color}"
    elif materia==2:
        mislene "{color=#0099ff}Cálculo Integral\nCálculo Diferencial\nCálculo 1 e 2. {/color}"
    elif materia==3:
        mislene "{color=#0099ff}Desenvolvimento Web I\nPhotoShop\nDesenvolvimento Web II.{/color}"

    hide mislenefeliz

    v "A aula passou rápido, gostei muito de tudo que ela explicou. "

    v "Ela parece ser uma mulher muito inteligente, vou gostar dela."

    v "Ouvi durante a aula dela uns cochichos sobre alguns dos professores estarem envolvidos com algumas coisas estranhas."

    v "Fiquei sabendo também que há boatos de que já morreu um aluno na faculdade e a alma dele nunca conseguiu sair daqui. Bom, todo lugar tem boatos não acredito muito nisso."

    v "Fiz amizade com uma garota que se chama Naomi, gostei muito do jeito dela. Bem extrovertida e diferente."

    show naomi:
          zoom 2.0
          yalign 0.1
    with dissolve

    Naomi "Agora é a aula do Sandro, pelo que parece ele é um ótimo professor só é muito reservado e não gosta de intimidade com os alunos."

    hide naomi
    menu:
        "Serio? Vamos ver então como será as aulas dele.":
            v "..."
        "Vou gostar dele, cada um em seu canto do jeito que eu gosto.":
            v "..."
        "Parece bom, sendo competente.":
            v "..."

    hide naomi
    hide cena12
    show cena12:
    with dissolve

    show sandro:
        zoom 1.7
        yalign 0.5
        ease 0.3 zoom 1.75
    with dissolve
    if materia==1:
        sandro "Olá alunos me chamo Sandro e serei o professor de Ciência Política de vocês, e o supervisor."
    elif materia==2:
        sandro "Olá alunos me chamo Sandro e serei o professor de Hidráulica e Saneamento de vocês, e o supervisor."
    elif materia==3:
        sandro "Olá alunos me chamo Sandro e serei o professor de Algoritmo de vocês, e o supervisor."

    sandro "Como supervisor quero avisa-los que irei ficar de olho em cada um de vocês, não gosto de nada mal feito e já vou deixar avisado."

    hide sandro

    v "Ele se virou para o quadro e encheu a lousa de matérias, uma pior do que a outra."
    show naomi:
        zoom 2.0
        yalign 0.1
        ease 0.3 zoom 2.2

    Naomi "Hey, psiu. Fiquei sabendo que o Sandro era muito próximo dos alunos, alguma coisa aconteceu com ele."
    Naomi "Ele não deixa nem mandarem mensagem para ele, prefere manter contato com os alunos so durante as aulas."

    hide naomi
    v "Eita, o que será que aconteceu com ele?"
    show naomi:
        zoom 2.0
        yalign 0.1
        ease 0.3 zoom 2.2
    Naomi "Eu não sei, mas to doidinha para descobrir."

    hide naomi
    v "As aulas eram rápidas como era o primeiro dia todas as aulas seriam pequenas para todos os professores se apresentarem."

    v "Temos 4 professores nesse período do curso. Não são muitos, mas como é o início é bem plausível."

    v "A aula do Sandro passou de forma muito rápida, gostei muito."

    v "O próximo professor entra na sala logo se apresentando."

    show geovane:
        zoom 1.5
        yalign 1.2
    with dissolve

    Geovane "Boa noite alunos, serei o professor de idiomas avançados durante esse semestre."

    Geovane "Vou fazer uma atividade interativa com vocês para deixar mais interessante."

    Geovane "Vamos começar, você!"

    hide geovane
    v "Para a minha sorte ele aponta para mim e pergunta."

    show geovane:
        zoom 1.5
        yalign 1.2
    with dissolve

    Geovane "Vou começar com você, me diga qual seu nível de inglês?"

    hide geovane

    menu:
        "Alto":
            $nivel = 3
            Geovane "Tenho uma boa para você então, como é alto nível será toda em inglês. How do you call the security guards outside of Samsung?"
        "Intermediário":
            $nivel = 2
            Geovane "Intermediário, hmm. O que posso trazer para você, já sei! What most interested you in college?"
        "Baixo":
            $nivel = 1
            hide geovane
            show geovanerosto2:
                zoom 1.5
                yalign 1.2
            with dissolve

            Geovane "Ah."
            Geovane "Nível baixo, não espero que se esforce tanto então, nem vale o esforço."
    if nivel==3:
        menu:
            "O que? Ta me zoando?":
                hide geovane
                show geovanerosto:
                    zoom 1.5
                    yalign 1.2
                with dissolve
                Geovane "Melhore o seu nível e não seja infantil"
            "Não sei te responder isso, sinto muito.":
                hide geovane
                show geovanerosto2:
                    zoom 1.5
                    yalign 1.2
                with dissolve

                Geovane "Você me parecia uma pessoa inteligente, me enganei"
            "Essa é boa haha, The Guardians of The Galaxy.":
                Geovane "Essa é uma pessoa de bom gosto."
    elif nivel==2:
        menu:
            "O que? Não entendi?":
                hide geovane
                show geovanerosto2:
                    zoom 1.5
                    yalign 1.2
                with dissolve
                Geovane "Imaginei, que frustrante"
            "Sei la cara não me interessei muito.":
                hide geovane
                show geovanerosto:
                    zoom 1.5
                    yalign 1.2
                with dissolve

                Geovane "Você me parecia uma pessoa inteligente, me enganei"
            "Essa é boa, I really liked the library.":
                hide geovane
                show geovane:
                    zoom 1.5
                    yalign 1.2
                with dissolve
                Geovane "Essa é uma pessoa de conhecimento"


    hide geovane
    hide geovanerosto
    hide geovanerosto2
    v "Olho para a Naomi e ela me olha sem entender também, só quero que essa aula acabe logo."

    v "A aula acaba e o novo professor entra, logo se apresentando."
    hide geovane

    show altamir:
        zoom 1.7
    with dissolve

    altamir "Boa noite alunos, essa é a ultima aula só quero conhecer vocês, me falem um pouco sobre vocês."

    altamir "Sou o professor de Organizações sociais e vamos realizar alguns projetos."

    altamir "Então vamos lá."

    hide altamir

    v "A maioria se apresenta e chega minha vez."

    hide altamir

    menu:
        "Não estou afim de me apresentar.":
            show altamirrosto:
                zoom 1.7
            with dissolve
            altamir "Tudo bem vou me lembrar disso na hora de distribuir seus pontos."
        "Me chamo {color=#0099ff}[nomeDoProtagonista]{/color}, e sou de outra cidade.":
            show altamirrosto2:
                zoom 1.7
            with dissolve
            altamir "Espero que se de bem aqui."
        "A sei lá, sou {color=#0099ff}[nomeDoProtagonista]{/color} e minha vida não é da sua conta.":
            show altamirrosto:
                zoom 1.7
            with dissolve
            altamir "Ok, próximo."

hide altamirrosto
hide altamirrosto2
hide altamir

v "A aula acaba me despeço de Naomi, e vou para casa foi um dia longo."
hide cena12
show cena13:   ## \n  ##
with pixellate
v "Ligo meu computador para ver as noticias e vejo uma bem estranha no jornal local."


s "'Jovem encontrada morta em universidade de Patos de Minas, não se sabe se foi suicídio ou assassinato."
s "O corpo da jovem continha marcas de espancamento, porém tudo indica que a mesma se jogou do terraço do colégio em uma tentativa de acabar com a própria vida.'"
s "O acontecido ocorreu depois do horário de aulas do dia de hoje. Não se tem suspeitos, mas foi pedido que todos tenham cuidado e as aulas continuam funcionando normalmente até o momento.'"
s "As investigações irão continuar na Universidade até que se tenha nota do que realmente aconteceu."
if masculino=="true":
    v "Nossa, nem sei o que pensar, isso foi lá na minha faculdade. Não conhecia a garota mas fico triste por isso."
    v "E Pensar que pode ter sido um assassinato me deixa muito assustado, mas não vou me abalar por isso amanha é um longo dia."
elif masculino=="false":
    v "Nossa, nem sei o que pensar, isso foi lá na minha faculdade. Não conhecia a garota mas fico triste por isso."
    v "E Pensar que pode ter sido um assassinato me deixa muito assustada, mas não vou me abalar por isso amanha é um longo dia."

hide cena13
show quarto2prontoo:
with fade

v "O dia começou estranho de várias formas, parece que o mundo está conspirando contra mim."

hide quarto2prontoo
show cena7:
with pixellate
stop music
play music "audio/telefone.mp3"

v "Já de início recebo uma ligação estranha da minha mãe, falando que teve um sonho horrendo comigo e que estava extremamente preocupada."
v "Me disse que havia recebido um sinal pra que eu não saísse de casa hoje."
v "Não posso deixar isso me abalar nem faltar a um dia de aula por besteiras assim."
stop music
play music "audio/Vibração.mp3"
s "Meu celular vibra..."
v "Deve ser a Naomi me mandando mensagem provavelmente pela notícia do dia anterior."

stop music
play music "audio/SomPrincipal.mp3"

$ renpy.movie_cutscene("NaomiConversa.webm")

v "Vou fazer umas compras, não tem nada para comer nesse apartamento"

show cena14:
with pixellate
stop music
play music "audio/Conversa.mp3"

s "Chegando ao mercado. Que estava rasoavelmente cheio."
s "{color=#0099ff}[nomeDoProtagonista]{/color} se dirige até a parte dos mantimentos."

v "O que será que eu pego? Hmm, deixa eu pensar"

vsz "Oie você por aqui?"

v "Oie Altamir."

show altamir:
    zoom 1.7
with dissolve

altamir "O que veio fazer aqui?"

hide altamir
menu:
    "Estou jogando basquete, não ve?":
        hide altamir
        show altamirrosto:
            zoom 2.0
        with dissolve
        altamir "A educação é uma dadiva mesmo.\nCuidado com o que fala e com quem você fala, as coisas por aqui não funcionam da forma como você pensa. "
        hide altamirrosto
        s "Ele saiu com a cara fechada sem se despedir quase me derrubando com seu carrinho"
        v "Todos nessa cidade se importam muito com essas relações, pessoal estranho.."
        v "Vou pagar essas compras e vou para casa."
        hide cena14
        show cena7:
        with pixellate
        stop music
        play music "audio/SomPrincipal.mp3"

        s "Chegando em casa..."
        v "Primeiro dia e o Sandro já passou atividade esse ano parece que vai ser longo."
        v "As pessoas agem de uma forma muito estranha nesse lugar, credo."
        v "Espero que de tudo certo com a aula hoje."
        hide cena7

    "Comprando algumas coisas pro meu apartamento tá bem vazio.":
        show altamir:
          zoom 1.7
        with dissolve
        altamir "Apartamento novo?"

        hide altamir
        v "Sim, me mudei recentemente."

        show altamirrosto2:
            zoom 1.7
        with dissolve
        altamir "interessante, espero que goste da cidade. Bom preciso ir, até a aula."
        hide altamirrosto2

        s "Ele fala e depois se dirige a prateleira á sua frente buscando algo e aproveito a deixa para ir me afastando."
        v "Todos nessa cidade se importam muito com essas relações, pessoal estranho.."
        v "Vou pagar essas compras e vou para casa."
        hide cena14


        show cena7:
        with pixellate
        stop music
        play music "audio/SomPrincipal.mp3"

        s "Chegando em casa..."
        v "Primeiro dia e o Sandro já passou atividade esse ano parece que vai ser longo."
        v "As pessoas agem de uma forma muito estranha nesse lugar, credo."
        v "Espero que de tudo certo com a aula hoje."
        hide cena7

    "Porque quer saber?":
        show altamir:
            zoom 1.7
        with pixellate
        altamir "Nenhum motivo especifico, apenas tentando conversar, como somos aluno e professor podemos ter uma boa relação fora do colégio também."
        hide altamir

        s "Ele fala e depois se dirige a prateleira em sua frente buscando algo e aproveito a deixa para ir me afastando."
        v "Todos nessa cidade se importam muito com essas relações, pessoal estranho.."
        v "Vou pagar essas compras e vou para casa."

        hide cena14
        show cena7:
        with pixellate
        stop music
        play music "audio/SomPrincipal.mp3"

        s "Chegando em casa..."
        v "Primeiro dia e o Sandro já passou atividade esse ano parece que vai ser longo."
        v "As pessoas agem de uma forma muito estranha nesse lugar, credo."
        v "Espero que de tudo certo com a aula hoje."
        hide cena7


show cena9:
with dissolve
v "Caramba isso aqui ta muito vazio, deve ter umas 10 pessoas no máximo andando pelos corredores. Parece que uma morte assusta mesmo as pessoas."

v "Paro em meu armário pra pegar minhas coisas e me deparo com Naomi."
if masculino=="true":
    v "Então você veio? Sabia que minha aura de bom aluno iria te convencer haha."
elif masculino=="false":
    v "Então você veio? Sabia que minha aura de boa aluna iria te convencer haha."
show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Muito pelo contrario coisa bonita, vim te salvar de uma aula com 3 pessoas pra gente  ir beber no bar e você conhecer meu amigo, tenho certeza que vocês se darão muito bem."

v "Naomi eu já disse não quero matar aula."

Naomi "Os professores não vao querer dar aula pra três pessoas em uma sala de 50 alunos, não estou te levando para o mal caminho anjinho."

s "O que fazer ?"
hide naomi
menu:

    "Ir com ela para o bar":
        $bar = 1
    "Ficar na aula e estudar":
        $bar = 2
    "Voltar pra casa e dormir":
        $bar = 3

if bar==1:
    v "Tudo bem você conseguiu eu vou com você."
    show naomirosto:
        zoom 2.0
        yalign 0.1
    with dissolve
    Naomi "Ebaaaa então vamos logo para o bar da Stef."

    v "Stef?"

    if masculino=="true":
        Naomi "É bobo, o bar é o nome da dona."
    elif masculino=="false":
        Naomi "É boba, o bar é o nome da dona."
    hide cena9
    hide naomirosto


    show cena15
    v "Naomi me leva para o tal bar da Stef."

    s "O bar estava quase lotado, havia muita gente da faculdade presente lá."

    if masculino=="true":
        v "Chegando lá me deparo com um rosto extremamente conhecido por mim e fico paralisado sem saber o que fazer ou falar."
    elif masculino=="false":
        v "Chegando lá me deparo com um rosto extremamente conhecido por mim e fico paralisada sem saber o que fazer ou falar."
    show menino2:
        zoom 1.56
    with dissolve

    josh  "Mas, eu não mereço nem um oi? Haha!"
    v "Josh??? O que está fazendo aqui porque não me ligou nem me avisou que viria?"
    hide menino2



    show menino2rosto:
        zoom 1.56
    with dissolve
    josh "Eu queria te fazer uma surpresa."
    hide menino2rosto
    show menino2:
        zoom 1.56
    with dissolve
    josh "Na verdade conheci a Naomi tem um tempo pela internet."

    josh "Nem me liguei que você iria se mudar pra mesma cidade dela."
    josh "Ela me chamou pra vir e como eu estou de férias do serviço decidi vir pra ver ela e você com uma surpresa, ela sabia de tudo e me ajudou a planejar haha."
    hide menino2
    v "Nossa eu nem sei o que falar, já estava com saudades eu me importo muito com você Josh, fico feliz em te ver."

    v "Após isso seguimos para o balcão e pedimos para uma moça muito bonita que estava no balcão as bebidas após decidirmos o que vamos beber."

    show stef:
       zoom 1.3
    with dissolve
    stef "Boa noite, me chamo Stefany e sou a dona do bar vou servir vocês pois nosso barman teve um problema de ultima hora então só servimos doses e bebidas prontas, o que vão querer?"
    hide stef

    menu:
        "Doses de tequila":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Três doses de tequila, por favor."
            hide naomi
            show steffofa:
             zoom 1.3
            with dissolve
            stef "Tudo bem. Um momento e já trago."
            hide steffofa

            v "A dona do bar saiu e foi pegar nossas bebidas."

            show stef:
              zoom 1.3
            with dissolve
            stef "Aqui as doses, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide stef

        "Long necks de Not Heineken":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Long necks de Not Heineken, por favor."
            hide naomi

            show steffofa:
              zoom 1.3
            with dissolve
            stef "Tudo bem. Um momento e já trago."
            hide steffofa
            v "A dona do bar saiu e foi pegar nossas bebidas."
            show stef:
              zoom 1.3
            with dissolve
            stef "Aqui as garrafas, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide Stef

        "Refrigerante":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Três refrigerantes, por favor."
            hide naomi
            show steffofa:
              zoom 1.3
            with dissolve
            stef "Tudo bem. Aguarda só um momento e já trago."
            hide steffofa

            v "A dona do bar saiu e foi pegar nossas bebidas."
            show stef:
              zoom 1.3
            with dissolve
            stef "Aqui as latas, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide stef
            v "Ela saiu e foi atender outras pessoas que estavam do lado contrário do balcão."

    hide stef
    show menino2:
        zoom 1.56
    with dissolve
    josh "A menina que morreu era da sala de vocês?"
    hide menino2
    v "Acho que sim, mas eu não conversei com ela em momento nenhum, literalmente em um momento ela estava na aula e no outro esmagada no chão da faculdade."
    show naomi:
        zoom 2.0
        yalign 0.1
    with dissolve
    Naomi "Parece que ela tinha ido com um amigo fumar no terraço, um amigo da sala mesmo. Ele saiu pra algum lugar, deixou ela sozinha e ela morreu. "

    Naomi "Não sei se ele matou ela ou se alguém matou ou ate mesmo ela se matou mas essa historia esta muito estranha pro meu gosto."
    hide naomi
    v "Credo."

    v "Conversamos e bebemos a noite toda, espero acordar em casa amanhã."
    $barconfirmado=0
    hide cena15
    show quarto2prontoo:
    with dissolve

    v "Um novo dia começa."

    hide quarto2prontoo
elif bar==2:
        v "Eu realmente acho que devo estudar, sinto muito."
        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Poxa, eu queria tanto que você conhecesse o Joshua, ele veio da mesma cidade que você, achei que se sentiria mais confortável com a cidade mas tudo bem."

        v "JOSH?! O JOHSUA?!"
        hide naomi
        show naomirosto:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Você o conhece? Que legal então vamooos você vai ver seu amigo."
        hide naomirosto
        menu: #decisão final para ver se realmente deve ir ao bar

            "Ir para o bar ver Josh":
                $barconfirmado=1

            "Não ir para o bar":
                $barconfirmado=2
elif bar==3:
        v "Na verdade Naomi não estou me sentindo bem, acho que vou pra casa descansar."
        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "O que houve? Está doente?"
        v "Não, só uma dor de cabeça e um cansaço estranho."
        Naomi "Tudo bem. Vai pra casa descansar qualquer coisa me liga."
        hide naomi
        v "Ok ligo sim."
        hide cena9

        show cena16:
        with dissolve
        v "Chego em casa me deito na cama fico umas horas mexendo em meu celular até ver uma foto que me choca completamente."
        v "A Naomi e o Josh lado a lado no bar bebendo felizes."
        hide cena16

        show cena7:
        with pixellate

        v "Imediantamente mando uma mensagem para a Naomi."

        $ renpy.movie_cutscene("naomieeu2.webm")


        v "Desligo meu telefone e fico olhando pro teto."
        v "Eu realmente não sei o que está acontecendo comigo e não sei porque mas não estou nada feliz com o rumo que as coisas estão indo."
        $barconfirmado=0
        hide cena7
        show quarto2prontoo:
        with dissolve

        v "Um novo dia começa."

        hide quarto2prontoo

if barconfirmado==1:
    v "Tudo bem você conseguiu eu vou com você."
    show naomirosto:
        zoom 2.0
        yalign 0.1
    with dissolve
    Naomi "Ebaaaa então vamos logo pra Stef."

    v "Stef?"
    if masculino=="true":
        Naomi "É bobo, o bar é o nome da dona."
    elif masculino=="false":
        Naomi "É boba, o bar é o nome da dona."
    hide naomirosto
    hide cena9
    show cena15:
    with dissolve
    v "Naomi me leva pro tal bar da Stef."

    if masculino=="true":
        v "Chegando lá me deparo com um rosto extremamente conhecido por mim e fico paralisado sem saber o que fazer ou falar."
    elif masculino=="false":
        v "Chegando lá me deparo com um rosto extremamente conhecido por mim e fico paralisado sem saber o que fazer ou falar."

    show menino2:
        zoom 1.56
    with dissolve
    josh  "Mas eu não mereço nem um oi? Haha!"

    v "Josh??? O que está fazendo aqui porque não me ligou nem me avisou que viria?"
    hide menino2
    show menino2rosto:
        zoom 1.56
    with dissolve
    josh "Eu queria te fazer uma surpresa."
    hide menino2rosto
    show menino2:
        zoom 1.56
    with dissolve
    josh "Na verdade conheci a naomi tem um tempo pela internet."

    josh "Nem me liguei que você iria se mudar pra mesma cidade dela."
    josh "Ela me chamou pra vir e como eu estou de férias do serviço decidi vir pra ver ela e você com uma surpresa, ela sabia de tudo e me ajudou a planejar haha."

    v "Nossa eu nem sei o que falar, já estava com saudades eu me importo muito com você Josh, fico feliz em te ver."
    hide menino2
    v "Após isso seguimos para o balcão e pedidos para uma moça muito bonita que estava no balcão as bebidas após decidirmos o que vamos beber."
    show stef:
      zoom 1.3
    with dissolve
    stef "Boa noite, me chamo Stefany e sou a dona do bar vou servir vocês pois nosso barman teve um problema de ultima hora então só servimos doses e bebidas prontas, o que vão querer?"
    hide stef
    menu:
        "Doses de tequila":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Três doses de tequila, por favor."
            hide naomi
            show steffofa:
              zoom 1.3
            with dissolve
            stef "Tudo bem. Um momento e já trago."
            hide steffofa
            v "A dona do bar saiu e foi pegar nossas bebidas."
            show stef:
              zoom 1.3
            with dissolve
            stef "Aqui as doses, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide stef
        "Long necks de Not Heineken":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Long necks de Not Heineken, por favor."
            hide naomi
            show steffofa:
                zoom 1.3
            with dissolve
            stef "Tudo bem. Um momento e já trago."
            hide steffofa
            v "A dona do bar saiu e foi pegar nossas bebidas."

            show stef:
                zoom 1.3
            with dissolve
            stef "Aqui as garrafas, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide stef
        "Refrigerante":
            show naomi:
                zoom 2.0
                yalign 0.1
            with dissolve
            Naomi "Três refrigerantes, por favor."
            hide naomi
            show steffofa:
              zoom 1.3
            with dissolve
            stef "Tudo bem. Um momento e já trago."
            hide steffofa
            v "A dona do bar saiu e foi pegar nossas bebidas."
            show stef:
              zoom 1.3
            with dissolve
            stef "Aqui as latas, anotei os pedidos na comanda, qualquer coisa só me chamar."
            hide stef
            v "Ela saiu e foi atender outras pessoas que estavam do lado contrário do balcão."



    show menino2:
        zoom 1.56
    with dissolve
    josh "A menina que morreu era da sala de vocês?"

    v "Acho que sim, mas eu não conversei com ela em momento nenhum, literalmente em um momento ela estava na aula e no outro esmagada no chão da faculdade."
    hide menino2
    show naomi:
        zoom 2.0
        yalign 0.1
    with dissolve
    Naomi "Parece que ela tinha ido com um amigo fumar no terraço, um amigo da sala mesmo. Ele saiu pra algum lugar, deixou ela sozinha e ela morreu. "

    Naomi "Não sei se ele matou ela ou se alguém matou ou ate mesmo ela se matou mas essa historia esta muito estranha pro meu gosto."

    v "Credo"

    v "Conversamos e bebemos a noite toda, espero acordar em casa amanhã."
    hide cena15
    show quarto2prontoo:
    with dissolve

    v "Um novo dia começa."

    hide quarto2prontoo

elif barconfirmado==2:
    v "Nossa que estranho ele veio sem me avisar, achei que quisesse me ver. Já que provavelmente ele não quer me ver vou ficar por aqui mesmo."
    v "Pode ir gatinha não se preocupe comigo, outra hora saímos e eu falo com ele."
    show naomi:
        zoom 2.0
        yalign 0.1
    with dissolve
    Naomi "Tudo bem, você que sabe. vou indo qualquer coisa me mande mensagem"
    hide naomi
    v "Ela fala e sai."
    v "Vou para a aula que é melhor."
    hide cena9
    show cena12:
    with dissolve
    v "Entro na sala e vejo poucas pessoas."

    show sandro:
        zoom 1.7
        yalign 0.5
    with dissolve
    sandro "Vocês já devem ter conhecimento do que aconteceu ontem."
    sandro "Como supervisor de vocês e professor da vitima não poderei ficar aqui então irei deixar uns vídeos e umas atividades pra vocês."
    hide sandro

    v "Sandro entra na sala com uma cara muito ruim provavelmente chateado por ter que trabalhar naquelas circunstancias."
    v "Ele fala apressadamente, coloca os vídeos que disse anota as atividades na lousa e sai tão rápido e bravo como entrou."
    v "Eu realmente deveria ter ido com a Naomi."

    hide cena12
    show cena16:
    with dissolve

    v "Chego em casa depois da aula me jogo no sofá, pego meu telefone e vejo uma foto que a Naomi postou com o Josh e nenhuma mensagem dele."
    v "É, realmente foi uma boa não ir."
    hide cena16
    show quarto2prontoo:
    with dissolve

    v "Um novo dia começa."

    hide quarto2prontoo

show cena7:
with pixellate
v "Eu descobri que o Josh estava na cidade e isso me deixou estranhamente feliz, eu não soube de nada antes, mas ele teve seus motivos."
stop music
play music "audio/mensagem.mp3"

v "Recebi uma mensagem hoje cedo muito estranha da diretoria da faculdade que todos teriam que ficar pós horário hoje para darmos depoimentos pelo assassinato."
v "Eu não tenho nada haver com isso mas ok."
stop music
play music "audio/SomPrincipal.mp3"

v "Vou tirar o dia pra fazer minhas atividades que os professores já postaram no portal."
v "Aproveitar até o horário que eles pediram pra gente aparecer mais cedo pra não atrapalhar nas aulas."
v "Já na hora, ajeito minhas coisas e vou rumo a Universidade."
hide cena7
show cena12:
with dissolve
show sandro:
    zoom 1.8
    yalign 0.5
with dissolve
sandro "Alunos infelizmente algumas situações ruins acontecaram ultimamente e teremos que passar por um procedimento padrão."
sandro "Então, não se assustem que a delegada Klara e o Detetive Krysller estão cuidando do caso."
sandro "E irão falar com vocês individualmente apenas para conversar não se preocupem."
hide sandro

show cena12:
with dissolve
show klaraa:
    zoom 2.0
    yalign 0.5
with dissolve

klaraa "Boa noite alunos eu sou a delegada responsável por esse caso e para começarmos, gostaria que todos fizessem uma fila na porta da sala em ordem alfabética, por favor."
klaraa "O professor Sandro irá chama-los, um por vez para mantermos a ordem."
hide klaraa
hide cena12
show cena11:
with dissolve
s "Após isso todos se dirigiram para a porta e a primeira aluna da ordem já ficou na sala."

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Será o que essa mulher quer falar com a gente? "
hide naomi

v "Não sei, mas coisa boa não deve ser."

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve

Naomi "Depois dos nossos nomes quero te levar em um lugar."
hide naomi

v "Okay, espero que não nos arranje problema."

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Após esses interrogatórios me encontre no corredor."

hide naomi

s "Após um tempo...."

show sandro:
    zoom 1.8
    yalign 0.5
with dissolve

sandro "Me fale seu nome e me acompanhe por favor"

hide sandro

v "Certo, meu nome é [nomeDoProtagonista]."

hide cena11
show cena12:
with dissolve

s "Entro na sala e os dois policiais estão na mesa do professor e tem um local na frente deles pra mim."

show klaraa:
    zoom 2.0
    yalign 0.5
with dissolve
klaraa "Tudo o que você falar será gravado, e poderá sera usado afavor ou contra você no tribunal. Onde você estava exatamente no dia 21/10?"

hide klaraa

menu:

    "Sai com amigos.":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Os professores apontaram que estava na sala, quais mentiras mais está nos contando?"
    "Eu havia acabado de chegar na cidade.":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Fontes confirmam que sim."
    "Não sei":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Não se passaram nem dois dias como não sabe?"

hide klaraa
show klaraa:
    zoom 2.0
    yalign 0.5
with dissolve

klaraa "Certo, e o que estava fazendo no horário de 20:25?"

hide klaraa

menu:

    "Estava no bar.":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Os professores apontaram que estava na sala, novamente mais uma e você estará em apuros."
    "Estava em sala de aula.":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "exatamente como todos confirmaram."
    "Novamente não me lembro":
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "A memória só lembra o que te convém?"

hide klaraa
show klaraa:
    zoom 2.0
    yalign 0.5
with dissolve

klaraa "Você entrou em contato com Annie durante aquele dia mais especificamente nesse horário?"

hide klaraa
menu:

    "Fiquei a aula toda falando com ela.":
        s "..."
    "Eu não estava na aula.":
        s "..."
    "Eu a vi de longe mas, não falei com ela":
        s "..."

show klaraa:
    zoom 2.0
    yalign 0.5
with dissolve

klaraa "Temos fontes de tudo cada mentira contada aqui terá uma consequência."
klaraa "Detetive. Entrado em contato ou não todos de sua turma tiveram o ultimo contato com a garota, minutos antes de sua morte."
hide klaraa

s "Ela fala e o outro policial se dirige a mim."

s "O policial fecha a cara e diz:"

show krysllerserio:
    zoom 1.8
with dissolve

krysller "Você conhece ou conversou com Guilherme Caixeta?"

hide krysllerserio

menu:

    "Meu melhor amigo.":
        show krysllerserio:
            zoom 1.8
        with dissolve
        krysller "Certeza? Parece que não"
    "Não falei com ele em momento algum.":
        show krysllerserio:
            zoom 1.8
        with dissolve
        krysller "Tudo bem, podemos seguir com essa afirmação."
    "Falo com ele sempre.":
        show krysllerserio:
            zoom 1.8
        with dissolve
        krysller "Ele não nos disse isso."

hide krysllerserio

show krysller:
    zoom 1.8
with dissolve
krysller "O que estava acontecendo no momento em que Annie saiu da sala e você a viu pela ultima vez."
hide krysller

menu:

    "Todos estavam conversando era troca de horário.":
        s "..."
    "Eu não estava prestando atenção nela.":
        s "..."
    "A aula havia acabado todos estavam saindo.":
        s "..."

show krysller:
    zoom 1.8
with dissolve

krysller "Obrigado, [nomeDoProtagonista], pode se retirar da sala."

hide krysller
hide cena12
show cena11:
with dissolve

v "Saio andando e vou direto para o corredor encontrar a Naomi, nem quero imaginar o que ela está aprontando."

hide cena11
show cena9:
with dissolve

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Finalmente, não aguentava mais te esperar. Eu consegui a chave do terraço que a garota foi morta quer dar uma olhada?"
Naomi "Parece que mesmo depois desse assassinato o pessoal continua indo la escondido."

hide naomi

v "Está louca????????? E se acontecer algo conosco."

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Relaxa a gente fica escondido."

hide naomi

menu:

    "Okay vamos.":
        show naomirosto:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Ebaaaa, vamos."
        hide naomirosto
        show cena19:
        with dissolve
        v "Ela fala muito sorridente e me arrasta escadas acima até encontrarmos um corredor que se acabava em uma porta com um cadeado enorme."
        v "Naomi pega uma chave do bolso e destranca o cadeado e entra."

    "Não, nem pensar!":
        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Vamos por favor é muito importante não me deixe sozinha com um assassino a solta nessa faculdade por favor."
        hide naomi
        v "Saco Naomi você não para de fazer merda nunca, não sei porque ainda te acompanho nisso."
        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Eba, vamos."
        hide naomi
        hide naomirosto
        show cena19:
        with dissolve
        v "Ela fala muito sorridente e me arrasta escadas acima até encontrarmos um corredor que se acabava em uma porta com um cadeado enorme."
        v "Naomi pega uma chave do bolso e destranca o cadeado e entra."

stop music
play music "audio/vento2.mp3"

show cena17:
with dissolve
s "Estava um vento forte, tinham uma bela vista de onde estavam, contudo estava vazio e frio. Era um bom lugar."

v "O local estava vazio e era muito bonito a visão lá de cima entramos e ficamos escondidos enquanto Naomi me falava algumas coisas."
show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Eu ouvi de alguns professores, que foi assassinato mesmo e que pode ser tanto os alunos da sala quanto um dos nossos professores. Louco ne?"
hide naomi

v "E porque estamos aqui? Não vamos descobrir isso aqui."

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
if masculino=="true":
    Naomi "Claro que vamos, fica quieto que a gente da um jeito."
elif masculino=="false":
    Naomi "Claro que vamos, fica quieta que a gente da um jeito."

hide naomi
v "O tempo foi passando e anoitecendo, nada acontecia até que um casal entrou pela mesma porta e começaram a conversar."

vsz "O que vocês falaram para eles?"
show guilherme:
    zoom 2.0
    yalign 0.1
with dissolve

guilherme "Nada de mais, só não disse que estava com a Annie um minuto antes da morte dela terminando com a garota né Talia."
hide guilherme
show taliadesesperada:
    zoom 1.5
    yalign 0.1
with dissolve

lia "Estamos ferrados, eu fiquei nervosa provavelmente vão desconfiar de mim."
hide taliadesesperada
show guilherme: #preocupado
    zoom 2.0
    yalign 0.1
with dissolve

guilherme "Calma amor, não matamos a garota, só queríamos tirar ela do nosso pé. Mas inventar aquelas coisas, mentir pra todo mundo não sei se foi o melhor a se fazer."
hide guilherme
show taliadesesperada:
    zoom 1.5
    yalign 0.1
with dissolve

lia "Não vai demorar muito para descobrirem, espalhamos aqueles boatos do Sandro e aposto que está tudo indo para ele."
hide taliadesesperada

show guilherme:
    zoom 2.0
    yalign 0.1
with dissolve
guilherme "Bom, pelo menos o verdadeiro assassino fica sem suspeitas."

hide guilherme
show taliadesesperada:
    zoom 1.5
    yalign 0.1
with dissolve
lia "Então sobre isso, eu posso ter falado indiretamente apontando quem seria, eu não disse nomes mas com certeza saberão quem foi."
hide taliadesesperada
show guilhermebravo:
    zoom 2.0
    yalign 0.1
with dissolve

guilherme "Porra Talia, fudeu muito. Com certeza ele vai falar que foi a gente. Pode até se vingar, você não pensa? Estamos muito ferrados."
guilherme "Sendo um bom aluno todos esses anos pra nada, que merda."
hide guilhermebravo
show taliadesesperada:
    zoom 1.5
    yalign 0.1
with dissolve

lia "Desculpe eu entrei em pânico porque aquela delegada sabia que eu estava mentindo e me pressionou."
hide taliadesesperada
v "A porta se abre e ambos ficam em silêncio. Estava muito escuro vi apenas a sombra de alguém."
v "Um homem adulto provavelmente, segurando uma faca enorme e aparentemente bem afiada usando luvas."
vsz "Nós tínhamos um acordo, eu limpava a barra de vocês com a garota e vocês limpavam a minha, não era??"
show taliadesesperada:
    zoom 1.5
    yalign 0.1
with dissolve

lia "Sim e fizemos, juro que fizemos ninguém sabe que foi você."
hide taliadesesperada
vsz "Ninguém sabe? Não sabem porque eu sou esperto, eu incriminei a Mislene colocando aqui o DNA dela junto com o DNA da garota."
vsz "Mesmo com a merda que você fez Talia, ainda sairíamos bem se você não tivesse dado com a língua nos dentes. Eles estão levando ela agora."
vsz "Após me interrogarem, dei a entender que ambos os dois estavam envolvidos e vou me livrar dos dois e das provas sumirei daqui."
stop music
play music "audio/Vento2.mp3"
s "A voz Misteriosa se irrita com o casal, o vento começa a ficar mais forte, o clima vai ficando desconfortável."

vsz "Passar uns anos na cadeia vai lhe fazer bem Guilherme."

$ renpy.movie_cutscene("terraco_1.webm")

v "Olhei para a Naomi e ela estava tão aterrorizada quanto eu."
v "E esse vento? está muito forte..."

show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Vamos sair daqui imediatamente, droga, merda, não era para gente ver isso. Eu sabia que os dois tinham ligação e ouvi que eles iam se encontrar aqui, droga."

hide naomiassustada
hide cena17
show cena19:
with dissolve
stop music
play music "audio/musicadesuspense.mp3"

v "Ela já sai me arrastando pra sairmos dali, provavelmente todos já estavam subindo para saber o que aconteceu."
show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Vamos sair daqui, a gente não tem ligação nenhuma com toda essa merda, ainda bem que ninguém viu a gente. Vamos fingir que nada aconteceu."
hide naomiassustada
v "Eu nem sabia o que dizer ainda estava sem reação por tudo. Estávamos no corredor quando várias pessoas passam correndo pela gente em direção ao terraço."

hide cena19
show cena9:
with pixellate
show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Nunca conte a ninguém nada do que ouviu."
hide naomiassustada
v "Porque? O garoto vai ser preso sem nem ter culpa."
show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve

Naomi "Ele tem culpa a garota tinha culpa, eu sabia, o Gabriel estava certo armaram tudo para Annie se foder."
hide naomiassustada
v "Quem é Gabriel?"
show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve

Naomi "O irmão da Annie estudou na faculdade também, ele estava investigando tudo para descobrir o que houve com a irmã."
Naomi "Pelo que parece ela havia descoberto um segredo da Talia e do Guilherme, que eles teriam mandado matar a garota."
hide naomiassustada
v "Estavamos tentando sair da faculdade mas todos os portões estavam trancados."

show naomiassustada:
    zoom 2.0
    yalign 0.1
with dissolve

Naomi "Alguém trancou os portões, precisamos encontrar o Gabriel, nada pode acontecer com ele vamos."
Naomi "Vou mandar uma mensagem para ele perguntando."
Naomi "Droga, meu celular acabou a bateria."
Naomi "Me empresta o seu {color=#0099ff}[nomeDoProtagonista]{/color} ?"

hide naomiassustada

s "Naomi pega o celular emprestado vai para um canto ali mesmo e manda mensagens para saber onde o Gabriel estava."

$ renpy.movie_cutscene("chatgabriel.webm")

show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Vamos para a biblioteca o Gabriel está lá."

hide naomi

v "E lá vai ela me arrastando pela faculdade novamente."
show cena18
with dissolve

s "A biblioteca estranhamente estava vazia. Era até melhor, teriam mais privicidade para conversarem sobre tal acontecimento."

v "Chegamos até a biblioteca, incrivelmente intacta depois de tudo que houve naquele local."
show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
Naomi "Gabriel? Sou eu."
hide naomi
show gabriel:
    zoom 0.6
with dissolve
gabriel "Naomi? Ainda bem que me achou achei que tivesse acontecido algo com você, esse lugar está uma loucura."
hide gabriel
show naomi:
    zoom 2.0
    yalign 0.1
with dissolve

Naomi "Você não imagina o que a gente viu. Um cara contou que matou a Annie a pedido da Talia e do Guilherme mas eu não entendi bem o porque esse cara tinha problemas com ela."
Naomi "Depois ele simplesmente matou a garota e incriminou o rapaz na nossa frente, estávamos escondidos mas vimos tudo o que aconteceu."
Naomi "E parece que ele incriminou a Mislene do assassinato precisamos fazer algo para ajudar."
hide naomi

show gabriel:
    zoom 0.6
with dissolve
gabriel "O meu bem, nem tudo é tão simples como você imagina, eu te explico tudo mas não temos tempo agora, vamos."

hide gabriel

v "ESPERA, alguém pode me dizer o que está acontecendo?"

show gabrielbravo:
    zoom 0.6
with dissolve
gabriel "Estamos correndo risco morte imbecil."
hide gabrielbravo

show cena20:
with dissolve
stop music
play music "audio/magia.mp3"
show gabriel:
    zoom 0.6
with dissolve

gabriel "Eu achei isso, em uma sala secreta na sala do reitor, algumas coisas ligadas a sacrifícios femininos e alguns cultos religiosos."
gabriel "Parece que eles querem que um Deus domine a terra algo assim, bizarro!."
gabriel "Eu tenho certeza que ele tem relação com a morte da Annie. Só não sei o porque ele colocou um professor pra fazer o trabalho sujo pra ele."

stop music
play music "audio/musicadesuspense.mp3"

hide gabriel
show naomi:
    zoom 2.0
    yalign 0.1
with dissolve
hide cena20
show cena18:
with dissolve
Naomi "Então, a Talia e o Guilherme precisaram dar um fim na Annie e ajudou o assassino a escolher a garota 'perfeita'."

hide naomi

v "WoW, olha pessoal como assim? O diretor? Gente? Magia Negra? isso não existe cara, vocês escutaram o que disseram? Tá errado."

show gabrielbravo:
    zoom 0.6
with dissolve
gabriel "Já estou me cansando de você, ou você acredita ou não. Não temos tempo pra ficar com drama ou medinho."
gabriel "Quero descobrir porque mataram minha irmã e dar o fora dessa merda de lugar, então decida o que vai fazer e vamos logo, precisamos sair daqui imediatamente."

hide gabrielbravo

menu:

    "Ir com Gabriel atrás do Reitor.":

        v "Tudo bem então vamos lá, quero me livrar disso logo."

        hide cena19
        hide cena9
        show cena9:
        with pixellate
        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve

        Naomi "Ali, vamos falar com os policiais. Eles estão levando a Mislene, ela é inocente precisamos impedir isso."
        hide naomi

        show gabriel:
            zoom 0.6
        with dissolve

        gabriel "Ela não é inocente tão como vocês pensam, vão levar ela de qualquer jeito, mas precisamos de um policial para impedir o reitor, de qualquer forma vamos logo."
        hide gabriel

        v "Delegada! Aqui!"

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Meninos, o que houve? O que estão fazendo na faculdade, achei que todos haviam saído."
        hide klaraa

        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Ninguém conseguiu sair."
        hide naomi

        v "Delegada, a professora Mislene é inocente não foi ela que assassinou a Annie."

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Criança nem tudo é simples como você pensa, sabemos disso, mas isso não quer dizer que sua amada professora é inocente."
        klaraa "Nós vamos leva-lá presa de qualquer forma."
        hide klaraa

        show mislenealgemada:
            zoom 1.34
        with dissolve

        mislene "Eu já disse que não fiz nada, essas provas são falsas, vocês têm que acreditar em mim."
        hide mislenealgemada

        show klaraa:
            zoom 2.0
            yalign 0.10
        with dissolve
        klaraa "Não se faça de sínica sua aliciadora, se depender de mim você apodrece na cadeia."
        hide klaraa

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "Tá, tá, chega!"
        hide gabrielbravo

        show gabriel:
            zoom 0.6
        with dissolve
        gabriel "Sabemos quem é o real assassino da Annie e da Talia, e precisamos que venha com a gente rápido."
        hide gabriel

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Tudo bem, Detetive leve essa mulher pra delegacia enquanto vou com os meninos."
        hide klaraa

        show krysllerserio:
            zoom 1.8
        with dissolve
        krysllerserio "Ok, Delegada."
        hide krysllerserio

        show gabriel:
            zoom 0.6
        with dissolve
        gabriel "Onde está o Reitor?"
        hide gabriel

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Estava em sua sala na ultima vez em que o vimos"
        hide klaraa

        show gabriel:
            zoom 0.6
        with dissolve
        gabriel "Vamos lá, no caminho a gente explica o que aconteceu."
        hide gabriel

        hide cena18


        show cena10:
        with pixellate

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Como assim? Nossa, muita informação para processar. A sala está vazia, vamos procurar algo que o incrimine."
        klaraa "Rápido todos procurem logo."
        hide klaraa

        s "Todos ficaram procurando, mas estranhamente eu escuto um barulho como se fosse um choro de uma criança."
        stop music
        play music "audio/choro.mp3"

        v "Pessoal, vocês estão ouvindo isso?"

        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "O que?"
        hide naomi

        v "É, parece um choro."
        show gabriel:
            zoom 0.6
        with dissolve
        gabriel "Aqui!"
        hide gabriel

        stop music
        play music "audio/musicadesuspense.mp3"

        hide cena25
        show cena10compl:
        s "Gabriel quebra um pedaço de madeira que tinha ali atrás de um armário e descobre uma porta secreta pelo que parece."

        v "Vamos."

        hide cena10
        show cena25
        with pixellate
        s "Descendo as escadas o lugar era horrendo, um calabouço e uma criança presa em uma das celas."
        ##hide calabouço

        show naomiemchoque:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Meu deus vamos ajuda-lá."
        hide naomiemchoque

        s "Gabriel pegou um pedaço de ferro e começou a bater no cadeado pra abrir a porta."
        hide cena25
        show cena21:
        with pixellate
        criança "Socorro, me tira daqui."

        s "Libertamos a criança e a Naomi foi em sua direção."
        s "Naomi pega na mão da criança e a leva para fora daquela cela."

        hide cena21
        show cena25:
        with pixellate

        s "Naomi espantada fala com a criança."

        show naomiemchoque:
            zoom 2.0
            yalign 0.1
        with dissolve

        Naomi "Você está bem querida? Como você se chama?"
        hide naomiemchoque

        show filhaaltamirchorando:
            zoom 1.6
        with dissolve
        filhaaltamir "Cadê meu papai? O moço mal mandou o papai fazer coisas ruins."
        hide filhaaltamirchorando

        show gabriel:
            zoom 0.6
        with dissolve
        gabriel "Quem é seu pai? Qual moço?"
        hide gabriel

        show filhaaltamirchorando:
            zoom 1.6
        with dissolve
        filhaaltamir "O papai chama Altamir, e o moço eu não sei, ele é barbado e uma roupa preta. Ajuda meu papai moço, ele não é ruim. O monstro me prendeu e o papai ia me salvar."
        hide filhaaltamirchorando

        show filhaaltamirchorando:
            zoom 1.6
        with dissolve
        filhaaltamir "Si,sim Tio..."
        hide filhaaltamirchorando

        show gabrielespantado:
            zoom 2.0
        with dissolve
        gabriel "Altamir?? Vamos ajudar seu pai mocinha, a tia Naomi vai te levar pra um hospital e a gente vai ajudar ele tá?"
        hide gabrielespantado

        show filhaaltamir:
            zoom 1.6
        with dissolve
        filhaaltamir "Tá bom Tio, muito obrigada! E eu me chamo Aika."
        hide filhaaltamir

        v "Caralho, como alguém tem coragem de fazer isso com uma criança."

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "Mano, por isso o Altamir matou as meninas, ele estava sendo chantageado pelo Reitor, tudo faz sentido agora."
        hide gabrielbravo

        hide cena25
        show cena10compl:
        with pixellate
        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        hide cena25
        show cena10compl:
        with pixellate
        klaraa "Pessoal aqui rápido."
        hide klaraa

        hide cena10compl
        show cena23:
        with pixellate
        show klaraa:
            zoom 2.0
            yalign 0.5
            xalign 0.9
        with dissolve

        s "A delegada grita e vamos até ela. Ela tinha encontrado um quadro um pentagrama enorme com algumas escritas, datas e coordenadas na sala do reitor."
        hide cena23
        show cena10compl:
        with pixellate
        hide klaraa

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Precisamos acha-lo rápido."
        klaraa "Vamos buscar a garota lá em baixo. "
        hide klaraa

        hide cena10compl
        show cena25
        with pixellate

        s "Todos descem as escadas novamente para buscar a garota."
        show reitor:
            zoom 1.2
        with pixellate
        r "Precisam achar quem?"
        hide reitor

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Parado, você está preso."
        hide klaraa

        show reitorrisada:
            zoom 1.2
        with pixellate
        r "Creio que não, vocês todos serão mortos, eu completei o ritual todos os portões estão trancados, ninguém sairá."
        hide reitorrisada

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "Você não vai matar ninguém."
        hide gabrielbravo

        show reitorrisada:
            zoom 1.2
        with pixellate

        stop music
        play music "audio/risadareitor.mp3"
        r "Vamos ver então, vocês estão fodidos, o ritual foi feito, o grande Lord aparecera á qualquer momento e nenhum de vocês será salvo."
        hide reitorrisada
        stop music
        play music "audio/musicadesuspense.mp3"

        s "Nesse momento coisas estranhas começaram a acontecer. O reitor começou a se transformar em um monstro sua pele estava derretendo."
        s "Estaríamos perdidos. A policial estava atirando nele, mas não fazia efeito. Balas normais não faziam efeito no monstro."

        $ renpy.movie_cutscene("composicao1.webm")

        stop music
        play music "audio/Tiro.mp3"

        s "De repente.\nUm som.\nUm tiro."
        s "O corpo do Reitor cai desacordado todo monstruoso, voltando ao normal, porém havia sido atingido com uma bala bem na cabeça."

        stop music
        play music "audio/musicadesuspense.mp3"

        v "Joshua?????"

        s "Corro em sua direção e fico do seu lado. Logo em seguida o Altamir chega extremamente desesperado."

        show altamirdesesperado:
            zoom 1.7
        with dissolve
        altamir "AIKA! Eu ouvi um tiro, Aika minha filha, cadê ela? Está bem?"
        hide altamirdesesperado

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Ela está bem, sabemos tudo que fez, porém sabemos que foi ameaçado com o sequestro de sua filha."
        klaraa "Preciso que de seu depoimento terá consequências mas sabemos que a culpa não é sua."
        hide klaraa

        show altamirtriste:
            zoom 1.7
        with dissolve
        altamir "Faço qualquer coisa, preciso pagar pelo que fiz as duas garotas. Só quero que minha filha fique salva e bem, ela é tudo pra mim."
        hide altamirtriste

        s "A delegada algema o Professor e o Reitor também, que estava desacordado no chão felizmente vivo, para pagar por seus atos. Ela sai arrastando o corpo enquanto o Altamir a ajuda."

        v "O que você fez para neutralizar ele?"
        show joshuabravo:
            zoom 1.56
        with dissolve
        josh "Você está bem Gabriel? Cara não me assusta assim. Fui na sua casa e lá estava uma bagunça."
        josh "Sorte que li os papeis que estavam lá. E respondendo sua pergunta {color=#0099ff}[nomeDoProtagonista]{/color}, balas de cobre com um tipo de liquido benzido."
        hide joshuabravo

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "O que você foi fazer na minha casa eu disse que não queria olhar na sua cara mais, seu merda."
        hide gabrielbravo

        show menino2:
            zoom 1.56
        with dissolve
        josh "Poxa, mas nem um obrigado?"
        hide menino2

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "Sai daqui imbecil, não fez mais que sua obrigação."
        hide gabrielbravo

        s "O clima entre os dois era estranho, eu já não sabia mais nada do que estava acontecendo e o porque de Joshua conhecer o Gabriel."
        s "Ou qual a relação estanha dos dois, mas finalmente acabou."
        s "Acabou."
        s "Porém, agora será meu recomeço. Recomeço de tudo e de todos creio eu. O mal acabou e poderemos seguir em frente."

        stop music
        play music "audio/Vitória.mp3"
        hide cena25
        show final1:
        with pixellate
        s "Parabéns, você completou o jogo com sucesso!"
        s "FIM..."
        stop music
        $ renpy.movie_cutscene("finalbom.webm")

    "Ir atrás do professor assassino.":

        v "Reitor? Pessoal temos que ir atrás do Professor não do reitor."

        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabrielbravo "Você está me desafiando? Falando que eu estou mentindo? Quem você pensa que é? Cansei de você. Que se foda vou atrás dele você querendo ou não."
        hide gabrielbravo
        menu:
            "Ir com o Gabriel":

                v "Tudo bem então vamos lá, quero me livrar disso logo."
                hide cena19
                hide cena9
                show cena9:
                with pixellate
                show naomi:
                    zoom 2.0
                    yalign 0.1
                with dissolve

                Naomi "Ali, vamos falar com os policiais. Eles estão levando a Mislene, ela é inocente precisamos impedir isso."
                hide naomi

                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Ela não é inocente como vocês pensam, vão levar ela de qualquer jeito mas precisamos de um policial pra impedir o reitor de qualquer forma vamos."
                hide gabriel

                v "Delegada! Aqui!"
                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Meninos, o que houve? O que estão fazendo na faculdade, achei que todos haviam saído."
                hide klaraa

                show naomi:
                    zoom 2.0
                    yalign 0.1
                with dissolve
                Naomi "Ninguém conseguiu sair."
                hide naomi

                v "Delegada, a professora Mislene é inocente não foi ela que matou a Annie."
                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Criança nem tudo é simples como você pensa, sabemos disso, mas isso não quer dizer que sua amada professora é inocente."
                hide klaraa


                show mislenealgemada:
                    zoom 1.34
                with dissolve

                mislene "Eu já disse que não fiz nada, essas provas são falsas, vocês têm que acreditar em mim."
                hide mislenealgemada

                show klaraa:
                    zoom 2.0
                    yalign 0.10
                with dissolve
                klaraa "Não se faça de sínica sua aliciadora, se depender de mim você apodrece na cadeia."
                hide klaraa

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Tá, tá, chega!"
                hide gabrielbravo

                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Sabemos quem é o real assassino da Annie e da Talia, e precisamos que venha com a gente rápido."
                hide gabriel

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Tudo bem, Detetive leve essa mulher pra delegacia enquanto vou com os meninos."
                hide klaraa

                show krysllerserio:
                    zoom 1.8
                with dissolve
                krysllerserio "Ok, Delegada."
                hide krysllerserio

                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Onde está o Reitor?"
                hide gabriel

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Estava em sua sala na ultima vez em que o vimos"
                hide klaraa

                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Vamos lá, no caminho a gente explica o que aconteceu."
                hide gabriel

                hide cena18
                stop music
                play music "audio/musicadesuspense.mp3"

                show cena10:
                with pixellate

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Como assim? Nossa, muita informação para processar. A sala está vazia, vamos procurar algo que o incrimine."
                klaraa "Rápido todos procurem logo."
                hide klaraa

                s "Todos ficaram procurando, mas estranhamente eu escuto um barulho como se fosse um choro de uma criança."
                stop music
                play music "audio/choro.mp3"

                v "Pessoal, vocês estão ouvindo isso?"

                show naomi:
                    zoom 2.0
                    yalign 0.1
                with dissolve
                Naomi "O que?"
                hide naomi

                v "É, parece um choro."
                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Aqui!"
                hide gabriel

                stop music
                play music "audio/musicadesuspense.mp3"

                hide cena25
                show cena10compl:
                s "Gabriel quebra um pedaço de madeira que tinha ali atrás de um armário e descobre uma porta secreta pelo que parece."

                v "Vamos."

                hide cena10
                show cena25
                with pixellate
                s "Descendo as escadas o lugar era horrendo, um calabouço e uma criança presa em uma das celas."
                ##hide calabouço

                show naomiemchoque:
                    zoom 2.0
                    yalign 0.1
                with dissolve
                Naomi "Meu deus vamos ajuda-lá."
                hide naomiemchoque

                s "Gabriel pegou um pedaço de ferro e começou a bater no cadeado pra abrir a porta."
                hide cena25
                show cena21:
                with pixellate
                criança "Socorro, me tira daqui."

                s "Libertamos a criança e a Naomi foi em sua direção."
                s "Naomi pega na mão da criança e a leva para fora daquela cela."

                hide cena21
                show cena25:
                with pixellate

                s "Naomi espantada fala com a criança."

                show naomiemchoque:
                    zoom 2.0
                    yalign 0.1
                with dissolve

                Naomi "Você está bem querida? Como você se chama?"
                hide naomiemchoque

                show filhaaltamirchorando:
                    zoom 1.6
                with dissolve
                filhaaltamir "Cadê meu papai? O moço mal mandou o papai fazer coisas ruins."
                hide filhaaltamirchorando

                show gabriel:
                    zoom 0.6
                with dissolve
                gabriel "Quem é seu pai? Qual moço?"
                hide gabriel

                show filhaaltamirchorando:
                    zoom 1.6
                with dissolve
                filhaaltamir "O papai chama Altamir, e o moço eu não sei, ele é barbado e uma roupa preta. Ajuda meu papai moço, ele não é ruim. O monstro me prendeu e o papai ia me salvar."
                hide filhaaltamirchorando

                show filhaaltamirchorando:
                    zoom 1.6
                with dissolve
                filhaaltamir "Si,sim Tio..."
                hide filhaaltamirchorando

                show gabrielespantado:
                    zoom 2.0
                with dissolve
                gabriel "Altamir?? Vamos ajudar seu pai mocinha, a tia Naomi vai te levar pra um hospital e a gente vai ajudar ele tá?"
                hide gabrielespantado

                show filhaaltamir:
                    zoom 1.6
                with dissolve
                filhaaltamir "Tá bom Tio, muito obrigada! E eu me chamo Aika."
                hide filhaaltamir

                v "Caralho, como alguém tem coragem de fazer isso com uma criança."

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Mano, por isso o Altamir matou as meninas, ele estava sendo chantageado pelo Reitor, tudo faz sentido agora."
                hide gabrielbravo

                hide cena25
                show cena10compl:
                with pixellate
                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                hide cena25
                show cena10compl:
                with pixellate
                klaraa "Pessoal aqui rápido."
                hide klaraa

                hide cena10compl
                show cena23:
                with pixellate
                show klaraa:
                    zoom 2.0
                    yalign 0.5
                    xalign 0.9
                with dissolve

                s "A delegada grita e vamos até ela. Ela tinha encontrado um quadro um pentagrama enorme com algumas escritas, datas e coordenadas na sala do reitor."
                hide cena23
                show cena10compl:
                with pixellate
                hide klaraa

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Precisamos acha-lo rápido."
                klaraa "Vamos buscar a garota lá em baixo. "
                hide klaraa

                hide cena10compl
                show cena25
                with pixellate

                s "Todos descem as escadas novamente para buscar a garota."
                show reitor:
                    zoom 1.2
                with pixellate
                r "Precisam achar quem?"
                hide reitor

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Parado, você está preso."
                hide klaraa

                show reitorrisada:
                    zoom 1.2
                with pixellate
                r "Creio que não, vocês todos serão mortos, eu completei o ritual todos os portões estão trancados, ninguém sairá."
                hide reitorrisada

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Você não vai matar ninguém."
                hide gabrielbravo

                show reitorrisada:
                    zoom 1.2
                with pixellate

                stop music
                play music "audio/risadareitor.mp3"
                r "Vamos ver então, vocês estão fodidos, o ritual foi feito, o grande Lord aparecera á qualquer momento e nenhum de vocês será salvo."
                hide reitorrisada
                stop music
                play music "audio/musicadesuspense.mp3"

                s "Nesse momento coisas estranhas começaram a acontecer. O reitor começou a se transformar em um monstro sua pele estava derretendo."
                s "Estaríamos perdidos. A policial estava atirando nele, mas não fazia efeito. Balas normais não faziam efeito no monstro."

                $ renpy.movie_cutscene("composicao1.webm")

                stop music
                play music "audio/Tiro.mp3"

                s "De repente.\nUm som.\nUm tiro."
                s "O corpo do Reitor cai desacordado todo monstruoso, voltando ao normal, porém havia sido atingido com uma bala bem na cabeça."

                stop music
                play music "audio/musicadesuspense.mp3"

                v "Joshua?????"

                s "Corro em sua direção e fico do seu lado. Logo em seguida o Altamir chega extremamente desesperado."

                show altamirdesesperado:
                    zoom 1.7
                with dissolve
                altamir "AIKA! Eu ouvi um tiro, Aika minha filha, cadê ela? Está bem?"
                hide altamirdesesperado

                show klaraa:
                    zoom 2.0
                    yalign 0.5
                with dissolve
                klaraa "Ela está bem, sabemos tudo que fez, porém sabemos que foi ameaçado com o sequestro de sua filha."
                klaraa "Preciso que de seu depoimento terá consequências mas sabemos que a culpa não é sua."
                hide klaraa

                show altamirtriste:
                    zoom 1.7
                with dissolve
                altamir "Faço qualquer coisa, preciso pagar pelo que fiz as duas garotas. Só quero que minha filha fique salva e bem, ela é tudo pra mim."
                hide altamirtriste

                s "A delegada algema o Professor e o Reitor também, que estava desacordado no chão felizmente vivo, para pagar por seus atos. Ela sai arrastando o corpo enquanto o Altamir a ajuda."

                v "O que você fez para neutralizar ele?"
                show joshuabravo:
                    zoom 1.56
                with dissolve
                josh "Você está bem Gabriel? Cara não me assusta assim. Fui na sua casa e lá estava uma bagunça."
                josh "Sorte que li os papeis que estavam lá. E respondendo sua pergunta {color=#0099ff}[nomeDoProtagonista]{/color}, balas de cobre com um tipo de liquido benzido."
                hide joshuabravo

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "O que você foi fazer na minha casa eu disse que não queria olhar na sua cara mais, seu merda."
                hide gabrielbravo

                show menino2:
                    zoom 1.56
                with dissolve
                josh "Poxa, mas nem um obrigado?"
                hide menino2

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Sai daqui imbecil, não fez mais que sua obrigação."
                hide gabrielbravo

                s "O clima entre os dois era estranho, eu já não sabia mais nada do que estava acontecendo e o porque de Joshua conhecer o Gabriel."
                s "Ou qual a relação estanha dos dois, mas finalmente acabou."
                s "Acabou."
                s "Porém, agora será meu recomeço. Recomeço de tudo e de todos creio eu. O mal acabou e poderemos seguir em frente."


                stop music
                play music "audio/Vitória.mp3"

                show final1:
                with pixellate
                s "Parabéns, pegou um caminho mais transtornado porém. Você venceu."
                s "Fim..."
                hide final1
                stop music

                $ renpy.movie_cutscene("finalbom.webm")

            "Não ir com o Gabiel":

                v "Não, olha aqui, quem cansou de você foi eu. Chega do nada querendo mandar em todo mundo."
                v "Vai se foder você e me deixa em paz eu vou atrás de quem matou e não de uma pessoa que não tem nada haver."
                v "Vamos Naomi."

                show naomi:
                    zoom 2.0
                    yalign 0.1
                with dissolve
                if masculino=="true":
                    Naomi "Desculpa Gabi, mas tenho que ir com ele."
                elif masculino=="false":
                    Naomi "Desculpa Gabi, mas tenho que ir com ela."
                hide naomi

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabrielbravo "AAAAA, Caralho vocês são imbecis? Ta bom, vamos. Só não digam que eu não avisei depois."
                hide gabrielbravo

                hide cena19
                hide cena9
                show cena9:
                with pixellate
                v "Tá, vamos logo."

                with pixellate
                hide cena9
                show cena11:
                with pixellate
                s "Fomos até a sala de aula e vimos o altamir saindo para a sala do reitor após ter terminando de guardar suas coisas, rapidamente tudo se encaixou."
                s " Seguimos ele."
                s "Quando ele entrou na sala do reitor, entramos logo atrás."

                hide cena11
                show cena10:
                with pixellate

                v "Foi você!!!!!!!"
                v "Você matou a Talia e a Anne."

                show altamir:
                    zoom 1.7
                with dissolve
                altamir "Olha, vocês precisam me entender. Preciso da ajuda de vocês."
                hide altamir

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Sua ajuda? Você matou minha irmã seu velho desgraçado."
                hide gabrielbravo

                v "Calma Gabriel, porque você precisaria da nossa ajuda?"

                show altamirtriste:
                    zoom 1.7
                with dissolve
                altamir "Ele levou minha filinha Aika. Tudo o que eu fiz foi por ela, ele me chantageou."
                altamir "A sequestrou e falou que se eu não matasse as garotas ela morreria, eu faço tudo por ela desde que a mãe morreu, já perdi uma não posso perder as duas."
                hide altamirtriste


                show cena22:
                with dissolve
                s "Diz e mostra em seu telefone uma foto da garota sorrindo."
                hide cena22

                show altamirtriste:
                    zoom 1.7
                with dissolve
                altamir "Me ajudem por favor."
                hide altamirtriste

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "O reitor? Eu sabia eu disse pra vocês."
                gabriel "Mas você não ficará livre pelo que fez com a Anne seu nojento, nem que eu mesmo tenha que fazer algo com minhas próprias mãos."
                hide gabrielbravo

                show altamir:
                    zoom 1.7
                with dissolve
                altamir "Ele está no calabouço, provavelmente ela está lá também."
                hide altamir

                s "Porém, chegamos tarde demais, uma porta secreta estava aberta que dava a uma escada. Descemos."

                hide cena10compl
                show cena25:
                    zoom 1.2
                with pixellate

                s "Entrando no calabouço.."

                show reitorcav:
                    zoom 1.2
                stop music
                play music "audio/risadareitor.mp3"
                reitorcav "Estava esperando vocês. Seu amiguinho infelizmente parece que chegou cedo demais."
                hide reitorcav

                stop music
                play music "audio/musicadesuspense.mp3"
                show joshuavirado:
                    zoom 1.0
                    yalign 0.9
                    xalign 1.2
                with pixellate

                s "Joshua todo destruído no canto da parede, mas ainda sim se esforçou para falar com seus amigos."
                josh "..."
                s "Joshua estava no chão todo machucado, aparentemente morto."

                hide joshuavirado

                show gabrielbravo:
                    zoom 0.6
                with dissolve
                gabriel "Joshua? O que você fez seu merda?"
                hide gabrielbravo

                show reitorcav:
                    zoom 1.2
                with pixellate
                stop music
                play music "audio/risadareitor.mp3"

                r "A culpa é dele, não mandei esse rapaz vir atrás de mim sozinho com balas de cobre aparentemente ele é bem esperto, pois é o único jeito de me neutralizar."
                r "Mas, eu sou mais não tentem intervir no meu caminho que o resultado será o mesmo a todos vocês."
                r "E a você Altamir, seu lixo. Você tinha um trato comigo e eu sou um homem de palavra. Novamente outros vão pagar pelo seu erro."
                hide reitorcav

                stop music
                play music "audio/musicadesuspense.mp3"
                show altamirdesesperado:
                    zoom 1.7
                with dissolve
                altamir "NÃO POR FAVOR. Me mate, mas não mate a Aika, ela não tem nada haver com isso."
                hide altamirdesesperado

                show reitorcav:
                    zoom 1.2
                with pixellate
                r "Matarei todos vocês!!!"
                hide reitorcav

                s "Ele em uma velocidade muito rápida empurra todos nós no chão e pega a garota que estava presa dentro de uma das celas"

                show reitorcav:
                    zoom 1.2
                with pixellate
                r "Começarei pela pequenina aqui."
                hide reitorcav

                v "É o fim, se ao menos a gente tivesse chegado antes, se eu tivesse ouvido o Gabriel, nada disso teria acontecido."

                show altamirtriste:
                    zoom 1.7
                with dissolve
                altamir "Eu errei e meu erro vai custar nossas vidas. Me desculpem!!."
                hide altamirtriste

                hide cena25
                show final2:
                with pixellate
                s "Suas escolhas, suas ações, te levaram a isso."
                s "GAME OVER...."

                $ renpy.movie_cutscene("final2.webm")

    "Já pegaram a Mislene o caso foi resolvido.":

        v "Pessoal, eu não quero me envolver nisso. Vamos embora, encontrar a policia e deixar eles resolverem."

        show naomi:
            zoom 2.0
            yalign 0.1
        with dissolve
        Naomi "Tem certeza?"
        hide naomi

        v "Não somos policiais nem nada do tipo, somos só estudantes, eu não quero me envolver mais nisso."


        show gabrielbravo:
            zoom 0.6
        with dissolve
        gabriel "Tudo bem, se você quer ser um covarde é problema seu, vai embora logo, não precisamos de você aqui."
        hide gabrielbravo

        hide cena19
        hide cena9
        show cena9:
        with pixellate

        s "Os dois vão em direção a sala do reitor, espero que os dois fiquem bem."

        hide cena9
        show cena11:
        with pixellate

        v "Vou andando em direção a sala de aula e encontro a Delegada algemando a professora Mislene, na porta da sala de aula."

        show mislenealgemada:
            zoom 1.6
        with pixellate
        mislene "Eu não fiz nada, me solte!!!"

        hide mislenealgemada
        v "Delegada? Que bom que encontrei vocês."
        v "Prof-Prfessora???"

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Não fale com ela. Cadê os seus amigos? Cadê o resto do pessoal? Você os abandonou??"
        hide klaraa

        v "Certo... Eles não quiseram vir comigo, não quero mais problemas, só quero paz."

        show klaraa:
            zoom 2.0
            yalign 0.5
        with dissolve
        klaraa "Tudo bem, você fez o certo. Detetive leve essa mulher logo."
        hide klaraa

        show krysllerserio:
            zoom 1.8
        with dissolve
        krysller "Ok, Delegada."
        hide krysllerserio

        stop music
        play music "audio/musicadesuspense.mp3"

        s "O reitor se aproxima lentamente, com passos pesados."
        s "O clima muda, todos ali ficaram com medo. Quando eles menos esperavam.."

        s "O reitor, se é que podemos chamá-lo assim, chega e joga em nossos pés uma coisa que deixou todos horrorizados."

        hide cena11
        show cena24:
        with pixellate

        s "Lá havia a cabeça dos seus amigos e de uma criança que eles não conheciam também.."
        s "Ninguém conseguia acreditar no que estavam vendo dentro daquela caixa."
        s "Como uma pessoa era capaz de fazer aquilo?"
        hide cena24
        show cena11:
        with pixellate

        show reitorcav:
            zoom 1.2
        with pixellate
        r "E vocês serão os próximos."
        hide reitorcav

        s "Ele fala e vem andando lentamente em nossa direção."
        s "As luzes se apagam o clima fica denso e frio."
        s "Era o fim, sim, estavam tão proximos da morte...."

        hide cena11
        show final3:
        with pixellate

        s "Você perdeu, infelizmente com as piores escolhas.."
        s "Escolhas..\nDecisões erradas os levaram para este caminho. e agora? Bom..."
        s "Fim...\n GAME OVER..."

        $ renpy.movie_cutscene("final3.webm")






return
