define S = Character("Sísifo", color="#8a0d08")
define T = Character("Tânatos", color="#603828")
define M = Character("Mérope", color="#ff720d")
define AT = Character("Atlas", color="#18990f")
define PL = Character("Platão", color="#1d3654")
define AR = Character("Filos Aris", color="#fc03d7")
define I = Character("Ícaro", color="#f39200")
define H = Character("Hades", color="#672483")
define PE = Character("Perséfone", color="#ff0808")
define Z = Character("Zeus", color="#ffffff")
define C = Character("Caronte", color="#a3a3a3")
define D = Character("Sofia Dio", color="#5e18ad")
define N = Character("")
# personagens
image Aristoteles = "ch_aristoteles.png"
image Atlas = "ch_atlas.png"
image Caronte = "ch_caronte.png"
image Diogenes = "ch_diogenes.png"
image Hades = "ch_hades.png"
image Icaro = "ch_icaro.png"
image Merope = "ch_merope.png"
image Persefone = "ch_persefone.png"
image Platao = "ch_platao.png"
image Sisifo = "ch_sisifo.png"
image Sisifo Asas = "ch_sisifo_com_colete.png"
image Tanatos = "ch_tanatos.png"
image Zeus = "ch_zeus.png"
#expressoes dos personagens
image Sisifo_sorrindo = "exp_sisifo_sorrindo.png"
image Sisifo_triste = "exp_sisifo_triste.png"
image Sisifo_pensativo = "exp_sisifo_pensativo.png"
image Sisifo_com_medo = "exp_sisifo_medo.png"
image Sisifo_surpreso = "exp_sisifo_surpreso.png"
image Merope_sorrindo = "exp_merope_sorrindo.png"
image Merope_furiosa = "exp_merope_furiosa.png"
image Sisifo Asas_com_medo = "exp_sisifo_asas_com_medo.png"
image Sisifo Asas_pensativo = "exp_sisifo_asas_pensativo.png"
image Atlas_surpresso = "exp_atlas_surpresso.png"
image Atlas_triste = "exp_atlas_triste.png"
image Atlas_furioso = "exp_atlas_furioso.png"
image Atlas_sorrindo = "exp_atlas_sorrindo.png"
image Tanatos_Sorrindo = "exp_tanatos_sorrindo.png"
image Tanatos_Furioso = "exp_tanatos_furioso.png"
image Zeus_Sorrindo = "exp_zeus_sorrindo.png"
image Zeus_furioso = "exp_zeus_furioso.png"
image Diogenes_surpresa = "exp_diogenes_surpresa.png"
image Diogenes_furiosa = "exp_diogenes_furiosa.png"
image Aristoteles_furiosa = "exp_aristoteles_furiosa.png"
image Aristoteles_surpresa = "exp_aristoteles_surpresa.png"
image Aristoteles_com_livro = "exp_aristoteles_com_livro.png"
image Platao_surpreso = "exp_platao_surpreso.png"
image Platao_sorrindo = "exp_platao_sorrindo.png"
image Icaro_surpreso = "exp_icaro_surpreso.png"
# cenários
image Atenas = im.Scale("bg_Atenas.jpg", 1920, 1080)
image Pirene = im.Scale("bg_Pirene.jpg", 1920, 1080)
image Olimpo = im.Scale("bg_olimpo.jpg", 1920, 1080)
image Porto = im.Scale("bg_Porto.jpg", 1920, 1080)
image Floresta Noturna = im.Scale("bg_Floresta_Noturna.jpg", 1920, 1080)
image Escola de Atenas = im.Scale("bg_Escola_Atenas.jpg", 1920, 1080)
image Oraculo = im.Scale("bg_oraculo_de_delfos.jpg", 1920, 1080)
image Creta = im.Scale("bg_Creta.jpg", 1920, 1080)
image Submundo = im.Scale("bg_Submundo.jpg", 1920, 1080)
image Escritorio_Platao = im.Scale("bg_escritorio_platao.jpg", 1920, 1080)
image Estrada = im.Scale("bg_Estrada.jpg", 1920, 1080)
image Creditos_Finais1 = im.Scale("Creditos1.png", 1920, 1080)
image Creditos_Finais2 = im.Scale("Creditos2.png", 1920, 1080)
image Creditos_Finais3 = im.Scale("Creditos3.png", 1920, 1080)
image Creditos_Finais4 = im.Scale("Creditos4.png", 1920, 1080)
# itens
image Obolo1 = im.Scale("item_obolo1.png", 600, 600)
image Obolo2 = im.Scale("item_obolo2.png", 600, 600)
image Colete = im.Scale("item_colete_alado.png", 1640, 349)
image Raio = im.Scale("item_raio_de_zeus.png",252,404)
image Raio2 = im.Scale("item_raio_de_zeus2.png",252,404)
image RaioTela = im.Scale("item_raio_de_zeus.png", 263, 870)
image Fruta_Roma = im.Scale("item_roma.png", 600, 639)
image Pedra = im.Scale("item_pedra_do_lamento.png", 830, 760)
image Corrente = im.Scale("item_corrente_divina.png", 714, 938)
# logo do estudio e logo do jogo
image Logo = im.Scale("icone_logo.png", 650, 650)
image Estudio = im.Scale("icone_estudio.png", 504.3, 700)
image Estudio2 = im.Scale("icone_estudio2.png", 504.3, 700)
image Estudio3 = im.Scale("icone_estudio3.png", 504.3, 700)
image Estudio_Anim:
    "Estudio"
    pause 1.0
    "Estudio2"
    pause 1.0
    "Estudio3"
    

label start:
    python:
        # método de descompressão

        # define a variavel caminho como uma string com o endereço 
        caminho = ("C:\\Users\\joazs\\Downloads\\aaa\\2JDM - TRABALHO DE SÍSIFO\\JOGO\\JOGO\\JOGO COM COMPRESSÃO\\Trabalho_de_Sisifo-win\\Trabalho_de_Sisifo-win\\game\\images")
        # chama o metodo diretorio para o endereço
        diretorio = os.chdir(caminho)
        # cria uma lista com os arquivos do endereço
        lista = os.listdir(caminho)
        # para cada arquivo x na lista de arquivos
        for x in lista:
            # verifica se tem algum arquivo que termina com a extensao zip, caso não tenha = significa que as imagens já estão descompactadas, então nada acontece
            if x.endswith('.zip'):    
                # como já se sabe o nome do arquivo desejado, apenas chama o arquivo e defiine a ação(leitura = "r")
                arquivozip = zipfile.ZipFile("arquivo_compactado.zip", "r")
                # extrair tudo que está dentro do arquivo zip
                arquivozip.extractall()
                # fecha o arquivo zip
                arquivozip.close()
                #  deleta o arquivo zip 
                os.remove("arquivo_compactado.zip")

    scene black with dissolve
    show text "{size=+60}FATEC Carapicuíba{/size}"with zoomin
    $renpy.pause(2, hard="True")
    scene black with dissolve
    pause 1
    show Estudio_Anim at truecenter
    $renpy.pause(3, hard="True")
    hide Estudio_Anim
    show Logo at truecenter with zoomin
    $renpy.pause(2, hard="True")
    hide Logo
    jump Cena1
return

init python:
    escolha1 = 0
    escolha2 = 0
    escolha3 = 0
    escolha4 = 0
    escolha5 = 0
    escolha6 = 0
    escolha7 = 0
    escolha8 = 0
    escolha9 = 0
    semreputacao = 0
    reputacao_aris = 0
    reputacao_plat = 0
    import zipfile
    import os

label Cena1:
    scene Olimpo
    play music "audio/Musica Tanatos.ogg"
    N "Algumas coisas são inevitáveis..."
    N "O calor da primavera despertará a fome assassina dos ursos depois do inverno..."
    N "As mamães pinguins sempre trarão peixe moribundo para a boca sedenta de seus filhotes..."
    N "Os urubus carnicentos perseguirão a putrefata carne do gado atolado nos mananciais..."
    N "Micélio novo se forma sobre as carcaças desovadas no deserto..."
    N "A morte inevitavelmente chega."
    N "Isso não é novo para ninguém, desde tempos imemoriais os avós de nossos avós realizam seus rituais para agradar este hóspede indesejado."
    N "Talvez assim ele nos poupe de sua crueldade, postergue a sua vinda, permitindo que continuemos a adorá-lo por mais um outono..., mas algumas coisas são inevitáveis..."
    N "Inevitável como a mais nova banda de Heavy Metal de ZEUS, o todo poderoso senhor do Olimpo, Deus dos DEUSES!!!"
    show Zeus at left with moveinleft:
        zoom 0.3
    Z "Garoto, você não faz ideia do que está perdendo, isso que é música de verdade!!!"
    show Tanatos_Furioso at right with moveinright:
        zoom 0.3
    T "Pela última vez, tio... eu não quero fazer parte de sua banda! O senhor bem sabe que instrumentos musicais não são bem a minha especialidade, eu prefiro os instrumentos da dor."
    hide Zeus
    show Zeus_Sorrindo at left:
        zoom 0.3
    Z "O problema dessa geração é exatamente esse... Vocês nunca têm disposição para viver, estão sempre melancólicos se arrastando pelos cantos, reclamando da vida!"
    Z "Vamos, garoto, sou eu, o Senhor do Olimpo quem está te convidando! Ninguém diria não a uma proposta como essa."
    T "Eu estou dizendo e pela milésima vez, me deixe em paz! Tenho mais o que fazer... Preciso ceifar algumas almas frescas que acabam de chegar no purgatório."
    Z "Achei que os emos todos já estivessem extintos, não imaginava que um grupo de tristonhos suicidas fossem durar mais de uma década!!! HAAHHAHAH!!!"
    Z "Moleque, você devia passar menos tempo trancado nesse quarto e mais tempo com o seu velho tio Zeus."
    Z "Se me ouvisse mais, conheceria o poder da música de verdade, não tem nada a ver com essas... hã ... como se chamam, lembrei, KPOP! Nada a ver com essas dancinhas de KPOP que vocês jovens tanto veem ultimamente."
    T "Quem você chamou de moleque?? Talvez você esteja ficando senil, pois não se lembra que eu tenho a idade deste planeta?!"
    Z "Como eu disse, um moleque... Não! Um bebezinho... hehehe. Você ainda tem muito o que aprender, garoto."
    T "Vê se me erra, velho gagá."
    N "{b}{size=42}{color=#f6ff00}Tânatos sai da cena, furioso{/b}{/size}{/color}"
    hide Tanatos_Furioso with moveoutright
    hide Zeus_Sorrindo
    show Zeus at left:
        zoom 0.3
    Z "Ele ainda tá na puberdade..."
    Z "Bem, talvez meu velho irmão Hades esteja disponível pra tocar nesse fim de semana..."
    hide Zeus with moveoutleft
    N "Tão inevitável quanto a vinda da morte é a repulsa da mesma pelas antiguidades de seu velho tio."
    N "Até mesmo os Deuses têm problemas familiares... "
    stop music fadeout 1
    jump Cena2
return

label Cena2:
    scene Pirene
    play music "audio/Musica Padrao Sisifo.ogg" 
    N "{b}{size=42}{color=#f6ff00}Enquanto isso na Terra{/b}{/size}{/color}"
    N "Mas essa não é uma história sobre os casos de família do Olimpo."
    N "E sim sobre um rapaz lá do interior da Grécia, seu nome é..."
    show Merope_furiosa at left with moveinright:
        zoom 0.28
    M "SÍSIFO!!!"
    stop music fadeout 1
    show Sisifo_surpreso at right with hpunch:
        zoom 0.3
    play sound "audio/Som_Grito_Sisifo.ogg" 
    S "AH!"
    stop sound fadeout 1
    S "Não me assusta assim, estava concentrado num projeto importante aqui na-"
    N "{b}{size=42}{color=#f6ff00}Sísifo se levanta de sua rede na varanda{/b}{/size}{/color}"
    play music "audio/Musica Padrao Sisifo.ogg"
    M "Eu fiquei a tarde inteira tentando falar contigo, você disse que apareceria!!!"
    M "Não quero saber, você passou dos limites dessa vez, o que você acha que papai vai pensar de você?"
    M "Você deveria ter ido na Feira de Verão no Oráculo... sabe que foi um momento importante pra mim, estávamos contando com a sua presença. Eu cantei Aphrodite’s Child pra uma plateia de duas mil pessoas, e você nem estava lá..."
    M "Aparentemente estava mais preocupado em pastorear ovelhas imaginárias pelo que estou vendo."
    hide Sisifo_surpreso
    show Sisifo_com_medo at right:
        zoom 0.3
    S "C-calma, “Pepezinha”, eu já estava indo, só fiquei de ajudar o velho Heráclito em seu discurso, por isso não pude comparecer a sua festa. Os trens para Jônia sempre se atrasam e..."
    M "Não me venha com “Pepezinha”. Estou cansada de suas palavras doces, Sísifo. Você disse que queria coisa séria, mas ainda é o mesmo moleque imaturo que roubava cavalos-de-troia de chocolate das lojas Greco-romanas... Grrr!"
    M "Acabou, não me procure mais!"
    N "{b}{size=42}{color=#f6ff00}Mérope sai e bate a porta{/b}{/size}{/color}"
    hide Merope_furiosa with moveoutright
    hide Sisifo_com_medo 
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Que vacilo, esqueci totalmente da festa dela... Agora ela não vai querer nem olhar na minha cara."
    S "O que eu faço pra ter ela de volta?"
    hide Sisifo_pensativo 
    stop music fadeout 1
    scene Olimpo 
    play music "audio/Musica Tanatos.ogg"
    show Zeus_Sorrindo at left with moveinleft:
        zoom 0.3
    Z "MUAHUAUHA! Esses mortais são hilários, já vi trilhões de D.R.’s mas nunca perde a graça."
    Z "Aí, garoto, você devia ver o tamanho da merda que esse tal Sísifo fez lá embaixo. A Terra é o meu reality show favorito."
    N "{b}{size=42}{color=#f6ff00}Tânatos (no quarto ao lado) - Aumenta o KPOP{/b}{/size}{/color}"
    hide Zeus_Sorrindo
    show Zeus at left:
        zoom 0.3
    Z "Pensando bem, até que aquela mortal “Pepezinha” canta bem, não é..."
    Z "Tive uma ideia."
    Z "Aí, garoto."
    show Tanatos_Furioso at right with moveinright:
        zoom 0.3
    T "Mas tu é insuportável hein, velho, não é à toa que teus irmãos todos fundaram reinos só pra se afastarem de você."
    T "Diga logo o que quer, mas se for pra entrar na banda já sabe a resposta."
    T "Eu só sei tocar triângulo."
    Z "Zeus me livre! Triangulo em Heavy Metal? Tá maluco?"
    Z "Tenho uma proposta pra você."
    Z "O que me diz de dar um pulinho lá nas terras Helênicas me trazer uma alma?"
    T "Estou ouvindo, prossiga..."
    Z "Isso mesmo, uma alma. É disso que você gosta, não é? Pois bem, assunta só, você vai lá embaixo e surrupia essa humana, ela atende por... “Pepezinha”, acontece que preciso de uma voz pra minha banda e essa mortal é a escolha certa."
    T "E Hades? Desistiu daquele zumbi?"
    hide Zeus 
    show Zeus_Sorrindo at left:
        zoom 0.3
    Z "Não, ele canta tão mal quanto você toca triângulo."
    hide Zeus_Sorrindo
    show Zeus at left:
        zoom 0.3
    Z "Pensei em chamar o velho Poseidon, mas ele só fala com peixe ultimamente."
    Z "Então só me resta ela, o que me diz?"
    hide Tanatos_Furioso
    show Tanatos at right:
        zoom 0.3
    T "Preciso de algo que valha meu tempo, o que receberei em troca?"
    Z "Pois, estava conversando com Ares, posso convocar uma guerra, sempre produz várias almas pra você."
    Z "Sem contar que os mortais adoram se matar por causas fúteis, vai ser moleza. E então?"
    hide Tanatos
    show Tanatos_Sorrindo at right:
        zoom 0.3
    T "Aceito."
    T "Pelo menos assim consigo ficar longe de você por um tempo..."
    hide Zeus with moveoutleft
    hide Tanatos_Sorrindo with moveoutright 
    stop music fadeout 1
    jump Cena3
return

label Cena3:
    scene Floresta Noturna 
    play music "audio/Musica Padrao Sisifo.ogg" 
    N "{b}{size=42}{color=#f6ff00}Mais tarde, no bosque{/b}{/size}{/color}"
    show Sisifo_pensativo at left with moveinleft:
        zoom 0.3
    S "Maldição, eu deveria ter me lembrado..."
    S "E agora, pra onde será que ela foi?"
    hide Sisifo_pensativo
    show Sisifo at left:
        zoom 0.3
    S "Conhecendo a peça, deve ter ido pro bosque praticar a arquearia."
    hide Sisifo
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "Ela adorava vir aqui desde pequena, foi quando Calisto, a caçadora, a viu o seu potencial com o arco... Arriscaria dizer que ela já superou sua tutora. Hehe."
    hide Sisifo_sorrindo
    show Sisifo at left:
        zoom 0.3
    S "Chega de devaneios, preciso me desculpar."
    hide Sisifo
    show Sisifo_pensativo at left:
        zoom 0.3
    S "Hm? Estou ouvindo algo, parece o bater de asas..."
    N "{b}{size=42}{color=#f6ff00}Um vulto corta o céu estrelado{/b}{/size}{/color}"
    S "Deve ser só a minha imaginação."
    hide Sisifo_pensativo with moveoutleft
    N "{b}{size=42}{color=#f6ff00}Algum tempo depois{/b}{/size}{/color}"
    show Sisifo_surpreso at left with moveinleft:
        zoom 0.3 
    S "Oh, estou ouvindo, ela está cantando."
    S "Reconheceria essa voz em qualquer lugar. Mérope!"
    hide Sisifo_surpreso with moveoutleft
    N "{b}{size=42}{color=#f6ff00}Mérope está concentrada na arquearia e na canção{/b}{/size}{/color}"
    show Merope at right with moveinright:
        zoom 0.28
    M "Ele vai ver só, “ajudando o velho Heráclito”, sei... E desde quando ele gosta de filosofia? Não vou cair nesse papinho, ele deve é estar com outra."
    M "E eu fui tola o suficiente para me apaixonar por aquele traste."
    M "Sinto algo se aproximando..."
    N "{b}{size=42}{color=#f6ff00}(Uma voz misteriosa faz uma ameaça){b}{size=42}{color=#f6ff00}"
    T "Pepezinha, seus dias na terra dos homens terminam aqui, Pereçais!"
    M "Sísifo, deixa de graça, não acredito que veio até aqui pra me assustar."
    M "Só você pra me chamar por esse nome ridículo..."
    hide Merope with moveoutright
    show Sisifo_surpreso at left with moveinleft:
        zoom 0.3
    S "O que? Ela está conversando com alguém, não consigo ouvir direito daqui."
    hide Sisifo_surpreso
    show Sisifo_com_medo at left:
        zoom 0.3
    S "Tive a impressão de tê-la ouvido dizer meu nome... Que estranho... Preciso me aproximar. Está tão escuro aqui."
    N "{b}{size=42}{color=#f6ff00}Grandes asas eclipsam a grande lua no céu{/b}{/size}{/color}"
    stop music fadeout 1
    play music "audio/Musica Tanatos.ogg"
    S "O quê?! Aquela coisa está se aproximando dela, preciso fazer algo... Agora!!!"
    menu:
        "Gritar":
            pause 1
            python:
                escolha1 = 1
            jump Escolha_Gritar

        "Proteger":
            pause 1
            python:
                escolha1 = 2
            jump Escolha_Proteger
        S "O que vou fazer agora?"
return

label Escolha_Gritar:
    scene Floresta Noturna
    show Sisifo_surpreso at left:
        zoom 0.3
    S "MEROPE! Abaixe-se!"
    hide Sisifo_surpreso 
    show Merope at right with moveinright:
        zoom 0.28
    M "Sísifo, isso não tem graça. Pare de me seguir."
    N "{b}{size=42}{color=#f6ff00}Mérope se distrai, não percebendo o que vem de cima{/b}{/size}{/color}"
    show Tanatos_Sorrindo at left with moveintop:
        zoom 0.3
    T "A primeira de muitas almas que virão, manifeste suas últimas palavras e despeça-te deste mundo cruel."
    M "Mas que porr..."
    M "Aaaah.."
    jump PosCena3
return

