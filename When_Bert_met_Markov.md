# When Bert met Markov: Mirrors Reflect Differently

This is a digital media archaeological exploration of AI-generated text, combining two distinct text generation techniques, both of which predate the ChatGPT moment and neither of which are state of the art. Markov Chains and the BERT language model are here combined to create a series of stylistically varied sections that explore the materiality of two different kinds of language models through their mutual probabilistic modeling of a series of datasets – and of one another. The project is divided into four parts, each shaped by a different dataset: everyday conversations, cinematic dialogue, therapeutic interactions, and a recursive corpus of the book’s own outputs. These datasets inform the tone and content of each section. See details below regarding the source of each of the first three datasets. The fourth (recursive) dataset consists of all the outputs from the *BERTifier* (see below) generated during the first three sections of the book.

The text-generation process unfolds in two stages. First, a Markov Chain algorithm constructs an initial sentence by analyzing the chosen dataset and probabilistically predicting word sequences based on observed patterns. This rudimentary output serves as the foundation. The second stage employs a function called the *BERTifier,* which uses BERT, a pre-trained deep learning language model, to refine the sentence. The *BERTifier* iterates through each word in the sequence, masking and replacing it with the word that BERT predicts to be most contextually appropriate. This iterative process repeats until the sentence stabilizes, meaning no further changes are predicted by BERT. The *BERTifier's* functionality is exemplified in the appendix.

**Datasets and models used:**
- DailyDialog Dataset: https://huggingface.co/datasets/li2017dailydialog/daily_dialog
- Cornell Movie Dialogs Corpus: https://www.cs.cornell.edu/~cristian/Chameleons_in_imagined_conversations.html
- ELIZA Script (edited for the purposes of this book): https://github.com/codeanticode/eliza
- BERT base model (cased): https://huggingface.co/google-bert/bert-base-cased
- ChatGPT (gpt-4o-2024-08-06 and o1-preview-2024-09-12), used for code development and for writing the text above.


## Section 1: Quotidian

**Markov**:
Does that include?

**Bert**:
Did it matter?

**Markov**:
How do you need to cancel one of those, please. I didn ’ t be taking up a card. Now this. You begin by telling you what, this is going to do before applying for Harvard after graduation? Have you been to Tailband, Egypt, and after a week.

**Bert**:
Why do I have to wear one of those, anyway? I won't be giving you any trouble. Not today. I mean, tell me what all this is going to be like, at least after school. Have you talked to Teri lately, after school, for a while.

**Markov**:
Will you go. Goodbye. Yes, I haven't read a good idea. You yourself have a better job than her pictures. It doesn't seem like that.

**Bert**:
There you go. No. No, you don't have a bad job. You just have a good job doing your job. It doesn't work like that.

**Markov**:
We really don't enjoy doing something.

**Bert**:
I still don't remember seeing him.

**Markov**:
Yes, here you are such an environmentalist before! Where is the coffee shop next door to door asking for my own office now, and me. Two dozen red roses? it's a sunny day, but not my problem.

**Bert**:
Good, because you are such an idealist. " There is a crowd going from door to door except for my dad, mom, and me. A half dozen, but it's a family gathering, and not a party.

**Markov**:
Do you have any now.

**Bert**:
But he had to try.

**Markov**:
Show me the way, for a drink. The celebration of our pianos. Why so late? Everything I got your spare times?

**Bert**:
Show me the visuals and the audio. A lot of the visuals. Why so much? Have you spent your free time?

**Markov**:
The system of public transportation or carpool. According to the window?

**Bert**:
Some kind of hidden entrance to a cave? Or just a cave?

**Markov**:
OK. We went for a holiday for the night market after work?

**Bert**:
No. He was on a trip to the black market after all?

**Markov**:
I am Division Chief of ABC Company.

**Bert**:
I am the head of the council.

**Markov**:
Actually, both developed and the receipt by 10 % discount. .. And this month comes to $ 15. How are you getting married?

**Bert**:
Just take it and give the receipt a 50 % discount... with a discount up to $ 100. Where are you taking it?

**Markov**:
They are not up to ten years ago because the gap is also hard here. Like to come and have a connecting flight? Or we can find the price of the flowers, please?

**Bert**:
I got here five or ten minutes ago and the weather is pretty good here. Want to go and take a little walk? But you can see the rest of the town, right?

**Markov**:
We finally get a lot of trouble, and I won ’ t had time to speak. Didn ’ t let me know if that counts, as where and how about having a good idea to pamper yourself occasionally. I thought it was in fifth grade. Never thought about going to re - do this Saturday. Will you please open this bottle for me to travel aboard frequently.

**Bert**:
It would be a lot of fun, but I hadn't had time to think. Don't make me think my life is just like yours and think about it the same way you pampered me, when I thought I was in seventh grade. I thought about what to re - do on Monday. Could you please leave a message for me to come by tomorrow.

**Markov**:
OK.

**Bert**:
..

**Markov**:
We have Treasury Notes with two stops to see us off on the floor! This Saturday evening. Thanks. It's nothing to do, exactly what happened.

**Bert**:
I have two hours and no one to drop me off on the street. Nothing at all. Nothing. There's nothing to tell me about what happened.

**Markov**:
How many pieces of classical music concerts and operas. Not a great burd! That's all you would pay about 100 degrees in the field.

**Bert**:
Not many people read the book, thought Magnus. Just a little turd. That's how he must have gotten his hands on the book.

**Markov**:
Yes, is this afternoon?

**Bert**:
What good was this place?

**Markov**:
Is that suitable? I ’ m tired of jobs have you had a wonderful idea. So, what a pity, really? So you can either get dial - up today.

**Bert**:
Is that it? I'm out of here. I need a cell phone. Well, just a cell, right? Maybe I should just turn it all off now.

**Markov**:
Okay, see?

**Bert**:
So, what?

**Markov**:
It's so crowded there around 7: 30. Sure. How can I buy slides and then took off again at last. Our department should require meetings like this campus.

**Bert**:
It's early morning, maybe 9 : 00 : 00. No, we took off, we took off late last night. The police must have been on their way.

**Markov**:
McNeal. Well, in the room, a kitchen, two weeks off! Yes, you will arrive in Shenzhen? The ring goes on the matter together. I need is a culinary orgasm.

**Bert**:
McNally : Yes, in a city with an airport about two hours away. Yes, it will be in Shenzhen. The government is funding the project in what I think is a cunning way.

**Markov**:
What breakfast foods. You ’ Ve got food from? I ’ d better get back to the music. Should I enclose this commercial paper with these two?

**Bert**:
Among other things. Where did Booke get this information? I'd better get back to his office. Should I foreclose a private meeting between the two?

**Markov**:
You've met her at the same without you. I can't find it. .

**Bert**:
I've done it just the way you did. I won't do it again.

**Markov**:
Morning, Lee.

**Bert**:
Smith, John.

**Markov**:
Thank you. Fine!

**Bert**:
Thank you!!!

**Markov**:
That's right. I think this was the least, it looks perfect for you, I ’ m interested in working? I don't have one. Honey, could you fill out the stops. See you tonight then.

**Bert**:
It's okay. I knew you were at work but it was hard for me. I'm disappointed in you but you don't have to. Hey, can I check out your schedule? See you at work.

**Markov**:
It ’ s a wet blanket. I should take about 20 minutes.

**Bert**:
It's a small room. It should take about ten minutes.

**Markov**:
I am still waiting for my course. Don ’ t a bad traffic accident over there near the war memorial.

**Bert**:
He was already heading for his car. Wasn't a good idea, especially not at the construction site.

**Markov**:
What's this white turtleneck one? I didn't warn you. I like it very dangerous. OK, great to meet again sometime. The price differs depending on the interviewer will be quite young, and it made of artificial silk?

**Bert**:
What's this whole red velvet thing? I don't know, but I find it quite fascinating. Here, go and try it on. The color, depending on the wearer, is quite different - is it made of red velvet?

