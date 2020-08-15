# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sh = Character("SaltHunter")

define ev = Character("Everyone")

define na = Character("Narrator")

define ho = Character("Hokusai")

define ji = Character("Jiro")

define ka = Character("Kazuo")

define oi = Character("Oi")

define phn = Character("Phone")

define pl1 = Character("Police Officer 1")

define pl2 = Character("Police Officer 2")

define sa = Character("Saburo")

define to = Character("Officer Toshizo")

define yu = Character("Yuko")

define Que = Character("???")




# The game starts here.

label start:

    scene bg credits
    with fade

    sh "Please do read till the full ending credits lmao, this should or would be a pet project all conditions are fullfilled"

    sh "This is a kinetic Visual Novel, meaning, no choices, so sit back and enjoy the ride"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    na "The Morning wind Blows. . ."

    "*Police Sirens Blare*"

    ka "I guess i'll Call Jiro."

    phn "brr..."

    ji "Yes, Jiro Here."

    ka "Jiro, You are'nt gonna like this."

    ji "I'm still trying to wake saburo up, what's the matter, Kazuo?"

    ka "It looks like someone was murdered at our HQ."

    ji "What?!"

    na "Phone hangs up."

    ka "Guess i'll ask what's going on."

    ka "Oi, You, Tell me what's shakin."

    pl1 "Apparently, this nutjob thought this area was remote enough to kill someone ay?"

    pl1 "Say, kid, why are you up this early ay?"

    ka "We own the warehouse sir, and. . ."

    "Screching Sfx"

    yu "*Pant* *pant*"

    yu "I Came As soon as Jiro Informed me."

    yu "What the Hell Happened Here? Kazuo?!"

    pl2 "Apparently, one of you nutjobs decided it was a good idea to murder someone in this ol shack over there."

    sa "What The Hell. . ."

    ji "Officer, we have nothing to do with the crime, nor the murder, we just came to the warehouse to check. . ."

    pl1 "We would like to speak to Saburo-San at the station, Would you come with us?"

    sa "Didn't Jiro Tell you? we are'nt related to the crime whatsoever?!"

    pl1 "Oy Mate, ya want yer arse arrested ay?"

    ka "Now now, officer, i'd come in his steed, if that's fine by you."

    ka "Oh, and i'll bring the rest along with me if you dont mind."

    pl1 "Shouldve done that a long time ago ey mate?"

    ka "*sighs* Why did it have to come to this"

    scene bg police station
    with fade
    show eileen happy

    Que "Hello You four, you must be the guys from the warehouse."

    Que "I'll be borrowing this young man for a while if you do'nt mind, you three can wait at reception."

    sa "Make it quick."

    Que "With pleasure, now young man, this way please."

    scene bg interrogation room
    with fade
    show eileen happy

    Que "Good Morning, My Name is Toshizo, That's Officer Toshizo to you."

    to "Don't Fret, We will do this interrogation to cover our bases, now."

    to "Give me your name, age, and occupation."

    ka ". . ."

    to "What's wrong, young man?"

    ka "Kazuo, Shiraga Kazuo, 18, painter."

    to "Mmhm, Allright Mr Shiraga, I got a few questions i found at the scene and a few general questions, do you consent?"

    ka "I consent."

    to "Allright, Now, Mr Shiraga, where were you when the crime occured, at approximately 4AM?"

    ka "I was at home, sleeping, I arrived at the scene of the crime at 5AM."

    to "Do you know the victim of the murder, his name is Izuka, Daisuke Izuka."

    ka "Haven't got a clue officer."

    to "Any idea why you might be the target of this attack?"

    ka "My guess is that it's because we are talent users."

    to "Talent Users? Don't worry, you got a workplace permit right?"

    ka "We do have a permit as talent users to use that place as our place of business."

    to "Then you don't need to worry."

    to "Aight, that should be everything so far, if we get more information, we shall contact you and your friends."

    scene bg police station
    with fade
    show eileen happy

    na "After that, the group went to a convenience store."

    scene bg convenience store
    with fade
    show eileen happy

    ka "Finally, i'm done with that ordeal."

    sa "tch, why does this shit happen to us specifically."

    ji "The world is twisted, Saburo."

    yu "I'm suprised that someone had the capacity to commit a murder like that."

    sa "At the very least, we should discuss this with someone."

    ji "How about this, we go back to my place and see if we have someone to talk about this."

    ka "It's Better than nothing, at least."

    ji "Then it's settled, let's head over after breakfast."

    scene bg jiro_room
    with fade
    show eileen happy

    ev ". . ."

    ji "I was about to clean this up, i swear."

    ji "It's just that Saburo decided to have fun, and do that Throwing himself through paper act again."

    sa "Ey Bastard!"

    sa "I told you months ago i wanted to try that again when i moved in."

    yu "Pfft... Jiro, At least the last piece Saburo did saved our finances."

    ji "*Sighs*"

    ji "Yeah, you're right, Now, what's our next best move?"

    ka "For one, we need to contact our clients about the situation."

    ji "Well, yeah, That's kind of given, but no."

    ji "Right now, we need someone who has a better grasp on the issue than us."

    yu "What about the katushikas?"

    sa "What about them?"

    sa "I thought we are going to let the police do their thing?"

    ka "The police often look down on cases involving talent users, they're not reliable."

    ka "Also, uncle Hokusai was the one who trained our talents, It'd make sense that he might have information on the issue."

    sa "Tch, Fine."

    ji "*nods*"

    phn "Brrr....Brrr..."

    ji "Hello?"

    oi "Jiro! I Saw the news!, Murder?"

    ji "Yeah, is your dad up, we might visit in a bit."

    oi "Not yet, but i'll tell him that you guys are coming over, allright?"

    ji "We'll be there in fifteen."

    "*hangs up*"

    ji "Aight guys, Next Stop, Hokusai's House!"

    scene bg hokusaihouse
    with fade
    show eileen happy

    oi "Four of you okay?"

    ji "As good as  we can be."

    ji "Oi, Don't Worry too much about us."

    scene bg hokusailvroom
    with fade
    show eileen happy

    ho "*waves* Ah it's you four."

    ho "Oi told me there was a murder at your headquarters, I'm sorry that it happened."

    sa "Don't worry uncle hokusai."

    sa "The police said that they would give information if they come up with anything."

    ho "Though from what i saw in the news, it dosent seem like any ordinary murder..."

    ho "A Talent user must be after the four of you."

    sa "And why are you so confident about that?"

    ho "I know at least normal people do not turn murder into art, or at least, normal people don't."

    ji "*Raises hand*"

    ji "Is there anything you can do to help us with the current predicament uncle hokusai?"

    ho "No, sadly."

    ho "However, i may know someone who might be able to help, his name is Rembrandt."

    ho "He's someone i met a while ago who was part of a detective agency and trained a bit with me."

    ho "I could try contacting the detective agency if needed."

    sa "Whoa, Hold on."

    sa "We're going to involve foreign private investigators? are you kidding me?!"

    yu "We have to clear our name Saburo."

    yu "I know it's not exactly ideal, but you have to understand that rome was not built in a day."

    ji "What Yuko Said. Saburo, I get that this is not exactly what you wanted."

    ji "But at the very least, there are more professional people involved in this right?"

    sa "Jiro, i get you, but our finances are barely keeping us afloat."

    ho "*Ahem*"

    ho "Don't worry about finances, I know his boss, i can work something out with him."

    ji "*pats saburo's back*"

    ji "It's Allright Saburo."

    ji "Relax, Aight?"

    sa "I guess, now that i think about it."

    ji "Good!"

    ho "I'll call the guys at mercurius."

    ho "In the meantime, here's some cash, go buy yourselves some drinks with oi."

    ev "Aight!"

    # Insert Transition Here. . .

    scene bg conveniencestore
    with fade
    show eileen happy

    "At the convenience store."

    sa ". . ."

    oi "C'mon, Saburo, usually you'd get upset when people tease you like this."

    sa "i..i just dont want to allright?!"

    ji "Relax Saburo, you got us."

    ev "*Laughs*"

    scene bg conveniencestore
    with fade
    show eileen happy

    sa "So, What about Rembrandt?"

    oi "He's a very nice guy."

    oi "He Also looks like a more handsome Saburo, let's just say."

    sa "Yeah, bet he can't do tricks like i do."

    ji "Relax Saburo, no one's got your charm."

    ji "*smirks*"

    sa "You're lucky that murder is illegal."

    ev "*Laughs*"

    na "At 2PM they returned to the hokusai residence."

    scene bg hokusaihouse
    with fade
    show eileen happy

    ho "I've Got Great News!"

    sa "Spill the beans Uncle Hokusai."

    ho "Rembrandt's boss said that its fine that we don't pay a fine."

    ho "Since i've helped him on a case a few months back, Rembrandt is coming in a few days."

    ev "Aight!"

    ho "I want you all to stay till rembrandt comes over, in case something happens."

    ka "Aight, this ought to be fun."

    ji "Yes! another stay at uncle Hokusai's place!"

    sa "i'd prefer if i stayed at home instead."

    ji "If you don't agree to Uncle Hokusai's terms, i have the key to my house y'know."

    sa "tch, i guess i'd have to stay here then."

    ho "Then it's settled y'all, pack your bags and come back safe, i'll prepare the rooms for y'all."

    ev "Allright Uncle Hokusai!"

    na "And then they stayed at Hokusai's Residence, untill rembrandt comes."

    "End Of Act 1"





    # Insert Transition Here. . .
    scene credits
    with fade

    sh "Disclaimer, all that is here is a placeholder, please do add assets, or so help me."

    sh "Do note, i only have barely enough to sustain my photosynthesis."

    sh "Disclaimer, i do not know how to make quotation marks, i have to relearn that again."

    sh "Do by all means Edit Script, and do put a note to what needs improv, it should be an after corona thing."

    sh "Just tell me which ones are edited by using the comments function (#function)"

    sh "I'm against L2D VN's and assets if you ask me lmao."

    sh "I Tried making the policemen australian, how did that work out? ay mate?"

    sh "Do note that this is not final translation/render, so please do help me"

    sh "Please Support Delight Works And Fate Grand Order, so they rerun another illya event"

    sh "This VN is brought to you by these sponsors: Delight works and Nasu."

    sh "I want illya. . ."

    sh "Abigail Williams is damn cute. . ."





    # This ends the game.

    return