label Escolha_Proteger:
    scene Floresta Noturna
    show Sisifo at left:
        zoom 0.3
    N "{b}{size=42}{color=#f6ff00}Sísifo pula na frente de Mérope{/b}{/size}{/color}"
    S "Cuidado, tem algo se aproximando, eu te protegerei."
    show Merope at right with moveinright:
        zoom 0.28
    M "O que está falando? Isso não é parte de uma pegadinha pra me impressionar?"
    M "Sei me defender sozinha, aliás, sou eu quem está armada aqui."
    N "{b}{size=42}{color=#f6ff00}O vulto aéreo se aproxima e ataca Sísifo{/b}{/size}{/color}"
    scene Floresta Noturna
    show Tanatos at center with moveintop:
        zoom 0.3
    show Merope at right:
        zoom 0.28
    show Sisifo_com_medo at left with hpunch:
        zoom 0.3
    S "Me largue criatura vil, Mérope, socorro!"
    M "Não consigo, ele está em cima de você, se eu disparar posso te ferir."
    N "{b}{size=42}{color=#f6ff00}Sísifo cai no chão{/b}{/size}{/color}"
    scene Floresta Noturna
    show Tanatos_Sorrindo at center with hpunch:
        zoom 0.3
    show Merope at right:
        zoom 0.28
    show Sisifo_com_medo at left:
        zoom 0.3
    T "Não, sua hora ainda não chegou, tenho um contrato com a outra mortal, saia!"
    N "{b}{size=42}{color=#f6ff00}Tânatos ataca a arqueira{/b}{/size}{/color}"
    jump PosCena3
return

label PosCena3:
    scene Floresta Noturna
    N "{b}{size=42}{color=#f6ff00}Tânatos ergue Mérope no ar, derrubando as flechas de sua aljava.{/b}{/size}{/color}"
    show Tanatos at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Merope at right:
        zoom 0.28
    S "Demônio, afaste-se de minha amada, eu Sísifo de Pirene lhe ordeno."
    scene Floresta Noturna
    show Tanatos_Furioso at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Merope at right:
        zoom 0.28
    T "Cala-te, homem, tenho uma missão e mortal algum irá se opor à vontade divina."
    N "{b}{size=42}{color=#f6ff00}Mérope perde a consciência, Tânatos desaparece na noite com o seu corpo. {/b}{/size}{/color}"
    hide Merope with dissolve
    hide Tanatos_Furioso with moveouttop
    hide Sisifo
    show Sisifo_triste at left:
        zoom 0.3
    S "Espere, Mérope!!!"
    S "Pela barba de Tritão, aquilo levou minha amada de mim..."
    S "O que farei agora?"
    S "Talvez... se eu tivesse realizado outra escolha..."
    S "E agora, como vou resgatá-la? Eu não deveria ter magoado ela, pra onde aquilo irá levá-la?"
    S "Ele disse algo sobre “vontade divina”, preciso de ajuda, talvez alguém de Pirene saiba de algo a repeito disso."
    S "Mérope... eu vou te trazer de volta, nem que custe a minha vida!"
    hide Sisifo_triste with moveoutleft
    N "Sísifo vai ao chão em lágrimas, ele não consegue acreditar no que acabou de ver..."
    N "A lua é testemunha da crueldade divina, a vida de uma inocente para satisfazer a vontade de um velho deus egoísta."
    N "O frio e a solidão envolvem Sísifo enquanto ele corre em direção de sua vila natal."
    stop music fadeout 1
    jump Cena4
return

label Cena4:
    play music "audio/Musica Padrao Sisifo.ogg" 
    scene Pirene
    N "Sísifo aproxima-se dos portões da vila, com o olhar perdido, esperando encontrar alguém que pudesse lhe explicar o que acabara de acontecer."
    N "Talvez esse alguém nem exista..."
    N "Alguém se aproxima, caminhando no escuro."
    show Diogenes at right with moveinright:
        zoom 0.3
    D "Mais um vem vindo, não, definitivamente não é este, tem algo errado com ele..."
    show Sisifo_surpreso at left with moveinleft:
        zoom 0.3
    S "Você! Você deve ter visto, uma criatura plumada cortando os céus logo ao sul daqui. Responda!"
    D "Não sei do que está falando, respire fundo e fale com calma."
    hide Sisifo_surpreso
    show Sisifo_triste at left:
        zoom 0.3
    S "Ele a levou de mim, asas negras como a noite..."
    S "Ela estava cantando."
    hide Diogenes
    show Diogenes_surpresa at right:
        zoom 0.3
    D "(Há algo de sombrio neste aqui, mas não parece que está mentindo a respeito disto)"
    hide Diogenes_surpresa
    show Diogenes at right:
        zoom 0.3
    D "O que aconteceu?"
    if escolha1 == 1:
        jump Se_Gritou
    elif escolha1 == 2:
        jump Se_Protegeu
return

label Se_Gritou:
    scene Pirene
    show Sisifo_pensativo at left:
        zoom 0.3
    show Diogenes at right:
        zoom 0.3
    S "Eu estava na floresta, com Mérope, minha amada, quando uma criatura com asas partiu o céu e a atacou."
    S "Eu tentei proteger, lutei contra a fera, mas ela se sobressaiu, levando-a em suas garras rumo ao desconhecido, você que está aí vagando pelas ruas, viu algo?"
    jump PosCena4
return

label Se_Protegeu:
    scene Pirene
    show Sisifo_pensativo at left:
        zoom 0.3
    show Diogenes at right:
        zoom 0.3
    S "Estava indo de encontro com minha amada Mérope no bosque, quando avistei uma figura sombria rondando os céus, gritei para avisá-la... mas não bastou, o demônio a capturou com suas garras e tirou-a de mim! Me ajude, você viu algo sobrevoando a cidade?"
    jump PosCena4
return

label PosCena4:
    scene Pirene
    show Diogenes_surpresa at right:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    D "Tragédia! Sinto muitíssimo pela sua perda, entretanto nada vi que fugisse do corriqueiro, por acaso essa Mérope que mencionou é a filha de Atlas?"
    D "(A filha de um deus raptada...isso definitivamente não cheira bem)"
    S "Precisamente, preciso trazê-la de volta."
    hide Diogenes_surpresa
    show Diogenes at right:
        zoom 0.3
    D "Sim, sim, já entendi, mas preciso de mais informações para te ajudar, por acaso há alguma característica desta figura que ainda não mencionou?"
    hide Sisifo
    show Sisifo_pensativo at left:
        zoom 0.3
    S "Ela disse algo sobre “vontade divina”, não sei o que isso significa..."
    hide Diogenes
    show Diogenes_surpresa at right:
        zoom 0.3
    D "Maldição!"
    D "(É tão ruim quanto imaginei)"
    hide Sisifo_pensativo
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "O quê? você sabe do que se trata?"
    hide Diogenes_surpresa
    show Diogenes at right:
        zoom 0.3
    D "Sei onde pode buscar ajuda..., mas é distante daqui você corre o risco de não a ver mais se não fizer o que digo. Encontrará sua resposta na Escola de Atenas."
    D "Aquilo que a tirou de você se trata de um monstro assertivo, raramente alguém retorna de seu chamado."
    D "Os universitários o conhecem bem, poderão te ajudar."
    hide Sisifo_sorrindo
    show Sisifo_surpreso at left:
        zoom 0.3
    S "Por acaso você já estudou lá? Suas vestes, sim, isso é um uniforme!"
    D "Sim, já fui aluna, entretanto não sou mais bem vinda, tenho minhas... diferenças com as pessoas de lá."
    hide Sisifo_surpreso
    show Sisifo_pensativo at left:
        zoom 0.3
    S "(Ela não está me revelando tudo, preciso que mostre o caminho até essa “Escola de Atenas”)"
    hide Sisifo_pensativo
    show Sisifo at left:
        zoom 0.3
    S "Me acompanhe, mostre o caminho até a escola e ficarei em dívida com você."
    D "Hmm, está bem. Se prepare, andaremos bastante."
    hide Sisifo with moveoutleft
    hide Diogenes with moveoutright
    jump Cena4_5
return

label Cena4_5:
    scene Estrada
    N "A dupla começa sua jornada, passando pelos portais que sinalizam o perímetro de Pirene, logo estão numa estrada."
    show Sisifo_pensativo at left with moveinleft:
        zoom 0.3
    show Diogenes at right with moveinright:
        zoom 0.3
    S "Você parecia pensativa na vila."
    S "Está procurando por alguém?"
    D "Sim, mas não se preocupe, certamente não é você."
    hide Sisifo_pensativo
    show Sisifo_surpreso at left:
        zoom 0.3
    S "Ei!"
    S "Não seja rude."
    S "Mas o que exatamente está procurando?"
    hide Sisifo_surpreso
    show Sisifo at left:
        zoom 0.3
    N "Sofia Dio, que se movia na frente, guiando o desconsolado para subitamente."
    D "Seus olhos."
    D "Tem algo neles."
    N "Depois de uma inspeção minuciosa, a garota volta a caminhar pela estrada."
    D "Eu procuro um homem honesto."
    D "Não sei se o que me diz é verdade, mas sei que suas intenções são maiores do que aparentam."
    N "A fala direta da garota deixa Sísifo mudo."
    N "Sísifo se sente derrotado por um momento, ele não sabe o que a garota quer dizer, mas por um instante ele se sente vulnerável."
    N "Talvez ele não confie em si mesmo."
    N "Ele abaixa a cabeça e a segue em silêncio."
    hide Sisifo with moveoutleft
    hide Diogenes with moveoutright
    jump Cena5
return

label Cena5:
    scene Atenas
    N "No dia seguinte Sofia e Sísifo ambos chegam à cidade de Atenas, a incólume capital da filosofia ocidental."
    show Diogenes_furiosa at left with moveinright:
        zoom 0.3
    show Sisifo_sorrindo at right with moveinleft:
        zoom 0.3
    D "Aqui estamos, Atenas. Não mudou uma vírgula desde que parti. As mesmas ruas, as mesmas estátuas, as mesmas hipocrisias."
    S "Ela está aqui? Diga me onde, para qual destes edifícios o monstro a levou?"
    hide Diogenes_furiosa
    hide Sisifo_sorrindo 
    show Diogenes at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    D "Vá com calma, eu não disse que ela estaria aqui."
    D "Mas quem pode te ajudar a encontrá-la está."
    S "E quem seria esta pessoa?"
    D "Minha irmã."
    hide Sisifo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Hm, você disse que não seria bem-vinda aqui, mas como se aqui é a casa de sua família?"
    D "É mais complicado do que isto, nós não concordamos com algumas coisas, foi quando me mudei para Pirene, ter uma vida mais simples, longe de tudo isto."
    D "Mas isso não vem ao caso agora, venha, encontraremos-na na praça."
    hide Diogenes with moveoutright
    hide Sisifo_pensativo with moveoutright
    N "{b}{size=42}{color=#f6ff00}Algum tempo depois{/b}{/size}{/color}"
    N "Sísifo se aproxima de uma palestra, a multidão ouve com atenção cada palavra proferida por uma jovem em cima do palanque."
    stop music fadeout 1
    play music "audio/Som_Plateia.ogg" 
    show Aristoteles_com_livro at center:
        zoom 0.3
    AR "...O mundo está aqui, o conhecimento é gerado no próprio mundo sensível que habitamos e vivemos dia após dia."
    AR "É assim que sempre foi desde o princípio, não há um segundo mundo de onde os deuses partem e chegam, bem como não há um segundo mundo de onde as ideias primeiras nascem e migram."
    AR "As coisas falam por si só."
    N "{b}{size=42}{color=#f6ff00}Sísifo se aproxima do palanque, ficando na primeira fila{/b}{/size}{/color}"
    hide Aristoteles_com_livro
    show Aristoteles at center:
        zoom 0.3
    show Sisifo at left with moveinleft:
        zoom 0.3
    AR "Você é o que você escolhe ser."
    N "{b}{size=42}{color=#f6ff00}A garota olha para os olhos de Sísifo e encerra seu discurso{/b}{/size}{/color}"
    stop music fadeout 1
    play music "audio/Som_Plateia_Aplaudindo.ogg" 
    N "{b}{size=42}{color=#f6ff00}A multidão aplaude com fervor{/b}{/size}{/color}"
    stop music fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg" 
    menu:
        "Sou um vingador":
            pause 1
            python:
                reputacao_aris += 1
                escolha2 = 1
            jump Escolha_Vingador
        "Sou um herói":
            pause 1
            python:
                reputacao_plat += 1
                escolha2 = 2
            jump Escolha_Heroi
        "Sou um camponês":
            pause 1
            python:
                semreputacao += 1
                escolha2 = 1
            jump Escolha_Campones
        AR "E então, quem é você?"
return

label Escolha_Vingador:
    scene Atenas
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right with dissolve:
        zoom 0.3
    S "Me chamo Sísifo, aqui estou para vencer o monstro que tirou minha amada de mim, busco vingança."
    N "{b}{size=42}{color=#f6ff00}Aris sorri{/b}{/size}{/color}"
    AR "Pois está disposto a derrubar uma criatura enviada das estrelas! Gosto de sua determinação, gostaria de te apresentar a alguém."
    hide Sisifo 
    hide Aristoteles 
    jump PosCena5
return

label Escolha_Heroi:
    scene Atenas
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right with dissolve:
        zoom 0.3
    S "Sou Sísifo, Herói de Pirene, estou respondendo ao desafio proposto pelos deuses, trarei a alma de minha amada de volta."
    N "{b}{size=42}{color=#f6ff00}Aris mantém-se séria{/b}{/size}{/color}"
    hide Aristoteles
    show Aristoteles_furiosa at right:
        zoom 0.3
    AR "O desafio que atende não foi proposto pelos deuses, é a sua causa que está enfrentando aqui."
    hide Sisifo
    hide Aristoteles_furiosa 
    jump PosCena5
return

label Escolha_Campones:
    scene Atenas
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right with dissolve:
        zoom 0.3
    S "Sou um camponês procurando alguém que me auxilie em minha busca. Me chame de Sísifo."
    hide Aristoteles
    show Aristoteles_surpresa at right:
        zoom 0.3
    AR "Uma folha em branco."
    AR "Todos nós estamos em busca de algo, talvez os meus métodos possam te levar a algum lugar."
    hide Sisifo 
    hide Aristoteles_surpresa
    jump PosCena5
return

label PosCena5:
    scene Atenas
    show Diogenes_furiosa at left with moveinright:
        zoom 0.3
    show Aristoteles_furiosa at right with moveinleft:
        zoom 0.3
    AR "Você, o que faz aqui? Pensei que houvesse renegado a civilização."
    D "Parece que vocês hipócritas ainda precisam de meu auxílio, estou guiando Sísifo."
    AR "E o trouxe até mim, já concluiu sua tarefa. Volte a rolar na lama com seus cães, cínica."
    show Sisifo_pensativo at center:
        zoom 0.3
    S "“Cínica”, o que isso quer dizer?"
    hide Aristoteles_furiosa
    show Aristoteles at right:
        zoom 0.3
    AR "É alguém desprovido de pudor, que vive na rua com os cães, aparentemente essa é a vida honesta que todo humano deveria seguir... Sem excessos, apenas as necessidades básicas do corpo, não é mesmo irmãzinha?"
    hide Sisifo_pensativo
    show Sisifo at center:
        zoom 0.3
    N "{b}{size=42}{color=#f6ff00}Sofia Dio - Revira os olhos{/b}{/size}{/color}"
    D "Bom, meu dever está cumprido, estarei na praça caso precise de mim para outra coisa que não seja me debochar, Sísifo."
    N "{b}{size=42}{color=#f6ff00}Sofia se aproxima das estatuas na praça e começa a apreciá-las{/b}{/size}{/color}"
    hide Diogenes_furiosa with moveoutright
    AR "Me siga, o lugar que precisa visitar é o grande colégio."
    hide Aristoteles with moveoutleft
    hide Sisifo with moveoutleft
    N "Sísifo e Filos atravessam a multidão na praça em direção à Escola de Atenas."
    jump Cena6
return

label Cena6:
    scene Escola de Atenas
    N "Sísifo acompanha a universitária, ambos passam pelos arcos frontais da universidade, observando as estatuetas e bustos de pensadores do passado que foram ali eternizados."
    show Sisifo_pensativo at left with moveinleft:
        zoom 0.3
    show Aristoteles at right with moveinright:
        zoom 0.3
    S "(Qual será o meu legado, será que lembrarão de mim como estas pessoas?)"
    N "A prospecção do futuro paira sobre as ideias do viajante, desconectando-o do ambiente por um breve momento."
    AR "Ei, Sísifo."
    AR "Está perdido no mundo das ideias? Este lugar tem esse efeito sobre as pessoas..."
    AR "Principalmente sobre aqueles que passam muito tempo aqui."
    AR "Agora venha."
    N "Ambos atravessam um grande hall com alas que levam até as salas, alguns estudantes vêm e vão, conversando entusiasmados pelo campus."
    N "Filos Aris guia o viajante até a sala de um professor."
    N "Entrando no que parece um escritório, com prateleiras totalmente populadas com livros dos mais diversos, há um senhor alto, com uma barba vistosa, sentado atrás da mesa enquanto escreve algo em seu computador."
    hide Sisifo_pensativo with moveoutleft
    hide Aristoteles with moveoutright
    scene Escritorio_Platao
    show Platao at center with moveinleft:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right with moveinright:
        zoom 0.3
    PL "As revisões das provas de Metafísica ocorrerão na próxima segunda-feira..."
    AR "Com licença, professor."
    hide Platao
    show Platao_surpreso at center:
        zoom 0.3
    PL "Oh, senhorita Aris, pois não?"
    AR "Olá, professor. Acredito ter encontrado alguém na “situação da caverna”. Heis o indivíduo."
    N "Os olhos de Sísifo percorrem toda a área da sala, tentando absorver tudo oi que está acontecendo ali na sua frente."
    N "O rapaz claramente desconcertado constrói um semblante sério para dizer algo a altura da conversa:"
    hide Platao_surpreso
    hide Sisifo
    show Sisifo_surpreso at left:
        zoom 0.3
    show Platao at center:
        zoom 0.3
    S "Quê?"
    PL "Sim... eu vejo, ele parece ser o que eu estava procurando para testar minha tese..., mas afinal, qual a situação deste garoto? "
    PL "Conte-me o porquê de acreditar que ele é alguém na situação da caverna."
    if escolha2 == 1:
        jump Se_Vingador_Ou_Campones
    elif escolha2 == 2:
        jump Se_Heroi
return

label Se_Vingador_Ou_Campones:
    scene Escritorio_Platao
    show Platao_surpreso at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right:
        zoom 0.3
    AR "Ele é alguém em busca de algo no campo divino, foi o que disse quando nos conhecemos"
    PL "É verdade o que a senhorita Aris está dizendo, garoto?"
    S "Sim, estou aqui porque..."
    jump PosCena6
return

label Se_Heroi:
    scene Escritorio_Platao
    show Platao_sorrindo at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Aristoteles_furiosa at right:
        zoom 0.3
    AR "Ele se diz um herói, confrontando diretamente o desafio divino."
    PL "Interessante... Diga-me sua história meu jovem."
    S "Pois bem, tudo começou quando..."
    jump PosCena6
return

label PosCena6:
    scene Escritorio_Platao
    show Platao_surpreso at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right:
        zoom 0.3
    N "Sísifo conta o motivo de ter buscado ajuda."
    PL "Pelos Céus!"
    PL "Sua amada foi atacada pela morte em pessoa... Isso... Achei que não acontecesse mais..."
    AR "Foi o que pensei, o que tiraria um deus de seu posto no Olimpo para atacar uma camponesa?"
    hide Platao_surpreso
    show Platao at center:
        zoom 0.3
    PL "Você e sua irmã fizeram bem em trazê-lo aqui."
    PL "Garoto eu consigo te ajudar a encontrar Mérope uma vez mais."
    hide Sisifo
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "Você o faria por mim?"
    S "Serei eternamente grato por isso, senhor Platão."
    PL "Sim, posso te ajudar, você já sabe o que estamos enfrentando: A morte se opôs a você."
    PL "Mas ela não é tão final quanto muitos acreditam."
    PL "Estou realizando uma pesquisa... e por acaso a situação que está vivendo agora se enquadra no que eu gostaria de acompanhar de perto."
    PL "Ajudarei a encontrar sua querida, e realizarei minha pesquisa de campo no processo."
    AR "Isso eu quero ver de perto... O senhor sempre esteve tão preso nas teorias, vai ser especial apreciá-lo vivendo a pesquisa na pele."
    hide Sisifo_sorrindo
    show Sisifo at left:
        zoom 0.3
    S "Toda ajuda é bem-vinda."
    S "Obrigado."
    PL "A senhorita Sofia poderia nos acompanhar, ela ficou na praça principal você disse?"
    AR "Isso mesmo, ela não quis retornar à escola."
    hide Platao
    show Platao_sorrindo at center:
        zoom 0.3
    PL "Vamos encontrá-la, talvez queira nos acompanhar na nossa jornada."
    hide Aristoteles with dissolve
    hide Sisifo with dissolve
    hide Platao_sorrindo with dissolve
    jump Cena7
return