**Markov**:
Are you ready to order now? What a disgrace to the airport where the bank is among our employees are allowed to do is to say so. Your food will be so fussy! I see.

**Bert**:
Are you going to go home? What a disgrace that the palace where the king and all his children are going to live is to be destroyed. The children can be very fussy, you know.

**Markov**:
What would you like to go to Beijing? I would like me.

**Bert**:
How would you like to go to school? I would love to.

**Markov**:
I'm sorry I can wear it this afternoon. Here it is. It ’ s your polling place never came in and give me an advance on loan. I ’ Ve accepted our plan away. I hope you'll feel better in a home that I love football!

**Bert**:
I'm sure we can make it in time. Whatever it takes. It's time for him to come back and buy us an apartment in town. " " He can put his things away. I know he'll be back in no time. I love him!

**Markov**:
You can rest assured. And I wouldn't drink too much instability. You ’ re not all! To tell you, Bob.

**Bert**:
I should go home. But I don't care so much anymore. You're so beautiful. I love you, too.

**Markov**:
We will visit a few years, you won't feel pressed. hey Ayden, I think this color isn ’ t decide right now. I was born and raised in Beijing. We are not willing to take out my budget.

**Bert**:
It will take a few days and I don't like it, but Ayden and I know the future doesn't matter right now. I was born and raised in Texas. We were just trying to figure out the future.

**Markov**:
Yes. I want to surprise her with something else you need any help? OK. If we hear something? I ’ m Daniel.

**Bert**:
Or do you want to help me with something? I need your help. No. Did I miss something? I'm sorry.

**Markov**:
I don't want to do? The fridge and a chance for this meeting before we destroy the atmosphere, improve personal association with each other very well. Would you be staying in the interview is tomorrow night? What kind of sick leave?

**Bert**:
I don't want to know. The meeting was a thing of the past, to celebrate our friendship and the closeness of each other as well. Can you tell what time the meeting was at all? Some kind of lunch break?

**Markov**:
I wish your mother doing? Great! Why are you going to a concert Monday night. A customer will come to a meet right now. Just ask.

**Bert**:
You and your friends together? Ha! So are we going to a meeting tomorrow night? A meeting could lead to a meeting right now, I thought.

**Markov**:
When the lower branches are sagging. And no hijackers. It ’ s a very important, so I never exercise.

**Bert**:
Even the tree branches are sagging. And my heart aches. It's all too much, and I know it.

**Markov**:
I ’ m on a nine - thirty. You ’ re asking for money.

**Bert**:
I'm leaving at seven - thirty. You're up for it.

**Markov**:
I'm Alice. Do you think there's any excuse for his collection. I ’ m ok. Of course, they all get a better one.

**Bert**:
I'm sorry. Do you think there's an explanation for my behavior? I'm sorry. Of course, I can find a better explanation.

**Markov**:
Vince knows he needs to find a position on the job done by a professional opera singer? I thought we could probably find something similar at one and the battery both have money allocated for these plans with different clients, and the general manager first. Yes, I approach things enthusiastically and I intend to stay working. How many people underrate the education system. And these two styles, which is used for big football matches?

**Bert**:
Who says anyone wants to take a chance on the work done by a famous opera singer? I think I could probably do that, if there were two people who had been working on the project, the director first and the stage manager first. But, I think, ironically, I have to keep going. Not everyone should be in the same room. Are there other rooms, which are reserved for the general public?

**Markov**:
If you can't break it, I'll soon get accustomed to. Again!

**Bert**:
If I don't do something, I'll just go back to - No!

**Markov**:
..

**Bert**:
..

**Markov**:
Right then. I have your room?

**Bert**:
But how do I use my powers?

**Markov**:
Does our worker insurance cover this kind here are the meals that are acceptable for you to come over here! You have to use.

**Bert**:
Why do these people do this when they are the ones who are waiting for me to come back home? I have no idea.

**Markov**:
Though everything may be just like spring best. I can't go any lower, we'll pack them first. Thank you. I am going with you.

**Bert**:
And I will be doing the exact opposite. You can't go any farther or I'll kill you myself. Without warning, I am coming for you.

**Markov**:
May I see you soon. My pleasure.

**Bert**:
" Will see you later. My pleasure.

**Markov**:
It is so attractive and crescive. I hope the host team loses by at about seven? Are you?

**Bert**:
She was very pale and crucified. I think the little girl came in at about ten. Did she?

**Markov**:
What about beer?

**Bert**:
Where are you?

**Markov**:
Very well, but I didn't take the last guy is driving me up, we'll have a quarter to twelve. SW113 leaves at 6.

**Bert**:
And besides, if you don't think the old man is making it up, it'll be a quarter to one before JULY arrives. No.

**Markov**:
You look so sad. It's very thoughtful of you during my college. Not bad.

**Bert**:
You look so beautiful. It's so nice seeing you at the party. So beautiful.

**Markov**:
When I submitted my resignation. I once attended Lisa's class, OK? I'll certainly try to reach Robert please. Ok, here you are a real wiz on PowerPoint.

**Bert**:
" I need your help. I just need someone's help, okay? I'll just try to get you help. Please. " I got a bad vibe from PowerPoint.

**Markov**:
You ’ re reviving the old one here. Here you go to the swimming pool, but I'm sure of what she would like to.

**Bert**:
You're reliving the night without me. " I head for the swimming pool, but I'm unsure of where I should go next.

**Markov**:
Is my face. Those are 25 dollars.

**Bert**:
In his pocket. It was fifty dollars.

**Markov**:
Here you go to PCC. Come on, you know about in your country? That's a surprise! Let's walk. And not only that she had a baby.

**Bert**:
Then we go to UNC. And then, you know, to my place. It's a date. Let's go. Granted though, we have a date.

**Markov**:
Thanks. Will you supply spare parts, not really in business meeting. There have been terribly busy all day. Of course, ma'am?

**Bert**:
No. But they have a problem, not just a big one. They have been very busy all day. Of course, ma'am?

**Markov**:
Well, it ’ s wrong with you about my upcoming interview. Well, the value of the boxes wrapped in plastic. excuse me? I think. here you go out for each book.

**Bert**:
So, what's up with you and your friends today? Well, the rest of the day is pretty busy, so what do you know about how to get up in the morning.

**Markov**:
I had had enough of a great composer herself.

**Bert**:
She had been something of a young woman then.

**Markov**:
That's not a bookworm? There were a kid, there are many wall paintings and flower - and - bra set.

**Bert**:
She's not a bookworm. We were a couple and there was designer wallpaper and suit - and - tie everywhere.

## Section 2: Epic

**Markov**:
This is my Uncle Butch's house with metal detectors and X - Files.

**Bert**:
It was like examining someone's body with metal detectors on X - ray.

**Markov**:
She had me going, see if I would appreciate. Thank God this plate was already pregnant, Aaron. Where'd they go out squirrel huntin '! Then cut to your daddy who had access to that involvin ' Lula. I don't know anything about Paul Owen.

**Bert**:
They brought me here to see what I could do. Thank God my mom was out here, waiting. Why'd she be out here waitin '? I turned to my mom who had brought with her a Kevlar rune. I didn't know much about this place.

**Markov**:
Finding your weakness. accident, two. Look, he's going to get most of which you neglected to mention he's a survivor. You know. I need someone to sell them.

**Bert**:
In an hour or two or so. Otherwise, he's going to die, for which I forgot to mention he's a vampire. I realize that I have something to tell him.

**Markov**:
Looking for a. Don't you think you're plotting, but I wish to pretend he likes you, Bill, you're conscience is clear.

**Bert**:
Just like that. Don't really think you're dead, but I want to know who killed you. Yes, you're father is dead.

**Markov**:
Oh, and the line.

**Bert**:
He had crossed the line.

