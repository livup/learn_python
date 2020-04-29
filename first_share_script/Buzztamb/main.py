system = {'dataform':0, 'looker':0, 'bigquery':0, 'stitch':0}
system_description = {'dataform':'Você tirou: DATAFORM!\n Você é uma pessoa fácil de lidar e simpática com as pessoas ao seu redor. É organizado(a) e gosta de tudo em seu devido lugar, e por isso é ótimo em identificar problemas, apesar de precisar de ajuda para solucioná-los.', 
    'looker':'Você tirou: LOOKER!\n Você é uma pessoa colorida e extravagante! Adora aparecer e dar sua opinião, mesmo quando não formulou muito bem as ideias. Para você, um trabalho bem feito é um trabalho bonito, que brilha o olho da audiência. Seus conhecidos o(a) consideram muito comunicativo e fácil de lidar, apesar de às vezes acharem que te faltam filtros na hora de falar!', 
    'bigquery':'Você tirou: BIG QUERY!\n Você é uma pessoa muito rápida e inteligente para solucionar problemas. Sua inteligência, no entanto, vem com um preço: muitos acham difícil se comunicar com você, apesar do seu vasto conhecimento sobre várias áreas. Outro traço forte da sua personalidade é a independência!', 
    'stitch':'Você tirou: STITCH!\n Você é uma pessoa misteriosa e com poucos amigos. Apesar disso é muito bom e eficiente em tudo o que faz. Mesmo estando quieto o tempo todo e longe das pessoas, é sempre muito ligado nas atualizações do mundo ao seu redor. E se por um lado nunca é o centro das atenções, por outro as pessoas sentem muito sua falta quando não está presente.'
    }
    
questions = {0 : 
    {'pergunta':'Hoje é o dia da sua formatura, você:', 
    'dataform':'1) Coloca uma roupa formal porque é assim que sua família quer',
    'looker':'2) Se veste da forma mais extravagante e colorida que consegue',
    'bigquery':'3) Coloca uma roupa básica e confortável',
    'stitch':'4) Nem vai na festa'},
    1 : 
    {'pergunta':'Hora do aloço na firma, você:', 
    'dataform':'1) Vai onde todo mundo vai, mesmo quando não é seu lugar preferido. O importante é a companhia',
    'bigquery':'2) Vai sempre no mesmo quilo de bom custo-benefício. Você é prático(a) demais para ficar escolhendo o restaurante todos os dias',
    'stitch':'3) Come Liv Up sozinho(a) no seu canto',
    'looker':'4) Usa muitos argumentos para convencer os colegas a irem no seu restaurante preferido'},
    2 : 
    {'pergunta':'Seu chefe aparece com um mega projeto para ensinar dados para os steakholder, você:', 
    'looker':'1) Ajuda em tudo e mais um pouco, mesmo com coisas não tão relevantes para o sucesso do projeto',
    'bigquery':'2) Faz rapidamente um rascunho daquilo que considera ideal para o projeto e passa para o time, sem se preocupar tanto se as pessoas vão entender suas anotações',
    'dataform':'3) Participa do projeto em tarefas conforme te solicitam',
    'stitch':'4) Se faz de desentendido e continua trabalhando nos seus próprios projetos'
    },
    3 : 
    {'pergunta':'Onde seria um primeiro encontro perfeito para você?', 
    'looker':'1) Em algum lugar surpreendente, como uma apresentação de teatro interativa',
    'dataform':'2) Algum lugar bem padrãozinho, como um cinema de shopping',
    'bigquery':'3) Na casa do date. Pra quê perder tempo com idas ao cinema?',
    'stitch':'4) Encontro? Não é comigo...'
    },
    4 : 
    {'pergunta':'O que você está achando da quarentena?', 
    'stitch':'1) Ótimo, finalmente posso ficar a sós!',
    'bigquery':'2) Acho bom, posso focar nos meus estudos e trabalho',
    'dataform':'3) Preferia estar fora, mas pelo menos consigo manter minhas rotinas',
    'looker':'4) AAAAAAAAAA QUERO INTERAÇÕES!!!'
    }
    }
for k in questions:
    a = questions[k]
    aux_dict = {}
    aux = 0
    for v in a:
        print(a[v])
        aux_dict[aux] = v 
        aux = aux + 1
    check = False
    while check == False:
        answer = input()
        if answer.isnumeric():
            answer = int(answer)
            if 0 < answer and answer < 5:
                check = True
    system[aux_dict[answer]] = system[aux_dict[answer]] + 1
biggest_value = 0
for k in system:
    if system[k] > biggest_value:
        biggest_value = system[k]
        biggest_key = k
print(system_description[biggest_key]) 