label Cena7:
    scene Atenas
    N "Aproximando da praça principal, o grupo avista Sofia Dio conversando com uma estatueta."
    show Diogenes at left with moveinleft:
        zoom 0.3
    D "Peço-lhe apenas uma moeda, o suficiente para que eu retorne para minha cidade."
    show Sisifo at right with moveinright:
        zoom 0.3
    S "Com licença."
    D "Agora não, estou ocupada."
    hide Sisifo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Não vê que é inerte, uma estátua! Está pedindo dinheiro para uma estátua!"
    D "O resultado é o mesmo não importa se estiver pedindo para uma pessoa ou para um bloco de gesso."
    show Aristoteles_furiosa at center:
        zoom 0.3
    AR "Seja menos dramática, já me arrependo de ter vindo aqui chamá-la."
    D "Não se desgaste, seja lá pra onde vão, eu fico."
    hide Sisifo_pensativo 
    show Platao at right:
        zoom 0.3
    PL "Aqui está...talvez minha pupila mais brilhante, seria um descaso com a dialética permitir-me deixá-la à mercê dos pombos e mendigos da cidade."
    PL "Venha conosco, criança."
    AR "Que consideração..."
    D "Observá-los discutir sobre o que faz uma pessoa ser boa, ao invés de sê-la?"
    D "Eu passo."
    PL "Não posso escrever o seu destino por você, se assim deseja, então assim será."
    hide Diogenes 
    show Sisifo_pensativo at left:
        zoom 0.3
    S "Discutir ao invés de ser... o que ela quer dizer com isso?"
    S "Ela não acredita no que diz, não é?"
    AR "Talvez não acredite, mas faz questão de fazer com que os ignorantes como você o façam."
    AR "Faz parte de seu show de falsa humildade."
    stop music fadeout 1
    play music "audio/Som_Ambiente_Porto.ogg"
    scene Porto 
    N "Aproximando do litoral ateniense, Platão guia o grupo até uma doca distante, isolada da aglomeração do mercado de peixes, longe dos grupos de marinheiros que circulam pelo local."
    show Sisifo at left with moveinleft:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right with moveinright:
        zoom 0.3
    PL "Precisamos esperar."
    S "E posso saber o que estamos esperando?"
    S "Precisamos agir agora."
    stop music fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg" 
    AR "A morte pode esperar, isso é necessário para fazer a travessia."
    hide Sisifo
    show Sisifo_com_medo at left:
        zoom 0.3
    S "Está me dizendo que precisamos atravessar o oceano?"
    PL "Para chegar ao outro lado da vida, antes precisa chegar ao outro lado do mar."
    jump Escolha_Cena7
return

label Escolha_Cena7:
    scene Porto
    show Sisifo_com_medo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    menu:
        "Claro que não":
            pause 1
            python:
                escolha3 = 1
            jump Escolha_Claro_Que_Nao

        "Talvez":
            pause 1
            python:
                escolha3 = 2
            jump Escolha_Talvez
        AR "Não está com medo de um pouco de água, não é?"
return

label Escolha_Claro_Que_Nao:
    scene Porto
    show Sisifo_com_medo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    S "O que... o que te faz p-pensar isso? B-bem o barco é como uma carroça, só que solta acima de dezenas de metros de escuridão desconhecida preenchida por algo que não oferece resistência alguma ao meu peso, eu só qu-..."
    if escolha2 == 1:
        jump Se_Vingador_Ou_Campones2
    elif escolha2 == 2:
        jump Se_Heroi2
return

label Escolha_Talvez:
    scene Porto
    show Sisifo_pensativo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    S "Hãn... Na verdade eu..."
    S "(O que estou dizendo?)"
    S "(Eu não vou dizer que morro de medo de água pra essa guria marrenta, ela jamais largaria do meu pé.)"
    S "(Além disso, onde estaria minha honra? Não... eu não vou dizer isso)"
    jump Escolha_Cena7
return

label Se_Heroi2:
    scene Porto
    show Sisifo_com_medo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    AR "Patético... achei que foste o herói de seu povo, tentando resgatar a princesa imaculada tirada de seus braços pelo monstro cruel!"
    AR "Veja só isto, professor... um marmanjo deste tamanho com medo de molhar os pés..."
    jump PosCena7
return

label Se_Vingador_Ou_Campones2:
    scene Porto
    show Sisifo_com_medo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    AR "Um rapaz do campo que jamais vira o mar antes... Até que é razoável."
    AR "Mas lembre-se de que enfrentaremos coisas muito mais traiçoeiras do que o mar, imaginei que a esta altura já tivesse consciência disto."
    jump PosCena7
return

label PosCena7:
    scene Porto
    show Sisifo_com_medo at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Platao_sorrindo at right:
        zoom 0.3
    PL "Hahaha!"
    PL "Pegue leve com o garoto, Aris!"
    PL "Veja nossa carona está prestes a chegar, já era hora."
    N "Adiante, no horizonte, uma sombra surge no mar e começa a se aproximar da superfície, como se um espessa tinta tivesse sido derramada no Mar Mediterrâneo."
    stop music fadeout 1
    jump Cena8
return

label Cena8:
    scene Porto
    play music "audio/Musica Tema Caronte.ogg" 
    N "Da sombra, ergueram-se primeiro os braços, depois o tronco obscuro, seguido do barco."
    N "Da névoa a criatura empunhou um remo, seu rosto era coberto por um capuz preto."
    show Sisifo_surpreso at left:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    S "Criatura das trevas, onde ela está?"
    S "Onde está Mérope?"
    PL "Controla-te homem, é por ela que estamos esperando!"
    show Caronte at center with moveinbottom:
        zoom 0.3
    C "Alto, Sou Caronte, a barqueira do pós vida."
    C "Percebo que você e seu grupo estão há algumas horas esperando por algo, e este algo poderia ser eu."
    C "Estou certa?"
    hide Sisifo_surpreso
    show Sisifo_com_medo at left:
        zoom 0.3 
    S "Isso é o que nos ajudará? Não consigo ver como."
    S "Isso é um monstro, precisamos abatê-lo."
    PL "Esse “monstro” é o nosso passaporte para a próxima etapa de nossa jornada, trate-o bem."
    C "Pois bem, posso levá-los a eterna danação agora mesmo."
    C "Embora..."
    C "Vocês pareçam um pouco vivos demais para isso. Tem certeza de que realizarão a travessia?"
    hide Platao
    show Aristoteles at right:
        zoom 0.3
    AR "Ei, calma aí. Não estamos mortos como pode ver, precisamos chegar ao outro lado do mar, não da vida."
    C "É uma pena..."
    hide Aristoteles
    show Platao at right:
        zoom 0.3
    hide Sisifo_com_medo
    show Sisifo_pensativo at left:
        zoom 0.3 
    S "Essa criatura é a morte?"
    PL "Não, não é quem levou Mérope."
    C "Posso levá-los ao outro lado... por um preço..."
    PL "Não temos dinheiro"
    hide Sisifo_pensativo
    show Sisifo_surpreso at left:
        zoom 0.3 
    S "O senhor trabalha naquele escola chique, não me venha com essa de “não tenho dinheiro”."
    hide Platao
    show Platao_sorrindo at right:
        zoom 0.3
    PL "Garoto eu sou filósofo e professor, uma coisa que eu definitivamente não tenho é dinheiro."
    C "A travessia ainda pode ser realizada..."
    C "Porém levará 100 anos para ser concluída."
    hide Platao_sorrindo
    show Aristoteles at right:
        zoom 0.3
    AR "Eu não tenho 100 anos sobrando para você!"
    hide Sisifo_surpreso
    show Sisifo_sorrindo at left:
        zoom 0.3 
    S "Alguns de nós não tem nem dez anos sobrando..."
    C "Então nada feito, o contrato não foi realizado."
    C "Retornem quando tiverem dinheiro, ou tempo para mim."
    hide Sisifo_sorrindo
    show Sisifo_surpreso at left:
        zoom 0.3 
    S "Espere!"
    N "A figura afunda no mar e desaparece."
    hide Caronte with moveoutbottom
    stop music fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg"
    show Platao at center:
        zoom 0.3
    AR "Belo plano velhote e agora?"
    hide Sisifo_surpreso
    show Sisifo_pensativo at left:
        zoom 0.3 
    S "Hmm.. Acho que tive uma ideia, venha, vamos voltar."
    S "Talvez alguém possa nos fazer um empréstimo."
    hide Sisifo_pensativo with dissolve
    hide Platao with dissolve
    hide Aristoteles with dissolve
    jump Cena9
return

label Cena9:
    scene Atenas
    N "O grupo retorna a metrópole ateniense."
    show Platao at left with moveinleft:
        zoom 0.3
    show Sisifo at center:
        zoom 0.3
    show Aristoteles at right with moveinright:
        zoom 0.3
    PL "O que tem em mente, Sísifo?"
    hide Platao
    show Platao_surpreso at left:
        zoom 0.3
    PL "Não vá me dizer que planeja roubar a casa da moeda ateniense!"
    hide Sisifo
    show Sisifo_sorrindo at center:
        zoom 0.3
    S "Não é pra tanto."
    S "Lembra se do que Sofia estava fazendo? Talvez ela tenha conseguido algum dinheiro."
    S "Talvez ela possa nos emprestar."
    hide Aristoteles
    show Aristoteles_furiosa at right:
        zoom 0.3
    AR "Sério? Você está trabalhando com a possibilidade de pedir dinheiro para uma pedinte que pode ou não o ter? Isso se ela te emprestar..."
    AR "É isso professor, avise o IML, Mérope está morta."
    hide Sisifo_sorrindo
    show Sisifo at center:
        zoom 0.3
    S "A chama da esperança ainda vive em mim, precisamos tentar."
    scene Atenas
    N "Chegando na praça, Sofia Dio está no palanque discursando com fervor:"
    show Diogenes at center:
        zoom 0.3
    D "Quando os homens capturam um porco ou um carneiro, não hesitam em alimentá-lo com fartura, até que fiquem saudáveis e fortes."
    D "Porém quando capturam um ser humano, o mais nobre dos animais, não lhe é dado nem uma migalha de pão, até que ele seja reduzido a um esqueleto e desapareça!"
    N "A multidão da praça mantém-se reflexiva pensando no que a garota está dizendo."
    N "Pouco tempo depois atiram-lhe algumas moedas e pães e frutas."
    hide Diogenes with dissolve
    show Platao at left:
        zoom 0.3
    show Sisifo_sorrindo at center:
        zoom 0.3
    show Aristoteles at right:
        zoom 0.3
    S "Viu só, ela é boa, vamos lá."
    N "Sísifo e seus companheiros aproximam-se da garota que se encontra lavando um cacho de uvas que lhe foi arremessado."
    hide Sisifo_sorrindo
    show Diogenes_furiosa at center:
        zoom 0.3
    PL "Se você tivesse cortejado Dionísio, não estaria lavando uvas."
    D "Se você estivesse lavando uvas, não estaria cortejando um tirano."
    hide Aristoteles
    show Aristoteles_furiosa at right:
        zoom 0.3
    AR "Não acha que está exagerando, irmã?"
    hide Diogenes_furiosa
    show Diogenes at center:
        zoom 0.3
    D "Eu sou como um professor de música, preciso cantar mais alto do que o coro para que eles possam ouvir a nota certa."
    hide Platao
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "Pois eu tenho um soneto para você."
    S "O que me diz de partilhar com um velho camarada algumas das moedas que recebeu?"
    scene Atenas
    jump minigame_Palavras
return

label minigame_Palavras:

    init python:
        lista = ["Cinismo", "Cão", "Humildade", "Honestidade", "Pureza", "Pobreza", "Igualdade"]
        listaDio2 = ["Rebeldia", "Cosmopolita", "Verdade", "Efêmero", "Presente", "Agora", "Indiferença"]
        listaDio3 = ["Anarquia", "Lanterna", "Barril", "Nômade", "Andarilho", "Simplicidade", "Autorrealização", ]
        listaDio4 = ["Estatua", "Pedir", "Agir", "Bondade", "Ser", "Impudor", "Espontaneidade", "Esmola", "Mendigo"]
        lista2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        listaPlat1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        listaPlat2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadas = 0
        botcli = True
        pode = 0
        num3 = 0
        num1 = 0
        num2 = 0
        pontAris = 0
        pontPlat = 0
        pontDio = 0
        palavra1 = ""
        palavra2 = ""
        palavra3 = ""
        palavra4 = ""
        palavra5s = ""
        palavra6 = ""
        palavra7 = ""
        palavra8 = ""
        palavra9 = ""
        palavra10 = ""
        quem = ""
        inicio = "Escolha uma palavra para compor seu soneto"
        a = []
        b = []
        c = []
        d = []
        es = []
        f = []
        g = []
        h = []
        i = []
        j = []
        score = 0

        lista_nova = []
        a = renpy.random.sample(lista, 5)
        palavra1 = a[num1]
        b = renpy.random.sample(listaDio2, 5)
        palavra2 = b[num1]
        c = renpy.random.sample(listaDio3, 5)
        palavra3 = c[num1]
        d = renpy.random.sample(listaDio4, 5)
        palavra4 = d[num1]
        es = renpy.random.sample(lista2, 5)
        palavra5s = es[num1]
        f = renpy.random.sample(listaAris, 5)
        palavra6 = f[num1]
        g = renpy.random.sample(listaAris3, 5)
        palavra7 = g[num1]
        h = renpy.random.sample(lista3, 5)
        palavra8 = h[num1]
        i = renpy.random.sample(listaPlat1, 5)
        palavra9 = i[num1]
        j = renpy.random.sample(listaPlat2, 5)
        palavra10 = j[num1]
        score = num1 + 1

    N "Agora você irá compor um soneto"

    call screen textmiddle
return

screen textmiddle:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable(
                    "palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra1]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra5s]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra8]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra9]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra2]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra6]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra10]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra3]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra7]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("textmiddle"), ToggleScreen("tela2")]
            elif score == 5:
                textbutton "[palavra4]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("textmiddle"), Function(renpy.call, label="pontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[score]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[inicio]{/color}"
return

screen tela2:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra8]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable(
                    "palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra1]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra2]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra7]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra10]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra3]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra4]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra6]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra9]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela2"), ToggleScreen("tela3")]
            elif score == 5:
                textbutton "[palavra5s]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela2"), Function(renpy.call, label="pontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[score]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[inicio]{/color}"
return

screen tela3:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra9]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra6]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable(
                    "palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra1]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra4]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra7]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra10]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra8]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra2]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra5s]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela3"), ToggleScreen("tela4")]
            elif score == 5:
                textbutton "[palavra3]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela3"), Function(renpy.call, label="pontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[score]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[inicio]{/color}"
return

screen tela4:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra6]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra2]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra10]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra5s]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra9]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable(
                    "palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra1]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra3]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra7]" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra8]" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1), ToggleScreen("tela4"), ToggleScreen("tela5")]
            elif score == 5:
                textbutton "[palavra4]" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela4"), Function(renpy.call, label="pontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[score]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[inicio]{/color}"
return