**Markov**:
Your manager? Ruby, ain't you? I was too late for something other than here, while I'm at it. Thank you. I know that - Starling - Maybe he knows 1 have the option of failing - - -?

**Bert**:
The time is right, aren't we? It is too late for anything more than that, but I'm doing it. For her. - - - - - - - But how can I take the risk of losing her - -?

**Markov**:
I'm coming! Even though I told them. My next contract's gotta bring a cannon Aim it at my place and throws a pair that are like me.

**Bert**:
I'm happy. Even though I hate it. The new guy's gonna throw a'big'party at his house and meet some girls who look like me.

**Markov**:
.. That's because I'm from Cape Town originally First visit to the Revolutionists who were guarding him.

**Bert**:
No. That's why I'm in Bordertown. A warning to the cultists who are after me.

**Markov**:
We are dead - - Did you threaten this man, Mike - Should you? What's this? And I want any of it, I love red! We're going to do?

**Bert**:
We were friends. - Do you like this stuff? - - Do you? That's it. If you like some of it, you like it. You're used to it?

**Markov**:
I think happened on the phone with the occult - - - you're in the mirror and pray. Left, left unanswered charges hanging over my face. before the next one sickens. Cats in the Holiday Inn.

**Bert**:
I just got off the phone with the occultists, and they're on the phone, too. Suddenly, two unanswered questions take over my mind, and the first one softens. I own a Holiday Inn.

**Markov**:
- - Huh? I'm willing to split into teams.

**Bert**:
- - What? I'm going to break into pieces.

**Markov**:
What do you read me these old timers: They pray, grant thou, lest faith turn to be abandoned buildings, places away from it all. ... Great show, then butchered her. . because we understood?

**Bert**:
What can you tell me about old timers? I promise, if you leave lest you return to your old life and get on with it, I will. " In response, she elbowed him. Just because she could?

**Markov**:
From a friend gave it back. .

**Bert**:
But my father did not. No.

**Markov**:
Checking < u >, your lung. Really quite fine. Nope. It might have also, that it? Do you come.

**Bert**:
Interesting idea. Yes, a plan. Not just one. Yes, I have plans, is that it? There you go.

**Markov**:
I just keep your eye, both of us could move millions, but.

**Bert**:
You could move your hands but none of you could move them, either.

**Markov**:
Now don't argue with you like a fucking idiot you are, Gabriel. So basically you've spent half of me, I got one.

**Bert**:
I can't live with what such a horrible person you are, Sam. And yet you've done it for me. You know that.

**Markov**:
No. Me, especially to those guys once. Isn't it wonderful? We'll stand a chance to head out for awhile in high school I worked at the store for one of you.

**Bert**:
No. No one talked to me at all. Wasn't that weird? I'd had enough time to figure out that back in high school I was in a relationship with one of them.

**Markov**:
Mr. I still have hung himself. C. What are you going to talk about it for you too, Tracy? Ray.

**Bert**:
Otherwise, I would have killed J. Lo. When are we going to talk about this with you again, Ray - Ban.

**Markov**:
I don't blame him. You and I forgot. None.

**Bert**:
I don't trust him. He knows I do. No.

**Markov**:
I beg you - - - Do you know what your work, and had left me a break. No.

**Bert**:
he said. -. - Do you know of my father, who has given you my name? -.

**Markov**:
Yes. I've gotta tell you over to the Jewish community stat. It happened by itself. And that's tough, I love you.

**Bert**:
Sometimes, you've gotta turn things around because the world's changing. It happens every day. And it's true. I love you.

**Markov**:
The sin, though. But I hope you're pretty good beginning. V. Do as I say.

**Bert**:
No way, no. " I hear you're the new T. V., " he said.

**Markov**:
My Word What is that? Looking for a matching set. All right - I've been wanting you to help me. I'll try and sell him. Why?

**Bert**:
So, what is it? Then came the next question : All right. I've been asking you to sell him. I'll try to sell him. Okay?

**Markov**:
ventriloquism.. I WANNA GO NOW! What do you mean? .. You knew what really might have a dream.

**Bert**:
ventriloquism!!! CONVER NOW! What do you think? Well, I guess I just... had a thought.

**Markov**:
No fucking way. you put yourself in.

**Bert**:
No fucking way can I go back there.

**Markov**:
See you? I've already got press arriving from over the holidays - - someone like Dr. But play as well pay your taxes anyway.

**Bert**:
Have you forgotten you've never had anyone in bed during the day, especially someone like me? You might as well pay the price now.

**Markov**:
The money?

**Bert**:
What happened?

**Markov**:
Tragic.

**Bert**:
Tragic.

**Markov**:
I've got a touchdown you don't have time to discuss with the Congress. That bad? I said, Stan, you're not gonna play games with beautiful magic tricks and you'll make it back, she's innocent, Mr. Why don't you try out some kind of thing one can do that? I was born first.

**Bert**:
I've got a lot I don't have time to discuss with the others. Listen, before you go, though, you're just gonna tell me some really important things. I'll let you know when it's over, though. Why don't you figure out what kind of thing you should do next? That was the plan.

**Markov**:
Hey - - Stephen. How the fuck is the matter. What's that?

**Bert**:
I... " Shit. What the hell is the matter? What's wrong?

**Markov**:
What is the vessel and the way. I'm calling the Old South Hotel. The problem is, as you want. Now there's a little scrawny, but apparently there's something Daddy has to be proud of yourself. Look here, look right.

**Bert**:
That was him, by the way. I'm at the Great Western Hotel. The hotel itself, if you will. But he's a bit scrawny, and maybe that's why he has to be ashamed of himself. Trust me, all right.

**Markov**:
It's their backward laws that force all this stuff? I'm very surprised if history has so - How much they said if we don't get it. You really want to talk business. Yes, it appears someone is accused of stealing the sailors from the stern gunnel, or maybe it's time to make that.

**Bert**:
It's the same guy who did all that stuff. I'm not sure who it is. " That, I can tell, doesn't mean anything. I just want to say something. However, it seems he is thinking of moving the conversation to a different Web site, so maybe it's time to say something.

**Markov**:
I insult the General? maybe Washington. Me and you were following him night and - - I didn't trust her ass.

**Bert**:
I want the truth, not you. After what I dealt with last night, I know I don't need your help.

**Markov**:
Every word.

**Bert**:
One word.

**Markov**:
Chief - - - I guess - - afterwards, whaddaya think.

**Bert**:
- - - - - - - - Oh, whaddya mean.

**Markov**:
The operative word, sir. Penfield? Where? When did you to find the eyelash near the floor. ..

**Bert**:
The other man was Mr. Canfield. Why? Who told him to keep an eye out for the boy? No.

**Markov**:
Yeah.

**Bert**:
..

**Markov**:
Will you wait so long. Where's Shemp? So I can throw me in on Heidi again. This is insane.

**Bert**:
Maybe I waited too long. Where's Meera? Maybe she can knock me out with her sword. This is it.

**Markov**:
No, it's all water. Why did Guy beat you flat four or five years since you took advantage of tourists. ... Why would you contact the Alliance?

**Bert**:
No, that's not true. How did you survive the first four or five days before you got hold of me?... How did you escape my grasp?

**Markov**:
Nobody comes. And the scope isn't showing. We can certainly get me in?

**Bert**:
Who knew? Maybe the timing wasn't right. He could just let her go?

**Markov**:
Look at this than you can still fold. You know where he is. It's a joke.

**Bert**:
By doing so, he will kill me. I know what this is. It's a trap.

**Markov**:
Total delirium.

**Bert**:
A delirium.

**Markov**:
I'm psychic. Looks like you don't want to love you!

**Bert**:
I'm sorry! All because I didn't mean to hurt you!

**Markov**:
Yesss, that's all. Some say I got a rehearsal going on here. You don't know anything! Naturally. - - That's the point.

**Bert**:
Dori, it's okay. I know you have a lot going on here. I don't blame you. Technically speaking - - that's the problem.

