﻿init:
    image boss_office = "boss_office.jpg"
    image office = "office.jpg"
    image office2 = "office2.jpg"
    image black_screen = "black_screen.jpg"
    image boss = "boss.png"
    image clown = "clown.png"
    image rat = "rat.png"
    image radik = "radik.png"
    image snop = "snop.png"

### Запись _something_ обозначает, что надо придумать что-то и вставить сюда

# Определение персонажей игры.
define start_screen = Character(None, kind=nvl)
define oleg = Character('Олег', color = "#8280ff")
define oleg_thoughts = Character('Олег', color = "#2a28be")
define boss = Character('Иван Михайлович', color = "#beffbe")
define clown = Character('Толя', color = "#befff1")
define rat = Character('Сергей', color = "#befff1")
define snop = Character('snoop', color = "#befff1")


# Игра начинается здесь:
label start:

    # Очки отношений
    $ active_points = 0
    $ clown_points = 0
    $ rat_points = 0
    $ worher_points = 0
    $ _x5_points = 0

    play music huefon

    window hide
    centered "Вы ведущий специалист информационной безопасности в крупной фирме, специализирующейся на перевозке грузов. Сегодня к вам обратилось руководство с поручением выявить виновного в утечке важных данных ."
    nvl clear
    centered "Вас, под видом обычного сотрудника, внедряют в отдел, где работает подозреваемый. Вы должны, полагаясь на дедуктивный метод, выявить причастного к сливу данных."
    nvl clear
    centered "От вас зависит дальнейшая судьба всей компании. Приступайте к расследованию."
    nvl clear
    centered "{size=+20}Барнаул, Алтайский край{/size}"
    nvl clear
    centered "{size=+20}11 сентября 2022 года{/size}"
    nvl hide

    ###
    # DAY 1
    ###

    ### Boss office scene
    scene boss_office with fade

    show boss at center with dissolve

    boss "Доброе утро, Олег Евгеньевич."
    boss "Меня зовут Иван Михайлович, и я являюсь руководителем этого отдела. Полагаю, Вас уже примерно ввели в курс дела?"

    oleg "Здравствуйте, Иван Михайлович. Да, меня вкратце посвятили в происходящее."
    oleg "Однако перед тем, как приступить к работе, мне хотелось бы узнать побольше об этом месте и работающих здесь людях."

    boss "Да, конечно. Данный отдел занимается логистикой. Как Вы понимаете, информация, к которой есть доступ у моих сотрудников, крайне важна для компании."
    boss "Именно поэтому Вам необходимо найти виновного в утечке в ближайшее время."
    boss "Всего в этом отделе работает 4 человека, у которых есть доступ к слитой информации. Думаю, стоит вкратце описать Вам каждого из них."

    show boss at left with fade

    show clown at right with dissolve
    boss "Первым в списке подозреваемых находится Анатолий. Довольно веселый и жизнерадостный человек, легок в общении."
    hide clown

    show rat at right with dissolve
    boss "Вторым подозреваемым является Сергей. Имеет весьма неприятный характер, откровенно говоря."
    boss "Пытается выслужиться любыми возможными способам передо мной, часто жалуется на своих коллег."
    hide rat

    show worker at right with dissolve
    boss "Третьим будет Геннадий. Пожалуй, лучший работник в этом отделе. Крайне продуктивен и трудолюбив."
    hide worker

    show active at right with dissolve
    boss "Далее по списку у нас Екатерина. Её можно назвать самым энергичным и социально активным сотрудником."
    boss "Она ответственна за большинство мероприятий по тимбилдингу. Именно благодаря ей, коллектив у нас, за некоторым исключением, довольно дружный."
    hide active

    show boss at center with fade

    boss "Что же, вроде рассказал Вам, Олег Евгеньевич, все, что знал."
    boss "Я руковожу этим отделом не так давно, и поэтому не настолько хорошо знаю своих людей, чтобы делать какие-то выводы самому."
    boss "Но все же, если будут какие-то вопросы, - обращайтесь."
    boss "Прошу также держать меня в курсе событий."
    boss "Однако не стоит бегать ко мне по каждому поводу, иначе Вы вызовете подозрения. Просто заходите ко мне время от времени, чтобы доложить обстановку"
    boss "И не забывайте, Олег Евгеньевич: Вас направили сюда, потому что Вы отлично зарекомендовали себя ранее, и высшее руководство рассчитывает на Вас."
    boss "От Вас зависит не только Ваша собственная репутация, но и репутация всей компании. Если вы выдадите себя, второй попытки уже не будет."
    boss "Поэтому я искренне желаю Вам удачи."

    oleg "Понял, спасибо за наводки, Иван Михайлович. Я понимаю, что время поджимает, поэтому приступлю к работе немедленно."

    boss "Отлично. Тогда вот Вам мой последний совет на сегодня: осмотрите весь отдел, чтобы уметь ориентироваться здесь, и познакомьтесь с каждым из подозреваемых лично."

    oleg "Вас понял, до свидания."

    scene black_screen with fade

    oleg_thoughts "(По всей видимости, это самое серьезное дело, за которое я брался)"
    oleg_thoughts "(Нужно не ударить в грязь лицом)"


    ### Active Scene


    ### Clown scene
    scene office with fade

    oleg_thoughts "(Ладно, теперь надо осмотреться здесь. Пойду-ка я поищу свое рабочее мес...)"

    with vpunch
    with hpunch
    show clown at center with dissolve

    clown "Ох-ох, ну и больно! Не витай в облаках, дружище!"
    clown "Тут все-таки логистический отдел, люди занятые работают. Не чета разгильдяем из главного управления!"

    oleg "Прошу прощения, призадумался тут немного."

    clown "Ничего, бывает. Хэй, да ты, похоже, тот самый новый сотрудник, о котором нам недавно говорили!"
    clown "Приятно познакомиться, меня Толей звать!"

    oleg "Взаимно, Меня Олег зовут. Cегодня мой первый день. Вот, Иван Михайлович проводил мне инструктаж."

    clown "Иван Михайлович любит толкать речи. Он тот еще оратор, этого у него не отнять."
    clown "Ладно, осваивайся тут потихоньку, а мне работать надо. Еще увидимся!"

    oleg "До встречи."
    oleg_thoughts "(Похоже, это был мой первый подозреваемый. И вправду, весьма позитивный человек)"

    hide clown

    ### Rat Scene.
    scene office2 with fade
    oleg_thoughts "(Хорошо, вот и первое знакомство. Теперь уже точно мне сле...)"

    "???" "Только познакомились, а он уже на 'ты'. Какое непрофессиональное поведение. Впрочем, как обычно..."

    oleg_thoughts "(Ну, кто на этот раз?)"

    show rat at center with dissolve

    rat "Моё имя Сергей, будем знакомы."
    rat "К сожалению, большинство сотрудников здесь придерживаются подобного неформального стиля общения."

    menu:
        rat "Как по мне, это пагубно влияет на рабочую атмосферу, Вы не согласны?"
        "Полностью согласен":
            oleg "Эм, да, конечно, это крайне непрофессионально, я полностью с Вами согласен."
            rat "Рад это слышать."
            rat "В этом месте наблюдается критическая нехватка адекватных работников."
            rat "Надеюсь, с Вашим приходом, здесь начнутся перемены."
            oleg "Не переживайте, я не подведу."
            rat "Тогда нам нужно будет как-нибудь обсудить нашу стратегию по повышению профессиональных качеств наших коллег."
            oleg_thoughts "(Только не это...)"
            $ rat_points += 1
        "Не согласен":
            oleg "На самом деле, я не думаю, что это как-то может навредить работе."
            #show rat_angry ?
            rat "Я смотрю, Вы уже пообщались с Екатериной. Подобное отношение как раз в её духе."
            rat "Смею напомнить: платить Вам будут не за пустую болтовню."
            rat "Очень жаль. Я думал, что с Вашим приходом, здесь начнутся перемены."
            oleg_thoughts "(Отлично. Первый день, и я уже успел с кем-то поссориться)"
            $ rat_points -= 1

    rat "Хорошо, не буду больше задерживать, у Вас сегодня много дел."
    rat "До встречи."

    oleg_thoughts "(Мда, начальник дал довольно точную характеристику этого Сергея)"

    show radik
    show snop
    snop "Продолжение следует..."

    return