screen tela5:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra2]{/color}{/font}{/size}" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra10]{/color}{/font}{/size}" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra6]{/color}{/font}{/size}" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra4]{/color}{/font}{/size}" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra3]{/color}{/font}{/size}" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra7]{/color}{/font}{/size}" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra9]{/color}{/font}{/size}" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("quem", "Sofia Dio gostou"), SetVariable("pontDio", pontDio + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable(
                    "palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra1]{/color}{/font}{/size}" action[SetVariable("pontDio", pontDio + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("quem", "Filo Aris gostou"), SetVariable("pontAris", pontAris + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra5s]{/color}{/font}{/size}" action[SetVariable("pontAris", pontAris + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if score < 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("quem", "Platão gostou"), SetVariable("pontPlat", pontPlat + 1), SetVariable("num1", num1 + 1), SetVariable("palavra1", a[num1+1]), SetVariable("palavra2", b[num1+1]), SetVariable("palavra3", c[num1+1]), SetVariable("palavra4", d[num1+1]), SetVariable("palavra5s", es[num1+1]), SetVariable("palavra6", f[num1+1]), SetVariable("palavra7", g[num1+1]), SetVariable("palavra8", h[num1+1]), SetVariable("palavra9", i[num1+1]), SetVariable("palavra10", j[num1+1]), SetVariable("score", score + 1)]
            elif score == 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavra8]{/color}{/font}{/size}" action[SetVariable("pontPlat", pontPlat + 1), ToggleScreen("tela5"), Function(renpy.call, label="pontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[score]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[inicio]{/color}"
return

label perdeu:

    python:

        lista = ["Cinismo", "Cão", "Humildade", "Honestidade", "Pureza", "Pobreza", "Igualdade"]
        listaDio2 = ["Rebeldia", "Cosmopolita", "Verdade", "Efêmero", "Presente", "Agora", "Indiferença"]
        listaDio3 = ["Anarquia", "Lanterna", "Barril", "Nômade", "Andarilho", "Simplicidade", "Autorrealização", ]
        listaDio4 = ["Estatua", "Pedir", "Agir", "Bondade", "Ser", "Impudor", "Espontaneidade", "Esmola", "Mendigo"]
        lista2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        listaPlat1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        listaPlat2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadas = 0
        botcli = True
        pode = 0
        num3 = 0
        num1 = 0
        num2 = 0
        pontAris = 0
        pontPlat = 0
        pontDio = 0
        palavra1 = ""
        palavra2 = ""
        palavra3 = ""
        palavra4 = ""
        palavra5s = ""
        palavra6 = ""
        palavra7 = ""
        palavra8 = ""
        palavra9 = ""
        palavra10 = ""
        quem = ""
        inicio = "Escolha uma palavra para compor seu soneto"
        a = []
        b = []
        c = []
        d = []
        es = []
        f = []
        g = []
        h = []
        i = []
        j = []
        score = 0

        lista_nova = []
        a = renpy.random.sample(lista, 5)
        palavra1 = a[num1]
        b = renpy.random.sample(listaDio2, 5)
        palavra2 = b[num1]
        c = renpy.random.sample(listaDio3, 5)
        palavra3 = c[num1]
        d = renpy.random.sample(listaDio4, 5)
        palavra4 = d[num1]
        es = renpy.random.sample(lista2, 5)
        palavra5s = es[num1]
        f = renpy.random.sample(listaAris, 5)
        palavra6 = f[num1]
        g = renpy.random.sample(listaAris3, 5)
        palavra7 = g[num1]
        h = renpy.random.sample(lista3, 5)
        palavra8 = h[num1]
        i = renpy.random.sample(listaPlat1, 5)
        palavra9 = i[num1]
        j = renpy.random.sample(listaPlat2, 5)
        palavra10 = j[num1]
        score = num1 + 1
    show Diogenes at center:
        zoom 0.3
    show Platao at left:
        zoom 0.3
    show Sisifo_pensativo at right:
        zoom 0.3
    D "Não me convenceu..."
    PL "Essa era sua ideia, garoto?"
    PL "Escolha melhor suas palavras quisera ver Mérope de novo."
    S "Calma, eu ainda não terminei."
    scene Atenas
    call screen textmiddle
return

label pontos:
    N "E sua pontuação é:"
    call screen pontuacao
return

screen pontuacao:
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "Você fez [pontAris] pontos com a Filo Aris"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.2
        text "Você fez [pontDio] pontos com a Sofia Dio"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.3
        text "Você fez [pontPlat] pontos com o Platão"
    frame:
        background "#e0dada"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        if pontDio < pontAris or pontDio < pontPlat:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pontuacao"), Function(renpy.call, label="perdeu")]
        else:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pontuacao"), Function(renpy.call, label="ganhou")]
return

label ganhou:
    python:
        if pontAris > pontPlat:
            reputacao_aris += 1
        elif pontPlat > pontAris:
            reputacao_plat += 1
        elif pontAris == pontPlat:
            semreputacao += 1
    scene Atenas
    show Sisifo_sorrindo at left:
        zoom 0.3
    show Diogenes at right:
        zoom 0.3
    S "...Pois faz parte de um estilo de vida honesto ajudar quem precisa."
    S "Tu bem sabes que saí de minha cidade às pressas, sem um tostão no bolso..."
    D "Tá, tá, já entendi."
    D "Aqui, isto vai ajudar você."
    hide Sisifo_sorrindo
    hide Diogenes
    show Obolo1:
        xpos 240 ypos 240
    show Obolo2:
        xpos 1000 ypos 240
    N "Sísifo obteve o Óbolo"
    hide Obolo1
    hide Obolo2
    jump Cena10
    stop music fadeout 1
return

label Cena10:
    play music "audio/Musica Segundo Ato.ogg"
    scene Atenas
    show Platao_sorrindo at left:
        zoom 0.3
    show Sisifo_sorrindo at right:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    PL "Este Óbolo é favorito de Caronte, dê a ela e poderemos atravessar."
    S "Adiante, chega de perder tempo."
    N "Sísifo, Platão e Filos Aris partem para o porto."
    hide Sisifo_sorrindo with moveoutright
    hide Aristoteles with moveoutright
    hide Platao_sorrindo with moveoutright
    show Diogenes_furiosa at left:
        zoom 0.3
    D "..."
    D "De nada..."
    hide Diogenes_furiosa with moveoutleft
    scene Porto
    stop music fadeout 1
    play music "audio/Som_Ambiente_Porto.ogg"
    N "Aproximando-se do cais, a sombra surge do mar."
    show Sisifo at left:
        zoom 0.3
    show Caronte at right with moveinbottom:
        zoom 0.3
    stop music fadeout 1
    play music "audio/Musica Tema Caronte.ogg"
    C "Sim... vocês retornaram..."
    C "Prepararam-se psicologicamente para uma travessia de 100 anos?"
    S "Tenho o dinheiro para atravessar."
    S "Procure outra alma perdida para te acompanhar por 100 anos."
    C "Excelente..."
    C "Embarquem, partiremos imediatamente para a terra de Minos."
    hide Caronte
    show Sisifo_com_medo at left:
        zoom 0.3
    S "Estou psicologicamente preparado, já o meu estomago..."
    show Aristoteles_furiosa at right with moveinright:
        zoom 0.3
    AR "Se vomitar em mim eu te chuto do barco."
    hide Sisifo_com_medo
    hide Aristoteles_furiosa
    scene Creta
    show Caronte at center with dissolve:
        zoom 0.3
    C "Porto de Creta, conforme o combinado."
    C "Aqui me despeço. Mas lembrem-se de mim quando vossa hora chegar."
    N "Caronte afunda e desaparece nas profundezas."
    hide Caronte with moveoutbottom
    stop music fadeout 1
    play music "audio/Musica Segundo Ato.ogg"
    show Aristoteles at left with moveinleft:
        zoom 0.3
    show Sisifo at center:
        zoom 0.3
    show Platao at right with moveinright:
        zoom 0.3
    AR "Eu hein, credo."
    S "Meu estômago..."
    PL "Já passou, garoto."
    hide Platao
    show Platao_sorrindo at right:
        zoom 0.3
    PL "Estamos em terra firme agora."
    hide Platao_sorrindo
    show Platao at right:
        zoom 0.3
    PL "Creta! Terra de Minos. Aqui encontraremos um querido amigo meu."
    AR "E quem seria essa pessoa, professor?"
    PL "Estamos indo ao encontro de..."
    hide Platao
    hide Sisifo
    hide Aristoteles
    show Atlas at right:
        zoom 0.6
    AT "SÍSIFO!!!"
    hide Atlas
    show Aristoteles at left:
        zoom 0.3
    show Sisifo_surpreso at center:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    S "Ah não..."
    S "Era o que me faltava..."
    N "Um homem desproporcionalmente alto se aproxima, sua voz soa como o trovão, seus passos chacoalham o solo, o céu parece se desdobrar conforme ele se move."
    N "Ele carrega um globo consigo."
    hide Platao
    hide Sisifo_surpreso 
    hide Aristoteles
    show Aristoteles at left with dissolve:
        zoom 0.25
    show Sisifo at center with dissolve:
        zoom 0.25
    show Atlas_surpresso at right with dissolve:
        zoom 0.32
    AT "Sísifo! Não esperava encontrá-lo aqui."
    hide Atlas_surpresso
    show Atlas at right:
        zoom 0.32
    AT "Você deveria ter aparecido no show de Mérope, ela sentiu sua falta."
    AR "Oh, quem é o seu amigo Sísifo?"
    hide Sisifo
    show Sisifo_pensativo at center:
        zoom 0.25
    S "Er... Este é Atlas..."
    S "O meu bom e velho sogro."
    hide Aristoteles
    show Platao_sorrindo at left:
        zoom 0.25
    PL "Minha nossa!"
    PL "Atlas, o titã! É uma honra conhecê-lo!"
    AT "Vejo que está entre novas amizades."
    hide Platao
    hide Sisifo
    hide Atlas
    show Atlas_surpresso at right:
        zoom 0.32
    menu:
        "Cantando":
            pause 1
            python:
                escolha4 = 1
                reputacao_plat += 1
            jump Escolha_Cantando
        "Atirando":
            pause 1
            python:
                escolha4 = 2
                reputacao_aris += 1
            jump Escolha_Atirando
        AT "Hmm... mas não vejo Mérope, onde está minha bebezinha?"
return

label Escolha_Cantando:
    scene Creta
    show Atlas at center with dissolve:
        zoom 0.32
    show Sisifo at left with dissolve:
        zoom 0.25
    show Platao at right with dissolve:
        zoom 0.25
    S "Ela foi praticar o canto de guerra para os deuses no Oráculo."
    PL "Antes fosse, garoto."
    PL "Adoraria presenciar o canto de Méreope, mas antes disso precisamos resgatá-la da morte."
    hide Atlas
    hide Sisifo
    hide Platao
    jump Cena11
return

label Escolha_Atirando:
    scene Creta
    show Atlas at center with dissolve:
        zoom 0.32
    show Sisifo at left with dissolve:
        zoom 0.25
    show Aristoteles at right with dissolve:
        zoom 0.25
    S "Ela está a praticar arquearia."
    S "Está tentando entrar para os patrulheiros de Pirene."
    AR "Uma causa nobre, porém, não é a verdade."
    AR "Mérope perdeu a vida e estamos tentando ressuscitá-la"
    hide Atlas
    hide Sisifo
    hide Aristoteles
    jump Cena11
return

label Cena11:
    scene Creta
    show Atlas_surpresso at center:
        zoom 0.32
    show Sisifo at left:
        zoom 0.25
    show Platao at right:
        zoom 0.25
    AT "O QUE?!"
    hide Atlas_surpresso
    show Atlas_triste at center:
        zoom 0.32
    AT "Minha filha... Está morta?"
    hide Sisifo
    show Sisifo_surpreso at left:
        zoom 0.25
    S "Pensei que vocês estavam do meu lado..."
    PL "Estamos no lado da verdade, Sísifo."
    hide Platao
    show Aristoteles at right:
        zoom 0.25
    AR "Verdades distintas, mas ainda sim verdades."
    AT "Como isso pôde acontecer..."
    AT "Como..."
    AT "O que aconteceu? Isso não pode ser verdade..."
    AT "Conte-me como, o que você sabe sobre isso?"
    S "Bem, ela se perdeu no bosque, fui ao seu encontro, mas cheguei tarde demais."
    hide Sisifo_surpreso
    show Sisifo_triste at left:
        zoom 0.25
    S "Pude apenas ver Tânatos levando sua alma para os céus."
    hide Aristoteles
    show Platao at right:
        zoom 0.25
    PL "Não foi b-"
    N "Sísifo pisa no pé de Platão."
    hide Platao
    show Platao_surpreso at right:
        zoom 0.25
    PL "AArrgh!!!"
    hide Sisifo_triste
    show Sisifo at left:
        zoom 0.25
    S "Aparentemente existe uma forma de trazê-la de volta, por isso esses dois estão me acompanhando."
    AT "Minha garotinha..."
    hide Atlas_triste
    show Atlas_furioso at center:
        zoom 0.32
    AT "Tânatos, TÂNATOS!"
    AT "Buscarei o sangue daquele verme mimado."
    AT "Partirei para o continente agora mesmo. Sei exatamente como encontrar a morte."
    N "Atlas corre em direção ao mar à passos largos"
    hide Atlas_furioso with dissolve
    scene Creta
    show Sisifo_surpreso at left:
        zoom 0.3
    show Platao at right:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    S "Espere!!!"
    S "Você sabe como alcançar a morte?"
    N "O Grande homem está irado demais para ouvir Sísifo e desaparece no horizonte."
    N "No desespero, Atlas deixou cair correntes de seus bolsos."
    PL "Os meios dos titãs não se aplicam para os homens."
    PL "Mesmo se ele nos dissesse, nada poderíamos fazer."
    PL "É por isso que eu te trouxa aqui, Sísifo."
    PL "Precisamos encontrar Ícaro, ele possui a ferramenta necessária para entrar no plano divino, sem precisar morrer."
    hide Aristoteles
    show Aristoteles_surpresa at center:
        zoom 0.3
    AR "As asas de Ícaro..."
    AR "Você sempre me surpreende, velhote! Isso é verdadeiramente engenhoso!"
    hide Sisifo_surpreso
    show Sisifo at left:
        zoom 0.3
    S "Ícaro..."
    S "Certo, vamos ao seu encontro."
    S "Hm..."
    S "Olha só isso."
    scene Creta
    show Corrente:
        xpos 616 ypos 68
    N "{b}{size=42}{color=#f6ff00}Sísifo pega as correntes{/b}{/size}{/color}"
    hide Corrente
    show Sisifo at left:
        zoom 0.3
    show Platao_surpreso at right:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    PL "São Correntes Divinas... O titã as utiliza para segurar o firmamento!"
    AR "Hmm... Atlas já deve estar longe agora..."
    AR "Isso nos pode ser útil, sugiro levá-la conosco."
    hide Sisifo
    hide Platao_surpreso
    hide Aristoteles
    jump Cena12
return

label Cena12:
    scene Creta
    N "Após uma breve caminhada, o grupo se aproxima de uma oficina."
    N "Próteses, tiras de couro, penas e cera estão espalhados por toda parte."
    show Platao at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    PL "Chegamos."
    PL "Esta é a casa de Ícaro, um dos melhores engenheiros da Escola de Atenas."
    hide Aristoteles
    hide Sisifo
    show Icaro_surpreso at right with moveinright:
        zoom 0.3
    I "Professor!"
    I "Que boa surpresa, há muito não vejo o senhor."
    PL "Ora, viemos de longe ao seu encontro."
    PL "Infelizmente as circunstâncias não são boas."
    hide Icaro_surpreso
    show Icaro at right:
        zoom 0.3
    I "Oh..."
    I "Entre e digam-me o que ocorreu."
    hide Platao
    hide Icaro
    N "Platão explica a situação para Ícaro."
    N "..."
    show Platao at left:
        zoom 0.3
    show Aristoteles at center:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    PL "E aqui estamos."
    PL "Vim pedir ajuda, eu conheço os caminhos para a divindade, mas não tenho os recursos necessários"
    AR "É aí que você entra."
    S "Precisamos de asas..."
    hide Platao
    hide Aristoteles
    hide Sisifo
    show Icaro at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Aristoteles at right:
        zoom 0.3
    I "Sim... eu entendo."
    I "Posso construir um colete especial para você."
    I "Eu adoraria acompanhá-los, Tânatos levou o meu pai..."
    AR "Sinto muito."
    I "Consigo construir um colete, mas preciso de suas medidas... e de sua ajuda"
    hide Sisifo
    show Sisifo_surpreso at left:
        zoom 0.3
    S "Ah pronto."
    I "A verdade é que os negócios não vão bem por aqui..."
    I "Tenho trabalhado sozinho, demoraria uma semana para construir um colete."
    I "Mas com a sua ajuda, poderíamos terminar bem mais rápido!"
    hide Sisifo_surpreso
    show Sisifo at left:
        zoom 0.3
    S "Quanto antes começarmos, mais cedo recuperarei ela."
    jump Question1
return

label Question1:
    scene Creta
    show Icaro at right:
        zoom 0.3
    menu:
        "Mármore":
            I "Precisamos de algo maleável para amarrar."
            jump Question1
        "Gesso":
            I "Precisamos de algo maleável para amarrar."
            jump Question1
        "Couro":
            jump Question2
        I "Qual material usaremos no peitoral?"
return

label Question2:
    scene Creta
    show Icaro at right:
        zoom 0.3
    menu:
        "Tecido":
            jump Question3
        "Algodão":
            I "Para as vestes escolha algo nem muito mácio nem muito rígido."
            jump Question2
        "Plástico":
            I "Para as vestes escolha algo nem muito mácio nem muito rígido."
            jump Question2
        I "Agora algo para revestir por dentro."
return

label Question3:
    scene Creta
    show Icaro at right:
        zoom 0.3
    menu:
        "Cota de Malha":
            I "Sustentação para as asas."
            jump Question3

        "Circuito":
            I "Sustentação para as asas."
            jump Question3

        "Panos":
            jump Question4
        I "O carro chefe: As asas."
return

label Question4:
    scene Creta
    show Icaro at right:
        zoom 0.3
    menu:
        "Cimento":
            I "Pegue a cola para o colete."
            jump Question4

        "Poliéster":
            I "Pegue a cola para o colete."
            jump Question4

        "Cera":
            jump Question5
        I "Me passe algo para colar as penas no lugar"
return

label Question5:
    scene Creta
    show Icaro at right:
        zoom 0.3
    menu:
        "Martelo":
            I "Por onde passaremos as tiras de couro?"
            jump Question5

        "Roldana":
            jump Cena13

        "Madeira":
            I "Por onde passaremos as tiras de couro?"
            jump Question5
        I "Por último, uma peça para içar as tiras de couro e as asas."
return

label Cena13:
    scene Creta
    show Colete:
        xpos 119 ypos 324
    N "Sísifo obteve o Colete Alado"
    hide Colete
    show Icaro at center:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Aristoteles at left:
        zoom 0.3
    I "Isso vai servir!"
    scene Creta
    show Icaro_surpreso at center:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Aristoteles at left:
        zoom 0.3
    I "Tem certeza de que nunca fez isso antes? Haha."
    AR "Ele só ficou olhando enquanto você fazia o trabalho pesado."
    scene Creta
    show Icaro at center:
        zoom 0.3
    show Aristoteles at left:
        zoom 0.3
    show Sisifo_surpreso at right:
        zoom 0.3
    S "Ei, não diminua minha participação."
    hide Aristoteles 
    show Platao at left:
        zoom 0.3
    PL "Sem discussões crianças."
    PL "Já temos problemas o suficiente com os deuses."
    S "O velhote tem razão."
    S "Mas agora eu lembrei de uma coisa..."
    S "Pra chegar aos domínios dos deuses..."
    hide Sisifo_surpreso
    show Sisifo_com_medo at right:
        zoom 0.3
    S "Eu vou ter que pegar um barco de novo?"
    hide Platao
    show Aristoteles at left:
        zoom 0.3
    AR "Ele tem hidrofobia, por isso está preocupado."
    hide Sisifo_com_medo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Não é bem assim..."
    I "Hmm... Entendi."
    I "Veja, há uma nova forma de alcançar o Olimpo!"
    I "Agora você tem asas, Sísifo, pode voar pelo mar."
    hide Sisifo_pensativo
    show Sisifo at right:
        zoom 0.3
    S "Eita, não sei se isso é uma boa ideia..."
    S "Talvez se eu voar o mais alto que puder..."
    I "Não seja tão extremo."
    I "Eu também tive que cruzar o mar, e assim como você, também tive medo dele."
    I "Porém meu velho pai me dizia para não voar nem muito alto, a ponto do Sol queimar as asas, nem muito baixo, para que eu não caísse no mar."
    AR "Agir com temperança..."
    AR "É uma lição de vida valiosa."
    AR "Tudo o que você faz neste mundo traz consequências..."
    S "Que seja!"
    S "Cruzarei o mar sozinho e trarei ela em segurança."
    hide Aristoteles
    show Platao at left:
        zoom 0.3
    PL "Lembre-se: a entrada para o reino dos deuses é localizada no topo do Oráculo de Delfos."
    hide Sisifo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "O lugar onde Pepezinha se apresentou..."
    PL "Para entrar lá, você precisa subir o mais alto que suas asas suportarem, então você alcançará o seu objetivo."
    scene black with dissolve
    N "(Enquanto Sísifo viaja)"
    N "..."
    N "Sísifo cruza o mar de Creta, cuidadoso para não se aproximar do Sol e nem do mar, assim como seus companheiros aconselharam. "
    stop music fadeout 1
    jump Cena14

label Cena14:
    scene Oraculo
    play music "audio/Musica Padrao Sisifo.ogg"
    N "O Oráculo de Delfos, a casa das profecias."
    N "Aonde os mortais vêm de todo o mundo para descobrirem o seu destino."
    N "Sísifo, munido das asas de Ícaro, se aproxima e rapidamente reconhece o titã."
    show Sisifo Asas at right with moveinright:
        zoom 0.25
    show Atlas_furioso at left:
        zoom 0.32
    AT "Zeus, desça aqui e me enfrente como um homem!"
    AT "...Ou como um deus, que seja!!!"
    S "Ele veio mesmo até aqui."
    S "Atlas! Aqui!"
    hide Atlas_furioso
    show Atlas_surpresso at left:
        zoom 0.32
    AT "Garoto, garoto!"
    AT "Isso é obra de Zeus!"
    hide Atlas_surpresso
    show Atlas_furioso at left:
        zoom 0.32
    AT "Consigo ouvir o som de sua guitarra daqui, do mundo dos homens."
    AT "Tânatos vive com ele no Olimpo."
    scene Oraculo
    show Sisifo Asas_com_medo at right:
        zoom 0.25
    show Atlas_furioso at left:
        zoom 0.32
    S "Eu... eu consigo trazê-la de volta."
    hide Atlas_furioso
    show Atlas_surpresso at left:
        zoom 0.32
    AT "Você é um mortal!"
    AT "Mortais não alcançam o próximo plano, pelo menos não em vida!"
    scene Oraculo
    show Sisifo Asas at right:
        zoom 0.25
    show Atlas_surpresso at left:
        zoom 0.32
    S "Eu não sou como os outros mortais."
    hide Atlas_surpresso
    show Atlas at left:
        zoom 0.32
    AT "É o que todos dizem..."
    S "Eu te provo!"
    S "Alçarei voo e resgatarei Mérope!"
    menu:
        "Voar":
            python:
                reputacao_plat += 1
                escolha5 = 1
            jump Escolha_Voar
        "Provocar":
            python:
                reputacao_aris += 1
                escolha5 = 2
            jump Escolha_Provocar
        S "O que vou fazer?"
return

label Escolha_Voar:
    scene Oraculo
    N "Sísifo se lança contra os céus, o ranger de suas asas mecânicas quebra o silêncio divino da noite delfina."
    show Sisifo Asas at center:
        zoom 0.3
    S "É só não olhar pra baixo, só não olhar pra baixo só não olhar pra baixo..."
    N "{b}{size=42}{color=#f6ff00}(Sísifo) - Olha pra baixo{/b}{/size}{/color}"
    hide Sisifo Asas
    show Sisifo Asas_com_medo at center:
        zoom 0.3
    S "Droga!"
    N "O medo de altura paralisa o mortal em plenos céus."
    N "Sísifo despenca das alturas."
    hide Sisifo Asas_com_medo
    show Atlas_surpresso at center:
        zoom 0.32
    AT "Achei que você estivesse indo para cima!"
    N "O colosso amortece a queda do homem com suas grandes mãos."
    hide Atlas_surpresso
    show Atlas at center:
        zoom 0.6
    S "Eu só estava me aquecendo, você não precisava fazer isso."
    S "Me largue!"
    hide Atlas
    show Sisifo Asas at right:
        zoom 0.25
    show Atlas at left:
        zoom 0.32
    S "Eu não preciso de você!"
    scene Oraculo
    show Sisifo Asas_pensativo at right:
        zoom 0.25
    show Atlas at left:
        zoom 0.32
    S "Hmm..."
    S "Na verdade..."
    jump PosCena14

label Escolha_Provocar:
    scene Oraculo
    show Sisifo Asas at right:
        zoom 0.25
    show Atlas at left:
        zoom 0.32
    S "Tânatos! Está me ouvindo?"
    S "Sou Sísifo de Pirene, o mortal que se opôs à vontade da própria morte!"
    S "Desça aqui e enfrente minha ira!"
    AT "Isso não vai funcionar."
    AT "Estou convocando a presença divina há tempos e nada..."
    AT "Tudo o que ouço é o som de guitarras."
    AT "Pensei que você fosse utilizar as asas de Ícaro para alcançar as alturas."
    scene Oraculo
    show Sisifo Asas_pensativo at right:
        zoom 0.25
    show Atlas at left:
        zoom 0.32
    S "(Já foi o maior perrengue voar até aqui...)"
    S "(E agora subir nessa montanha gigantesca...Não vou conseguir)"
    S "(Talvez Atlas possa me dar um empurrãozinho, afinal ele tem a força de um titã)"
    AT "Garoto! Estou falando com você!"
    AT "Bata suas asas e suba o monte!"
    S "Tenho uma ideia melhor"
    jump PosCena14

label PosCena14:
    scene Oraculo
    show Sisifo Asas at right:
        zoom 0.25
    show Atlas at left:
        zoom 0.32
    S "Altas, me empreste sua força."
    hide Atlas
    show Atlas_surpresso at left:
        zoom 0.32
    AT "O que quer dizer?"
    S "Me arremesse para cima, assim aproveitarei de seu impulso para voar mais alto."
    hide Atlas_surpresso
    show Atlas_sorrindo at left:
        zoom 0.32
    AT "Boa ideia, garoto!"
    AT "É por isso que Mérope gosta de você."
    AT "Tu sempre encontras a melhor solução para os problemas."
    hide Atlas_sorrindo
    hide Sisifo Asas
    show Atlas at left:
        zoom 0.6
    show Sisifo Asas at right:
        zoom 0.25
    AT "Venha, suba em minhas mãos."
    N "O colosso se ajoelha e Sísifo sobe em suas mãos."
    hide Sisifo Asas with moveouttop
    N "..."
    N "Atlas gira no próprio eixo para gerar impulso e arremessa o salvador para as estrelas!"
    N "Sísifo voa por entre as 12 casas do Zodíaco, abrindo suas asas e voando com o poder do titã!"
    hide Atlas
    stop music fadeout 1
    play music "audio/Musica Tanatos.ogg"
    scene black with dissolve
    pause 1.0
    scene Olimpo
    show Merope_furiosa at left with moveinleft:
        zoom 0.28
    show Zeus at right:
        zoom 0.3
    M "Você vai me levar de volta AGORA!"
    M "Não vou cantar pra velho nenhum!"
    Z "“Velho nenhum”?"
    Z "Eu sou o seu deus, me obedeça ou enfrente a danação eterna."
    Z "Se ordeno que cante então você canta!"
    M "Não interessa, podia ser o papa pintado de ouro."
    M "Você mandou me sequestrar! Criminoso nojento!"
    hide Zeus 
    hide Merope_furiosa
    show Tanatos at center:
        zoom 0.3  
    T "E eu fui tolo o suficiente de achar que teria paz..."
    T "Agora tenho o dobro de problemas com esses dois gritando no pé do meu ouvido o dia inteiro."
    T "Eu mereço..."
    show Merope_furiosa at left:
        zoom 0.28
    show Zeus at right:
        zoom 0.3
    M "E você, calado!"
    M "Tu é cumplice disso tudo."
    M "Meu pai é o poderoso Atlas, ele deve estar marchando para cá agora mesmo."
    M "Se preparem para a próxima titanomaquia." 
    T "Que ideia genial a sua, tio."
    T "Se “Pepezinha” estiver falando a verdade, o Olimpo inteiro corre perigo."
    M "E não me venha com “Pepezinha”!!!"
    N "Aproximando-se das margens do firmamento, Sísifo de Pirene começa a ouvir uma gritaria vinda do Olimpo."
    hide Tanatos
    hide Zeus
    hide Merope_furiosa
    show Sisifo Asas_com_medo at center:
        zoom 0.3
    S "SAI DE BAIXO!"
    hide Sisifo Asas_com_medo
    show Merope_sorrindo at left:
        zoom 0.28
    M "Sísifo?"
    hide Merope_sorrindo
    N "Sísifo, tal qual um míssil, chega no olimpo e cai em cima de Zeus, nocauteando-o!"
    show RaioTela:
        xpos 842 ypos 117
    N "Na queda, Zeus deixa o seu lendário Raio cair de seu bolso."
    hide RaioTela
    show Tanatos_Furioso at right:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Zeus_furioso at center with hpunch:
        zoom 0.3
    Z "Ayeee!!!"
    T "Mas o que?"
    T "Tio!"
    S "Argh.. Minha cabeça..."
    S "Que velho duro da Porr-"
    N "Na queda, Zeus deixa o seu lendário Raio cair de seu bolso."
    T "O que você fez com o meu tio?"
    T "Consegue imaginar as consequências disto?"
    T "Espere... eu lembro de você, é o fracote de Pirene!"
    S "O “fracote” ascendeu ao mundo dos deuses sozinho!"
    T "O erro foi meu, não deveria ter deixado testemunhas!"
    scene Olimpo
    show Tanatos_Sorrindo at right:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    show Zeus_furioso at center:
        zoom 0.3
    T "Basta, arrancarei a alma de seus corpos da forma mais dolorosa possível!"
    N "Os olhos do senhor da morte acendem em brasas, o demônio alado parte em sua direção!"
    scene Olimpo
    jump Minigame_Raio 
return

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.1), false=[Hide('countdown'), Jump("Pergunta")])
    bar value time range timer_range xpos 535 ypos 963 xmaximum 300 at alpha_dissolve
    python:
        
        pose = (((time) - 5.08)/-0.0049)
        if time >= 4.1:
            tempo = 5
        if time < 4.1:
            tempo = 4
        if time < 3.1:
            tempo = 3
        if time < 2.1:
            tempo = 2
        if time < 1.1:
            tempo = 1
        if time < 0.1:
            tempo = 0
            
        tempo = int(time)

    imagebutton:
            idle im.Scale("item_raio_de_zeus.png",55,215)
            hover im.Scale("item_raio_de_zeus2.png",55,215)
            clicked [ToggleScreen("countdown"), Function(renpy.call, label="Ganhou_raio")]
            xpos 960 ypos (int(pose))
    
    frame:
            background "#00e77bff"
            xpos 600 ypos 40
            text "{size=60}[tempo]{/size}"