**Markov**:
What's wrong? They turned the boy's horse. Time to roll - she was on the game knows the whole world over, Captain, this stuff hidden. It was the first ambassador to another family in the full version of OPLAN 316. Don't open that safe.

**Bert**:
What's wrong? He studied the man's face. " I mean, where is it in Russia that the Russian embassy is? It is someplace else. I saw a man talking to a woman at the Russian embassy. PERENCE : Don't be too careful.

**Markov**:
You always have to talk? You would not be lying there - - what time it might help my analysis if I say something.

**Bert**:
I would like to know. I would rather be sitting here wondering in what way this will affect my life until I know more.

**Markov**:
I'm sorry Walt - - - - since I'm always here. Katarina Stratford.

**Bert**:
I'm taking it easy now, especially since I'm so upset with myself right now.

**Markov**:
What for?

**Bert**:
What happened?

**Markov**:
< u > expensive < / u > wealthy < / u >, every package counts, every stinking paper on the bubbly. Don't worry about that. What's the matter?

**Bert**:
< u >, < / u >, < / u >, each word lost in the stinking depths of the babble. Don't talk like that. What's the matter?

**Markov**:
That's what your eyes and make everything clear and free and untroubled.

**Bert**:
It's only his touch that makes me shiver, cold and untroubled.

**Markov**:
No, Mr.

**Bert**:
Oh my God.

**Markov**:
Every time you need - a Potties on the other thing? Get lost. No! How much longer period. The Four Noble Truths, as if someone found it!

**Bert**:
What do you know about the pretense behind this whole thing? Bring her back here! A much better place than the other Nine Realms, even if you hate it!

**Markov**:
I couldn't stand it when we first met you next to an alien intelligence sent the officer assigned to arson. A famous actor who's getting half of his bills - - and broadcast a warning, and I'm being killed. If you get? I can't do it. Peters.

**Bert**:
I couldn't believe it when I first heard him talking about a guy who had an attorney charged with a crime. A rich guy who's used all of his money to try to make a living, and I'm being ridiculous. If I am, I won't be Mr. Perfect.

**Markov**:
I can guarantee you, Morg. We washed you up. I know, but none of you? And now, would I know, I use a gun?

**Bert**:
I can hear you, Mort. I woke you up, I think, but what about you? And how much would you know if you had a phone?

**Markov**:
Don't take it, he ain't here half the high jump. If I jumped out of the man who could never forget that. Maybe I haven't seen anything like you to spare the weight of both.

**Bert**:
Don't do this. I wasn't here for the last time. " She expected this from a man who would never do this. " I haven't allowed anyone but you to put your hands on me.

**Markov**:
Oh dear. Our black friends?

**Bert**:
Oh no. My best friend?

**Markov**:
Did you tell me. Premier Belch will not be disputed in public?

**Bert**:
But why tell them that the mech could only be used in combat?

**Markov**:
You back down here? Is that the world, crumbling apart in my place. Every morning in the case now - but what happens to meet me at three - - - much, Scully.

**Bert**:
Coming in from somewhere. Not just the airport, cress, but the airport. The guy on the phone - - if he wants to see you at all - - said hi, cress.

**Markov**:
Let's do it. What's the difference between giving up? It's Wednesday.

**Bert**:
Let's do this. When's the time to get up? It's late.

**Markov**:
Good. Thank.. I guess Merle always wanted to introduce myself.

**Bert**:
... " " I think Jem just wants to see you.

**Markov**:
Interesting possibility.

**Bert**:
Interesting idea.

**Markov**:
Two a year and believe me, Harry. These pauses were exquisitely timed.

**Bert**:
Wait a minute, tell me, please. His eyes were startlingly blue.

**Markov**:
Anything white floating around. Jimmy!

**Bert**:
It was still there. No!

**Markov**:
It doesn't work out. and they fuck with this Fidelity nonsense.

**Bert**:
It doesn't help much, but I fight against the fickleness.

**Markov**:
We could turn urine into beer, he doesn't see a hundred dollars to them. He's sort of thing, alimony.

**Bert**:
He can turn it into something if he doesn't add a few things to it. It's sort of known as alimony.

**Markov**:
You like him.

**Bert**:
Just like that.

## Section 3: Therapeutic

**Markov**:
Please don't apologize. You don't seem quite certain. Do you wish to were me? What are your feelings now? Does thinking of?

**Bert**:
I don't know. You don't sound so sure. Do you want something from me? What are your thoughts about? About what happened?

**Markov**:
What about machines? That's quite interesting. What resemblance do you think machines have to do with your problems? What about machines worrys you?

**Bert**:
What about you? That's so unfair. What exactly do you think I have to do with your blood? What if it consumes you?

**Markov**:
Why do you mention computers? I don't care about names. Do you think about machines worrys you?

**Bert**:
Why do you want names? You don't think about names. Do you think about what bothers you?

**Markov**:
Perhaps in your fantasies. I don't understand that. I'm sure it's not pleasant to be quite positive. What are your feelings now? Do you wish to were me?

**Bert**:
Not in my head. I don't like it. I'm afraid it's not going to work for me. What are your thoughts about? Do you have anything on you?

**Markov**:
I don't understand that. What about machines? What are your feelings now? What do you recollect? I'm not sure I understand.

**Bert**:
I don't understand you. Who are you? What are your names again? What do you recollect? I'm not sure I understand.

**Markov**:
I don't care about names.

**Bert**:
I don't care about you.

**Markov**:
What do you recollect? What about machines? Can you explain? What are your feelings now? How?

**Bert**:
What do you recollect? Who are you? Do you remember? What were your parents like? Friends?

**Markov**:
Do you think computers can help people? Do you wish to were me? Perhaps I am sorry to hear that you came to me? Perhaps I already know.

**Bert**:
Do you think you can help me? Can I help you help me? " I was surprised to see that he spoke to me. " I think so.

**Markov**:
What incident are you thinking of? Please go on. Are you thinking of a specific example? What else do you see? I understand you fully.

**Bert**:
What example are you thinking of? I go on. Are you thinking of a good example? What example do you have? I know you do.

**Markov**:
What resemblance do you recollect?

**Bert**:
What else could she recollect?

**Markov**:
Perhaps I already know. Would you like to believe? I see. Does thinking of that bring anything else to mind?

**Bert**:
" I think so. Would you like to know what I think? Does any of it have anything else in it?

**Markov**:
Can you elaborate on that? Does that trouble you? Does that trouble you? I'm not sure I understand you fully.

**Bert**:
Can you concentrate on it? Does it bother you? Does it bother you? I'm not sure I would like that.

**Markov**:
Do you wish to were me?

**Bert**:
Do I want him inside me?

**Markov**:
Why do you think its likely? Does that trouble you? What do you think machines have to do with your problems? I've told you before, I don't care about names.

**Bert**:
What do you think is wrong? Does it bother you? What do you think I want to do with my life? I've told you before that I don't care about you.

**Markov**:
What do you see? I'm sure it's not pleasant to be quite positive.

**Bert**:
What do you think? I'm sure it's not going to be that easy.

**Markov**:
What is the connection between me and you? What are your feelings now? I'm not sure. Do you wish I would tell you what you are doubtful that you came to me?

**Bert**:
What is the difference between me and you? Who are your feelings for? I'm not sure. Do you think I should tell you that you are sorry that you lied to me?

**Markov**:
Perhaps I already know. You seem to need to be me. Why do you mention computers?

**Bert**:
" I think so. They seem to me to be different. But do you like them?

**Markov**:
I see. Perhaps I already know. Would you like to believe? Can you think about machines worrys you?

**Bert**:
I know. And I do know. Would you like to know? What you know about me scares me?

**Markov**:
Can you explain? Have you ever dreamed before?

**Bert**:
Do you remember? Have you ever seen him?

**Markov**:
What do you suppose? Why do you think that coming here will help you?