return

init:
    $ timer_range = 0
    $ timer_jump = 0

label Minigame_Raio:
    $ time = 5.0
    $ timer_range = 5.0
    "Pegue o raio"
    call screen countdown
    pause 5.0
return

label Pergunta:
    menu:
        "Avançar":
            hide screen countdown
            jump Perdeu_raio
        "Tentar novamente":
            jump Minigame_Raio
return

label Perdeu_raio:
    N "Como um alce no meio da estrada, Sísifo se encontra paralisado de medo, e não consegue pensar em nada para impedir o ataque da criatura"
    show Tanatos at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    T "Você é meu, Sísifo de Pirene."
    T "Sua alma arderá para sempre no coração das estrelas!"
    N "O fim está próximo... Tânatos se prepara para o ataque final."
    hide Sisifo  
    hide Tanatos
    show Tanatos at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    M "Aqui, monstro!"
    T "Você será a próxima, não se acanhe Pepezinha."
    N "Quando se vira para a caçadora, Tânatos não acredita no que vê."
    N "Mérope muniu seu arco com o raio de Zeus!"
    N "A humana dispara."
    T "Não faça isso, você não sabe do que isso é capaz!"
    jump PosCena14_2
return

label Ganhou_raio:
    python:
        if reputacao_aris > reputacao_plat:
            reputacao_aris += 1
        elif reputacao_plat > reputacao_aris:
            reputacao_plat += 1
    show Sisifo_pensativo at left:
        zoom 0.3
    S "(O lendário Raio mágico de Zeus...)"
    S "(Tive uma ideia)"
    N "Sísifo pula e pega o raio que Zeus deixou cair"
    S "Pepezinha, atire isso!"
    show Merope_sorrindo at right:
        zoom 0.28
    M "O que..."
    M "Entendi!"
    N "O mortal joga o raio para Mérope, que prontamente o dispara contra o monstro utilizando o seu arco de caça!"
    hide Merope_sorrindo
    hide Sisifo_pensativo
    jump PosCena14_2
return

label PosCena14_2:
    scene Olimpo
    N "Um poderoso clarão seguido de um estampido atinge o Olimpo."
    show Tanatos_Furioso at right:
        zoom 0.3
    T "Nãããão!!!"
    stop music fadeout 1
    play sound "audio/Som_Grito_Tanatos.ogg"
    T "Argh..."
    stop sound fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg"
    N "Tânatos vai ao chão, atordoado pela grande energia da arma mitológica."
    hide Tanatos_Furioso
    show Sisifo Asas at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    S "Isso... Funcionou! Conseguimos!"
    hide Merope
    show Merope_furiosa at left:
        zoom 0.28
    M "“Conseguimos”?"
    M "Eu que fiz tudo."
    S "Claro, claro, você pode ficar com os créditos."
    hide Merope_furiosa
    show Merope at left:
        zoom 0.28
    M "E agora, como vamos sair daqui?"
    S "Com as minhas asas, eu te carrego."
    S "Mas antes, precisamos nos assegurar de que Tânatos não vira atrás de nós."
    jump Escolha_PosCena14_Segunda
return

label Escolha_PosCena14_Segunda:
    scene Olimpo
    show Sisifo Asas at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    menu:
        "Asas":
            jump Escolha_Asas
            python:
                escolha6 = 1
        "Raio":
            jump Escolha_Raio
            python:
                escolha6 = 2 
        "Corrente":
            jump Escolha_Corrente
            python:
                escolha6 = 3
        M "Tem alguma ideia?"
return 

label Escolha_Asas:
    scene Olimpo
    show Sisifo Asas_pensativo at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    S "(Não podemos fugir agora)"
    S "(Se Tânatos despertar, ele virá atrás de nós mais uma vez)"
    S "(Sem contar que utilizar o colete nele não nos ajudará em nada, uma vez que ficaremos sem asas para fugir!)"
    jump Escolha_PosCena14_Segunda
return

label Escolha_Raio:
    scene Olimpo
    show Sisifo Asas_pensativo at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    S "(Atirar mais uma vez não mudará nada, ele já está apagado e a morte não pode morrer)"
    S "(Preciso pensar em outra opção)"
    jump Escolha_PosCena14_Segunda
return

label Escolha_Corrente:
    scene Olimpo
    show Sisifo Asas at right:
        zoom 0.3
    show Merope at left:
        zoom 0.28
    S "Já sei, as correntes de Atlas!"
    S "Me ajude a prender suas asas."
    hide Sisifo Asas 
    hide Merope
    scene black with dissolve
    N "O casal prende as asas de Tânatos com as correntes de Atlas. "
    jump Cena15
return

label Cena15:
    N "Imobilizado e desacordado, a morte não vê Sísifo descer do Monte Olimpo com Mérope nos braços."
    scene Oraculo
    show Merope at left:
        zoom 0.23
    show Sisifo Asas at right:
        zoom 0.25
    AT "Minha amada filha... está viva!"
    hide Merope
    hide Sisifo Asas
    show Merope_sorrindo at center:
        zoom 0.23
    show Atlas_sorrindo at left with moveinleft:
        zoom 0.32
    AT "Suportar a Terra nos ombros não é nada comparado ao medo de te perder."
    AT "Este sim é um peso que não estou preparado para carregar."
    N "Atlas recebe sua filha nos braços, garantindo-lhe a segurança que apenas um pai carinhoso pode providenciar."
    M "Eles precisarão de mais do que isso para me tirar deste mundo."
    M "Obrigada, Sísifo."
    show Sisifo_pensativo at right:
        zoom 0.25
    S "Recusamos o chamado da morte, mas isso trará a ira de Zeus..."
    S "Precisamos sair daqui antes que ele desperte."   
    N "Os três retornam para Pirene."
    N "Uma vez seguros, Atlas informa os pensadores em Creta sobre o sucesso do resgate."
    scene black with dissolve
    N "Os dias passam, o casal retoma a sua vida na pequena Pirene..."
    N "Mas os seus feitos acabam tendo influência mundial..."
    N "Com a morte imobilizada, e Zeus em profundo sono, os seres vivos do mundo dos homens tornaram-se imortais."
    N "Os relatos ao redor do globo multiplicam-se... pessoas com ferimentos graves e fraturas mortais continuam vivas, soldados em guerra vivem mesmo com um corpo recheado de projéteis, a carne consumida nas refeições continua a trabalhar como se estivesse em seu corpo."
    N "Um verdadeiro milagre desconhecido pela ciência, estes foram os Dias Prometidos, uma nova era para a humanidade."
    N "Mas a bonança dos mortais custava caro para alguns deuses..."
    stop music fadeout 1
    play music "audio/Musica Tanatos.ogg"
    scene Submundo
    show Hades at left with moveinleft:
        zoom 0.3
    show Persefone at right with moveinright:
        zoom 0.3
    H "E Zeus, o que ele tem feito a respeito disso?"
    PE "Ele não responde há semanas, nenhum deus tem notícias de Zeus."
    H "O incompetente de meu irmão mais velho se autoproclama Senhor dos Deuses para isso..."
    H "É uma lastima que todo o meu reinado se resuma a um bando de mortos vivos enquanto ele aproveita a boa-vida no alto do Olimpo."
    PE "Acabo de receber uma mensagem de Ares por meio de Mercúrio."
    PE "Aqui diz que o Deus da guerra está perdendo forças, uma vez que não há mais mortos em guerra."
    PE "O planeta vermelho está desaparecendo do céu..."
    H "EU estou perdendo forças."
    H "O que é um deus dos mortos SEM mortos?"
    H "Isso não pode continuar."
    H "Onde está Tânatos?"
    PE "Ele também está desaparecido, vossa deidade."
    H "Soltem os cães..."
    H "Eu mesmo irei ao Olimpo resolver isso."
    stop music fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg"
    scene Pirene
    N "Enquanto isso em Pirene..."
    N "Sísifo tem passado dias pensando nos eventos do Olimpo e suas consequências em todo o mundo."
    N "Pela primeira vez na vida, ele percebe com clareza a influência de seus atos no mundo que o envolve."
    N "Porém há uma ideia que ainda o perturba todos os dias..."
    N "A morte..."
    N "Ela chegou para sua amada uma vez e ele sabe que é uma questão de tempo até que tudo volte a se normalizar."
    N "E é por isso que ele precisa de um plano."
    show Merope at left with moveinleft:
        zoom 0.28
    show Sisifo at right:
        zoom 0.3
    M "Está tudo bem?"
    M "Percebo que está aéreo nestes últimos dias."
    hide Sisifo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Estou preocupado."
    M "Com o que?"
    M "Ah... Você acha que as pessoas voltarão a morrer, não é?"
    M "Pior que isso, você acha que eles virão te levar."
    hide Sisifo_pensativo
    show Sisifo at right:
        zoom 0.3
    S "Eu SEI que eles virão."
    S "Zeus não vai dormir para sempre... Quando despertar, ele ordenará que Tânatos me leve, eu sei que ele vai."
    M "Acho que você está complicando demais as coisas, Sísifo."
    M "Nós já os vencemos uma vez, não vão conseguir nos pegar de novo."
    M "Pois você tem a mim, e eu tenho você."
    S "Se eles vierem... ou melhor, quando eles vierem, prometa que não enterrará o meu corpo."
    M "E por que eu faria isso?"
    S "Prometa que o fará, por favor."
    S "Eu tenho um plano..."
    M "Eu... Eu prometo."
    stop music fadeout 1
    jump Cena16
return

label Cena16:
    scene Olimpo
    play music "audio/Musica Tanatos.ogg"
    N "Hades viaja, partindo do submundo até a capital dos deuses, o Olimpo."
    show Hades at left with moveinleft:
        zoom 0.3
    show Zeus at right with moveinright:
        zoom 0.3
    H "Mas que patifaria é esta?"
    H "ZEUS!" 
    Z "Me dá mais cinco minutinhos."
    H "Acorde velho incopetente!"
    H "É assim que você quer governar os reinos?"
    hide Zeus
    show Zeus_furioso at right:
        zoom 0.3
    Z "Opa, opa estou acordado."
    Z "O que aconteceu? Minha cabeça... aiai..."
    H "Você que me diga, veja está bagunça."
    hide Hades 
    hide Zeus_furioso
    show Tanatos_Furioso at center with moveinright:
        zoom 0.3
    T "Ei, tem alguém aí?"
    T "Me ajudem, não consigo me mexer com isso me prendendo."
    show Hades at left:
        zoom 0.3
    show Zeus at right:
        zoom 0.3
    H "Vocês são dois patetas, isso que vocês são."
    H "Pensei que aqui o meu garoto fosse aprender alguma coisa de útil por aqui, ledo engano."
    H "Venha aqui, Tânatos."
    Z "O que aconteceu com você moleque, cadê, cadê a humana que estava aqui!"
    scene Olimpo
    show Tanatos at center:
        zoom 0.3
    show Hades at left:
        zoom 0.3
    show Zeus at right:
        zoom 0.3
    T "Pensei que ela estivesse com você!"
    Z "Minha cabeça... dói muito."
    Z "Ela disse um nome antes de eu apagar..."
    Z "Sísifo, se não me engano."
    T "Sim, sim, o fracote de Pirene, agora me lembro, eles me prenderam aqui com estas correntes."
    H "Estão me dizendo que apanharam pra dois humanos?"
    H "Fica cada vez pior..."
    N "{b}{size=42}{color=#f6ff00}Hades rompe as correntes, liberando a morte de sua prisão{/b}{/size}{/color}"
    Z "Garoto, não é qualquer um que consegue derrubar dois deuses do Olimpo daquele jeito."
    H "Definitivamente..."
    H "Filho meu, traga-me a alma daquele que causou tudo isto, ele é um humano especial..."
    H "Faça isso e eu lhe herdarei o submundo quando minha hora chegar!"
    T "Mas ele nos venceu uma vez, por que não o faria de novo?"
    H "Os ventos da vingança sopram do nosso lado agora."
    H "Pegue o que restou destas correntes, e use-as para trazer a alma dele de uma vez por todas."
    H "Somente a alma vai servir..."
    scene Olimpo
    show Tanatos_Furioso at center:
        zoom 0.3
    show Hades at left:
        zoom 0.3
    show Zeus at right:
        zoom 0.3
    T "Ugh... vocês acham que eu sou o cara dos favores, né?"
    T "Tá bom... eu trago a alma dele, afinal, a sua proposta é bem melhor do que a do velho gagá."
    hide Tanatos_Furioso with moveouttop
    stop music fadeout 1
    jump Cena17
return

label Cena17:
    scene Pirene
    play music "audio/Musica Padrao Sisifo.ogg"
    N "Algumas semanas depois..."
    show Sisifo at left with moveinleft:
        zoom 0.3
    show Merope at center with moveinright:
        zoom 0.28
    S "Mérope, onde eu posso descarregar estas pedras?"
    M "Deixe-as próximas do morro."
    M "Vamos precisar delas mais tarde."
    N "O casal, agora recém-casado, se prepara para construir sua casa na vila de Pirene."
    N "Porém eles não estão sozinhos..."
    stop music fadeout 1
    play music "audio/Musica Tanatos.ogg"
    hide Merope 
    hide Sisifo
    show Tanatos_Sorrindo at center:
        zoom 0.3
    T "Encontrei os passarinhos..."
    T "Uma pena eu só poder levar um deles..."
    T "Que seja, minha missão será bem-sucedida."
    N "{b}{size=42}{color=#f6ff00}Tânatos voa em direção do casal, tomando cuidado para não ser visto{/b}{/size}{/color}"
    hide Tanatos_Sorrindo
    stop music fadeout 1
    play music "audio/Musica Terceiro Ato.ogg"
    show Sisifo_pensativo at left:
        zoom 0.3
    show Merope at center:
        zoom 0.28
    S "Hm...?"
    S "Tive a impressão de que algo estava se aproximando."
    S "Deve ter sido coisa da minha cabeça."
    hide Sisifo_pensativo
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "“É o peso das ideias nessa sua cabeça oca” como Filos Aris diria, haha."
    M "Os materiais de construção não vão se organizar sozinhos..."
    hide Sisifo_sorrindo
    show Sisifo at left:
        zoom 0.3
    S "Tá, tá, já vou."
    N "Tânatos (à distância)"
    hide Sisifo 
    hide Merope
    show Tanatos_Sorrindo at center:
        zoom 0.3
    T "Ele está se afastando..."
    T "Essa pode ser a minha chance de atacar."
    N "Quando o mentiroso se encontra distraído, a morte o pega de surpresa!"
    hide Tanatos_Sorrindo
    show Sisifo_surpreso at left:
        zoom 0.3
    show Tanatos at center with moveintop:
        zoom 0.3
    T "Agora, Sísifo, o fracote de Pirene, eu tomarei sua vida!"
    stop music fadeout 1
    N "{b}{size=42}{color=#f6ff00}O sem-vida agarra Sísifo, imobilizando-o{/b}{/size}{/color}"
    play sound "audio/Som_Grito_Sisifo.ogg"
    S "AH!"
    stop sound fadeout 1
    play music "audio/Musica Terceiro Ato.ogg"
    S "Você de novo, me deixa, cara!"
    S "Zeus me prometeu uma vida segura, depois do episódio do Olimpo."
    scene Pirene
    show Tanatos at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    T "Como assim?"
    T "O que quer dizer com isso?"
    hide Sisifo
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "Há! Não acha estranho você ter ficado preso por tanto tempo, ainda mais na casa de Zeus!"
    S "Ele queria se livrar de você!"
    T "Como... como você..."
    S "(Não acredito que ele caiu nessa)"
    S "(quem diria que a morte era tão ingênua)"
    hide Tanatos_Sorrindo
    show Tanatos_Furioso at center:
        zoom 0.3
    T "Cala-te! Morra em silêncio homem!"
    N "{b}{size=42}{color=#f6ff00}Tânatos joga as correntes de Atlas contra Sísifo, separando sua alma de seu corpo{/b}{/size}{/color}"
    hide Sisifo_sorrindo
    show Sisifo_com_medo at left:
        zoom 0.3
    S "O que você fez??"
    S "Aaargh! Isso arde."
    scene Pirene
    show Tanatos_Sorrindo at center:
        zoom 0.3
    show Sisifo_pensativo at left:
        zoom 0.3
    T "Fiz o que eu deveria ter feito da última vez."
    T "Agora você está MORTO, isso significa que pertence ao meu reino."
    S "(Como imaginei, agora preciso contar com a Mérope cumprindo sua parte da promessa)"
    scene black with dissolve
    N "Utilizando as correntes, Tânatos prende Sísifo e o carrega pelos céus, até desaparecer na noite."
    N "Mérope chorou muito nesta noite, porém ela sabia o que fazer, e foi fiel à vontade de seu marido."
    N "..."
    N "A águia dos mortos carregou a alma de Sísifo pelas doze casas do Olimpo, realizando a travessia para o pós-mundo."
    N "O mentiroso permaneceu estranhamente quieto durante a travessia, a morte não reclamou."
    scene Submundo
    show Tanatos at center:
        zoom 0.3
    show Sisifo at left:
        zoom 0.3
    T "E é até aqui que posso trazê-lo."
    T "O restante do percurso será com a minha amada irmã."
    N "Uma névoa espessa circunda o mundo cinzento e frio."
    N "Dela surge um rosto, depois mãos, depois um remo."
    stop music fadeout 1
    play music "audio/Musica Tema Caronte.ogg"
    show Caronte at right with moveinbottom:
        zoom 0.3
    C "Alto, da margem em diante a terra obedece a mim."
    C "O que traz para mim, irmãozinho?" 
    hide Sisifo
    show Sisifo_surpreso at left:
        zoom 0.3
    S "Isso, quer dizer, essa é a sua irmã?"
    S "Já nos conhecemos antes."
    hide Sisifo_surpreso
    show Sisifo_sorrindo at left:
        zoom 0.3
    S "Ela é Carente!"
    C "Caronte..."
    hide Sisifo_sorrindo
    show Sisifo at left:
        zoom 0.3
    S "Sim, você também é isso."
    T "Trate de atravessá-lo em segurança."
    N "{b}{size=42}{color=#f6ff00}O anjo da morte voa para longe{/b}{/size}{/color}"
    hide Tanatos with moveouttop
    C "A bordo Sísifo de Pirene."
    C "As terras fluviais serão nosso lar."
    C "Mas antes, você precisa pagar o preço..."
    jump Escolha_Cena17