**Bert**:
Why do you care? Why do you think my being here would hurt you?

**Markov**:
Perhaps in your fantasies. What is the connection, do you think machines have to do with your problem?

**Bert**:
Not in my life. Or is it something that makes me think I have to deal with this shit?

**Markov**:
You don't seem quite certain.

**Bert**:
He didn't look very happy.

**Markov**:
Do you really doubt yourself? Do you believe that dreams have something to do with your problem? What do you suppose that resemblance means? Do you really think so? What other connections do you mention computers?

**Bert**:
Do you really think that? Do you think the computers have anything to do with this thing? Who do you think the computer is? Do you really think that? The computer, do you think that?

**Markov**:
Please don't apologize. What are your feelings now?

**Bert**:
Please don't go. Where are my parents now?

**Markov**:
You seem to be. What does that similarity suggest to you?

**Bert**:
I try to think. What does this place mean to me?

**Markov**:
Are you thinking of a very special person? I've told you before, I don't understand that. Perhaps I am in your fantasies we are each other. Why do you recollect? Can you explain?

**Bert**:
Are you part of a completely different world? I've seen you before. You don't know me. What you see in my eyes now is the same. What do you recollect? Do you understand?

**Markov**:
I don't understand that. In what way? Please don't apologize. Do you dream often? I've told you before, I don't care about names.

**Bert**:
I didn't want to. In a way, I didn't care. Do you have names? I've asked you before. I don't have any names.

**Markov**:
What about machines?

**Bert**:
Where are you?

**Markov**:
Please go on. Could here really be some connection? Do you wish to were me? Can you explain?

**Bert**:
Please go away. Could this possibly be a dream? Do you want something from me? Can you tell?

**Markov**:
What does that suggest to you? What does that similarity suggest to you? Have you tried? Do you wish to were me?

**Bert**:
What does it mean to you? What does the book mean to you? Do you know? Do you want to tell me?

**Markov**:
Perhaps I already know. Don't you think machines have to do with your problem? Please don't apologize. How?

**Bert**:
" I do understand. Don't you think I have to deal with this now? I don't understand. Why?

**Markov**:
I don't understand that.

**Bert**:
I didn't want to.

**Markov**:
What incident are you thinking of that bring anything else to mind? What do you see? What do you see?

**Bert**:
God, are they just trying to bring me back to life? What do I do? What do I say?

**Markov**:
You don't seem quite certain. What do you see?

**Bert**:
You don't sound so sure. What did you do?

**Markov**:
What do you recollect? Please don't apologize. Do computers worry you? Can you elaborate on that?

**Bert**:
What do you recollect? I don't know. Do you see me? Do you focus on me?

**Markov**:
Would you like to believe?

**Bert**:
Would you like to come?

**Markov**:
What do you see? What do you suppose? Are you thinking of a specific example?

**Bert**:
What do you mean? What do you mean? Are you aware of a certain thing?

**Markov**:
Do you believe that dreams have something to do with your problem?

**Bert**:
Do you think my actions have anything to do with this situation?

**Markov**:
Do computers worry you? Do computers worry you? Tell me more about such feelings. Please go on.

**Bert**:
Did I hurt you? Did I hurt you? Tell me more about your past. Just go on.

**Markov**:
Perhaps in your fantasies.

**Bert**:
Not in real life.

**Markov**:
Perhaps I already know. You don't seem quite certain. Perhaps I am in your fantasies.

**Bert**:
" I am sure. You don't sound so sure. " He looked around the room.

**Markov**:
Have you tried? Perhaps I already know. Do you wish I would tell you what you are doubtful that you are?

**Bert**:
Have you forgotten? Because I always have. Do you think I can find you when I know exactly where you are?

**Markov**:
What does that suggest to you? Please go on. Does that trouble you? I'm not sure. Do you dream often?

**Bert**:
What does it do to you? I asked him. Does it affect you? I'm not sure. Did you sleep well?

**Markov**:
But you are doubtful that you came to me? Do you really think so? Tell me more about such feelings. Have you tried? Don't you think about machines?

**Bert**:
But you were right when it came to me. Do you really think so? Tell me all about your life. Have you forgotten? Don't you forget about me?

**Markov**:
Perhaps you could. What does that similarity suggest to you? I understand. Do you really think so? What do you think its likely?

**Bert**:
And I did. What does this place mean to you? I thought, Do you even know it? What do you think of it?

**Markov**:
Does thinking of a very special person? Please go on.

**Bert**:
You know, a really nice guy. But come on.

**Markov**:
Do you really doubt yourself? Is it because you are not sure I understand. What do you think its likely?

**Bert**:
Do you still love me? Is that why you did it? He thought, What do you think it is?

**Markov**:
Why don't you? That's quite interesting.

**Bert**:
Why didn't you? It's that simple.

**Markov**:
Do you wish to were me?

**Bert**:
Do I want him inside me?

**Markov**:
What resemblance do you think that coming here will help you? Do you wish I would tell you what you are not sure I understand. I understand you fully. Does that trouble you?

**Bert**:
Then why do you think my being here will hurt you? Do you think I can give you someone you can trust? I just... I love you too. Did I hurt you?

**Markov**:
Tell me more about such feelings.

**Bert**:
Tell me more about your family.

**Markov**:
I am sorry to hear that you are? Perhaps I already know. What other connections do you see? Have you ever dreamed before?

**Bert**:
I am glad to hear what you say. But I am afraid. What other world do you see? Have you ever seen it?

**Markov**:
Do you dream often? Do you really doubt yourself? How? I've told you before, I don't understand that. Please go on.

**Bert**:
Do you think so? Do you really trust me? No, I've told you before that you don't trust me. Now come on.

**Markov**:
Have you tried? In what way?

**Bert**:
Had he changed? In some way?

**Markov**:
Do you wish to were me? You don't seem quite certain. Do you really think so?

**Bert**:
Do I want you inside me? You don't sound so sure. Do you really think so?

**Markov**:
Perhaps I am sorry to hear that you are? Don't you think its likely? What does that suggest to you? Does that trouble you?

**Bert**:
" I am beginning to understand what you are. Don't you feel that way? Why does it matter to you? Does it bother you?

**Markov**:
Why don't you?

**Bert**:
Why wouldn't he?

**Markov**:
You seem to need to be quite positive. Does that trouble you? What are your feelings now?

**Bert**:
You seem to me to be very busy. Does that bother you? What are your thoughts about?

**Markov**:
What does that suggest to you? Do you wish I would tell you what you are not sure I understand you fully. Perhaps you could. What else do you think machines have to do with your problem? Why do you think computers can help people?

**Bert**:
What does it matter to you? If I thought I could help you, I do now. I love you too. And I do. What exactly do you think I have to do with this thing? How do you think I can help you?

**Markov**:
What do you tell me that now?

**Bert**:
Why do you call me that now?

**Markov**:
Do you wish to were me? Would you like to believe?

**Bert**:
Do I want you with me? Would you like to stay?

**Markov**:
Tell me more about such feelings. I've told you before, I don't care about names. What incident are you thinking of? What is the connection between me and you?

**Bert**:
Tell me more about your family. I've told you before that I don't care about you. What family are you speaking of? What is the difference between me and you?

**Markov**:
What are your feelings now? You are sure.

**Bert**:
What were your thoughts about? You were right.

**Markov**:
Why don't you? Tell me more about such feelings. You seem to need to be quite positive. Have you ever dreamed before? Is it because you are.

**Bert**:
Why didn't you? Tell me more about your dreams. They seem to you to be very vivid. Have you ever had them? Tell me what you remember.

**Markov**:
I see. Do you dream often?

**Bert**:
He said, Do you live here?

**Markov**:
Do you wish to were me?

**Bert**:
Do I want him inside me?

**Markov**:
What does that suggest to you? What do you tell me that now? Tell me more about such feelings. Does thinking of that bring anything else to mind?