return

label Escolha_Cena17:
    scene Submundo
    show Sisifo at left:
        zoom 0.3
    show Caronte at right:
        zoom 0.3
    menu:
        "DISCÓBOLO":
            jump Escolha_discobolo
            python:
                escolha7 = 1
        "ÓBOLO":
            jump Escolha_obolo
            python:
                escolha7 = 2 
        "AULO":
            jump Escolha_aulo
            python:
                escolha7 = 3
        S "O que era?"
return 

label Escolha_discobolo:
    scene Submundo
    show Sisifo_pensativo at left:
        zoom 0.3
    show Caronte at right:
        zoom 0.3
    S "(Não, não é isso.)"
    S "(Platão disse uma vez o item favorito da barqueira...)"
    S "(O que era mesmo?)"
    jump Escolha_Cena17
return

label Escolha_aulo:
    scene Submundo
    show Sisifo_pensativo at left:
        zoom 0.3
    show Caronte at right:
        zoom 0.3
    S "(Isso não está certo)"
    S "(Aulo é um instrumento, não é isso que agrada a barqueira do Submundo...)"
    jump Escolha_Cena17
return

label Escolha_obolo:
    scene Submundo
    show Sisifo_sorrindo at left:
        zoom 0.3
    show Caronte at right:
        zoom 0.3
    S "Pois você é favorecida pela Óbolo."
    S "O Item que marca a devoção pelas travessias e barcos dos mundos."
    S "Veja bem..."
    jump minigame_Doki_Doki
return

label minigame_Doki_Doki:

    init python:
        listaCar1 = ["Barco", "Travessia", "Óbolo", "Dinheiro", "Névoa", "Remo", "Morte"]
        listaCar2 = ["Água", "Mar", "Rio", "Sofrimento", "Eternidade", "Esquecimento", "Aqueronte"]
        listaCar3 = ["Érebo", "Dor", "Lamento", "Invulnerabilidade", "Tânatos", "Porto", "Era", "Lágrima"]
        listaCar4 = ["Miséria", "Fantasma", "Etéreo", "Onda", "Afundar", "Náufrago", "Ilha", "Pós-Vida"]
        listaFA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        listaPL3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PL1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PL2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDoki = 0
        botcli2 = True
        podees = 0
        nDum3 = 0
        nDum1 = 0
        nDum2 = 0
        pontFiloAris = 0
        pont_PL = 0
        pontCaronte = 0
        palavrinha1 = ""
        palavrinha2 = ""
        palavrinha3 = ""
        palavrinha4 = ""
        palavrinha5s = ""
        palavrinha6 = ""
        palavrinha7 = ""
        palavrinha8 = ""
        palavrinha9 = ""
        palavrinha10 = ""
        quem_Doki = ""
        fDrase = "Escolha uma palavra para compor seu soneto"
        aa =[]
        bb = []
        cc = []
        dd = []
        ees = []
        ff = []
        gg = []
        hh = []
        ii = []
        jj = []
        sDcore= 0

        lista_novaa =[]
        aa =renpy.random.sample(listaCar1, 5)
        palavrinha1 = aa[nDum1]
        bb = renpy.random.sample(listaCar2, 5)
        palavrinha2 = bb[nDum1]
        cc = renpy.random.sample(listaCar3, 5)
        palavrinha3 = cc[nDum1]
        dd = renpy.random.sample(listaCar4, 5)
        palavrinha4 = dd[nDum1]
        ees = renpy.random.sample(listaFA2, 5)
        palavrinha5s = ees[nDum1]
        ff = renpy.random.sample(listaFAris, 5)
        palavrinha6 = ff[nDum1]
        gg = renpy.random.sample(listaFAris3, 5)
        palavrinha7 = gg[nDum1]
        hh = renpy.random.sample(listaPL3, 5)
        palavrinha8 = hh[nDum1]
        ii = renpy.random.sample(lista_PL1, 5)
        palavrinha9 = ii[nDum1]
        jj = renpy.random.sample(lista_PL2, 5)
        palavrinha10 = jj[nDum1]
        sDcore= nDum1 + 1

    N "Agora você irá compor outro soneto"
    hide Sisifo 
    hide Caronte

    call screen telinha1
return

screen telinha1:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable(
                    "palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha1]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha5s]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha8]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha9]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha2]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha6]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha10]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha3]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha7]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha1"), ToggleScreen("telinha2")]
            elif sDcore== 5:
                textbutton "[palavrinha4]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha1"), Function(renpy.call, label="pDontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sDcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fDrase]{/color}"
return

screen telinha2:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha8]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable(
                    "palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha1]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha2]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha7]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha10]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha3]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha4]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha6]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha9]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha2"), ToggleScreen("telinha3")]
            elif sDcore== 5:
                textbutton "[palavrinha5s]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha2"), Function(renpy.call, label="pDontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sDcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fDrase]{/color}"
return

screen telinha3:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha9]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha6]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable(
                    "palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha1]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha4]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha7]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha10]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha8]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha2]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha5s]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha3"), ToggleScreen("telinha4")]
            elif sDcore== 5:
                textbutton "[palavrinha3]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha3"), Function(renpy.call, label="pDontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sDcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fDrase]{/color}"
return

screen telinha4:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha6]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha2]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha10]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha5s]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha9]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable(
                    "palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha1]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha3]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha7]" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha8]" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1), ToggleScreen("telinha4"), ToggleScreen("telinha5")]
            elif sDcore== 5:
                textbutton "[palavrinha4]" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha4"), Function(renpy.call, label="pDontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sDcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fDrase]{/color}"
return

screen telinha5:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha2]{/color}{/font}{/size}" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha10]{/color}{/font}{/size}" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha6]{/color}{/font}{/size}" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha4]{/color}{/font}{/size}" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha3]{/color}{/font}{/size}" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha7]{/color}{/font}{/size}" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha9]{/color}{/font}{/size}" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Caronte gostou"), SetVariable("pontCaronte", pontCaronte + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable(
                    "palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha1]{/color}{/font}{/size}" action[SetVariable("pontCaronte", pontCaronte + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Filo Aris gostou"), SetVariable("pontFiloAris", pontFiloAris + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha5s]{/color}{/font}{/size}" action[SetVariable("pontFiloAris", pontFiloAris + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sDcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("quem_Doki", "Platão gostou"), SetVariable("pont_PL", pont_PL + 1), SetVariable("nDum1", nDum1 + 1), SetVariable("palavrinha1", aa[nDum1+1]), SetVariable("palavrinha2", bb[nDum1+1]), SetVariable("palavrinha3", cc[nDum1+1]), SetVariable("palavrinha4", dd[nDum1+1]), SetVariable("palavrinha5s", ees[nDum1+1]), SetVariable("palavrinha6", ff[nDum1+1]), SetVariable("palavrinha7", gg[nDum1+1]), SetVariable("palavrinha8", hh[nDum1+1]), SetVariable("palavrinha9", ii[nDum1+1]), SetVariable("palavrinha10", jj[nDum1+1]), SetVariable("sDcore", sDcore+ 1)]
            elif sDcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavrinha8]{/color}{/font}{/size}" action[SetVariable("pont_PL", pont_PL + 1), ToggleScreen("telinha5"), Function(renpy.call, label="pDontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sDcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fDrase]{/color}"
return

label pDerdeu:

    python:

        listaCar1 = ["Barco", "Travessia", "Óbolo", "Dinheiro", "Névoa", "Remo", "Morte"]
        listaCar2 = ["Água", "Mar", "Rio", "Sofrimento", "Eternidade", "Esquecimento", "Aqueronte"]
        listaCar3 = ["Érebo", "Dor", "Lamento", "Invulnerabilidade", "Tânatos", "Porto", "Era", "Lágrima"]
        listaCar4 = ["Miséria", "Fantasma", "Etéreo", "Onda", "Afundar", "Náufrago", "Ilha", "Pós-Vida"]
        listaFA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        listaPL3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PL1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PL2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDoki = 0
        botcli2 = True
        podees = 0
        nDum3 = 0
        nDum1 = 0
        nDum2 = 0
        pontFiloAris = 0
        pont_PL = 0
        pontCaronte = 0
        palavrinha1 = ""
        palavrinha2 = ""
        palavrinha3 = ""
        palavrinha4 = ""
        palavrinha5s = ""
        palavrinha6 = ""
        palavrinha7 = ""
        palavrinha8 = ""
        palavrinha9 = ""
        palavrinha10 = ""
        quem_Doki = ""
        fDrase = "Escolha uma palavra para compor seu soneto"
        aa =[]
        bb = []
        cc = []
        dd = []
        ees = []
        ff = []
        gg = []
        hh = []
        ii = []
        jj = []
        sDcore= 0

        lista_novaa =[]
        aa =renpy.random.sample(listaCar1, 5)
        palavrinha1 = aa[nDum1]
        bb = renpy.random.sample(listaCar2, 5)
        palavrinha2 = bb[nDum1]
        cc = renpy.random.sample(listaCar3, 5)
        palavrinha3 = cc[nDum1]
        dd = renpy.random.sample(listaCar4, 5)
        palavrinha4 = dd[nDum1]
        ees = renpy.random.sample(listaFA2, 5)
        palavrinha5s = ees[nDum1]
        ff = renpy.random.sample(listaFAris, 5)
        palavrinha6 = ff[nDum1]
        gg = renpy.random.sample(listaFAris3, 5)
        palavrinha7 = gg[nDum1]
        hh = renpy.random.sample(listaPL3, 5)
        palavrinha8 = hh[nDum1]
        ii = renpy.random.sample(lista_PL1, 5)
        palavrinha9 = ii[nDum1]
        jj = renpy.random.sample(lista_PL2, 5)
        palavrinha10 = jj[nDum1]
        sDcore= nDum1 + 1
    scene Submundo
    show Caronte at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    C "Não me convenceu..."
    S "Calma, eu ainda não terminei."
    hide Caronte
    hide Sisifo
    call screen telinha1
return

label pDontos:
    scene Submundo
    N "E sua pontuação é:"
    call screen pDontuacao
return

screen pDontuacao:
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "Você fez [pontFiloAris] pontos com a Filo Aris"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.2
        text "Você fez [pontCaronte] pontos com a Caronte"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.3
        text "Você fez [pont_PL] pontos com o Platão"
    frame:
        background "#e0dada"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        if pontCaronte < pontFiloAris or pontCaronte < pont_PL:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pDontuacao"), Function(renpy.call, label="pDerdeu")]
        else:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pDontuacao"), Function(renpy.call, label="gDanhou")]
return

label gDanhou:
    python:
        if pontFiloAris > pont_PL:
            reputacao_aris += 1
        elif pont_PL > pontFiloAris:
            reputacao_plat += 1
        elif pontFiloAris == pont_PL:
            semreputacao += 1
    jump Cena18
return

label Cena18:
    stop music fadeout 1
    play music "audio/Musica Terceiro Ato.ogg"
    show Caronte at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    C "Está bem, você vai atravessar."
    C "Sem... mesmo sem o meu dinheiro..."
    hide Sisifo
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "A água não é o meu forte, porém eu sempre pago minhas dívidas."
    S "Você tem a minha palavra."
    hide Sisifo_sorrindo
    show Sisifo at right:
        zoom 0.3
    N "E a travessia foi feita."
    N "No mesmo barco, Sísifo cruzou o rio das lamentações."
    N "Chegando na fortaleza de Hades, o coração do submundo."
    N "Tão misteriosa quanto a forma que surgiu, Caronte desapareceu nas sombras, deixando o mortal sozinho com as trevas."
    hide Caronte with moveoutbottom
    show Persefone at left with moveinleft:
        zoom 0.3
    PE "Quem se aproxima?"
    S "Sou o seu prisioneiro."
    S "Você sabe quem sou."
    PE "É verdade, eu sei."
    PE "O homem que aprisionou a morte..."
    PE "Você tem um propósito nesta vida, talvez até nas outras."
    PE "Apreciaríamos ter alguém como você por perto."
    S "Não tenho interesse em servir os deuses."
    PE "Então você sabe quem sou eu?"
    S "Sim, você é a dama da primavera."
    PE "E você é surpreendente."
    PE "Vejo o porquê de meu marido se interessar tanto por você."
    PE "Onde estão meus modos?"
    PE "Sente-se, será atendido em breve."
    hide Sisifo
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "Obrigado."
    PE "Está com fome?"
    PE "Um convidado especial deve ser bem tratado, temos as mais doces frutas dos nove reinos aqui, no Hades."
    N "{b}{size=42}{color=#f6ff00}Perséfone estende a mão, oferecendo uma romã carmesim para o mortal{/b}{/size}{/color}"
    S "É uma gentileza sua!"
    S "Aceito, obrigado."
    hide Sisifo_sorrindo
    show Sisifo_pensativo at right:
        zoom 0.3
    S "(Já estou no inferno, morto... melhor aproveitar minha estadia)."
    hide Persefone
    hide Sisifo_pensativo
    show Fruta_Roma:
        xpos 646  ypos 245
    N "{b}{size=42}{color=#f6ff00}Sísifo, ainda amarrado pelas correntes, estende o pescoço e morde a fruta{/b}{/size}{/color}"
    hide Fruta_Roma
    show Persefone at left:
        zoom 0.3
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "Está deliciosa."
    N "{b}{size=42}{color=#f6ff00}Sísifo, come uma romã, depois um cacho de uvas, depois um pernil, sua fome parece aumentar a cada mordida{/b}{/size}{/color}"
    N "Foi um banquete interminável, apenas um ser imaterial conseguiria comer tanto."
    N "Após uma eternidade de espera, Hades surge."
    N "O rancor cicatriza o seu rosto, se é que pode ser chamado disso."
    N "Sua carranca fria é rígida como uma estátua de cobre."
    N "Seu olhar penetra a alma de Sísifo, estraçalhando-a, o mentiroso se sente uma presa, pronta para ser abatida."
    show Hades at center:
        zoom 0.3
    H "Você tem alguma noção do que fez?"
    H "Ao tornar eterno cada ser vivo, você prejudica os deuses que se alimentam do fervor da morte."
    H "Você colapsaria o próprio mundo que habita!"
    H "E por quê?"
    jump Escolha_Cena18_P
return

label Escolha_Cena18_P:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    menu:
        "POR GLÓRIA":
            python:
                reputacao_plat += 1
                escolha8 = 1
            jump Escolha_PorGloria
        "POR FAMA":
            python:
                reputacao_aris += 1
                escolha8 = 2
            jump Escolha_PorFama
        "POR MIM":
            python:
                semreputacao += 1
                escolha8 = 3
            jump Escolha_PorMim
        "POR MEDO":
            python:
                semreputacao += 1
                escolha8 = 4
            jump Escolha_PorMedo
        H "Por qual motivo?"
return

label Escolha_PorGloria:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo_sorrindo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "Por glória, eu me tornei um herói entre meu povo."
    S "Fui venerado, construíram monumentos em minha imagem, cantarão sonetos sobre mim para as gerações futuras."
    S "Eu seria um Deus."
    if escolha2 == 1:
        jump Se_Vingador_Ou_Campones3
    elif escolha2 == 2:
        jump Se_Heroi3
return

label Escolha_PorFama:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "Por fama."
    S "Sísifo de Pirene, o homem que desafiou a morte... e venceu."
    hide Sisifo
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "Soa bem, não é?"
    hide Sisifo_sorrindo
    show Sisifo at right:
        zoom 0.3
    S "Mesmo se eu falhasse, lendas são eternas."
    H "São eternas enquanto houver alguém para proferi-las."
    S "Por isso tratei de eternizar todos lá de cima."
    jump PosCena18
return

label Escolha_PorMim:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "É o que faço melhor."
    S "Eu conquisto tudo o que está ao meu alcance."
    hide Sisifo
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "É a minha vontade que importa, se eu tive a oportunidade de vida eterna, não irei desperdiçá-la."
    hide Sisifo_sorrindo
    show Sisifo at right:
        zoom 0.3
    H "O delírio de sua espécie."
    H "Vocês todos se consideram demais."
    S "Eu conheço as consequências do que realizei, eu sempre soube o que viria com isto."
    S "O que me traz a este momento."
    S "Sou o homem que provocou curiosidade em Hades."
    jump PosCena18
return

label Escolha_PorMedo:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo_com_medo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "(Por medo)"
    S "(Estou na presença do senhor do mundo de baixo, não posso demonstrar fraqueza agora)"
    S "Foi... Por..."
    jump Escolha_Cena18_P
return

label Se_Heroi3:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    H "Um Herói que recebe os favores divinos, a contemplação reservada apenas para os habitantes do Empíreo."
    H "Que audácia!"
    jump PosCena18
return

label Se_Vingador_Ou_Campones3:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    H "Você não sabe o que está falando."
    H "Heróis vêm e vão, garoto."
    H "Hércules, Aquiles, Dante..."
    H "Vários são os nomes, você vê onde todos estão agora?"
    H "No fundo do Tártaro!"
    H "Entretanto você fez o que nenhum deles teve coragem de fazer."
    jump PosCena18
return

label PosCena18:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    H "Você é um tolo, Sísifo de Pirene, esta é a verdade."
    H "Mas ao meu lado... ao meu lado eu te transformaria em um Deus..."
    H "Você é inescrupuloso, a principal característica de um de nós."
    PE "E é por isso que te daremos uma escolha."
    PE "O que acha de um lugar na alta cúpula do reino dos mortos?"
    N "{b}{size=42}{color=#f6ff00}Perséfone fita os olhos de Sísifo com um olhar paralisante, ela poderia devorá-lo com a expressão em sua face{/b}{/size}{/color}"
    N "{b}{size=42}{color=#f6ff00}(Hades) - Um sorriso tímido talha a firme máscara de Hades, enquanto observa Perséfone com orgulho{/b}{/size}{/color}"
    H "E então, jurará lealdade a nós?"
    jump Escolha_Cena18_S
return

label Escolha_Cena18_S:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    menu:
        "NEGAR":
            python:
                reputacao_aris += 1
                escolha9 = 1
            jump Escolha_Negar
        "ACEITAR":
            python:
                reputacao_plat += 1
                escolha9 = 2
            jump Escolha_Aceitar
        H "Por qual motivo?"
return

label Escolha_Negar:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "Sou fiel a minha causa e a ela apenas."
    S "Declino vossa proposta."
    N "Perséfone e Hades se entreolham como se já sabendo da resposta e o que fazer a seguir."
    PE "Você é fiel ao sabor do vento, isso que quis dizer."
    PE "O homem fez sua escolha."
    PE "Agora, se me permite."
    PE "Servos!"
    N "{b}{size=42}{color=#f6ff00}Num estalar de dedos, mortos vivos entram no salão, fiéis a vontade de seu senhor{/b}{/size}{/color}"
    PE "Guiem esta alma para o salão do julgamento."
    jump Cena19
return

label Escolha_Aceitar:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    S "É por isso que vim até aqui."
    hide Sisifo
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "Eu aceito."
    hide Sisifo_sorrindo
    show Sisifo at right:
        zoom 0.3
    H "Você é astuto, gosto disso."
    H "Servos!"
    N "{b}{size=42}{color=#f6ff00}Num estalar de dedos, mortos vivos entram no salão, fiéis a vontade de seu senhor{/b}{/size}{/color}"
    H "Levem-no para o quarto de hóspedes."
    H "Precisamos prepará-lo para os rituais."
    jump Cena19
return

label Cena19:
    scene Submundo
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    PE "Você está se esquecendo de uma coisa, querido."
    PE "Para que ele possa iniciar seus ritos póstumos, antes é necessário concluir a vida!"
    PE "E um passarinho me contou que o corpo de Sísifo ainda não foi velado."
    H "Como seria possível!"
    H "Sua esposa não esteva em sua presença? Ela não sabe que partiu?"
    PE "O corpo do homem jaz sete palmos acima de onde deveria estar, já era hora de ter sido enterrado."
    hide Sisifo
    show Sisifo_surpreso at right:
        zoom 0.3
    S "Isso é uma falta de respeito!"
    S "A mulher que jurei minha vida, não deu importância à conclusão de minha passagem."
    hide Sisifo_surpreso
    show Sisifo at right:
        zoom 0.3
    H "De fato."
    H "Mas não seja por isso."
    H "Enviarei subordinados que tratarão disto prontamente."
    S "Se me permite."
    N "Os deuses na presença de Sísifo se calaram por um momento, surpresos e ansiosos para o que ele diria a seguir."
    S "Mérope era minha esposa, e ela traiu a minha honra."
    S "Peço-lhe que permita que eu mesmo faça vingança."
    hide Hades
    hide Sisifo
    hide Persefone
    jump minigame_Hades_Persefone
return

label minigame_Hades_Persefone:

    init python:
        lista_HP_1 = ["Morte", "Lamento", "Dor", "Primavera", "Bosque", "Romã", "Inverno"]
        lista_HP_2 = ["Fogo", "Submundo", "Piedade", "Inumano", "Entropia", "Penumbra", "Eclipse"]
        lista_HP_3 = ["Paixão", "Ébano", "Serpente", "Flor", "Riqueza", "Morto-vivo", "Palácio", "Aurora"]
        lista_HP_4 = ["Inferno", "Natureza", "Soberano", "Hospedeiro", "Ódio", "Plutão", "Psique", "Cérbero"]
        listaFiloA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFiloA = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFiloA3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista_PLATAO_3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PLATAO_1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PLATAO_2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDokiDoki = 0
        botcli3 = True
        podeesss = 0
        nHPum3 = 0
        nHPum1 = 0
        nHPum2 = 0
        pont_Filo_Aris3 = 0
        pont_PLATAO_3 = 0
        pont_HP = 0
        palavras_1 = ""
        palavras_2 = ""
        palavras_3 = ""
        palavras_4 = ""
        palavras_5s = ""
        palavras_6 = ""
        palavras_7 = ""
        palavras_8 = ""
        palavras_9 = ""
        palavras_10 = ""
        quem_Doki_Doki = ""
        fHPrase = "Escolha uma palavra para compor seu soneto"
        aaa =[]
        bbb = []
        ccc = []
        ddd = []
        eees = []
        fff = []
        ggg = []
        hhh = []
        iii = []
        jjj = []
        sHPcore= 0

        lista_novaaa =[]
        aaa =renpy.random.sample(lista_HP_1, 5)
        palavras_1 = aaa[nHPum1]
        bbb = renpy.random.sample(lista_HP_2, 5)
        palavras_2 = bbb[nHPum1]
        ccc = renpy.random.sample(lista_HP_3, 5)
        palavras_3 = ccc[nHPum1]
        ddd = renpy.random.sample(lista_HP_4, 5)
        palavras_4 = ddd[nHPum1]
        eees = renpy.random.sample(listaFiloA2, 5)
        palavras_5s = eees[nHPum1]
        fff = renpy.random.sample(listaFiloA, 5)
        palavras_6 = fff[nHPum1]
        ggg = renpy.random.sample(listaFiloA3, 5)
        palavras_7 = ggg[nHPum1]
        hhh = renpy.random.sample(lista_PLATAO_3, 5)
        palavras_8 = hhh[nHPum1]
        iii = renpy.random.sample(lista_PLATAO_1, 5)
        palavras_9 = iii[nHPum1]
        jjj = renpy.random.sample(lista_PLATAO_2, 5)
        palavras_10 = jjj[nHPum1]
        sHPcore= nHPum1 + 1

    N "Agora você irá compor outro soneto"

    call screen tela_HP_1
return

screen tela_HP_1:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable(
                    "palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_1]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_5s]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_8]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_9]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_2]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_6]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_10]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_3]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_7]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_1"), ToggleScreen("tela_HP_2")]
            elif sHPcore== 5:
                textbutton "[palavras_4]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_1"), Function(renpy.call, label="pHPontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sHPcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fHPrase]{/color}"
return

screen tela_HP_2:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_8]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable(
                    "palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_1]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_2]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_7]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_10]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_3]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_4]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_6]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_9]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_2"), ToggleScreen("tela_HP_3")]
            elif sHPcore== 5:
                textbutton "[palavras_5s]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_2"), Function(renpy.call, label="pHPontos")]
    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sHPcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fHPrase]{/color}"