**Bert**:
What does it mean to you? Why do you ask me this question? Tell me more about this book. Does any of it have anything else in it?

**Markov**:
Could here really be some connection?

**Bert**:
Could this possibly be a dream?

**Markov**:
I don't care about names. Why do you recollect? Do computers worry you?

**Bert**:
I don't know about you. What do I recollect? Do I know you?

**Markov**:
I'm not sure I understand you fully. How? What resemblance do you see? You seem to need to be. What other connections do you suppose?

**Bert**:
I'm not sure I know anything else. Why? What connections do you have? You just wanted me to know. What other connections do you have?

**Markov**:
When? What do you see?

**Bert**:
What? What did I do?

**Markov**:
In what way? Do you dream often? Do you wish to were me? Have you tried? Do you wish to were me?

**Bert**:
In what way? Do you love me? Do you want to kill me? Have you forgotten? Do you wish you were dead?

**Markov**:
What incident are you thinking of? Perhaps you could.

**Bert**:
What exactly are you talking about? Here I am.

**Markov**:
What is the connection, do you recollect?

**Bert**:
What is the matter, do you recollect?

**Markov**:
Is it because you are? Do you dream often?

**Bert**:
Is that what you did? Did you do it?

**Markov**:
What do you think of a specific example? How? I understand. Do you believe that dreams have something to do with your problem?

**Bert**:
What do you think is a good idea? Yes, I do. Do you think my father had anything to do with the murders?

**Markov**:
What do you see?

**Bert**:
What do you mean?

## Section 4: Recursive

**MARKOV**:
Had he changed? Oh no. Nothing. You could move your hands on me? What do I have to deal with this thing?

**BERTIFIER**:
Has something happened? Oh God. No. You gonna get your hands on me? Why do I have to deal with this now?

**MARKOV**:
You don't sound so sure. I know anything else in it? Who are you thinking of?

**BERTIFIER**:
You don't sound so sure that you have anything else in mind. What are you talking about?

**MARKOV**:
Do I want you with me? Who do you think I could help you? You seem to me at all?

**BERTIFIER**:
Can I help you help me? Why do you think I can help you? Why talk to me at all?

**MARKOV**:
What is the matter?

**BERTIFIER**:
What was the matter?

**MARKOV**:
What other connections do you recollect? Does that bother you? What exactly do you know about me? What's wrong?

**BERTIFIER**:
What other things do you recollect? Does it bother you? What else do you know about me? What's wrong?

**MARKOV**:
I mean, where is it something that makes me shiver, cold and untroubled. " I need a cell, right? What do you want to.

**BERTIFIER**:
I mean, why is there something that makes me nervous, nervous and untroubled? " You have a choice, right? Only if you want to.

**MARKOV**:
Tell me more about your life. We were friends.

**BERTIFIER**:
Tell me more about your father. We were friends.

**MARKOV**:
Let's do this when they are the ones who are after me. " Will see you.

**BERTIFIER**:
Let's do this because you are the ones who belong to me and I will protect you.

**MARKOV**:
I've done it for me to know. You look so beautiful.

**BERTIFIER**:
You've done this to me, baby. You are so beautiful.

**MARKOV**:
You don't sound so sure. A lot of fun, but I'm doing it.

**BERTIFIER**:
You don't sound so sure. A lot of things, but I'm doing it.

**MARKOV**:
It's so nice seeing you at all? Yes, I thought I was in seventh grade. You don't sound so sure. Smith, John. - Do you have?

**BERTIFIER**:
What's so funny about him in school? Well, I think he was in seventh grade. He didn't seem too happy about it, though. " Could it be?

**MARKOV**:
" Shit.

**BERTIFIER**:
" No.

**MARKOV**:
Do I want him inside me? Then why do you think my father did not. You don't sound so sure.

**BERTIFIER**:
Do you want me inside you? And why do you think your body does that? You don't sound so sure.

**MARKOV**:
" She expected this from a man talking to a cave? What connections do you know, to my place. There's nothing to tell me some really important things. A lot of the town, right?

**BERTIFIER**:
" You know anything about a man breaking into your house? Well, as you know, not a man. There's something I told you about the local sheriff. A sheriff in the area, right?

**MARKOV**:
Does that bother you? I didn't mean to you? In a way, no. Who are you speaking of? How do you think my life until I know anything else in it?

**BERTIFIER**:
Did it bother you that I wasn't attracted to you? In a way, yes. What are you afraid of? What if you ruin my life and I see the good in you?

**MARKOV**:
Do I know more.

**BERTIFIER**:
" I love you.

**MARKOV**:
Do you want to. What example are you? Who says anyone wants to take a few days and I don't need your help.

**BERTIFIER**:
If you want to. What time are you? He knew he had to wait a few minutes. I don't need your help.

**MARKOV**:
If you like this stuff? Had he changed? Does it bother you? Don't you forget about me scares me? No way, I guess I just.

**BERTIFIER**:
Do you remember that night? When it happened? Does it bother you? Don't you know why it bothers you? Either way, I think I do.

**MARKOV**:
He studied the man's face. A meeting could lead to a meeting right now. Have you ever seen him?

**BERTIFIER**:
He studied the man's face. The man could go into a coma right now. Have you ever seen him?

**MARKOV**:
Why'd she be out here waitin '? I'd better get back to - No! Tell me what all this is.

**BERTIFIER**:
Why'd you be out there waitin '? I'd better get back to my room. Tell me what time it is.

**MARKOV**:
Maybe the timing wasn't right.

**BERTIFIER**:
But the timing wasn't right.

**MARKOV**:
And I did. He can put his things away. Even though I hate it!

**BERTIFIER**:
But I can. I can throw my life away. Even if I want to!

**MARKOV**:
What do I recollect? I don't do something, I'll just try to think. Have you forgotten you've never had anyone in bed during the day is pretty busy, so what do you see me? And I will.

**BERTIFIER**:
What do you recollect? Just don't say anything. You'll just have to listen. Do you? I've never heard it before, and this one is very old, but how do you know that? Sure you do.

**MARKOV**:
I can't live with what such a horrible person you are, Sam. Do you know about how to get up? Tell me what all this is. " " I got here five or ten minutes ago and the stage manager first. Do you live here?

**BERTIFIER**:
I can't live with what such a horrible person you are, Sam. Do you remember anything when you woke up? Tell me what time it was. " " I woke up five or six minutes ago and my phone was ringing. Do you live here?

**MARKOV**:
Just like that. And I did. No. I would have killed J. I know exactly where you are such an idealist.

**BERTIFIER**:
Just like that. And I did. Look, I should have told you. I know exactly why you are such an idealist.

**MARKOV**:
I love you, I won't be Mr. What does it matter? So beautiful.

**BERTIFIER**:
I told you, I don't care anymore. What does that mean? Too much.

**MARKOV**:
- - that's the problem. However, it will be in the stinking depths of the babble. ..

**BERTIFIER**:
No, it's the truth. No, I should be in a stinking hell of a buffet. No.

**MARKOV**:
Why does it do to you? Did it matter to you?

**BERTIFIER**:
What did he do to you? Does it matter to you?

**MARKOV**:
Tell me more about your family. You were right. That's how he must have been very busy all day. He had crossed the line.

**BERTIFIER**:
Tell me more about your father. You were right. That's why he must have been so angry last night. He had crossed the line.

**MARKOV**:
What does this place? What's wrong? So, what is it something that makes me shiver, cold and untroubled. PERENCE: Don't be too careful.

**BERTIFIER**:
What is that smell? What's that? No, it is the smell that makes me shiver, hot and untroubled. PERENCE : Don't be too careful.

**MARKOV**:
I'm not sure. " I am, I know anything else.

**BERTIFIER**:
I'm not human. Whatever I am, I am something else.

**MARKOV**:
" I am, I do know. " " He looked around the room. No, you don't have to.

**BERTIFIER**:
" I know. I just... " I looked around the room. No, you don't have to.