return

screen tela_HP_3:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_9]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_6]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable(
                    "palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_1]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_4]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_7]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_10]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_8]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_2]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_5s]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_3"), ToggleScreen("tela_HP_4")]
            elif sHPcore== 5:
                textbutton "[palavras_3]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_3"), Function(renpy.call, label="pHPontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sHPcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fHPrase]{/color}"
return

screen tela_HP_4:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_6]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_2]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_10]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_5s]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_9]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable(
                    "palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_1]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_3]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_7]" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_8]" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1), ToggleScreen("tela_HP_4"), ToggleScreen("tela_HP_5")]
            elif sHPcore== 5:
                textbutton "[palavras_4]" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_4"), Function(renpy.call, label="pHPontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sHPcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fHPrase]{/color}"
return

screen tela_HP_5:
    grid 2 5:
        xalign 0.5
        yalign 0.5
        spacing 20
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_2]{/color}{/font}{/size}" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_10]{/color}{/font}{/size}" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_6]{/color}{/font}{/size}" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_4]{/color}{/font}{/size}" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_3]{/color}{/font}{/size}" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_7]{/color}{/font}{/size}" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_9]{/color}{/font}{/size}" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]

        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Hades e Perséfone gostaram"), SetVariable("pont_HP", pont_HP + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable(
                    "palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_1]{/color}{/font}{/size}" action[SetVariable("pont_HP", pont_HP + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Filo Aris gostou"), SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_5s]{/color}{/font}{/size}" action[SetVariable("pont_Filo_Aris3", pont_Filo_Aris3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]
        frame:
            background "#e0dada"
            xpadding 40
            ypadding 20
            xalign 0.5
            yalign 0.5
            if sHPcore< 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("quem_Doki_Doki", "Platão gostou"), SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), SetVariable("nHPum1", nHPum1 + 1), SetVariable("palavras_1", aaa[nHPum1+1]), SetVariable("palavras_2", bbb[nHPum1+1]), SetVariable("palavras_3", ccc[nHPum1+1]), SetVariable("palavras_4", ddd[nHPum1+1]), SetVariable("palavras_5s", eees[nHPum1+1]), SetVariable("palavras_6", fff[nHPum1+1]), SetVariable("palavras_7", ggg[nHPum1+1]), SetVariable("palavras_8", hhh[nHPum1+1]), SetVariable("palavras_9", iii[nHPum1+1]), SetVariable("palavras_10", jjj[nHPum1+1]), SetVariable("sHPcore", sHPcore+ 1)]
            elif sHPcore== 5:
                textbutton "{size=34}{font=LinLibertine_RB.ttf}{color=#005c7a}[palavras_8]{/color}{/font}{/size}" action[SetVariable("pont_PLATAO_3", pont_PLATAO_3 + 1), ToggleScreen("tela_HP_5"), Function(renpy.call, label="pHPontos")]

    frame:
        background "#22f0c3"
        xpadding 40
        ypadding 20
        xalign 0.02
        yalign 0.01
        text "{color=#ffffff}[sHPcore]{/color}"
    frame:
        background "#22f0c3"
        xpadding 100
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "{color=#ffffff}[fHPrase]{/color}"
return

label pHPerdeu:

    python:

        lista_HP_1 = ["Morte", "Lamento", "Dor", "Primavera", "Bosque", "Romã", "Inverno"]
        lista_HP_2 = ["Fogo", "Submundo", "Piedade", "Inumano", "Entropia", "Penumbra", "Eclipse"]
        lista_HP_3 = ["Paixão", "Ébano", "Serpente", "Flor", "Riqueza", "Morto-vivo", "Palácio", "Aurora"]
        lista_HP_4 = ["Inferno", "Natureza", "Soberano", "Hospedeiro", "Ódio", "Plutão", "Psique", "Cérbero"]
        listaFiloA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFiloA = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFiloA3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista_PLATAO_3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PLATAO_1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PLATAO_2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDokiDoki = 0
        botcli3 = True
        podeesss = 0
        nHPum3 = 0
        nHPum1 = 0
        nHPum2 = 0
        pont_Filo_Aris3 = 0
        pont_PLATAO_3 = 0
        pont_HP = 0
        palavras_1 = ""
        palavras_2 = ""
        palavras_3 = ""
        palavras_4 = ""
        palavras_5s = ""
        palavras_6 = ""
        palavras_7 = ""
        palavras_8 = ""
        palavras_9 = ""
        palavras_10 = ""
        quem_Doki_Doki = ""
        fHPrase = "Escolha uma palavra para compor seu soneto"
        aaa =[]
        bbb = []
        ccc = []
        ddd = []
        eees = []
        fff = []
        ggg = []
        hhh = []
        iii = []
        jjj = []
        sHPcore= 0

        lista_novaaa =[]
        aaa =renpy.random.sample(lista_HP_1, 5)
        palavras_1 = aaa[nHPum1]
        bbb = renpy.random.sample(lista_HP_2, 5)
        palavras_2 = bbb[nHPum1]
        ccc = renpy.random.sample(lista_HP_3, 5)
        palavras_3 = ccc[nHPum1]
        ddd = renpy.random.sample(lista_HP_4, 5)
        palavras_4 = ddd[nHPum1]
        eees = renpy.random.sample(listaFiloA2, 5)
        palavras_5s = eees[nHPum1]
        fff = renpy.random.sample(listaFiloA, 5)
        palavras_6 = fff[nHPum1]
        ggg = renpy.random.sample(listaFiloA3, 5)
        palavras_7 = ggg[nHPum1]
        hhh = renpy.random.sample(lista_PLATAO_3, 5)
        palavras_8 = hhh[nHPum1]
        iii = renpy.random.sample(lista_PLATAO_1, 5)
        palavras_9 = iii[nHPum1]
        jjj = renpy.random.sample(lista_PLATAO_2, 5)
        palavras_10 = jjj[nHPum1]
        sHPcore= nHPum1 + 1
    scene Submundo
    show Hades at center:
        zoom 0.3
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    H "Não me convenceu..."
    S "Calma, eu ainda não terminei."
    hide Hades
    hide Sisifo
    hide Persefone
    call screen tela_HP_1
return

label pHPontos:
    N "E sua pontuação é:"
    call screen pHPontuacao
return

screen pHPontuacao:
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.1
        text "Você fez [pont_Filo_Aris3] pontos com a Filo Aris"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.2
        text "Você fez [pont_HP] pontos com Hades e Perséfone"
    frame:
        background "#22f0c3"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.3
        text "Você fez [pont_PLATAO_3] pontos com o Platão"
    frame:
        background "#e0dada"
        xpadding 20
        ypadding 20
        xalign 0.5
        yalign 0.5
        if pont_HP < pont_Filo_Aris3 or pont_HP < pont_PLATAO_3:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pHPontuacao"), Function(renpy.call, label="pHPerdeu")]
        else:
            textbutton "{size=40}{font=LinLibertine_RB.ttf}{color=#005c7a}E agora?{/color}{/font}{/size}" action[ToggleScreen("pHPontuacao"), Function(renpy.call, label="gHPanhou")]
return

label gHPanhou:
    python:
        if pont_Filo_Aris3 > pont_PLATAO_3:
            reputacao_aris += 1
        elif pont_PLATAO_3 > pont_Filo_Aris3:
            reputacao_plat += 1
        elif pont_Filo_Aris3 == pont_PLATAO_3:
            semreputacao += 1
    jump Cena20
return

label Cena20:
    show Hades at center:
        zoom 0.3
    show Persefone at left:
        zoom 0.3
    show Sisifo at right:
        zoom 0.3
    S "E é assim que trarei Mérope."
    S "Permita-me realizar minha vingança!"
    S "Serei um aliado poderoso."
    N "{b}{size=42}{color=#f6ff00}Hades - Olha para Sísifo, depois para Perséfone{/b}{/size}{/color}"
    H "Assim será, sua alma retornará ao corpo, uma vez no mundo material o resto vai ser fácil."
    N "Os senhores do submundo, mesmo desconfiados, permitiram conceder a vingança ao mortal."
    scene black with dissolve
    N "Após um interlúdio que mais pareceu um século, sua alma foi transportada para o mundo."
    N "..."
    N "Mérope estava esperando, ao lado do cadáver putrefato de seu amado, quando de repente."
    stop music fadeout 1
    scene Pirene
    show Merope at left:
        zoom 0.28
    show Sisifo_com_medo at right with moveinbottom:
        zoom 0.3
    play sound "audio/Som_Grito_Sisifo.ogg"
    S "AAAARRRGH!!!"
    stop sound fadeout 1
    play music "audio/Musica Padrao Sisifo.ogg"
    N "O cadáver treme, levantando o peito e depois batendo as costas com força no chão."
    hide Merope
    show Merope_sorrindo at left:
        zoom 0.28
    M "Você conseguiu, você... realmente conseguiu..."
    S "Precisamos sair daqui."
    S "AGORA!"
    scene Pirene
    show Merope at left:
        zoom 0.28
    show Sisifo at right:
        zoom 0.3
    N "Apenas com as roupas do corpo, o casal foge, foge muito, para longe, onde a morte não possa mais encontrar."
    N "E é em Creta que encontram refúgio."
    N "..."
    N "Lá eles podem contar com a proteção do poderoso Atlas."
    N "As asas de Ícaro."
    N "A juventude materialista de Aris."
    N "A sabedoria divina de Platão."
    N "..."
    N "E os anos se passam."
    N "Sísifo quase se esquece do motivo primeiro que o levou ali, a verdade é que ele se sentia feliz."
    N "Feliz por ter fugido da morte duas vezes."
    N "E feliz por ter confiado em Mérope."
    N "Porém, tal como a morte, a vontade divina é Inevitável."
    N "Para toda primavera agradável, há um sombrio inverno. "
    hide Sisifo
    hide Merope
    jump Cena21
return

label Cena21:
    scene Creta
    show Sisifo at left with moveinleft:
        zoom 0.3
    show Platao at center:
        zoom 0.3
    show Aristoteles at right with moveinright:
        zoom 0.3
    PL "Você viu o outro lado do mundo, o mundo da mente."
    hide Platao
    show Platao_sorrindo at center:
        zoom 0.3
    PL "Você esteve no plano divino!"
    hide Platao_sorrindo
    show Platao at center:
        zoom 0.3
    PL "Isso acrescentará muito na minha pesquisa do mito da caverna."
    hide Sisifo
    show Sisifo_pensativo at left:
        zoom 0.3
    S "Essa é aquela sua teoria maluca do prisioneiro que vê sombras, não é?"
    hide Sisifo_pensativo
    show Sisifo at left:
        zoom 0.3
    hide Platao
    show Platao_sorrindo at center:
        zoom 0.3
    PL "Sim, sim. Estive escrevendo um romance, baseado em você, na sua jornada maluca, e o mito."
    PL "Nele, o herói Sócrates vive acorrentado no fundo de uma caverna com seus companheiros, observando apenas sombras de objetos carregados por pessoas livres na frente da caverna."
    PL "Estas pessoas acreditam que o mundo real é apenas aquilo, somente as sombras."
    PL "Um dia, Sócrates é liberto, e observa o lado de fora da caverna, ele vê as cores, formas e pessoas do mundo real."
    PL "Quando ele retorna a caverna e conta para seus amigos, eles não acreditam no que Sócrates diz!"
    hide Platao_sorrindo
    show Platao at center:
        zoom 0.3
    AR "Muitas pessoas precisam ver para crer."
    AR "E olha que as vezes nem isso é o suficiente."
    hide Platao
    hide Aristoteles
    show Icaro at right:
        zoom 0.3
    I "Fascinante."
    I "Já viajei por toda a Grécia, já conheci todo tipo de gente, mas sempre aparecem histórias surpreendentes que nunca ouvi antes, tal como a de Sísifo de Pirene."
    scene black with dissolve
    N "O grupo tem vivido dias agradáveis, todos vivem na casa de Ícaro agora, que foi muito receptivo."
    N "Eles o ajudam em seus projetos de engenharia, porém uma surpresa indesejada aguarda."
    N "..."
    N "Durante uma noite fria, a mente de Sísifo se pôs a sonhar."
    N "Sonhou com o mundo inteiro em suas mãos, sonhou com as terras pertencentes aos deuses sob sua posse."
    N "Sua alma viajou para longe, atravessando a dor, o lamento, o fogo, o esquecimento e a invulnerabilidade."
    N "Este foi seu último sonho."
    stop music fadeout 1
    play music "audio/Musica Tema Julgamento.ogg"
    scene Submundo
    show Sisifo_surpreso at left:
        zoom 0.3
    S "Onde estou? Como vim parar aqui?"
    S "O que está acontecendo?"
    show Persefone at right with moveinright:
        zoom 0.3
    PE "Você veio cumprir sua sentença, Sísifo."
    S "Quem?"
    N "{b}{size=42}{color=#f6ff00}Sísifo se espanta ao perceber com quem está falando{/b}{/size}{/color}"
    hide Sisifo_surpreso
    show Sisifo_com_medo at left:
        zoom 0.3
    S "D-Dama da primavera?"
    S "O que você fez comigo?"
    S "Vocês não poderiam me encontrar, eu fui para onde não me encontrariam!"
    show Hades at center with moveinright:
        zoom 0.3
    H "Nós temos olhos por toda parte..."
    hide Persefone
    show Zeus at right:
        zoom 0.3
    Z "Assim como a morte, nós somos inevitáveis."
    S "Isso não é justo, eu deixei todos vocês para trás!"
    S "Como vim parar aqui de novo?"
    hide Zeus
    show Persefone at right:
        zoom 0.3
    PE "Você provou do fruto proibido aqui, nas terras inferiores."
    PE "Sua alma criou um elo com este mundo."
    PE "Tornou-se prisioneiro, assim como eu fui um dia."
    PE "Mas agora sou eu quem faz justiça."
    H "Sua vida terminou."
    H "E agora você será julgado por tudo o que fez na Terra."
    stop music fadeout 1
    jump Consequencia_Final
return

label Consequencia_Final:
    if reputacao_plat == 9:
        jump Campos_Elisios
    elif reputacao_plat != 9 and reputacao_plat > reputacao_aris:
        jump Campos_Asfódelos
    else:
        jump Tartaro
return

label Campos_Elisios:
    play music "audio/Musica Final Campos Elisios.ogg"
    scene Submundo
    show Sisifo at left:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    show Persefone at right:
        zoom 0.3
    H "Sísifo, o auto nominado “Herói” de Pirene."
    H "Você trouxe a salvação de sua espécie, perpetuando-a indefinidamente pela glória da vida."
    H "Foste devoto aos meios dos deuses."
    PE "Você adquiriu asas e as utilizou para voar mais alto do que qualquer homem jamais fizera."
    PE "Jurou lealdade aos seus superiores, provou do fruto proibido e vinculou sua alma ao pós-vida."
    hide Persefone
    show Zeus at right:
        zoom 0.3
    Z "Você foi ardiloso em suas decisões, verdadeiramente sábio, um exímio discípulo de Platão."
    Z "Ele tem sido observado de perto, este homem é um verdadeiro profeta, sempre fiel ao mundo das ideias."
    Z "Pois as ideias são a forma real de seu universo."
    Z "Uma pintura, esticada na borda da existência, onde vocês contemplam apenas uma ilustração virtual dos verdadeiros fatos."
    H "A essência da realidade é demais para uma mente humana, mas você se dedicou para ter a visão mais pura do todo."
    N "Enquanto Sísifo é julgado pelos deuses, o céu se transforma, toda a forma do universo se manifesta acima de sua cabeça."
    N "Sísifo pode ver tudo."
    N "Sua alma é transportada ao paraíso sem sair do lugar, mil anos se passam em um instante."
    hide Zeus
    show Zeus_furioso at right:
        zoom 0.3
    Z "Mas isto não é destino para você."
    Z "A sua estrada ainda não terminou, isso é apenas parte do seu trajeto."
    N "Um clarão se forma nas mãos de Zeus, o que antes fora uma guitarra toma a forma de uma lança pontiaguda como um raio."
    N "Os olhos de Zeus são a tempestade."
    Z "A nossa vontade é inexorável, é isso que nos torna deuses."
    Z "Homem nenhum se aproximará disto."
    hide Sisifo
    show Sisifo_pensativo at left:
        zoom 0.3
    S "Eu fui leal, mesmo assim todo o meu trabalho foi em vão."
    N "Zeus dispara seu raio onde uma vez fora o coração de Sísifo."
    scene black with dissolve
    N "O homem tem sua alma obliterada."
    N "..."
    N "Porém o que se manifestou como um gesto de crueldade àquele que os serviu, logo tomou outro significado."
    N "Essa é a piedade divina."
    show Atlas at center:
        zoom 0.32
    AT "Essa foi metade da história de Sísifo de Pirene."
    AT "A outra metade está para ser encontrada."
    AT "Mas somente se tomar as decisões corretas na sua segunda chance..."
    stop music fadeout 1
    jump limpar_variaveis
return

label Campos_Asfódelos:
    play music "audio/Musica Final.ogg"
    scene Submundo
    show Zeus at left:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    show Persefone at right:
        zoom 0.3
    H "Sísifo, o comedido de Pirene."
    H "Agiste com temperança, salvando sua espécie do oblívio, mesmo que por um breve período."
    H "Foste devoto a causas muitas."
    PE "Você mostrou-se empacado, infiel a uma única vertente filosófica."
    PE "Talvez por imprudência, talvez por desejar voar mais alto do que suas asas alcançavam..."
    Z "Por buscar razões demais para justificar seus meios, você não chegou ao final de caminho algum."
    Z "Mas aos olhos dos deuses, você não foi tão inútil quanto parece."
    hide Zeus
    show Zeus_Sorrindo at left:
        zoom 0.3
    Z "Fizeste bastante barulho lá embaixo."
    Z "Não posso negar, senti-me inclinado a convidar-te a minha banda, hahah."
    hide Persefone
    show Sisifo_surpreso at right:
        zoom 0.3
    hide Zeus_Sorrindo
    show Zeus at left:
        zoom 0.3
    S "Eu jamais f-"
    Z "Jamais faria isso, eu sei, nós sabemos."
    H "Por isso, de hoje em diante você será meu prisioneiro."
    S "Não pode ser!"
    S "Eu aprendi tanto com Platão quanto com Aris."
    S "Me aproximei da filosofia e a absorvi em minha vida."
    S "Minha recompensa por tudo isso é ser prisioneiro do senhor dos mortos?"
    hide Sisifo_surpreso
    show Sisifo at right:
        zoom 0.3
    H "Exatamente."
    hide Zeus
    show Persefone at left:
        zoom 0.3
    PE "Você teve uma chance única de aprender com os melhores, de ver o mundo sob uma perspectiva singular."
    PE "Mas ainda assim foste traiçoeiro, com os deuses e seus subordinados."
    PE "Esperávamos mais de você na Terra."
    H "Como você não aprendeu em vida, terá o resto da eternidade em meu reino para comtemplar como a justiça divina é feita."
    H "A nossa vontade é absoluta."
    scene black with dissolve
    N "Involuntariamente, a alma de Sísifo se põe a caminhar."
    N "Saindo da fortaleza, ele vaga sem propósito pelo mundo inferior."
    N "Passa por ruínas de templos antigos, cidades arrasadas, vales eternamente profundos."
    N "Eventualmente tropeça em uma alma ou outra."
    N "..."
    N "Em sua jornada interminável, Sísifo é condenado a ouvir os julgamentos de todas as almas que entram no submundo."
    N "Seus olhos ardem em chamas incandescentes até virarem cinzas."
    N "Seu discernimento e inteligência necrosam por entre os éons."
    N "Seu último trabalho é desvanecido pela entropia."
    stop music fadeout 1
    jump Creditos
return

label Creditos:
    scene black with dissolve
    show Creditos_Finais1
    $renpy.pause(2, hard="True")
    scene black with dissolve
    pause 1
    scene black with dissolve
    show Creditos_Finais2
    $renpy.pause(2, hard="True")
    scene black with dissolve
    pause 1
    scene black with dissolve
    show Creditos_Finais3
    $renpy.pause(2, hard="True")
    scene black with dissolve
    pause 1
    scene black with dissolve
    show Creditos_Finais4
    $renpy.pause(2, hard="True")
    scene black with dissolve
    pause 1
    jump Compressao
return

label Compressao:
    python:
        # método de compressão

        # chama o metodo diretorio para o endereço
        diretorio = os.chdir(caminho)
        # cria um arquivo zip com o método ZipFile que está na biblioteca zipfile
        # define o nome do arquivo e a ação (escrita = "w")
        arquivozip = zipfile.ZipFile("arquivo_compactado.zip", "w")
        # cria uma lista com os arquivos do endereço
        lista = os.listdir(caminho)
        # para cada arquivo x na lista de arquivos
        for x in lista:
            # verifica se tem algum arquivo que termina com a extensao jpg ou png, difícil não ter, pois o jogo não teria como rodar sem as imagens
            if x.endswith('.png') or x.endswith('.jpg'):
                # se o arquivo for uma imagem, então será compactado para dentro do arquivo zip, com o método de compressão usual
                arquivozip.write(x, compress_type = zipfile.ZIP_DEFLATED)
                # depois de comprimida a imagem é deletada
                os.remove(x)
        # fechando o arquivo zip
        arquivozip.close()
return

label Tartaro:
    play music "audio/Musica Final.ogg"
    scene Submundo
    show Zeus at left:
        zoom 0.3
    show Hades at center:
        zoom 0.3
    show Persefone at right:
        zoom 0.3
    H "Sísifo, o homem."
    H "Você foi descomedido em vida, agindo de forma egoísta e colocando terceiros para realizar os seus trabalhos."
    PE "Em sua jornada, aproximou-se da filosofia de Aris."
    PE "Um grave erro, serviu aos homens quando poderia servir a algo maior do que si mesmo."
    PE "Podendo aproximar-se da divindade, por que não o fez de pronto?"
    hide Zeus
    show Zeus_Sorrindo at left:
        zoom 0.3
    Z "Pois eu não te culpo."
    Z "Os mortais todos são egoístas por natureza."
    Z "Se você fez o que fez foi por sobrevivência!"
    Z "Eu faria o mesmo."
    H "A diferença é que você é um deus, ninguém vai te punir."
    Z "Por isso mesmo."
    hide Zeus_Sorrindo
    show Zeus at left:
        zoom 0.3
    hide Persefone
    show Sisifo_surpreso at right:
        zoom 0.3
    S "Eu—Eu não sabia."
    hide Sisifo_surpreso 
    show Sisifo_sorrindo at right:
        zoom 0.3
    S "Mas poderíamos negociar a minha pena."
    S "Apenas segui um código de moral que é amplamente cultivado em meu povo."
    S "Se eu não me protegesse, ninguém mais o faria."
    hide Sisifo_sorrindo
    show Sisifo at right:
        zoom 0.3
    Z "Nem mesmo Mérope?"
    hide Sisifo
    show Sisifo_com_medo at right:
        zoom 0.3
    S "Cl-claro."
    S "E-ela me protegeria."
    N "{b}{size=42}{color=#f6ff00}Sísifo treme de medo{/b}{/size}{/color}"
    hide Zeus
    show Persefone at left:
        zoom 0.3
    PE "Ela já salvou sua vida, mais de uma vez."
    PE "E você nem a considera."
    PE "Percebe o que estamos dizendo?"
    H "O seu orgulho tornou-se sua ruína."
    H "Patético."
    hide Sisifo_com_medo
    show Sisifo_triste at right:
        zoom 0.3
    S "Por favor, tenha piedade de minha alma!"
    H "A sua vida foi a piedade, aqui você encontrará sua sentença."
    H "O preço por obrigar os outros a realizar trabalhos sem resultados."
    N "Os deuses se retiram do recinto, Sísifo sai logo depois."
    scene Submundo
    N "Angustiado pela solidão das ruínas, Sísifo começa a caminhar."
    N "Ele passa por um bosque, banhado pelos rios da invulnerabilidade, chegando em um fiorde."
    show Sisifo_pensativo at right:
        zoom 0.3
    S "Eu ainda posso fugir deste lugar."
    N "Seguindo um caminho de pedregulhos, Sísifo começa a subir uma serra."
    N "Após alguns momentos, sente algo em seu bolso."
    N "..."
    N "Uma pequena pedra."
    jump Final_Tartaro_Segunda_Parte
return

label Final_Tartaro_Segunda_Parte:
    scene Submundo
    show Pedra:
        xpos 551 ypos 163
    N "Sísifo obteve a Pedra do Lamento"
    hide Pedra
    show Sisifo_pensativo at center:
        zoom 0.3 
    S "Como isso veio parar aqui?"
    S "Não importa, preciso continuar subindo."
    N "Conforme se aproxima da montanha, a pedra parece ficar cada vez mais pesada."
    N "Ela cresce, Sísifo começa a carregá-la em mãos."
    N "Ao passo em que se aproxima do topo, a pedra cresce mais e mais, ficando cada vez mais pesada."
    N "O homem agora faz grande escorço para rolar a pedra."
    N "Ele já não sabe para onde está indo, apenas segue, cismado com a pedra."
    hide Sisifo_pensativo
    show Sisifo_sorrindo at center:
        zoom 0.3 
    S "É por aqui, eu vou conseguir sair, só mais um pouco..."
    N "Próximo do cume, a pedra fica infinitamente pesada e não se move mais."
    N "O esforço é grande, o homem treme de dor esforçando-se para mantê-la estavel."
    N "A rocha rola montanha abaixo..."
    hide Sisifo_sorrindo
    show Sisifo_triste at center:
        zoom 0.3 
    S "Maldição! Não posso deixar isto para trás, preciso pegá-la."
    N "Apressadamente, ele desce até a base da montanha, observando da base, ela parece surrealmente alta."
    N "A pedra o encara num silêncio ensurdecedor."
    jump Subir_a_montanha
return

label Subir_a_montanha:
    scene Submundo
    show Sisifo_sorrindo at center:
        zoom 0.3 
    N "Com muito pesar, o mortal se dispõe a rolar a pedra montanha acima."
    N "Seus músculos estão exaustos."
    N "O suor corta sua expressão decidida."
    S "Estou quase no topo, só mais alguns metros."
    N "Suas pernas tremem, mas tardam a falhar, esperando o momento em que o mortal quase alcança o pico da montanha."
    N "..."
    N "..."
    N "A rocha despenca montanha abaixo, rolando como um trovão pelo mundo inferior."
    hide Sisifo_sorrindo
    show Sisifo_pensativo at center:
        zoom 0.3 
    S "Essa foi por pouco, eu preciso... preciso dela..."
    N "O frenesi da alma penada se manifesta cada vez mais, borbulhando no suor fervente que escorre a fronte exausta da figura."
    N "..."
    N "Sísifo chega ao pé da montanha"
    hide Sisifo_pensativo
    show Sisifo_sorrindo at center:
        zoom 0.3
    S "Sim, minha companheira, eu te levarei para um lugar melhor, permita-me guiá-la, venha, vamos."
    jump Subir_a_montanha
return

label limpar_variaveis:
    
    python:
    # escolhas e reputações
        escolha1 = 0
        escolha2 = 0
        escolha3 = 0
        escolha4 = 0
        escolha5 = 0
        escolha6 = 0
        escolha7 = 0
        escolha8 = 0
        escolha9 = 0
        semreputacao = 0
        reputacao_aris = 0
        reputacao_plat = 0
    # primeiro Doki_Doki
        lista = ["Cinismo", "Cão", "Humildade", "Honestidade", "Pureza", "Pobreza", "Igualdade"]
        listaDio2 = ["Rebeldia", "Cosmopolita", "Verdade", "Efêmero", "Presente", "Agora", "Indiferença"]
        listaDio3 = ["Anarquia", "Lanterna", "Barril", "Nômade", "Andarilho", "Simplicidade", "Autorrealização", ]
        listaDio4 = ["Estatua", "Pedir", "Agir", "Bondade", "Ser", "Impudor", "Espontaneidade", "Esmola", "Mendigo"]
        lista2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        listaPlat1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        listaPlat2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadas = 0
        botcli = True
        pode = 0
        num3 = 0
        num1 = 0
        num2 = 0
        pontAris = 0
        pontPlat = 0
        pontDio = 0
        palavra1 = ""
        palavra2 = ""
        palavra3 = ""
        palavra4 = ""
        palavra5s = ""
        palavra6 = ""
        palavra7 = ""
        palavra8 = ""
        palavra9 = ""
        palavra10 = ""
        quem = ""
        inicio = "Escolha uma palavra para compor seu soneto"
        a = []
        b = []
        c = []
        d = []
        es = []
        f = []
        g = []
        h = []
        i = []
        j = []
        score = 0

        lista_nova = []
        a = renpy.random.sample(lista, 5)
        palavra1 = a[num1]
        b = renpy.random.sample(listaDio2, 5)
        palavra2 = b[num1]
        c = renpy.random.sample(listaDio3, 5)
        palavra3 = c[num1]
        d = renpy.random.sample(listaDio4, 5)
        palavra4 = d[num1]
        es = renpy.random.sample(lista2, 5)
        palavra5s = es[num1]
        f = renpy.random.sample(listaAris, 5)
        palavra6 = f[num1]
        g = renpy.random.sample(listaAris3, 5)
        palavra7 = g[num1]
        h = renpy.random.sample(lista3, 5)
        palavra8 = h[num1]
        i = renpy.random.sample(listaPlat1, 5)
        palavra9 = i[num1]
        j = renpy.random.sample(listaPlat2, 5)
        palavra10 = j[num1]
        score = num1 + 1
    # segundo Doki_Doki
        listaCar1 = ["Barco", "Travessia", "Óbolo", "Dinheiro", "Névoa", "Remo", "Morte"]
        listaCar2 = ["Água", "Mar", "Rio", "Sofrimento", "Eternidade", "Esquecimento", "Aqueronte"]
        listaCar3 = ["Érebo", "Dor", "Lamento", "Invulnerabilidade", "Tânatos", "Porto", "Era", "Lágrima"]
        listaCar4 = ["Miséria", "Fantasma", "Etéreo", "Onda", "Afundar", "Náufrago", "Ilha", "Pós-Vida"]
        listaFA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFAris = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFAris3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        listaPL3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PL1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PL2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDoki = 0
        botcli2 = True
        podees = 0
        nDum3 = 0
        nDum1 = 0
        nDum2 = 0
        pontFiloAris = 0
        pont_PL = 0
        pontCaronte = 0
        palavrinha1 = ""
        palavrinha2 = ""
        palavrinha3 = ""
        palavrinha4 = ""
        palavrinha5s = ""
        palavrinha6 = ""
        palavrinha7 = ""
        palavrinha8 = ""
        palavrinha9 = ""
        palavrinha10 = ""
        quem_Doki = ""
        fDrase = "Escolha uma palavra para compor seu soneto"
        aa =[]
        bb = []
        cc = []
        dd = []
        ees = []
        ff = []
        gg = []
        hh = []
        ii = []
        jj = []
        sDcore= 0

        lista_novaa =[]
        aa =renpy.random.sample(listaCar1, 5)
        palavrinha1 = aa[nDum1]
        bb = renpy.random.sample(listaCar2, 5)
        palavrinha2 = bb[nDum1]
        cc = renpy.random.sample(listaCar3, 5)
        palavrinha3 = cc[nDum1]
        dd = renpy.random.sample(listaCar4, 5)
        palavrinha4 = dd[nDum1]
        ees = renpy.random.sample(listaFA2, 5)
        palavrinha5s = ees[nDum1]
        ff = renpy.random.sample(listaFAris, 5)
        palavrinha6 = ff[nDum1]
        gg = renpy.random.sample(listaFAris3, 5)
        palavrinha7 = gg[nDum1]
        hh = renpy.random.sample(listaPL3, 5)
        palavrinha8 = hh[nDum1]
        ii = renpy.random.sample(lista_PL1, 5)
        palavrinha9 = ii[nDum1]
        jj = renpy.random.sample(lista_PL2, 5)
        palavrinha10 = jj[nDum1]
        sDcore= nDum1 + 1
    # terceiro Doki_Doki
        lista_HP_1 = ["Morte", "Lamento", "Dor", "Primavera", "Bosque", "Romã", "Inverno"]
        lista_HP_2 = ["Fogo", "Submundo", "Piedade", "Inumano", "Entropia", "Penumbra", "Eclipse"]
        lista_HP_3 = ["Paixão", "Ébano", "Serpente", "Flor", "Riqueza", "Morto-vivo", "Palácio", "Aurora"]
        lista_HP_4 = ["Inferno", "Natureza", "Soberano", "Hospedeiro", "Ódio", "Plutão", "Psique", "Cérbero"]
        listaFiloA2 = ["Material", "Físico", "Aluno", "Lógica", "Homem", "Humano", "Mortal", "Terreno", "Realismo", "Infinito"]
        listaFiloA = ["Mudança", "Retórica", "Metafísica", "Futuro", "Temperança", "Ética", "Terra", "Ateísmo", "Substância", "Forma"]
        listaFiloA3 = ["Potencial", "Ciência", "Virtude", "Corpo", "Razão", "Lógica", "Ego", "Poética", "Teatro", "Amizade"]
        lista_PLATAO_3 = ["Imaterial", "Imaginário", "Surreal", "Divino", "Deus", "Religião", "Alma", "Partícula", "Espírito", "Timeu"]
        lista_PLATAO_1 = ["Professor", "Matemática", "Dualismo", "Ideia", "Amor", "Diálogo", "Sócrates", "Estagnação", "Moral", "Teologia"]
        lista_PLATAO_2 = ["Mente", "Empíreo", "Passado", "Céu", "Elemento", "Emoção", "Caverna", "Imagem", "Mito", "Fantástico"]
        rodadasDokiDoki = 0
        botcli3 = True
        podeesss = 0
        nHPum3 = 0
        nHPum1 = 0
        nHPum2 = 0
        pont_Filo_Aris3 = 0
        pont_PLATAO_3 = 0
        pont_HP = 0
        palavras_1 = ""
        palavras_2 = ""
        palavras_3 = ""
        palavras_4 = ""
        palavras_5s = ""
        palavras_6 = ""
        palavras_7 = ""
        palavras_8 = ""
        palavras_9 = ""
        palavras_10 = ""
        quem_Doki_Doki = ""
        fHPrase = "Escolha uma palavra para compor seu soneto"
        aaa =[]
        bbb = []
        ccc = []
        ddd = []
        eees = []
        fff = []
        ggg = []
        hhh = []
        iii = []
        jjj = []
        sHPcore= 0

        lista_novaaa =[]
        aaa =renpy.random.sample(lista_HP_1, 5)
        palavras_1 = aaa[nHPum1]
        bbb = renpy.random.sample(lista_HP_2, 5)
        palavras_2 = bbb[nHPum1]
        ccc = renpy.random.sample(lista_HP_3, 5)
        palavras_3 = ccc[nHPum1]
        ddd = renpy.random.sample(lista_HP_4, 5)
        palavras_4 = ddd[nHPum1]
        eees = renpy.random.sample(listaFiloA2, 5)
        palavras_5s = eees[nHPum1]
        fff = renpy.random.sample(listaFiloA, 5)
        palavras_6 = fff[nHPum1]
        ggg = renpy.random.sample(listaFiloA3, 5)
        palavras_7 = ggg[nHPum1]
        hhh = renpy.random.sample(lista_PLATAO_3, 5)
        palavras_8 = hhh[nHPum1]
        iii = renpy.random.sample(lista_PLATAO_1, 5)
        palavras_9 = iii[nHPum1]
        jjj = renpy.random.sample(lista_PLATAO_2, 5)
        palavras_10 = jjj[nHPum1]
        sHPcore= nHPum1 + 1
    
    jump Cena1
return