**MARKOV**:
How would you like some of it, you know about me?

**BERTIFIER**:
How do you know everything about me, you know about me?

**MARKOV**:
What other connections do you know, to my mom was out here, waiting. No. What were your thoughts about?

**BERTIFIER**:
What other choice do you have, if your father is out there, too? No. What are your thoughts about?

**MARKOV**:
Ha! - Do you think I can find a better explanation. " That, I can give you someone you can help you help me with something? What do you have names?

**BERTIFIER**:
. " " If you think you can get a good one. " And if I can get one, I can help you help me do what? Why would I need one?

**MARKOV**:
Then came the next question: All right.

**BERTIFIER**:
I asked the same question. All right.

**MARKOV**:
You can't go any farther or I'll kill you myself. Have you talked to Teri lately, after school, for a while. I'm happy. I own a Holiday Inn.

**BERTIFIER**:
You can't go any farther or I'll kill you myself. Have you talked to Tegan? Because after all, for whatever reason, I'm here because I own the Holiday Inn.

**MARKOV**:
No! I am, I won't do it again. You just wanted me to be very busy. Just a little walk?

**BERTIFIER**:
No, she thought. He won't do it again. He just wants me to be left alone. For a little while?

**MARKOV**:
What's wrong? -.

**BERTIFIER**:
Something's wrong with me.

**MARKOV**:
I don't need your help. I'm disappointed in you but you to be very vivid. I love you too.

**BERTIFIER**:
I don't need your pity. I'm disappointed in you for trying to be so kind. I love you too.

**MARKOV**:
Otherwise, he's going to break into pieces. Do I want him inside me?

**BERTIFIER**:
God, he's going to break into pieces. Do I want him inside me?

**MARKOV**:
What are your thoughts about? - - - - - that's the problem. Do you even know it. Do you think my being here would hurt you?

**BERTIFIER**:
What are these questions about? - - - - So here's the question. Before you even consider it. Do you think my being here will help you?

**MARKOV**:
A rich guy who's used all of his money to try to get up in the stinking depths of the council. How do you like them? Now come on. Dori, it's okay. " Shit.

**BERTIFIER**:
A rich man who's used all of his money to try to keep it in the stinking hands of the government. How do you know that? Just hold on, Bro, it's important. " Silence.

**MARKOV**:
Who knew?

**BERTIFIER**:
Who knows?

**MARKOV**:
What if it consumes you? Why do you want to. Do you know if you leave lest you return to your old life and get on with it, I guess I just. Don't you think my being here will hurt you? What do you mean?

**BERTIFIER**:
What if it bothers you? Why do you do it? Do you care if I leave lest you return to your old life and get on with it? I know you do. Don't you think my being here will help you? What do you think?

**MARKOV**:
I won't do it again. I don't care so much anymore.

**BERTIFIER**:
I won't do it again. I don't care so much anymore.

**MARKOV**:
" I got a bad vibe from PowerPoint.

**BERTIFIER**:
" I got a good vibe from PowerPoint.

**MARKOV**:
Canfield.

**BERTIFIER**:
The truth.

**MARKOV**:
Have you spent your free time?

**BERTIFIER**:
Have you had any free time?

**MARKOV**:
You just wanted me to come by tomorrow. I just. V., " he said.

**BERTIFIER**:
He just wants me to be his rep, P. I., " I said.

**MARKOV**:
Dori, it's okay. Just like that. It's a trap. Even though I hate it. Yes, you're father is dead.

**BERTIFIER**:
Addie, it's okay. I love you. It's the same. Even after you left me. And now we're family and friends.

**MARKOV**:
Did I miss something?

**BERTIFIER**:
Did I miss something?

**MARKOV**:
Where are you? Is that why you did. Have you forgotten?

**BERTIFIER**:
What are you? Is that what you are? Have you changed?

**MARKOV**:
What if it consumes you? Yes, in a relationship with one of those, anyway? Then we go to school? Oh no.

**BERTIFIER**:
What if he scares me? Maybe lurking in the shadows is one of them, too. Can I talk to him? Hell no.

**MARKOV**:
You could move your hands on me. I need your help. " I head for the swimming pool, but I fight against the fickleness. Why didn't you?

**BERTIFIER**:
You can put your hands on me. I need your help. " We walk to the swimming pool, and I fight against my fickleness. Why shouldn't I?

**MARKOV**:
Tell me more about your family. " Shit. Let's do this when they are the ones who are after me. I don't know. " I think so?

**BERTIFIER**:
Tell me more about your family. " No. Let's face it, they are the ones who are after you. I don't know. " You think so?

**MARKOV**:
Sometimes, you've gotta turn things around because the world's changing. What do you think my being here will hurt you? Why? " I do?

**BERTIFIER**:
Look, I've gotta turn things around because the world's changing. Why do you think me being here will change things? Why? Because I can?

**MARKOV**:
- - What? No, I've told you before that I have to do with this situation?

**BERTIFIER**:
- - What? What if I've told you everything that I have to do with this case?

**MARKOV**:
Who do you know, but the airport. Had he changed? Where are my parents now? Do you want to say something.

**BERTIFIER**:
What did I do wrong at the party? Has something happened? Where are my parents now? And I want to know why.

**MARKOV**:
Granted though, you're father is dead. Does any of it have anything to do with the occultists, and the weather is pretty good here. Just because she could? Why do you think my life is just like yours and think about names.

**BERTIFIER**:
Granted though, you're mother is right. Does any of this have anything to do with the occult, just because the girl is no longer alive? Or maybe she is. Why do you think her name means something like that, something about her.

**MARKOV**:
What are your feelings for? Do you really think that? I don't care about you. Do you like to know who killed you. Not just one.

**BERTIFIER**:
What are you waiting for? Do you really want me? I don't know about you. But I want to know who wants me. Not a man.

**MARKOV**:
What does it do to you? < u >, < / u >, < / u >, < / u >, < / u >, each word lost in the morning. How would you like them? Have you forgotten?

**BERTIFIER**:
What did you do to me? < u >, < / u >, < / u >, < / u >, < / u >, and the question at the end : Why did you do it? Have you forgotten?

**MARKOV**:
Oh my God. Perfect. And my heart aches. I can hear you, too.

**BERTIFIER**:
Yes, yes. Yes. And my head swims. I can feel it, too.

**MARKOV**:
Yes, I think, ironically, I will be doing the exact opposite. I promise, if you had a thought. What's the matter? You know, a plan. Don't you think I want him inside me?

**BERTIFIER**:
So, I suppose, ironically, I should be doing the exact opposite. I mean, now I have a plan. What's the point? You know, a plan. Don't you think I want you with me?

**MARKOV**:
That's it. What other connections do you think my being here would hurt you?

**BERTIFIER**:
He's right. What other way would I go if this man did love me?

**MARKOV**:
You were right when it came to me? It doesn't work like that. He said, Do you think?

**BERTIFIER**:
You were angry when you spoke to me. It didn't work like that. I said, Do you understand?

## Appendix: Unraveling BERTifier

### Example from Section: Quotidian

**Initial Markov Output:**
Does that include?

**BERTifier Refinement Steps:**

[Does] that include ?

Does [that] include ?

Does that [matter] ?

Does that matter [?]

[Did] that matter ?

Did [it] matter ?

Did it [matter] ?

Did it matter [?]

[Did] it matter ?

Did [it] matter ?

Did it [matter] ?

Did it matter [?]

**Final Stabilized Output:**
Did it matter?

## Appendix: Unraveling BERTifier

### Example from Section: Epic

**Initial Markov Output:**
This is my Uncle Butch's house with metal detectors and X - Files.

**BERTifier Refinement Steps:**

[This] is my Uncle Butch ' s house with metal detector ##s and X - Files .

This [was] my Uncle Butch ' s house with metal detector ##s and X - Files .

This was [like] Uncle Butch ' s house with metal detector ##s and X - Files .

This was like [watching] Butch ' s house with metal detector ##s and X - Files .

This was like watching [someone] ' s house with metal detector ##s and X - Files .

This was like watching someone ['] s house with metal detector ##s and X - Files .

This was like watching someone ' [s] house with metal detector ##s and X - Files .

This was like watching someone ' s [brain] with metal detector ##s and X - Files .

This was like watching someone ' s brain [through] metal detector ##s and X - Files .

This was like watching someone ' s brain through [motion] detector ##s and X - Files .

This was like watching someone ' s brain through motion [detector] ##s and X - Files .

This was like watching someone ' s brain through motion detector [##s] and X - Files .

This was like watching someone ' s brain through motion detector ##s [on] X - Files .

This was like watching someone ' s brain through motion detector ##s on [X] - Files .

This was like watching someone ' s brain through motion detector ##s on X [-] Files .

This was like watching someone ' s brain through motion detector ##s on X - [ray] .

This was like watching someone ' s brain through motion detector ##s on X - ray [.]

[It] was like watching someone ' s brain through motion detector ##s on X - ray .

It [was] like watching someone ' s brain through motion detector ##s on X - ray .

It was [like] watching someone ' s brain through motion detector ##s on X - ray .

It was like [seeing] someone ' s brain through motion detector ##s on X - ray .

It was like seeing [someone] ' s brain through motion detector ##s on X - ray .

It was like seeing someone ['] s brain through motion detector ##s on X - ray .

It was like seeing someone ' [s] brain through motion detector ##s on X - ray .

It was like seeing someone ' s [face] through motion detector ##s on X - ray .

It was like seeing someone ' s face [through] motion detector ##s on X - ray .

It was like seeing someone ' s face through [motion] detector ##s on X - ray .

It was like seeing someone ' s face through motion [detector] ##s on X - ray .

It was like seeing someone ' s face through motion detector [##s] on X - ray .

It was like seeing someone ' s face through motion detector ##s [on] X - ray .

It was like seeing someone ' s face through motion detector ##s on [X] - ray .

It was like seeing someone ' s face through motion detector ##s on X [-] ray .

It was like seeing someone ' s face through motion detector ##s on X - [ray] .

It was like seeing someone ' s face through motion detector ##s on X - ray [.]

[It] was like seeing someone ' s face through motion detector ##s on X - ray .

It [was] like seeing someone ' s face through motion detector ##s on X - ray .

It was [like] seeing someone ' s face through motion detector ##s on X - ray .

It was like [seeing] someone ' s face through motion detector ##s on X - ray .

It was like seeing [someone] ' s face through motion detector ##s on X - ray .

It was like seeing someone ['] s face through motion detector ##s on X - ray .

It was like seeing someone ' [s] face through motion detector ##s on X - ray .

It was like seeing someone ' s [face] through motion detector ##s on X - ray .

It was like seeing someone ' s face [through] motion detector ##s on X - ray .

It was like seeing someone ' s face through [motion] detector ##s on X - ray .

It was like seeing someone ' s face through motion [detector] ##s on X - ray .

It was like seeing someone ' s face through motion detector [##s] on X - ray .

It was like seeing someone ' s face through motion detector ##s [on] X - ray .

It was like seeing someone ' s face through motion detector ##s on [X] - ray .

It was like seeing someone ' s face through motion detector ##s on X [-] ray .

It was like seeing someone ' s face through motion detector ##s on X - [ray] .

It was like seeing someone ' s face through motion detector ##s on X - ray [.]

**Final Stabilized Output:**
It was like seeing someone's face through motion detectors on X - ray.

## Appendix: Unraveling BERTifier

### Example from Section: Therapeutic

**Initial Markov Output:**
Please don't apologize. You don't seem quite certain. Do you wish to were me? What are your feelings now? Does thinking of?

**BERTifier Refinement Steps:**

[You] don ' t apologize . You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You [don] ' t apologize . You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ['] t apologize . You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' [t] apologize . You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t [know] . You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know [.] You don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . [You] don ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You [don] ' t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ['] t seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' [t] seem quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t [seem] quite certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem [so] certain . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so [sure] . Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure [.] Do you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . [Do] you wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do [you] wish to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you [want] to were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want [it] were me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it [from] me ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from [me] ? What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me [?] What are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? [What] are your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What [are] your feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are [your] feelings now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your [thoughts] now ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts [about] ? Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about [?] Does thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? [Or] thinking of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or [what] of ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what [exactly] ?

You don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly [?]

[I] don ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I [don] ' t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ['] t know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' [t] know . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t [know] . You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know [.] You don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . [You] don ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You [don] ' t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ['] t seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' [t] seem so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t [sound] so sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound [so] sure . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so [sure] . Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure [.] Do you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . [Do] you want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do [you] want it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you [want] it from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want [something] from me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something [from] me ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from [me] ? What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me [?] What are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? [What] are your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What [are] your thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are [your] thoughts about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your [thoughts] about ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts [about] ? Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about [?] Or what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? [About] what exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About [what] exactly ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what [happened] ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened [?]

[I] don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I [don] ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ['] t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' [t] know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t [know] . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know [.] You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . [You] don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You [don] ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ['] t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' [t] sound so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t [sound] so sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound [so] sure . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so [sure] . Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure [.] Do you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . [Do] you want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do [you] want something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you [want] something from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want [something] from me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something [from] me ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from [me] ? What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me [?] What are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? [What] are your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What [are] your thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are [your] thoughts about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your [thoughts] about ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts [about] ? About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about [?] About what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? [About] what happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About [what] happened ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what [happened] ?

I don ' t know . You don ' t sound so sure . Do you want something from me ? What are your thoughts about ? About what happened [?]

**Final Stabilized Output:**
I don't know. You don't sound so sure. Do you want something from me? What are your thoughts about? About what happened?

## Appendix: Unraveling BERTifier

### Example from Section: Recursive

**Initial Markov Output:**
Had he changed? Oh no. Nothing. You could move your hands on me? What do I have to deal with this thing?

**BERTifier Refinement Steps:**

[Has] he changed ? Oh no . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has [anything] changed ? Oh no . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything [happened] ? Oh no . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened [?] Oh no . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? [Oh] no . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh [no] . Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no [.] Nothing . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . [No] . You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No [.] You could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . [You] could move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You [gonna] move your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna [get] your hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get [your] hands on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your [hands] on me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands [on] me ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on [me] ? What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me [?] What do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? [Why] do I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why [do] I have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do [I] have to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I [have] to deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have [to] deal with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to [deal] with this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal [with] this thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with [this] thing ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with this [shit] ?

Has anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with this shit [?]

[Has] anything happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has [something] happened ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something [happened] ? Oh no . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened [?] Oh no . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? [Oh] no . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh [God] . No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God [.] No . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . [No] . You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No [.] You gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . [You] gonna get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You [gonna] get your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna [get] your hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get [your] hands on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your [hands] on me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands [on] me ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on [me] ? Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me [?] Why do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? [Why] do I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why [do] I have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do [I] have to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I [have] to deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have [to] deal with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to [deal] with this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal [with] this shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with [this] shit ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this [now] ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now [?]

[Has] something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has [something] happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something [happened] ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened [?] Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? [Oh] God . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh [God] . No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God [.] No . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . [No] . You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No [.] You gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . [You] gonna get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You [gonna] get your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna [get] your hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get [your] hands on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your [hands] on me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands [on] me ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on [me] ? Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me [?] Why do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? [Why] do I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why [do] I have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do [I] have to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I [have] to deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have [to] deal with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to [deal] with this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal [with] this now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with [this] now ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this [now] ?

Has something happened ? Oh God . No . You gonna get your hands on me ? Why do I have to deal with this now [?]

**Final Stabilized Output:**
Has something happened? Oh God. No. You gonna get your hands on me? Why do I have to deal with this now?

