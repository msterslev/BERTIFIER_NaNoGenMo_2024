---
documentclass: book
classoption: oneside
fontsize: 11pt
title: "When Bert met Markov"
subtitle: "Mirrors Reflect Differently"
author: "Malthe Stavning Erslev"
header-includes: |
   \usepackage{xurl}
   \usepackage{hyperref}
   \hypersetup{breaklinks=true, urlcolor=blue, linkcolor=blue}
   \usepackage{emptypage}
   \usepackage{fancyhdr}
   \pagestyle{fancy}
   \fancyhf{}
   \fancyhead[L]{\textbf{WHEN BERT MET MARKOV}}
   \fancyhead[R]{\leftmark}
   \fancyfoot[C]{\thepage}
   \renewcommand{\UrlFont}{\small\ttfamily}
---

# BERTIFIER adaptation for NaNoGenMo 2024
\thispagestyle{empty}

This is a digital media archaeological exploration of AI-generated text, combining two distinct text generation techniques, both of which predate the ChatGPT moment and neither of which are state of the art. Markov Chains and the BERT language model are here combined to create a series of stylistically varied sections that explore the materiality of two different kinds of language models through their mutual probabilistic modeling of a series of datasets – and of one another. The project is divided into four parts, each shaped by a different dataset: everyday conversations, cinematic dialogue, therapeutic interactions, and a recursive corpus of the book’s own outputs. These datasets inform the tone and content of each section. See details below regarding the source of each of the first three datasets. The fourth (recursive) dataset consists of all the outputs from the *BERTifier* (see below) generated during the first three sections of the book.

The text-generation process unfolds in two stages. First, a Markov Chain algorithm constructs an initial sentence by analyzing the chosen dataset and probabilistically predicting word sequences based on observed patterns. This rudimentary output serves as the foundation. The second stage employs a function called the *BERTifier,* which uses BERT, a pre-trained deep learning language model, to refine the sentence. The *BERTifier* iterates through each word in the sequence, masking and replacing it with the word that BERT predicts to be most contextually appropriate. This iterative process repeats until the sentence stabilizes, meaning no further changes are predicted by BERT. The *BERTifier's* functionality is exemplified in the appendix.

**Datasets and models used:**

- DailyDialog Dataset: \url{https://huggingface.co/datasets/li2017dailydialog/daily_dialog}

- Cornell Movie Dialogs Corpus: \url{https://www.cs.cornell.edu/~cristian/Chameleons\_in\_imagined\_conversations.html}

- ELIZA Script (edited for the purposes of this book): \url{https://github.com/codeanticode/eliza}

- BERT base model (cased): \url{https://huggingface.co/google-bert/bert-base-cased}

- ChatGPT (gpt-4o-2024-08-06 and o1-preview-2024-09-12), used for code development and for writing the text above.

_This project is part of a larger research project, BERTIFIER, which focuses on practice-based ways to perform digital media archaeoloy of langujage models, particularly BERT._

\chapter{Section 1: Quotidian}
\thispagestyle{empty}

**Markov**:
Let's make ready, you can find it quiet. Making coffee is often over 40 ° C.

**Bert**:
Let's get warm so we can get really warm. The temperature is just over 30 degrees C.

**Markov**:
If you need a hand to someone with an acceptance? Yeah, look over there. The problem is now.

**Bert**:
Can you extend your hand to me as an invitation? Please, come over here. This place is beautiful.

**Markov**:
Have you seen the movie is hilarious.

**Bert**:
" I find your comment rather hilarious.

**Markov**:
Excuse me. I have been interrupted all the time? Ok, we'll always be very convenient.

**Bert**:
Believe me, I have been here all this time. Anyway, it'll all be very interesting.

**Markov**:
Or maybe I'll try it myself. How did he say?

**Bert**:
Or maybe he'd do it again. What did he want?

**Markov**:
I have to pay in 60 days. Yes, of course they are often for parents and I enjoyed it.

**Bert**:
I have to leave in two days. Well, of course you are welcome here, and you know it.

**Markov**:
Here is the draft contract says that he would probably have a three - week vacation periods. So you must first learn how to use the credit card company will provide a layoff notice or proof of salary do you really did a wonderful evening. Certainly! You may select which ever you ’ ll show you how to use.

**Bert**:
There is no money and so far you will only have two two - week vacations. If you do not know how to spend the money your employer will check your payroll, as evidence of how long you have lived a good life. Me : You will see how much I'll teach you how to cook.

**Markov**:
How much is this damage is minor.

**Bert**:
Not anywhere in the world, anyway.

**Markov**:
it will cost a nickel, sir. that is very high quality. Good afternoon, ma'am, they'll say that? Sorry. Informal clothes like sports very much.

**Bert**:
It would be a pleasure, sir, it is of excellent quality. Good evening, ma'am, I'd like that. Mr. Hollis seems to like you very much.

**Markov**:
How about this red wine and just a baby girl! I ’ Ve decorated the Christmas package they sent it in with him last week. I guess I didn't like them now. Any other discomfort? Please put it into the slot at the menu.

**Bert**:
How about some hot chocolate and then a hot shower? " " I just left a note. I gave them back to you last night. I guess I don't need them anymore. Any more questions? I put them in a drawer with a pen.

**Markov**:
That ’ ll take them? I have a cup of tea in our departments. I suppose it could have presentations on the Internet Well, I am employed satisfactorily. May I have to decide.

**Bert**:
I've got it. I have a cup of coffee in my hand and I know I should put it on the table now that I am working satisfactorily. But I have to go.

**Markov**:
Here's my VISA. Can I help you? What ’ s too good. How beautiful the flower is! Does the class.

**Bert**:
It's from Delia. Can I help you? It's so beautiful! How beautiful this one is! From my mother.

**Markov**:
Thanks very much. I think we should play the piano for his driver and, well.

**Bert**:
Thanks so much. I think you should play this game with the kids and enjoy it.

**Markov**:
Jared, of course! It's the end of the two and a team, hoping they will leave without me? Have you injured your tooth been bothering you? Hi, is that our site. I ’ ll just check.

**Bert**:
Yes, of course. That's the plan for now, but the rest of you guys will come with me. Have you seen the mugger with him? Please, get in the car. I'll be fine.

**Markov**:
Tickets for that permit is thirty dollars on the tv stations for showing popular kinds of things do you have to check these sunglasses are! .. Totally. ..

**Bert**:
TJ turned on the TV, then turned on the tv. " How many pairs of shoes do you have to buy? They are... expensive. But still.

**Markov**:
What do you have any seats available by the burglar. OK! 5 % and a focus of the TV that your knowledge and to deal with? I don't buy your own business. I ’ d only make vegetarian dishes.

**Bert**:
Why do you want the money coming from a burglary warrant of $ 500, which the owner of the property under your control has to deal with? You won't mind your own business. You'll only eat vegetarian food.

**Markov**:
Of course. He ’ s not an easy conversation. I want 20 hundred bills and computing freight costs, dear! Could you help me.

**Bert**:
Of course. It's not an easy task. I have a few things in the other room, too. Can you help me.

**Markov**:
But I am up to 100 RIB, and so in large groups. I know what produce is? I ’ Ve been watching soap operas? Do you get? Well, they're making a mistake, you got everything.

**Bert**:
" We were talking about watching FOX with more than a few people. You know how it is. " " Most people get into soap operas. If they want. Look, you're making a mistake, you know that.

**Markov**:
I assume there'd be more than $ 1, 000 Euros worth of work, which is empty. I could have been watching that man down in the church, then, why? I ’ ll keep that in L. And you?

**Bert**:
I think there'll be more than $ 100, 000 winnings ahead of us, which is good. You guys have fun with that guy over at the casino over there, right? I'll do that, too. Shall we?

**Markov**:
No, I usually go to the contract? It seems they will be perfect, though. Ok. How lucky you didn't return my camera out.

**Bert**:
Or should I just stick to the plan? Which means I should be going, too. No. No. I can't get the words out.

**Markov**:
We can fix things. Thank you for help, we just got this outfit? too.

**Bert**:
I can do this. Thank you for everything. I just need an hour, please.

**Markov**:
Actually, would you do exercise everyday, your credibility and the internet from any hotspot as well as the others later. It drove my mom crazy!

**Bert**:
And how did you get away with stealing the car and stealing money from the hotspot as well as the bank account? You drive my mother crazy!

**Markov**:
OK, I'll be waiting for you to dinner with us? I just forget it. Haven't seen you in a different way. Does the test skips a lot to us. we can consider it a try.

**Bert**:
So, who'll be waiting for you for dinner with me? I really like you. Haven't liked you in a long time. But this conversation means a lot to me. I should give it a try.

**Markov**:
You have to pay a commission of 4 %. Would you get the best for you.

**Bert**:
You seem to have a score of 100 %. Now I have an answer for you.

**Markov**:
Yeah? You can park? Hello, this letter to Japan?

**Bert**:
So, what was it? Like, a trip to Europe?

**Markov**:
Five for eighty - seven. Lucy, I ’ m really looking forward to your performance today. Yes, I know. Certainly. Who finances the magazine, which I'm sure that's high enough so that it was hot outside.

**Bert**:
Message number twenty - one : Hey, I'm really looking forward to the party tonight. Really, I am. Mr. Stone has the door unlocked. I'm glad it's open, now that it is dark outside.

**Markov**:
Well, what do you say is that I owe you one that is smaller than May. Yes, the president of their superior quality, as I succeed, but I don ’ t have onions on my Accord. The ATM will not get good equipment. Yeah? I'm interested in if you would be officiating.

**Bert**:
So, what can I say, if it was you, it was me, right? But not vice versa, a good thing, because you are right. I don't like interruptions in the Accords. The ATF does not have much time. Anyway, I'm here, and I will be officiating.

**Markov**:
Have you forgotten? About 2 days. What day are the best employees!

**Bert**:
Did you?????! Your father had the wrong idea!

**Markov**:
So I hear it. That one there. You are kidding me! What about water pollution?

**Bert**:
" I got it! No surprise there! You are kidding me! What about the money?

**Markov**:
Any time.

**Bert**:
This time.

**Markov**:
It's always warm? Well, I just dropped in that big a deal. Wow! They are grown - ups.

**Bert**:
It's that simple. Well, we can live with that for a while. Ha! We are grown - ups.

**Markov**:
I want to post my pictures tomorrow? Is the production manager. Maybe so. 100 US dollars?

**Bert**:
You want to see a movie tomorrow? asked the cashier. $ 10, 000 US dollars?

**Markov**:
It is 260 dollars.

**Bert**:
It was seven thirty.

**Markov**:
I just wanted to spend.

**Bert**:
I just want to know.

**Markov**:
Maybe we could go to the store across town. The offer is way cheaper than going roughly in a flat with that. 7 bus to get cheated! OK, let's go!

**Bert**:
Maybe we should go to a flat in London. A flat is much better than being alone in a flat, really. A place to be alone. Okay, let's go!

**Markov**:
All right. When do you? I'd like to come.

**Bert**:
All right. Why would I? I'd have to leave.

**Markov**:
You do? But how can we do for you?

**Bert**:
I know. But what can I do for you?

**Markov**:
Which would you like it? If we are neighbors! No - can - eat ' dinner special. I was also reading about Michael Milliken, the company? It has more scratches on the map.

**Bert**:
How do you like it? If you put a'you - can - eat'on it, I was already thinking about the pecan in the bowl. It had two forks on each side.

**Markov**:
Don't tell me a cup? Well, that too? The price factor can be hard to find a shopping cart through. You just need to eat?

**Bert**:
Don't call me a bitch. Get over it now. The food court would be able to move the food court to where it would have to be?

**Markov**:
Please let me write this kind as to improve my oral English teacher.

**Bert**:
He helped me put my shoes on and take my wet clothes off.

**Markov**:
It doesn't seem to like the apartment, not yet. Dad, it's important that you looked so thin.

**Bert**:
He doesn't want to leave the house, not yet. No, it's just that it is so cold.

**Markov**:
Are they all for today, I have a reservation I made apple pie too, Mr. Is it higher than other kinds of tricks on others, and then he type out our room.

**Bert**:
Are you up for it? I have to admit he has some talent too, though. He can work with all kinds of kids and adults, and he always makes up a story.

**Markov**:
All right, around 61, he does, actually. I just bought a bunch of antibiotics. We've managed to start by listening to and more persons have the carpet cleaned before you move so quickly.

**Bert**:
All right, very well, this is over now. We just need a couple of antibiotics. We've got to stop the bleeding, and try to get the wound closed before we move too fast.

**Markov**:
They always eat pizza, English composition? It's a great ancient poet named Quyuan.

**Bert**:
Many people eat Chinese and Japanese cuisine. It's a very popular dish in Puntland.

**Markov**:
Honey, it's dead. Does he mean I couldn't careless. Let's go on.

**Bert**:
Yeah, that's right. Did that mean I wasn't clueless? Let's move on.

**Markov**:
I ’ m not going to the night cream for my mother - in flash. Hi, Zhengjun, what religions do they look!

**Bert**:
I'm just looking for some ice cream for my hard - ons. Oh, Jeez, what else can I do!

**Markov**:
I see. I will take a picture here, Miss Cai. Hi, Mary?

**Bert**:
He thought, I do have a place here, Shadwell. Why not here?

**Markov**:
Why don't you go. You need to reconfirm our flight will get a lot of planning in a while? What's he like that you are experienced and great food. I took a taxi. My husband is so beautiful.

**Bert**:
Why can't I go? I need to reaffirm my identity and do a bit of shopping for a change. What's it like when you have coffee and fast food? I call a cab. My apartment is too small.

**Markov**:
Lisa, I see. We can have all kinds of meat? This one is $ 13.

**Bert**:
Yeah, I know. I can do all kinds of things. This one costs $ 100.

**Markov**:
It's 500 dollars! I want to get a student if he asked. Sure.

**Bert**:
That's 100 %. I wanted to be a writer. I wanted to write.

**Markov**:
Why do you use your break time and consideration again. Your check will be working now you really didn't do anything about it. You just need to return my call last week.

**Bert**:
How could I feel the same way about him now? My mom would understand, but I still couldn't do anything about it. I just had to make a decision this time.

**Markov**:
.. Yes, someone else for you?

**Bert**:
No. There was something different about him?

**Markov**:
I know a little stupid. It ’ s help wanted section. Yes. I had it!

**Bert**:
It looks a little bit like God's most precious gift. No wonder he loves me!

**Markov**:
My father is a hard disk onto one city bus, or we may have accidentally insinuated that she still single. I think Beethoven's music is a fancy place. I'm still single.

**Bert**:
The party was a social event on the school grounds, and I could have easily insinuated that I was leaving. I thought today's party was a good idea. I'm staying here.

**Markov**:
Good morning, ladies, the service was quite confusing for me?

**Bert**:
This time, though, the situation was completely different - why?

**Markov**:
And your cameras. I'm sorry, Madam. I cannot let anything happen to me it's RIB deposit.

**Bert**:
Feel the pain. I'm sorry, madam. I just made it clear to you what'll happen right now.

**Markov**:
I think Clinton deserves high marks in hundreds and the new look of the bookcase. So how did the boss and tell me what room had the drivers speak English? Sure. The landlord lives downstairs.

**Bert**:
I think I remember the size of it, the angular shape of the bookcase. Want to call my mother and tell her that cars and their drivers speak French? No. My mother speaks French.

**Markov**:
I'd be glad to hear that.

**Bert**:
I'd be glad to hear it.

**Markov**:
.. Yes, madam. How lucky you didn't fill out this form, sir.

**Bert**:
No. No, madam. No. I didn't fill out a form, either.

**Markov**:
I ’ Ve got to finish it tomorrow. And who ’ s unless there is mold on the motor.

**Bert**:
" Is Lace going to do it again? Maybe that's why there was blood on the floor.

**Markov**:
Www! A well written business plan, tell me what you are. I'm hungry. Yes, sir. What do you think of your own business.

**Bert**:
Aww, you stupid little fucker, tell me who you are. I'm sorry. Yes, sir. What do you know of my real name.

**Markov**:
Hi Joe. Can I help you? Are we too late. The plane is boarding gate?

**Bert**:
" Hi. Can I help you? " Not so much. My dad was the boss?

**Markov**:
Many people have cars. For example for delicates, you know the extensions? Just go. It's not far.

**Bert**:
These things happen sometimes. They start as coincidences, you know, right? I know. It's a coincidence.

**Markov**:
There ’ s the one who caused the accident too. ..

**Bert**:
He's the one who caused the accident....

**Markov**:
At least I enjoy being by myself in the new cards to write you a chance of snow. What happened? She worked at CAB Company for four academic years. Please don't eat meat, but I hate the bus is turning right to get us Americans to change our appointment. You are the advantages of it.

**Bert**:
At least I get paid by someone with a credit card to buy me a coat of paint. What else? I work for FRU for a hundred bucks. I don't have money, but I think this guy is just trying to use his talent to make an impression. There are the consequences of that.

**Markov**:
The Pairszone?

**Bert**:
" Velocity?

**Markov**:
Now, when you come with a network of work, resulting in more detail. what's the boarding passes from our place and play with us all the time. Oh, there might be helpful in explaining things and she lived at home. It's been nice talking to me?

**Bert**:
Now, before you start asking a lot of questions, give me some information about who's on his way to the hospital and talking to me all the time. Also, I can be helpful in finding out if he is still alive. What's so important now to you?

**Markov**:
Are you sure? Open you suitcase, my name is Mary. So, you are. Well, to the Ritz? You are welcome.

**Bert**:
Are you coming? In my language, your name is Sam. Yes, you are. Sam turned to the dolphin. You are coming.

**Markov**:
There's some tape, iodine, and also a politician. And then what did you do that! This customer is very popular a traditional English breakfast. Are you ready to order room service?

**Bert**:
There's duct tape, iodine, and even a razor. Wow, how do you do that? This place looks more like a typical nursing home. Are you going to order room service?

**Markov**:
But Ernie, it is confidence in your home will beautiful on your computer turned back on Tuesday or Wednesday be best. You have to work under pressure, if need more practice before I show you around, we have one or two glasses of eggnog, but it remains like a gentleman. But you don't want to work as a hotel which is nearest to our company, but still a beginner. Are you ready to establish from the Marketing Department. I do, but when I come to later.

**Bert**:
" But if he was working in a restaurant or working for a real estate development company, that would be fine. I want to talk to him. I want to know if I like him, if I like one or two pieces of eggnog, if he feels like a jerk. " I don't want to work in a department that is similar to my own, which is called Department C. Are we going to work in the same department? I know all about what I want to do.

**Markov**:
And I'm going to fail. How can I suggest you look for another one quickly.

**Bert**:
" I'm going to bed. Now, I suggest you go take a shower first.

**Markov**:
I wouldn't really know.

**Bert**:
I don't really know.

**Markov**:
I use those sites. Is it still under arrest.

**Bert**:
He paced the room. Fighting them, killing them.

**Markov**:
Goodbye. I wish you could, I suppose I don't know what to say. I heard it's going very well, now I am doing.

**Bert**:
Yes, I think I do. I... I don't know what to say. I think it's all very well and here I am again.

**Markov**:
Fine.

**Bert**:
..

**Markov**:
If you refuse to take it. And what's your secret?

**Bert**:
But I have to do something. So what's the point?

**Markov**:
Why not? But I have to wear when I get one for me to cut off their various skills to use the contents of the times. My stomach is the expiration date on your salad? We have a question. Is there anything I can hardly get such an important role in British history.

**Bert**:
Why not? Do I have to ask? I have permission for you to work on the case, to know the details of the case. Your name and the expiration date of the contract. I have a request. Got it? You should not play such an important role in the case.

**Markov**:
You seem a bit tired, Jeanine, you have seen you for your wool carpet. Hi, my mother after knowing her only a few new ties for my mother. Oh, dear!

**Bert**:
You look a bit pale, Geraldine. I have booked you for the red carpet. Oh, yes, but give me just a few more minutes on your part. Oh, please!

**Markov**:
I can't forget about it except a jam a few too many times did you? Harry is a loan. Ok, let's see. It will help sales?

**Bert**:
You didn't think about looking in the mirror a little too many times did you? That was a lie. Well, let's see. What will happen now?

**Markov**:
Is it really a shame. Yeah, why didn ’ t want the degree of intensity, speed and accent. That's a relief for me to the Gold Line station?

**Bert**:
Is it just a ride? No, I don't like the idea of accent and accent and accent. What's a ride from here to the Red Line station?

**Markov**:
Can you give me a couple of minutes. Thank you so ticked off about? I bet he's really reserved, normally. How about this one? He ’ s nothing special.

**Bert**:
Can you give me a couple of minutes? Are you that ticked off again? I guess it's more complicated than that. What about this guy? He's nothing special.

**Markov**:
They might be interesting to you. Is that Miss.

**Bert**:
It will be up to you. Please, please.

**Markov**:
J - A - N - S. I'm going to do this? It's easy to go out and buy some potted plants for the position of computer time. Wow, my mother. I was chosen as one daughter - in - box.

**Bert**:
S - S - S - S - I'm going to... what? It's time to go home and get some potted plants in the middle of the night. Oh, my God, I was looking for my sister - in - law.

**Markov**:
It stands for General Audiences, PG means Parental Guidance suggested, R, I must have thought of this film. Sure. Yes. Where was the film will be sent tomorrow.

**Bert**:
PI means Child Care I. PI means Parental Guidance I. Well, I should have thought up a name for PHI. It means the child will be born soon.

**Markov**:
Would you transfer from? If I enter your PIN in future. Where is the most important thing to us all week.

**Bert**:
Can I go home? Can I be a PI right now? That was the most important question to ask this morning.

**Markov**:
I am too busy to be really healthy. Can you help to promote sales. Thank you very much! How about the social benefits. Well, then, see you.

**Bert**:
I am too tired to be so happy. Do I have to say goodbye? Thank you so much. What happened the other night? Well, now I have to.

**Markov**:
You really have to say so.

**Bert**:
He would have to do it.

**Markov**:
I came here for all my belongings? I don't know how to do? Things are different from what I hear what happened? Add the class for me, sir.

**Bert**:
I came up with all the things that I didn't know how to do. You know, like when I saw what happened. Sold the house to me, too.

**Markov**:
Yes, simple, but I am? We'd like to go. He is in the world from time to learn how to use it? Are you watching? Don't you think of when in Rome, do you think of anything.

**Bert**:
Yes, yes, yes I do. You'll want to know. You came into my life in order to learn how to control me. Are you sure? Don't you worry, just in case, because you care about me.

**Markov**:
OK, sir? This is Robert Jordan. What are you doing in your resume and I ’ m sure I agree. Well, then what about the hiking?

**Bert**:
Yes, sir. This is Detective Smith. What have you got on your mind? I'm sure you do. Yes, but what about the police?

**Markov**:
Whoa! What can I get the highest marks? That's good. Did it come with me? Welcome.

**Bert**:
Whoa. How do I get my life back? That's it. Can you talk to me? Please.

**Markov**:
What if I get a job as a trainee every summer at a much cheaper place that's already furnished. Let's go there myself. My credit card. Like to come back in China that the most impressive should be happy to have a ride on vacation?

**Bert**:
What if I get a job as a trainee next year in a much better place that's better off? Let's not do that. The student protests. Should I go there in hopes that the new student will be able to get a job on campus?

**Markov**:
Are you interested in. All right, we blow air two or more a living room dining room Wow, you sign it. ( ten minutes.

**Bert**:
If you want to. Every day, you can have one or two for lunch or dinner. Please, just do it. In five minutes.

**Markov**:
Charles Dickens. I admit I always get up early today. Have you ever used a 24 hour clock? Here we go right after you get?

**Bert**:
I mean, I know you must be up early today. Have you ever had a false alarm before? Can I call you if I can?

**Markov**:
The Honda I have no idea I would change the channel? How long is my birthday. I don't know how to operate and repair all kinds of books for my subscriptions to all the gifts for my meetings all day and I am so happy to recommend gin and tonic. No need!

**Bert**:
Besides, I had no doubt he would change the subject. How early is my birthday? I don't know how to buy and sell these kinds of things in an antique shop and keep these things in my house all day. I was just going to drink gin and tonic. No way!

**Markov**:
Yeah, this may seem like the control unit is on the internet so I was very professional. Sometimes it's wise to check. That's OK. Oh well.

**Bert**:
Well, it did look like the whole thing was in the papers. It was very interesting. So it's safe to say that it's interesting. Very interesting.

**Markov**:
I ’ m afraid you must be much simpler and cheaper to buy some fruit instead? I've gotten chow mein. We're set up an E - N - S.

**Bert**:
I'm sure it will be much easier and easier to get the word out. They've got charlatans. They've set up an A - B - B.

**Markov**:
Man, you rub shoulders with the choice to make the tango so great to be a very popular. I'll have to stay at school, I didn't know it looks interesting.

**Bert**:
Instead, we hold hands with our parents and watch our parents either laugh, or say something really funny. I'll have to admit at least, I don't think anything is funny.

**Markov**:
Really? Does this train go to school, he has ever tried a kind of you. Yes, I'd like to live. And give the landlord agrees.

**Bert**:
Why? Would my father go to jail if he had not seen this side of me? Yes, I'd like to know. I knew the man well.

**Markov**:
I'm just too expensive. Around 3: 30 am. I need you to change into another person. In cooperation with your boss. Good coming, before that to make an advance against my personal credit card authorization number.

**Bert**:
I'm not so sure. At 8 : 00 am, I want you to change into new clothes. In touch with your parents. After that and after that, make an appointment with your new credit card account number.

**Markov**:
It's nice to see that, please. It wasn't too happy to hear this? I ’ Ve tried to call me, I'm just curling my eyelashes.

**Bert**:
It's nice to hear it, too. Why isn't it nice to hear it? " " Lace tried to kill me. I'm not batting my eyelashes.

**Markov**:
What else does he look like for your help. Your dentist must be a shame not to give you enough. You're welcome. But I have the chance? Two people were trying to call the security of this over with Dan and I don't understand why they do, it does not warrant an agency appointment.

**Bert**:
How long would it take you not to know? The dentist would be a fool not to tell you that. You're right. Do you see my point? Some people are going to get the hang of it eventually, and if they don't know what to do, it might not be an easy task.

**Markov**:
First of all the time when the boss will get better at Whole Foods is way cheaper than getting two singles, not every Chinese can play against other people around me is the green and black could also help you. Here's fifteen Yuan.

**Bert**:
Well, at a time when the money to be spent on Whole Foods is probably less than a dollar, but if you really can communicate with the people around you, both white and black can really help you. That's the problem.

**Markov**:
All right, I'll take one. The Northern Line? Well, the newspaper.

**Bert**:
All right, I'll do it. The Red Court. Yes, Red Court.

**Markov**:
Actually, that's a plus. Come in please. Can I get.

**Bert**:
Well, that's a start. Come on in, " he said.

**Markov**:
Yes, my name is Liu Wei. I thought I ’ Ve researched the company. But I'm not very good advice!

**Bert**:
Hey, my name is Decklan. Uh - oh, Decklan owns this place. And I'm giving him full credit!

**Markov**:
Hello baseball fans, and have a really good. OK, that's a good job and I've never been told about something that she is thinking of seeing them in cold weather will be available then? Excuse me, what's the problem?

**Bert**:
No more questions. I made that very clear. Well, that's a good thing. I've always known, but now, everything is kind of slipping away and my life could be lost forever. Tell me, what's your name?

**Markov**:
. Du Tao, the area is about, I ’ Ve got some wonderful clothes.

**Bert**:
" Hey guys, the party is over. " " Mindy has some new ideas.

**Markov**:
Oh, thanks. Please sign your name and address of the Avenue B bus or D / P? Single or double?

**Bert**:
Oh my God. What was the name and number on the card? S / A / S? Male or female?

**Markov**:
Next month, you'll be able to follow suit. I see it.

**Bert**:
Next time, I'll be sure to call you if you need anything.

**Markov**:
I ’ d like to have some change I can help you? Oh, what ’ s wrong? My wife is too much. Great! Actually I will buy it.

**Bert**:
I'd like to make an offer I can make you. So, what's next? The offer is too much. No. But I can make it.

**Markov**:
That ’ s cheques, but I have this week.

**Bert**:
It's cheque, which I get every day.

**Markov**:
Thank you for your order, sir. Thank you. Look, Sally! You are so old. Everything seems fine, I will be settled.

**Bert**:
Thank you for your help, Sally. Thank you. Please, Sally. You are so kind. Everything is fine. Everything will be fine.

**Markov**:
Don't you agree. Chen Hong, I won at work, otherwise you'll fail. Smith?

**Bert**:
Don't you worry, Mr Smith. You stay at home, and I'll call Mr Smith?

**Markov**:
How much for your reminder. Thanks. .. What can I expect too much TV instead of contact lenses.

**Bert**:
So much for watching TV. But... how do you get so much stuff out of those boxes.

**Markov**:
Oh, I know little about marriage. Thank you very much indeed. This is only ten in the coming negotiation.

**Bert**:
No, I know nothing about it. Thank you very much sir. It is very important to our fan club.

**Markov**:
Could you tell me something about it now. Yes, you can give proper response when you're watching. I can't wait to retire rich. How much? ..

**Bert**:
Can you tell me all about it now? Look, I can get a job if you're interested. I can't afford to be young. Too young. No.

**Markov**:
I don ’ t want you to dinner and dancing, music, order a large space. A Twin, please. Oh. What ’ s my idol.

**Bert**:
I don't take you to parties, parties, parties, or any other place. The same as you. Me : He's my boyfriend.

**Markov**:
I think that climate change is responsible for a restaurant. Let me see. May I take the Bus 151 which goes the national anthem? Thanks.

**Bert**:
I think that climate change is bad for the world. Let me think. Should I play the piano, or sing the national anthem? No.

**Markov**:
Put them under the seat belt.

**Bert**:
Put it in your back pocket.

**Markov**:
I would like to be here for days? Got it.

**Bert**:
He would have to stay here for now. Damn it.

**Markov**:
Of course. What?

**Bert**:
Of course, right?

**Markov**:
I want to start alignment meetings nextweek. Three months.

**Bert**:
I have to be home by midday. No problem.

**Markov**:
Me neither! What's this, her glance.

**Bert**:
Why? " It's strange in a way.

**Markov**:
Our maths teacher is rather humorous. I have to understand the terms correctly, it's true that one. Let me think, is there. Thank you for understanding. Oops!

**Bert**:
My maths class is so boring. I have to get the words out, it's not that easy. Let me say it was easy. Thank you for asking. Oops!

**Markov**:
I can touch them with a knife and fork? What's he going? I'm not really like sci - fi game in which all employees before 4 p. Guess I have coffee, juice or iced water, please.

**Bert**:
Who would stab me with a knife or something? How's it going? I'm not much for sci - fi, in fact I start at 10am. Can I have coffee or tea or bottled water, please.

**Markov**:
You can get free medical care. Yes, I suppose.

**Bert**:
He could do the same thing. Yes, he could.

**Markov**:
I can't agree more. Okay, you're right, we will send you a note when we are allowed to go to school? That is not difficult to write! Yes.

**Bert**:
I couldn't agree more. And when you're ready, I will write you a letter when you are ready to go to bed. It is so easy to write. Please.

**Markov**:
What does my father isn't there a hotel that isn't broken, then. Well, I've never had bad mouthed him? I think the government might need your resume I ’ ll exchange it for now, you know which one do you want me to go this weekend? Thirty meters ahead is blocked. Where is it for ourselves.

**Bert**:
How come my dad isn't at my house and isn't there right now? What if I'm pushing too hard for him? You know the police will find your car and you can drive away from here because you know the road and you want it to be that way. Ten miles away, maybe. This is it for me.

**Markov**:
We are planning a college. I'm worried that my pronunciation is very pretty little girl, you are right, Sarah.

**Bert**:
You are at a disadvantage. I'm sure that your mother is a good little girl and you are good, too.

**Markov**:
Later he told me that. What's your favorite flavor? Thank you for help with preparing dinner.

**Bert**:
So you brought me dinner. What's your favorite color? Thank you for helping me with dinner.

**Markov**:
Before he was no reply. You can find a Carol Larson here. Fourteen the day before? Can I fill you in the way to go when you come out with Jack! What's it for?

**Bert**:
But there was still time. I could take a quick shower later. Like the night before. Do you have someone on the phone to call when you wake up? No. What's that for?

**Markov**:
Yes. Yes, I need to work is quite thin. I suppose.

**Bert**:
No. No, this train of thought is too long, I think.

**Markov**:
My friend says he should give us a discount for a workshop on efficient time management. Like what? Is your taxi engaged?

**Bert**:
My dad said it would give me a chance at a career in the insurance business. Why not? In the insurance business?

**Markov**:
Wait, will you set call transfer.

**Bert**:
Okay, now I could barely breathe.

**Markov**:
I was really tiring! He is so cool carrying this around your house?

**Bert**:
It is so tidy. What is so special about living in this house?

**Markov**:
Bye. I'm Mary. Thank you very much? sure. I don't mind.

**Bert**:
Hi, I'm Claire. Thank you so much, Claire. I didn't know.

**Markov**:
Yeah. Yes. Why don't you give me some green salad together. If everything goes well for me, can you give me the opportunity to learn English.

**Bert**:
No. No. Why don't you make me some tea, please? If all is well with you, then please give me a chance to speak privately.

**Markov**:
I hate that idea. Goodbye until then?

**Bert**:
I like that idea. So what now?

**Markov**:
Just a moment.

**Bert**:
For a while.

**Markov**:
Really? We made it 5 to 4. I need to know? Right. Umm.

**Bert**:
Right. I want... Right. Right. I want to be... Right. Hmmm.

**Markov**:
Hello, I do it. Don't run so Oh, that's really a big deal. I'm Bob. Let me throw on a diet coke.

**Bert**:
Please, just do it. Don't worry. No, it's not a big deal. I'm fine. Let me put on some hot cocoa.

**Markov**:
Can you start on building my nest egg. He is like a dreary Saturday. That will conserve the heat of the letter if it keeps flashing, which is a green hand like him.

**Bert**:
" I plan on using a green hand. It looks like a dreary hand. It will confuse the rest of your body if it starts bleeding, which is a green hand like yours.

**Markov**:
No problem.

**Bert**:
No answer.

**Markov**:
Yes, I'm afraid the team. I never ordered. That's easy.

**Bert**:
No, I'm on the pill. I was kidding. It's okay.

**Markov**:
I know. It was birdseed. Give me another? Men, women are more independent.

**Bert**:
She smiled. It was Fareed. Just a friend. Yes, you are very kind.

**Markov**:
sounds fascinating.

**Bert**:
How strange.

**Markov**:
That's funny. That ’ s my name is Laura Wills.

**Bert**:
That's him. That's his name, Jacky.

**Markov**:
This is just suggestion. Actually, I can ’ t deny that. I haven't. The funniest thing I need some help.

**Bert**:
This is a joke. No. I can't do this. I can't. The funniest is I need your help.

**Markov**:
Please go to the responsibilities are for everyone, and you can take a bus pass yet? They're doing a lot more! What kind of smell do you think of all, you were part of our staff. I know. Our president has asked me.

**Bert**:
You know how many people are watching you, and you can do a good job there. You're doing a lot better. What kind of job do you have to do if you are part of the government? I asked. The government never finds out.

**Markov**:
The order was for me to subscribe?

**Bert**:
The question was for him to subscribe?

**Markov**:
I see. First of all, she brings back memories. Since you had enough. You did a great time. what would you add the vegetables are very nice girl.

**Bert**:
I know. Most of all, it brings back memories. But you were right. You had a great life and, as you said, you were a great man.

**Markov**:
I've got it. What makes you look great!

**Bert**:
I've got it! It makes me feel better!

**Markov**:
Who was it? It's too early.

**Bert**:
What is it? It's too late.

**Markov**:
This package also includes a variety of exhibitions they have to walk. There ’ s wrong?

**Bert**:
This conversation really says a lot about where I want to go. What's next?

**Markov**:
It's too bad. Predictable! Really? Looking out of doing this the right to re - inspection should be delivered in two months. That was a nice day!

**Bert**:
It's so simple. Predictable. Why? And because of that, my book on cross - breeding will be published in two weeks. It was a brilliant idea!

**Markov**:
Yes, what kind of errands do we? No, these are fine. Michael? Hope to see that happening.

**Bert**:
So, what kind of errand boy are you? Thank - you, Mr. Jones. Nice to see you again.

**Markov**:
I went to a neurologist for a couple of hours to finish so soon? Go ahead please. I am. Whom would you tell me please? Ok.

**Bert**:
I talked to a neurologist for a couple of days and came back here. Hold on to where I am. How soon can I see you again? No.

**Markov**:
But as to what I am in no time to go out and organize incoming mails. I would.

**Bert**:
But unfortunately for her he was in no hurry to go back and use the bathroom, which he did.

**Markov**:
Enough!

**Bert**:
!!

**Markov**:
He must be very pleased. I'm sorry, I ’ m from the United States. Hello. We might have found much difference between your counter - offer three hundred and fifty thousand dollars to learn something of Chinese are marrying foreigners. Its colour is it convenient for you to say good - looking box.

**Bert**:
I must be somewhere else. I'm not sure I'm in the United States or Canada. I might have been worth fifty or a hundred, maybe a hundred and fifty dollars, but the thousands of dollars are too many. What happens after that is for me to say good - bye again.

**Markov**:
I feel, so I need money for homeless people on first. I write that down. The initial fee.

**Bert**:
I searched, but I found nothing in the yearbook either. I wrote it down. The history section.

**Markov**:
Have we sold out.

**Bert**:
Then he walked away.

**Markov**:
Sure. Come and take our examinations. Would you like? I hear that.

**Bert**:
No. Go and do your job. Would you mind if I did that.

**Markov**:
Yes, I am happy with your computer for this reason?

**Bert**:
What if she was messing with his head for some reason?

**Markov**:
It ’ s go! Unfortunately, I have a job in a minute. Where is the first guest to arrive at our bar!

**Bert**:
Let's see. Well, I saw this guy at the bar. He was the first guy to walk into the bar!

**Markov**:
You can get off. But Mom! what's interesting to study for an interview for this? How many people underrate the education value of the unnecessary health rules to exclude foreign food. Don't worry about you?

**Bert**:
I gotta get going. " God, it's weird to walk into an apartment like this. So many people puke their guts out of their empty stomachs and eat and drink. Don't think about it?

**Markov**:
It was the best seller. The Italian restaurant in town! Three days. Does this dress with your gay friend who play it all goes well with a hillside view. No, thank you.

**Bert**:
It was a bestseller. The first edition was good. Second edition. Just a visit from a good friend to see if everything went well with the second edition. No, thank you.

**Markov**:
Of course not.

**Bert**:
Of course not.

**Markov**:
Most people grow accustomed to bargaining! Yes. We've still got time!

**Bert**:
The voices were back to normal. Hey, I've still got you!

**Markov**:
Those are new products.

**Bert**:
There were no words.

**Markov**:
I have no idea. We are at the EDD? No, I see myself in a job with satisfying working hours?

**Bert**:
I have no idea why you work for the UDD. Why do you always work in a place with long working hours?

**Markov**:
Did this just can't connect to the mountains with me? it ’ s too loud, and they are buying for chain department stores and sports games require flexible movements and real time strategy, amazing! what did you go.

**Bert**:
Sometimes you just don't go to the movies or anything because it's really bad and the movies are bad for some reason, and the movies are bad and the prime time shows are bad. Wherever you go.

**Markov**:
I have to go to buy extra ticket if I smoked? the survey report on their ski trip I've ever had any type of girl. I have roses, and most of the construction site manager? Well, what brings you here? Do you think of five percent for you.

**Bert**:
I have to go and get a job. I have to go out and make some money. I've never done that sort of thing, you know that, but what about the scams? So, what brings you here? Why not spend a million dollars on it.

**Markov**:
There ’ s necessary for you? I had a really bad in the theatre then. Yes, and what you say your white blood cell count is now verified, so you won't get into Sociology. Thank you " when you make an announcement that my blood pressure isn't that busy. That doesn ’ t want to pay for my department.

**Bert**:
What's good for me is I liked it that way at one point too. However, from what they say my white blood cell count is not high enough and I can't stop calling out " thank you " until I reach the conclusion that my cell count isn't that high and I don't want to be in that position.

**Markov**:
Most people like it. I am supposed to write it all!

**Bert**:
The girl read it! She was going to read it again!

**Markov**:
42. It's funny that we are waiting?

**Bert**:
No. It's just that you were worried?

**Markov**:
Got it, but my house when I got married?

**Bert**:
Was he sleeping in my bed when we were together?

**Markov**:
Thank you. That will solve it. Are you busy tomorrow evening. I know that we will be windy today.

**Bert**:
Thank you. I can do that. Keep me updated next week. I hope that things will get busier soon.

**Markov**:
He was excellent. Does have your name to the Caribbean on? I wish I were you there.

**Bert**:
That was it. You changed your mind for the first time. I wish I knew you better.

**Markov**:
Would that be all. It is No. No, I can finish it on now? I'm hoping we'll be better in the whole movie. Good evening.

**Bert**:
Let it be done. Me : Okay. But maybe we can get it done tomorrow. I'm sure it'll be done in the next week. Tomorrow night.

**Markov**:
Yes, it's how you feel that I haven ’ t bring cash with me, could you repeat that please. No! They concluded that the window, you swim?

**Bert**:
Yes, that's what I thought, I can't take you with me, can I do it again? Yes, I thought, the monster took you away?

**Markov**:
I know it, and what about tomorrow? However, a civil engineer on a diet coke? Don't worry. I'm off again. Where are they window seats or aisle seats?

**Bert**:
I know that, but what about food? Like, a sick person in a hospital cot? Don't worry, I'm hungry too. Why are there bench seats and bench seats?

**Markov**:
English is very kind of expectations do you listen to a cookout for new, isn ’ t think so, too, but my written Spanish isn't very mountainous, is it to Mr. Almost all the time we traveled together was in University.

**Bert**:
It was the sort of thing where you go to a cookout or something you don't know about, though, and that way it didn't so much as bother me, either. And all the time we spent together was at home.

**Markov**:
I'm under a spell. Instead of walking. Do you know? Tomorrow is my wallet. Surely you've noticed the date on a camel.

**Bert**:
I'm taking a walk. All of it. Do you understand? This is a walk. And you've got to be riding a camel.

**Markov**:
Thank you for. Theaters wouldn't let kids in Taiwan! I must see your passport please? Nurse, get the bread and potatoes.

**Bert**:
Thank you again. The police don't want you in jail. You can enjoy your time here. Here, have some mac and cheese.

**Markov**:
Much better.

**Bert**:
Much better.

**Markov**:
Are they urgent, tell me that day. A seminar of technical qualification have you been to the cable isn't working. What is the Regent Beijing but we have to disagree with you? I'm now a member of the older ones.

**Bert**:
Are you going to give me another chance? That kind of a thing has the effect that the world isn't changing. This is a new world. I want to be with you. I'm not a repeat of the last time.

**Markov**:
Name it.

**Bert**:
Do it.

**Markov**:
It seems that English already is the next door. You have gotten through university without them!

**Bert**:
That means that their house is right next door. I have gone to bed with them!

**Markov**:
Forex registration? Utilities are extra. , one of my new pink bikini. That's not as important to learn violin when I see.

**Bert**:
And a bathroom. Utilities, too. For example, a hot pink bikini. It's not that hard to find one, you know.

**Markov**:
Excuse me. Have you got working experience, I don't know how I could do some online research? Of course. It ’ s just a small slice. Yeah, I hate spending too much for all your patience.

**Bert**:
Trust me. If you need any help, I don't know if I can take any more chances. Of course. It's only a little bit. Besides, I was getting really tired of doing my job.

**Markov**:
I ’ d like to make? My favorite singer won!

**Bert**:
I'd love to play! My favorite game ever!

**Markov**:
I'm sure you let it go and get it back and forth. I was reading. Every thing for him?

**Bert**:
I'm sure she let it go and tossed it back and forth while I was gone. A present for me?

**Markov**:
Hey, look! Here we can. Then we can issue you with that? I think that will be all.

**Bert**:
Oh, no. But I do. Maybe I can help you with something. I hope you will be okay.

**Markov**:
It's her birthday. He's in a few people who listen to the property manager right away and get it?

**Bert**:
What's the point? Who's spending a million dollars to go to the grocery store right now and do that?

**Markov**:
Yes, we have more free time at home. They could generally be divided into 8 big cuisines, such as Remembers ’ Day. You want to miss a train journey is as a Westerner, it's the golden season to take the shirt.

**Bert**:
Luckily, I had some free time at school. It could also be divided into three - day periods, such as Thanksgiving and Labor Day. I had to go a long way in being a learner because it's the only way to get a degree.

**Markov**:
May I get some popcorn first. Sure, you know, I can have a list of departments first, I ’ m not.

**Bert**:
" You want some popcorn then? Well, you know, I only have a couple of hours left and I'm starving.

**Markov**:
That ’ s just that scarf with a brief summary.

**Bert**:
It's just a story, a real story.

**Markov**:
I'm glad you told him and his study. What ’ s correct.

**Bert**:
I'm sure you remember me from your childhood. That's all.

**Markov**:
Sir, the postage on these documents. One dollar.

**Bert**:
Yes, the postmark on the envelope. One word.

**Markov**:
I want to take it! We've got to show it off big time! I'm sorry, but I've just been sung, and you can invite more customers with goggles, swimming pool. I feel like going.

**Bert**:
I have to do something. I've got to shake it off this time. I'm tired, and they've probably already left, so I should get some rest and start using the swimming pool. I feel like shit.

**Markov**:
So Kim, should I wear? Welcome to Lincoln Bank. I guess. Let's just window shop a little on the day before yesterday. It's really quite exciting.

**Bert**:
" So what do we do? Go to the bar, I mean? There's a coffee shop a little open the night before tonight. It's actually pretty cool.

**Markov**:
I'd like to carry it all sounds so relaxing. I've given you a ticket and figuring out how to plant organic vegetable? That's cool.

**Bert**:
I'd like to do something and have some fun. I've set up a place and figured out how to make a living. It's fun.

**Markov**:
I can't find the relevant department. Kyoto is lovely. My first job was. Are you aware of my wardrobe are hand - made wonders that could be found on these clothes more for fun ', A.

**Bert**:
I couldn't imagine my wardrobe changing. That was all. The only question was'are you aware that my clothes are custom - made? They should be included in my wardrobe, thank you ', anyway.

**Markov**:
No wonder you say we have a registration card. Don ’ t I? I can't help missing him while he is going to be passionate about journalism and passionate about journalism and passionate about journalism and passionate about this floor lamp? It is my favorite white bread, cheese, and you are.

**Bert**:
Look, I know you have other friends too. Don't you think I can't imagine meeting him when he is going to be passionate about politics and passionate about politics and passionate about music and passionate about the music industry? I was just waiting for you, and now here you are.

**Markov**:
, I would remember if she is. What happened? So he had water on me. Will you? I've already got it.

**Bert**:
But I can see where he is. What else? Because I have nothing on him. Do I? I've still got him.

**Markov**:
A Visa. I fear that he had been two - thirds of Americans, so the new job.

**Bert**:
The blood. The fact that there had been two - thirds of it, in the first place.

**Markov**:
Hi, Linda, John and I will take you to pick up parcels? Yes, I ’ Ve met my old job and then we'll issue you a room the day of next month.

**Bert**:
Yes, yes, you and I will get together and have a weekend together. Yes, you and I have shared a hotel room, and I'll get you a room the day after next week.

**Markov**:
Yes, have you noticed? Oh, I can't turn it on yet? I asked if there is a high chance of freezing rain. Do you take the tour guide.

**Bert**:
So what have you done? Well, I can't figure it out yet. I wonder if there is a better chance of your survival? " I asked the tour guide.

**Markov**:
Do you mind I have the same time and money. As usual, is that?

**Bert**:
Thank you. You picked the right time and place. What time, is it?

**Markov**:
40 miles per hour. Yes, of course. What happens now?

**Bert**:
Fifty miles an hour? Yes, of course. What happened then?

**Markov**:
Disasters have happened. If you can ’ t actually know him. She believes everything about him in time. Great.

**Bert**:
She would have laughed. But she doesn't really believe it. She knows nothing about it this time. Nothing.

**Markov**:
Hi, sir. Yes, it pays off. I want to be done. Are you sure about that? What can I do for you if you persist in it.

**Bert**:
Yes, yes. Yes, it pays off. You have to be strong. Are you sure about that? What will I do to you if you subsist on me.

**Markov**:
For nearly four years. Would you like to buy something you can decline to buy?

**Bert**:
Just over a hundred. Would you like to see what I would like to see?

**Markov**:
I am not feeling well. Please be seated. I watched United play Chelsea. .

**Bert**:
I am not feeling well. Please be here when I see you....

**Markov**:
that ’ s Big Island.

**Bert**:
It's too late.

**Markov**:
We need to go look for it?

**Bert**:
You want to go back to school?

**Markov**:
Well, I think he is out of the cabinet above the ear. What am I right? Why?

**Bert**:
Suddenly, I think something comes out of the darkness behind my eyes. Or am I dreaming? What?

**Markov**:
That would be spacious and clean up the passengers relaxed and open - minded in class is a type of apartment in a very popular. Yes. Hello sir, calm down, Jack, I promise. I'm not sure how to use the credit card?

**Bert**:
It would be nice to grow up with someone young and grown - up, which was the kind of life she found most appealing. No. I need to calm down, though, she thought. I'm not sure how to use my credit card?

**Markov**:
I think I've ever seen.

**Bert**:
I know you've been busy.

**Markov**:
I ’ Ve bought for you today? I know her mother. Hey!

**Bert**:
What had Booke done to my mother? I hated my mother. No!

**Markov**:
Yes, we haven't won the Pools, I'd like to go four times a day off.

**Bert**:
Besides, I hadn't left the house yet. I'd have to take three days a week off.

**Markov**:
It says there are so smart. I ’ m still bummed out. So I've noticed you've been munching away on business? Many times there are a good match!

**Bert**:
He thinks I am super hot and I'm totally bunked out. And I've heard you're totally bunked out with him. At least I have a new one!

**Markov**:
Will you help me know when you're thirsty, actually, it will be three of us. Well, generally speaking, how did he tell you that you would mind so much for letting me know. Wow, Good for you now have a reservation on Flight No. I'm not sure. I find it.

**Bert**:
If you let me know that you're thirsty, well, that would be out of character. So, strictly speaking, how can I tell you that you can drink the water without letting me know? What other refill you could have possibly asked for? Honestly, I'm not sure how to find out.

**Markov**:
I thought espresso was an accident just from press releases and hoopla is done. Yes.

**Bert**:
Pre - espresso is an optional option for laptops and desktops only, i. e.

**Markov**:
They're big! Thank you. I guess this place is Hebes Province. Thanks. If I need.

**Bert**:
They're beautiful. Thank you. I love this place. The Grand Canyon. Everything. Anything you want.

**Markov**:
What account would you like to buy a new position? Yes, it sounds like risky business. This is the same model as I know.

**Bert**:
Which company would you like to take a management position? Well, that was a good question. This is the same company that I own.

**Markov**:
You know I could, but let ’ s got Richard ’ s my only option right now. After a while.

**Bert**:
I wish I could, but he's saying it's my only option right now. For a while.

**Markov**:
Hearing you say you want to send you home? My book says I work. .. Richard, why don't you think I ’ d rather watch television last night? I see.

**Bert**:
Did you think I wanted to watch your house? The one where you lived? Oh, yeah, but didn't you think I'd rather watch you at home? I asked.

**Markov**:
Have you fixed them? I am looking for Bob? In fact, the monthly payment date so that I was just thinking of taking off? Do you have a question? We have roast chicken, either!

**Bert**:
Have you got any? I was looking for one. In fact, a big, fat one. I was just thinking about that one. Do I have a choice? I want roast beef, too!

**Markov**:
I've always dreamed of owning our own hotel tonight. Just keep it in the short in the living room and maybe I can clarify that.

**Bert**:
I'd always dreamed of having my own room here. I left it on the floor in the living room, so I could clarify things.

**Markov**:
I tell you about my grades. Haven't we been to the tree? Doris, Helen. And getting advancement in salary? It seems like you.

**Bert**:
I told you about the job. Haven't you talked about the job with me, too? About the increase in pay? That sounds like fun.

**Markov**:
I heard the new apartment soon. Let's go. And we arrange the time of the population. Let me hold you up here tomorrow. You know what.

**Bert**:
We have a big day tomorrow. Let's go. Then we have the rest of the day. Let me pick you up again tomorrow. You know that.

**Markov**:
If you are Settling in at the map.

**Bert**:
Then it started rattling around on a stick.

**Markov**:
Yeah, it happened. I could, but I've got time to exercise. The captain decided to wipe off any job that I can check it. How you celebrate Easter?

**Bert**:
Yes, it is, I know, but I've had time to think. The police have to drop off the body before they can find it. Should I call him?

**Markov**:
They even offer in - law is driving me up? Do I need thirty thousand. Do you carry the bags, and take over for me for that too. I've been to Japan before, our terms are net 30. Will you be a fair offer.

**Bert**:
Now my mother in - law was telling me everything. " I have two tickets. If you have one, and you have one for me, I would say I've agreed to it, but the tickets are $ 500. Let it be a big deal.

**Markov**:
Good, good for you? and junk food!

**Bert**:
Too much time for what? Time for what!

**Markov**:
Do you want to.

**Bert**:
If you want to.

**Markov**:
We are contacting you. How can I do for you?

**Bert**:
They are tormenting me. What can I do for them?

**Markov**:
I miss my parents.

**Bert**:
I miss my mom.

**Markov**:
I think I wouldn't say that I can't imagine how terrified I was laughing through the same exam tomorrow. Honey, just to be true! Just amazing! I want to visit you this, but not in the same field.

**Bert**:
I know I can't explain. I can't explain how much I hate going to the chemistry room alone. God, has he been amazing? Really amazing? I want to tell him yes, but not in the chemistry room.

**Markov**:
Yes. 42.

**Bert**:
No. No.

**Markov**:
I ’ d better tell me shall I get an autograph from him. Excited about what he looks like a tour guide? Relax, it will come up with something?

**Bert**:
We'd better find him before we do an autopsy on him. Expect him to think he looks like a tour guide. Relax, who would put up with that?

**Markov**:
And so, we bulk purchase film tickets. Isn't there anyone else traveling with you? Please understand?

**Bert**:
If not, you can use the money. Isn't there someone else working for you? You know?

**Markov**:
Why?

**Bert**:
Why?

**Markov**:
Where did you obtain your degree?

**Bert**:
When did I get a tattoo?

**Markov**:
And how much weight you use to me in! That ’ s so lovely. What's the matter?

**Bert**:
Amazing how much I can do without touching her. She's so beautiful. What's the matter?

**Markov**:
No, I think I do for you to attend Friday night's basketball game. But I like its color.

**Bert**:
Anyway, I think I arranged for you to attend last year's football game. And you attended the game.

**Markov**:
So what's on it. Many people bend the rules before I decide to stay here. Stones? Oh, that's how you keep weeping like that green vegetable but I was in the office?

**Bert**:
Look what's out there. Some people want the truth. Others want to be honest. Why? Well, that's why I was acting like a complete idiot when I was in the hospital?

**Markov**:
Well, we forgot to get any perks on the news that you graduated? I want to go up to, but she's so helpful. Do you need.

**Bert**:
Yes, I want to see the perks of the new life I have. I want to look forward to it because it's so exciting. And I do.

**Markov**:
Yeah, well, thank you very much all the same. It sounds like a little while I'll go to my aunt?

**Bert**:
Oh, yes, thank you very much all the same. It was only a moment. I'll talk to your mother?

**Markov**:
The re - examination results indicate that one of those here, but don't go to the second - hand side. Where did you think about the content. Can't you see what they teach at the end of the rest.

**Bert**:
The T - 3 will be in front of you now, so don't look to the right - hand side. What do you know about the ship? Don't even know what to do with the rest of the crew.

**Markov**:
It is. Yeah but, what did you apply for a Business English Why did the program. But I'd like to do with my timesheet?

**Bert**:
As one? Maybe, but how do we work as one? But I know the answer. What I'd like to do with a spreadsheet?

**Markov**:
Thanks for the camping trip, I ’ m headed for a moment, I am going to work with? Of course we can take bus 301 which will be held to them. I want to travel. I hope so. I don ’ t be able to break up was painful because I didn't enjoy it?

**Bert**:
Go to the bus stop. I'm waiting for the bus. I was supposed to be here. Of course you can take the bus that will be waiting for you if you want to walk. I hope so. Hadn't being able to walk would be better if I didn't take it?

**Markov**:
He seemed to be something weighing on your birthday present or let her know you are – 767 - 4512. I have been it, keep in shape. Good afternoon, how annoying! Do you have any questions you may sign the memo in the way.

**Bert**:
There has to be something written on your credit card to let me know you have $ 525, 999. I just want you to talk to me. " Okay, how much? If you want to talk you can get a memo over the phone.

**Markov**:
What's in the scenery the exercise.

**Bert**:
It's just that, the truth.

**Markov**:
What about your trip.

**Bert**:
Something about the man.

**Markov**:
Can I bring it whenever you have good taste, and then flip it, do you have questions about this. It's too much. Really? Have a great idea. We can always get shy when she gets the worm.

**Bert**:
When you see them, they ask you questions, and you answer them, and you answer them like that. It's so stupid. Why? What a stupid question. She can never be sure until she knows the answer.

**Markov**:
We can't have been connected to a two hour drive. It's your turn. Let me tell you in just a shy guy who sat in front of others, and I am calling is to sign this approval sheet?

**Bert**:
It couldn't have been reduced to a two hour session. That's the problem. Let me point it out to the next person who sits in front of me, and then sit down, and read the next paragraph?

**Markov**:
Hi Steve. Kate Green. We have a small apartment.

**Bert**:
" Ms. Ellen White, I have a new client.

**Markov**:
It would help. Attitude. I bought it on the snow is so strange today? If we had a beautiful necklace!

**Bert**:
I would have preferred Attitude. I thought walking in the rain was more fun. " " I have a wedding ring!

**Markov**:
Do you like to. I know.

**Bert**:
If you want to, you can.

**Markov**:
Bye. what ’ s nothing more to pull out your email address of the sheep ’ s right! Here is a free talk?

**Bert**:
No. There's no way to find out the exact location of the vampire's lair. What about the entire city?

**Markov**:
A tour company will pay much better to look high into the platform. Is that all? It stops snowing, but I don ’ t we? If this is the big day? Yes, and some loose powder, and my favorite brand.

**Bert**:
The construction workers would do everything possible to get her off the ground. Was that right? It was raining, so why wouldn't they? And what about the apartment building? Oh, and the hot tubs were her favorite things.

**Markov**:
Well, this is defective.

**Bert**:
However, this is restrictive.

**Markov**:
We like it?

**Bert**:
You got it?

**Markov**:
Have you got any news from university, the less heavy route, we do, we can save me! How unlucky for Rikknen, and I believe you should go with you.

**Bert**:
If you bring these people to me as a more serious threat than you think, I will kill you. Very unlucky, Tikkun, but I think I can live with that.

**Markov**:
There we go for something sweet! I've known enough. How long is the price is rising What kind of world business, the effect of the towers. What did you go. If there is actually my great uncle, that's fine.

**Bert**:
Okay, time for an explanation. I've had enough. How high is the sun now? Some sort of dark cloud at the top of the mountain? Where do I start? There he is, my best friend, he's gone.

**Markov**:
Yes, there're usually two reasons for our one - bedroom house? .. Yes. Oh, yes.

**Bert**:
No, there's only two bedrooms in this two - bedroom house. Yes. Yes. Yes, yes.

**Markov**:
You see I am sure my wife in your spare time. Everybody is talking about, food, but you can give you the loan on mortgage. Swimming is a great opportunity.

**Bert**:
You know I like having my kids in my spare time. It is for friends and family, so I can get them a job and education. That is a good thing.

**Markov**:
Generally it will snow or not? Jim Stewart from the campus. I'd like to taste my fist? If they ’ re doing a good idea!

**Bert**:
Whether it will be or not, he says from behind me. You'd love to break my heart. But you're not a bad guy!

**Markov**:
This is Jones.

**Bert**:
He was right.

**Markov**:
What shall we go?

**Bert**:
Where would he go?

**Markov**:
You have to think about that new employees a one - way ticket to Venice.

**Bert**:
I had to think about giving my brother a one - way ticket to hell.

**Markov**:
Good work! I think he will tell him about it? 30 % to the correct thing to do that. I'm afraid so, you should pay more than last year ’ s very good terms and conditions of my life!

**Bert**:
This story, I think you should tell me about it. 100 % is the best way to put it. I'm feeling better, and I feel better because this story's about the problems and problems in my life!

**Markov**:
I am sorry.

**Bert**:
I am sorry.

**Markov**:
I'm impressed.

**Bert**:
I'm sorry.

**Markov**:
Experience a plus.

**Bert**:
What a mess.

**Markov**:
No, you jerk! You'll have to go to the third floor, to this one? Don't put mustard in it. You can still learn a lot of blood.

**Bert**:
Yeah, I know. It'll have to wait until the next day, but next time, don't put Giselle in danger. She might just lose a lot of blood.

**Markov**:
It sure does. Don ’ t buy a brick.

**Bert**:
He always did. Don't throw a fit.

**Markov**:
John manages to sleep. What degree have you had to move.

**Bert**:
He smiled at her. This time, she tried to smile.

**Markov**:
I've already been a long time to think about half an hour. Is that a window seat? It ’ s interesting that Americans can make it to be honest, diligent, persevering and creative people are working.

**Bert**:
I've only had a little time to think for half an hour. Is that your vibe? It's amazing how you can use it to ensure creative, diligent, persevering, creative people are involved.

**Markov**:
I need to understand her at moment.

**Bert**:
I want to see you every day.

**Markov**:
How do you often come here for months.

**Bert**:
Nor will I ever be alone for long.

**Markov**:
I guess so. Plus I'm going to join us. If you want to try it?

**Bert**:
I think so. But I'm going to show you. Do you want to see it?

**Markov**:
Hello, this is nice. I'll make sure that our hotel chef was trained in Florence. I'm sorry I can get through. It's unbelievable!

**Bert**:
Okay, this is it. I'll make sure that the fire alarm is still in place. I'm sure everyone will hear it. It's unbelievable!

**Markov**:
I really love him when he should be packed in small sizes for small women.

**Bert**:
I can tell you that they can be used in different ways for different purposes.

**Markov**:
Have a third country. Hey, Cindy? Can we take part in. Is this the right.

**Bert**:
In a good way. Okay, okay. Everything you do is okay. Make it all okay.

**Markov**:
And what dances do you need to try it on the table and I'll have enough. I haven't. We'll fly. My warmest congratulations on your arm, then, I will help. How nice it is, I quit smoking.

**Bert**:
Reaching between us, I reach to place it on the table. I'll drop it if I don't. It'll help. The sweetest consolation of my life - yes, it will help. How sweet it was when I was little.

**Markov**:
Well, there is something under my bed! The traffic jam is said that the contract ready by tomorrow and I am an excellent team player. He was just calling to apply for unemployment benefits? That's all right soon. This may be far - sighted, with a guy, but it is.

**Bert**:
Yes, there is money in my account. The flight attendant has just watched the plane pull away, and I am an expert poker player. I am not going to ask for the money. It's just too much. It may be heavy - handed, in my opinion, but it is.

**Markov**:
No problem. thank you for your kindness.

**Bert**:
Once again, thank you for your help.

**Markov**:
ok. RIB. How many stops are there in the same language as far as you know what to do your parents yet? Would you be back around 2: 30. Both the green consumer.

**Bert**:
J. D. : How many words are needed in the English language as long as you know how to get a phone number? Will you be there at 9 : 00? is my first question.

**Markov**:
When do we still arrived in LA the same.

**Bert**:
How long he had lived in all the world.

**Markov**:
Hi cousin! No thanks. I suppose so, but what will happen to me from nowhere and snatched the bag. Perhaps it ’ s a terrible gossip.

**Bert**:
Oh no. No one, I hope not, knows what will happen to me, here, in this place. But it's no big deal.

**Markov**:
Yes. Thunderstorms make the beds.

**Bert**:
Mr. Thunderbolt would make his move.

**Markov**:
I haven't been drinking tonight. That's fine, still a major avalanche was reported in the afternoon, Mrs. Bottom's up, we'll wait a second. And have you been? Have you talked to Alex ’ s calling?

**Bert**:
I haven't been here long. It's strange, like a giant avalanche somewhere off in the distance. No. Something's wrong. It'll be a while. Where have you been? Have you responded to Mom's call?

\chapter{Section 2: Epic}
\thispagestyle{empty}

**Markov**:
Would I? Put all that matters now. Yes.. He told you that.

**Bert**:
Do you? You know me, he said. Yes, I know you do.

**Markov**:
Told you this morning. You don't know how to use the few times. ! I'm trying to mess him up.

**Bert**:
Tell me that again. I don't know what to say a million times over. I'm going to pick you up.

**Markov**:
Such a terrible thing in Cave Springs?

**Bert**:
What a beautiful place. Hot springs?

**Markov**:
Two hundred to one when we want. The Office of - the - ground Conway - want to help you. Call what off? I'm Johns.

**Bert**:
A place to sleep if you want. The middle of - the - night people who want to see you. Call it that. I'm sorry.

**Markov**:
They wrong? You and your mom and dad. Nowhere - - Yeah, like great sex. Are you serious? Destiny took us in the middle of it.

**Bert**:
No questions. You know, mom and dad. - - - - Okay, no more questions. Are you okay? He found himself in the middle of nowhere.

**Markov**:
Mornay has come. Just like my service. I can't.

**Bert**:
Loren Hale will die. He raised the gun. I can't.

**Markov**:
Hartdegen. That's not consistent.

**Bert**:
Indifference? That's not true.

**Markov**:
Nobody was WATCHING? We're the good news this week we could get a message to her. They're.. I need reservations for three days to make it less and less to me. I just want to thank you.

**Bert**:
What about WATCHS? They're the only way any way I can get a message to you. They're useless. I paid you for two years to give them less and less to me. I just want to help you.

**Markov**:
You meant - - The King of Prussia, reducing them to worry. Oh..

**Bert**:
That was it. The Council of Elders was asking me to leave....

**Markov**:
Not so long to act this way.

**Bert**:
Taking too long to get his bearings.

**Markov**:
I just don't want to know a < u > Fuck me, what do you have to come because I checked the transfer, you did before. The Sick Boy reaches out and where I was a man - - - You're not gonna know then that dog - breeding surge in foreign coverage by local stations.

**Bert**:
I just don't want to know. > > " Tell me, how can you tell me that when you make a decision, you make it? " There it was, as if he were a man and - " We're going home, " a multi - layered voice, the voice of a woman.

**Markov**:
In the twilight of my way.

**Bert**:
In the twilight came a sound.

**Markov**:
I want to watch tomorrow on the Queen again? What do you want? but I'm out of the United Nations still making the monitor. You have a word with Adonis, but I am to receive you when you make it.

**Bert**:
I want to spend time with my family again. What do I do now? I'm sure that the United Nations is on its way. I have a meeting with Adonis, and I want to see him before I do anything.

**Markov**:
The same.

**Bert**:
The truth.

**Markov**:
well, perhaps - - studyin ' you could just be a member of the original tape. Besides.. At - at - at least start wearing a green flower?

**Bert**:
Sorry, just half - thinkin'you might not be a part of the whole thing. Sorry. " Oh, well, at least not for the opposite sex?

**Markov**:
Then.. Sure. I thought Gretchen sounded kind of psychosis, and you have a new speedboat.

**Bert**:
No. " Yeah, I knew it was because of psychosis, but I had a normal life now.

**Markov**:
It's lovely. Sally.

**Bert**:
It's Mr. Stone.

**Markov**:
some of us don't become a king, that assassination. On the count of three. Veil nebula. The Remans gave me.

**Bert**:
At least I didn't have to work for an hour. On the count of three, Garrick left. The doorman followed him.

**Markov**:
Well, what the polls, they'll shut down immediately. Buy a boring, all wars have innocent and an apple? Where is it when they stopped him. I put my mind.

**Bert**:
But, for the moment, I'd given up hope. Would the rest of the world be gone in an instant? This was not how I wanted it. This was my life.

**Markov**:
Your kid was some fucking fanboy. I was goin ' to nominate a new passion, about ten years now, Captain, are you doing this at home the last couple of desperate men with switchblade mentalities who run it and put you on your shoulders to the west side bunks, the jury can have a garden full of this part of it as real as you. good to let her.

**Bert**:
This guy is a total playboy. He is goin'to have a big party in about two hours or so anyway, with him showing up every time a whole bunch of teenage boys in switchblade vests can see him, and him pushing the buttons on his own belt buckles so the boys can get a room, but no one makes it as far as that, just him and me.

**Markov**:
Yes, of course.

**Bert**:
Yes, of course.

**Markov**:
It's just that. But I thought it was just warming up, then if you put the challenger is now.

**Bert**:
That's not true. If you think I have really screwed up, stop trying to tell the truth right now.

**Markov**:
< u > are < / u > Filmschool < / b > here. They voted me most of ' em on the London Times. Jackets off the hangman's deck - and helpless. Why do you mean that posh bird who gets the hiccups when she gets the Reynolds pen. If you feel that you are.

**Bert**:
/ a > bar < / b > barstool < / b > bar. You gave me one of'em, the night before. He looked at the barman's face with some amusement. What do you call the plump girl who gets the hiccups, who gets the long legs? Now I know who you are.

**Markov**:
Don't be such a pleasant rattle of my chest with big saps. How about me - - I love when you came to see me. If you ever say that. All right - - Something black - hearted snake.

**Bert**:
Don't get all that fucking shit out of your head, you puss. Think about it - - make it clear you want to kill me. And I will do it. All right - - you cold - hearted bitch.

**Markov**:
Maybe not.

**Bert**:
Or worse.

**Markov**:
What? All of a fine young people starting out in the face. ... I'm starvin ' and you owe Shaw, can you lie to me! Just a little at a time.

**Bert**:
Why? All of the good old times kept me in the dark.... I'd slept well, so I, uh, let him talk to me. Just a minute at a time.

**Markov**:
But he's zeroing in on our own dirty work and get some Goddamned pilots to fly low. What do you need to change this file on them like that? I haven't seen her in the car. Come on back home. Okay, Dad.

**Bert**:
Now he's zeroing in on his friend, trying to get the Goddamn guy to calm down. Why do I have to have a crush on her like that? I haven't liked her in the slightest. Come on, man. Please, stop.

**Markov**:
I don't.

**Bert**:
I couldn't.

**Markov**:
Elliot? L.

**Bert**:
M. S.

**Markov**:
She told him. He's the technical side, Selina, I'm, like, if I'm harboring a fugitive? Maybe she'll help me plan a car somewhere. Yes!

**Bert**:
I ask myself. What's this weirdness? Karissa thinks I'm... well, maybe I'm harboring a fugitive. Maybe she'll help me get a job here. No!

**Markov**:
You wanna come back to your house last night I sounded off like a man should ever see your documents? What? Can you trust me. You can still win the locals call Deadwood to play this one time, Gerry - - is here. I'm not crazy.

**Bert**:
You can go back to your house the minute you take off and no one will ever see your car. Okay? If you follow me, you will never see the kids at Rosewood Day or the high school kids, but this is crazy. I'm not crazy.

**Markov**:
I can't. I'm handing out swords. * being some local drug dealer, a great deal to get it. What, the shit out of it was on the outside. It's not really pain.

**Bert**:
I can't believe I'm into p * * n and that the drug lord made a big deal to kill me. Now get the hell out of here and hit the road. It's not just me.

**Markov**:
It's disgraceful.

**Bert**:
It's disgraceful.

**Markov**:
Nice talk, there's nobody there. Kirk..

**Bert**:
They say that there's nothing left of him now.

**Markov**:
Yes, sir. Yes. We're having a mid - career so they don't know what a king. I'm Mr.

**Bert**:
No, no. No. They're in their mid - twenties. I don't care about these people. I'm sorry.

**Markov**:
She's Not! We need the money back. You love me - - - Don't go making it with him? No. The most wonderful woman, never, ever since I kept having to take a look, Doctor, you'd be.

**Bert**:
It's true. I wanted my life back. I thought I loved you and wouldn't fall in love with you, either. The most amazing, most amazing thing was if you were going to lose your life, too, you'd die.

**Markov**:
It's 1997. One way. Break my neck that'll be on until we try? How the hell should I give you a doctor, Dr.

**Bert**:
It's nothing. Nothing more. What a state she'll be in when I return. Why the hell would I call her a whore? No.

**Markov**:
I did, Evelyn! I'm serious, darling! Thanks. Where's the ice is melting.

**Bert**:
I mean, yeah, I'm okay, too. Really. It's like everything is okay.

**Markov**:
Hey. That's all right, Modern American Poetry? Pull back. But, will yuh, I wouldn't have done. Masseria's been after me.

**Bert**:
No. It's not right. Feel the pain. Push it. No more. Push, it can't be right. Mab's coming for me.

**Markov**:
Everything under control.

**Bert**:
Everything under control.

**Markov**:
And they run away from this world. You mean your desire to kiss ass.

**Bert**:
But you stay away from the truth. You know you have to protect yourself.

**Markov**:
No can do it. My wife's father died. It sure is.

**Bert**:
I could feel it. My mother's father did. He always did.

**Markov**:
I've got something. That's my home town? I apply a phase reversed signal to triangulate on.

**Bert**:
I've got it. What's the IP address? I need a GPS tracking device to triangulate it.

**Markov**:
Is he dead? There was a joke.

**Bert**:
Was he joking? It was a joke.

**Markov**:
God - - he wipes the soot from his point of arrival? How you like being around me again? A mother knows what's up.

**Bert**:
But what if he cheated on her once, at the moment of conception? Would he love being with her again? Oh yes, that's right.

**Markov**:
So tonight, well, what'd you hear any bullshit about I pick one out, and you can't. No, wait. It's OK. Maybe nothing.

**Bert**:
But hey, man, where'd you get that stuff? You want it back, but you don't. Hell, no. It's nothing. Just nothing.

**Markov**:
No one will believe you me, damn you. What do you think he'd advise her to stay with us, or did Clay Shaw is important. Gold dig him up between the teeth and he's back, ' A?

**Bert**:
No one can count on you, not anymore. Why do you think I'd ask you to come with me when and if the rumor was true? To look him straight in the eye while he's at Triple - A?

**Markov**:
Call Chub Meritt and have some more about things. or you're sorry - - Got a warrant for her.

**Bert**:
Call Deb Dent and talk some more about it, if you're interested. " Got a question for you.

**Markov**:
Which gulls, Mr. I have found you in the car.

**Bert**:
You linger there, too. I just saw you in the mirror.

**Markov**:
Somehow or other police would know that road.

**Bert**:
He knew the police would find the body.

**Markov**:
Listen to music! Away to fuck. Maybe I dont know, maybe not in the morning.

**Bert**:
Not with her. With only her. And he would never sleep, especially not in the dark.

**Markov**:
You can't save everybody. You guys made me go. I like well what I got it all.

**Bert**:
I didn't lose it. The world sucked me in. And as for me I lost it too.

**Markov**:
What was that for no reason for panic. So what does that mean? No kidding.

**Bert**:
It will work, I want to say. So what do we do? I ask.

**Markov**:
We all agree with you. She keeps screaming to the president is off - load of bombs and 1 on weekends; your Mother's still sleeping. but I would understand. Immediately. Let's have a look at you, too.

**Bert**:
We all agree with her. She keeps saying that the world is half - full of 1. 5 million people and that everyone's going crazy, but you never know. Okay? Let's take a look at it, then.

**Markov**:
This is the quietest I've ever heard from him before in my life I ever dreamed of it.

**Bert**:
This is the sweetest I've ever heard from her and in my heart I am proud of her.

**Markov**:
He's a corporal or a girl. You mean we're not screwy - - Where's my father took me fishing here when the artificial intelligence?

**Bert**:
He's a corporal and a sergeant. I hope you're not picky. " Why'd my father let me go out with a fellow soldier?

**Markov**:
Maybe you should.

**Bert**:
And I did.

**Markov**:
Chauncey..

**Bert**:
Anal. Math.

**Markov**:
Fear and Desire. Yes - - but is it? He's reaching in, what is they, they'd have another drink!

**Bert**:
No. No. No! " What is it? He's dead, and so would I if I'd had the chance!

**Markov**:
Their next target is Albuquerque. He takes around the office. Hot water bottle.

**Bert**:
The next stop was downtown. He glanced at his watch. His phone rang.

**Markov**:
I'm afraid I do. I need you to be true. Rick.. Isn't there some other time? We've got to get involved, its - - - but how do we do.

**Bert**:
I'm sure it is. I want it to be over... But isn't there any other way? We've got to get out of here.... What do we do.

**Markov**:
I can't talk or I'll have to go.

**Bert**:
I can't, but I'll have to try.

**Markov**:
He's been waiting too long. That would sap anyone's self confi.

**Bert**:
He'd been gone too long. That would sap tonight's emotional suspense.

**Markov**:
And she was an accident, fire the sonofabitch went to a shop. Mama said - - You're wrong about everything. One last push.

**Bert**:
Maybe it was an accident, but the sonofabitch fell into the river, I guess. " You're right about that. One more thing.

**Markov**:
There ought to let Sonny handle it - - we appreciate that. Thanks. I suppose. You.. where's the car, a photographer.

**Bert**:
I want to see you like this. And I love you. God, I want to cry. But he's a man, a man.

**Markov**:
Nothing to do the press that there is no S on his own. You should stickaround sometimes. No.

**Bert**:
Time to show the world that she had a life of her own. She could go back home. Now.

**Markov**:
Keep your voice down. Will you be available? Well not exactly sure, let's drink to God, it's a mistake, don't ask me, I will respect the sentiment. We meet at City Hall, and I'll take your bath? You choose the wine.

**Bert**:
Keep your voice down. Can you be sure? To help be sure, let's pray to God that there's no danger and don't hurt anyone. I really appreciate the offer. We meet at the bar, and we'll have a drink. You get some rest.

**Markov**:
It's just a test afterward.

**Bert**:
It's just a little bit.

**Markov**:
. it was the last one out there.

**Bert**:
But I was the only one standing there.

**Markov**:
But next time, phone - - please - - regrettably appropriate for a second time and location for the next business trip. How about Susan Lefferts. You're not being funny, James, this is just as free as a dog's hind leg. They want you on report if I say that's a lot. Thanks.

**Bert**:
Maybe next year, and maybe not today, but regrettably, at the same time, not on the same page anymore. What about the Lefferts? You're just being silly, honey, this is almost as big as a man's six feet. I want you to know that I know it's a man. Please.

**Markov**:
I bet him a favor? When I send to Commander. And your all set - up is the center of the sting. This one?

**Bert**:
He owed me a favor. Wanted to talk to me. Maybe this little hook - up was the beginning of a relationship. Which one?

**Markov**:
Who's been talking about. On the cake already in the middle of the planet? Pull up! but..

**Bert**:
He'd been thinking this : Is the time right in the middle of the night? Pull over and...

**Markov**:
And - - Hello, Scott. Intensely. I remember you. Don't have Weather Channel in the car.

**Bert**:
- - - Oh, no. Insane, I told myself. Don't do that again in the future.

**Markov**:
That I killed Iris too, Anderson, Kate. Well, both Beverly Hills. Yes. How many women. The word torture does not walk out?

**Bert**:
" You know those people in California, right? Well, in Beverly Hills, California. So many people. Anybody who can help with that?

**Markov**:
This is the wrong window again - - nothing it produces reaches the platform? They're handling the fine is yours. Yeah - - It's almost like a happy pig, I've read - -!

**Bert**:
Where is the ticket now? - - There it is, the ticket! You're lucky the girl is here! - - - She's acting like a little girl! I've got it now!

**Markov**:
Say everything. It's our only hope. I feel about it now. Your gun.

**Bert**:
My mother. She's the only thing that I care about right now. My mother.

**Markov**:
Deliver that safely to his knees, though. Miss Daniel, hang in the river. And the hell - - they pop back to Resurrection.

**Bert**:
Delivering me to my parents, too. And now they are in my room. What the hell? And they are waiting for me.

**Markov**:
Not every girl makes a good one. Kip.

**Bert**:
Just a man, a good man, you know.

**Markov**:
Your brother's always looked after you leave there's a good one on purpose? that way, too. Man, hey. . That's right.

**Bert**:
His head's bleeding. If you think there's a wound there, it looks pretty bad, too. Almost healed. " " He's fine.

**Markov**:
Blood has been haunting Leon. Have you been? I mean Is that the tongue.

**Bert**:
I had some, too. Have you eaten? I asked, biting my lip.

**Markov**:
Yeah.

**Bert**:
..

**Markov**:
There's a farmhouse. No I didn't know what that means.

**Bert**:
It's a dream. But I don't know what it is.

**Markov**:
He said they can. I didn't even warm them a dirty tramp - - It's my opinion it took several photographs, there's a monster.

**Bert**:
I know you did. I didn't even call you a " pussy. " It's my fault you took the pill, that's a fact.

**Markov**:
I'm not too rowdy, but it's yours. No, please! and that we're up to it.

**Bert**:
I'm not being sent away, if that's possible. Okay, well, then, you're up to something.

**Markov**:
Sorry. You guessed it - - - it's better if Simone stayed single. I'm here.

**Bert**:
No, I just - - - - It's okay. I was there. I'm here.

**Markov**:
No kidding. That doesn't tell us what form they would! Me? Yes.

**Bert**:
No way. He won't tell me what color they are. No. No.

**Markov**:
Where did you see the greatest frontier since white men become friends. Hay.. Precisely. They're watching for him. Look out, too.

**Bert**:
And then I see the stop sign. The two young men waiting. Yes. Precisely. They're waiting for me. Help me, please.

**Markov**:
Somebody always does. No, I'm not certain. Splendid! I have to fight. Life doesn't have a strict and hallowed sect.

**Bert**:
He really does. Well, I'm not surprised. Splendid as he used to be. He doesn't have a big, hallowed bed.

**Markov**:
But I don't want you to give the tickets changed for dinner. Is that it? Thanks.

**Bert**:
" I don't want you to leave your clothes on for me. Is that okay? ".

**Markov**:
And still in the emergency room - - Recognize the beat.

**Bert**:
They were in the living room and he recognised her scent.

**Markov**:
it'll sound like such a bright side though.

**Bert**:
It'd seemed like such a good idea then.

**Markov**:
Okay, I come home? thank you!

**Bert**:
How dare he come here, damn it!

**Markov**:
Did you ever get around without a doubt. At twenty - six. He will be will be over, what about the idea? You carried a gun pressing against me.

**Bert**:
And I would love him without a doubt. Chapter Twenty - One Tristan What would happen to me now, what was my future? I felt the wall push against me.

**Markov**:
I'm just.

**Bert**:
I'm sorry.

**Markov**:
You eat Chinese, watch your mouth. Well, I guess he's pretty worn out. Would you put it in, right? I thought you were a lot of care. Know what I am.

**Bert**:
Just wake up and close your eyes. Yeah, I think it's pretty far away. Will you let me sleep, please? I thought I had a lot of questions. About who I was.

**Markov**:
But never to touch.

**Bert**:
But not by much.

**Markov**:
Me, too. What are you going to tell me who the claiment was, is it? I can knock a man would have let us out, too. I only dog paddle. What?

**Bert**:
Me, too. How are they going to tell me where the Tangent is and destroy it? I really wish the government would just let me go, though. I can barely breathe. Why?

**Markov**:
Yep. It couldn't have known.

**Bert**:
No. He couldn't leave her.

**Markov**:
Maybe he just stop it, don't be like this. Christopher, you don't have meetings about rainbows. Half a day now. I thought it was all Carlos left her award in the head of the Thirteenth Dalai Lama cannot fall from the Post. Just a moment, don't you?

**Bert**:
If you can do that, don't worry about it. Remember, I don't need anything but injections. Just a minute please. He knew that once he had inserted the needle into his arm, the Eleventh Dalai Lama would come into the room. Just a minute, isn't it?

**Markov**:
Nay, I really want to go out with you? Hello there. Yes, it's our responsibility. Why's that? I want the dough?

**Bert**:
Granted, I just wanted to hang out with him. Why not? Now, it's my turn. What's next when I get some answers?

**Markov**:
No! What scheme? Don't eyeball your kids handling the sales part.

**Bert**:
No. What now? Don't eyeball the guy on the other side.

**Markov**:
This is really you, but this one. I told you to be on duty at the league office - type killings. So, he needs. ?

**Bert**:
This is about me, not a girl. I want it to be about me, the allure of a girl. So, what is it?

**Markov**:
I tend to doubt. I forgot to pick the right track. It would kind of this place goin ' on ' em back to her? No big deal.

**Bert**:
I had to go. I had to find the right guy before I got out of this mess and'find'someone close to me. No big deal.

**Markov**:
Not so fast. Real polite. .. Ice skate. Oh, really.

**Bert**:
Not so much. So much... No, she thought. No, no.

**Markov**:
I think they have nothing to go into his chest.

**Bert**:
I wished I had something to put in my pocket.

**Markov**:
Doesn't she? What else can I look?

**Bert**:
Didn't I? Where else would I be?

**Markov**:
Its all right. You're gonna use me. that's the lamest idea I've ever met. Jane, I'm gonna hang no more fighting here.

**Bert**:
You were right. You're gonna love me and that's the nicest thing you've ever said. Well, I'm gonna have a say in it.

**Markov**:
It's that they must come in before? Is there something I programmed you to throw me the bad children, and I'm through with that fella killed Caesar? ..

**Bert**:
How's he to have been here before? Is it because I want him to show me his dark side, that I'm here, that Thane is here? No.

**Markov**:
I've got ' em started fightin '. This has to cancel the fight. Mooning over Julie when we talked about this some kind of action on the other nuns found out that door, the darling of the deals going down the volume on our flight status.

**Bert**:
I've got'em all comin '. He had to get a grip. Listening to music, he listened, drinking a cup of coffee as the two men walked through the door and the beat of the music turned up the volume to a higher pitch.

**Markov**:
You want to be opened.

**Bert**:
I wanted to be alone.

**Markov**:
I thought - - Same trees. !

**Bert**:
He said, " The question is!

**Markov**:
We need to know a little early. If the bus. Goodnight chairs. Oh, I was simply a chance.

**Bert**:
I had to get a job here. On the phone. In my office. Alone. It was worth the wait.

**Markov**:
You've got it: no shrinkage. ' Only one thing - - with my husband the hero in Vietnam.

**Bert**:
I've got it all back under control. " For one thing, everything about him was a lesson in manners.

**Markov**:
Well, how's Donna? They seemed to be a heavy punter. We're on the show tomorrow night, I'll pick you up with you. I'm sorry.

**Bert**:
Hey, where's Dad? He used to be the local ranch hand. We're at the ranch over there. I'll bring something over for you. I'm starving.

**Markov**:
I'm a civilian. A monster. I hear you are witnessing genius! And I'll mount you on the day before you get lonely after vespers? Especially compared to Venezuela - the RSVP's are amazing.

**Bert**:
I'm a monster! A monster! I know you are scaring me. But I'll see you again one day when I get back to Estella. And thanks to you, the EMT's doing great.

**Markov**:
Yes, but you're father's in a moment please. You know what's out there. Who gives a man?

**Bert**:
Yeah, but you're what's in the world now. You are what's out there. Who needs a friend?

**Markov**:
Kalen, look.

**Bert**:
Laylen, too.

**Markov**:
150? Current version.

**Bert**:
No. My fault.

**Markov**:
I can help them. Look, you don't smoke. Go ahead. I got it.

**Bert**:
I can do this. God, I can't breathe. Come on, just do it.

**Markov**:
Tomorrow night? Well, no fuck that up too late now, yeah, sure.

**Bert**:
Last night. Yeah, I messed it up pretty badly but, well, okay.

**Markov**:
And you don't wanna use my butter money.

**Bert**:
" I don't even have the insurance money.

**Markov**:
Yes, I make a phone call. I'll open a little.

**Bert**:
Look, I got a phone call. It's just a call.

**Markov**:
I.. Have you decided that one, eh? For all his minions are marked that way. Triple! Monsieur Blaine, if she's alive.

**Bert**:
No. " But you know this guy, right? Maybe all the goons are in the building. Maybe they killed him, and he's dead.

**Markov**:
Where are you gonna hide a black, one of the day I want the melon? Or it may seem like our boy a little counseling.

**Bert**:
How could you ever be so happy, even if that day had been a memento? How you could look at that day with such joy.

**Markov**:
I didn't know it exists. I don't know you've at least 30 days in peace? I'll be in this hotel? How do you think?

**Bert**:
I don't know how long. I don't think I'm at least two weeks from the time I'll be in the hospital. What do you think?

**Markov**:
You're right. Out of the Chinese. I been out here from Cable Junction.

**Bert**:
They're here. One of the guards. They come in here from the back.

**Markov**:
Ah, no, no. In the trunk was opened, Marty. He was myopic. the information and < i >.

**Bert**:
No, no, no. But the door had closed behind him. He was interjecting a text message : < Hello >.

**Markov**:
I wanna know.

**Bert**:
I should have.

**Markov**:
Go to sleep, hon? If they don't arrest you, Alexander will have your little wormy brain, Gabe.

**Bert**:
Go to hell, hon. If they don't eat you, they will eat your pretty busty ass, too.

**Markov**:
Won't do any damage to city property. Now his wife should be ready shortly.

**Bert**:
Don't do any harm to your family. And your father will be back soon.

**Markov**:
Did you? Noooo! I don't blame you. 45 - - Look - - Because I don't need to call for a hand here. . sometimes I feel, huh?

**Bert**:
Do you? Oooh, I don't get it. - - - - - - - You don't have to ask for a reason... how you feel, right?

**Markov**:
Nothing? team. We're gonna have my own mescal. Andy? The new soldiers can't fight it.

**Bert**:
Oh my God, I'm gonna make this woman miscarry. No. The poor woman doesn't deserve this.

**Markov**:
I beg you - - last night he disappeared? Do those big four, casualties. We know now they are? Christ, Jerry. White gangs is tweakers and a half.

**Bert**:
I saw them yesterday, the night I died. All the other attacks and attacks. I know what they are. Something about them. A pair of tweezers and a knife.

**Markov**:
Drop it. ..

**Bert**:
Tell me. Please.

**Markov**:
Get against the Italians.

**Bert**:
Ready for the kill.

**Markov**:
I know you had to have a nice big breakfast. But the Mayor of Darktown.

**Bert**:
I think I need to get a good night sleep. Like the likes of James Bond.

**Markov**:
She hasn't looked at it. The money! So don't feel you should have done it. if they concern me. Needle marks, Hooker.

**Bert**:
He hadn't looked at me. The police. I don't think they would have done it, but they killed me. And my mother, too.

**Markov**:
We're all involved with running dope and dollar signs and ratings.

**Bert**:
They're all obsessed with the dope and the alcohol and drugs.

**Markov**:
Where's my damn money!

**Bert**:
It's my own fault!

**Markov**:
So that's cool with me for? I promise this: fifteen units Mountain View. So why did you get his trousers and braces. Wait!

**Bert**:
And there's a thank - you. He got them right here in Mountain View. And where did he get those knee - braces?!!

**Markov**:
. Who is this? I want to come with me? Tell the captain say?

**Bert**:
" What is it that you intend to do with me? " the man asked?

**Markov**:
What do you have a weak signal over there, in steps Carlton Fisk baseball card. She was just wondering if, say something now. Well, it's living human tissue.

**Bert**:
Or maybe it has a phone number on it, or a David Fitch credit card. It looks much, much, much better now. No, it's not a card.

**Markov**:
They put the picture around you. Sure you can almost smell the urine of menopausal Italian nuns. Here, your first time.

**Bert**:
I smell the blood of women. But I can also smell the blood of menopausal pregnant women. Yes, pregnant pregnant women.

**Markov**:
Well don't think you would bring, He has to go to your face! What matters is the god's honest truth. Well, she had hanging - - have you down and we're out the word from me! Night jobs - - he was talking about fucking twelve different girls?

**Bert**:
I don't think it will matter. It has to be in your eyes. What matters is the God's honest truth. Now, you see - - you let me go, you're taking me away from you. Holy shit - - he was talking about those two little girls?

**Markov**:
If I'm not sure. ...

**Bert**:
" I'm not sure I can sleep.

**Markov**:
How reliable is this you assholes, Taylor. I'm not smarter than us? But Johnnie runs Chicago because Gino is his new girl friend. Fink.

**Bert**:
How stupid are all these idiots for thinking that I'm even smarter than you? " Donny asked Mr. Santino and his new best friend, Dominick.

**Markov**:
I don't know. Ten - four - four.

**Bert**:
I don't know. Four - oh - four.

**Markov**:
Thanks.

**Bert**:
..

**Markov**:
with what * you've done to her room, just wrote the opening tonight.

**Bert**:
" Look what you've got on it. " I read the note again.

**Markov**:
What's the point, Commissioner. Running to her! I was a little compassion.

**Bert**:
That's the guy, though. Looks to me like he needs a little help.

**Markov**:
Sollozzo and McCluskey are going to say.

**Bert**:
Palaemon and McCloskey were quick to agree.

**Markov**:
What is this going to dinner with us? Wait a minute and already she's making progress. an I says, you didn't write down everything this community. Airbag, Radiohead, from OK Computer.

**Bert**:
When is she going to leave with him? For a moment, maybe he's imagining things, but he knows that she won't be back until tomorrow morning. Checkpoint : Level 1 of Grand Central Station.

**Markov**:
Have a great driver, always. Follow!

**Bert**:
Be a good boy, boy! Go!

**Markov**:
The salesman never saw the other clerk - Harrison Feed and Grain.

**Bert**:
The film also tells the true story of the monarchs of Zaire.

**Markov**:
We can talk. Gaston told me about Scotland - - Shit!

**Bert**:
We can talk. He told me about you and - No!

**Markov**:
I don't think I've got a steady worker. feel my lips, and her faith in everything here. Then stay away from windows, you can take it. Oh, Chad - - Oh, it's in Italian Operas?

**Bert**:
I can't believe I've hired a good man to keep her safe and put my trust in her life. Just stay away from her. I can do this. Please, I beg. What if she's reading Soap Opera Digest?

**Markov**:
When you're dealing with? You're psy - chiatrist? well, in the movies the young ones called home, that's gonna happen to Ms. < u > hiding < / i > Deliver them to mind. Two more minutes!

**Bert**:
Who you're dealing with? They're psycho podiatrists who just went to the hospital a few days ago and now nothing's gonna happen. " < < i > < i < i > Delivered the message. Ten more minutes!

**Markov**:
Here, let me see. Kate. Quietly, please. She said she'd been bitten by some animal in the Rye < / u >.

**Bert**:
Please, let me go, please. Faster, faster. She thought she'd been hit with an elbow to the head. No. " No.

**Markov**:
Hi, mom. Does that mean, sie war gleich tot - brauchen kein angst zu. Yeah, well, eh?

**Bert**:
Well, well? Does that count? Sie, bleißt, wissen kein leben, right? Well, well, well?

**Markov**:
Andy, disapproves of the Psychic, ' I broke my hand reminds me of treating her right ear, and guess who was not a thing, go be a < u > sorry.

**Bert**:
No one disapproves of the Psychic. > Something in his voice reminds me of not my own father, but someone who knows what his fate will soon be. > > Not yet.

**Markov**:
I got pain an ' Ned's an ' happy. Why have you heard was coming back. Sid and Breeze look sideways at each other. .

**Bert**:
It feels good. " It's not so bad. The noise he makes is getting louder. He and Rann look over at each other again.

**Markov**:
You're beautiful what you're calling her a whiskey man myself of this? Before the guy who doesn't even say it's poetic. What do ya. Been years since then. We're in a camel.

**Bert**:
You're right, you're giving me full credit for all of this. For a man who doesn't even know it's true. But not now. Ten years from now. You're not a camel.

**Markov**:
Did you have children. I want to tell me what you do need a lot of Good was done to save a few shocks to your belt like a horse till it just means the Sacred Scrolls aren't worth a squad up there on out of quitting. , No, no money.

**Bert**:
But you have to. You have to convince yourself that you really think a lot of money is going to stop some guy busting into your house with a gun, which really means the other Ts can't find the gun and use it, and Ts have, like, no money.

**Markov**:
They're called squirbs.

**Bert**:
They're just quarrels.

**Markov**:
What's this? Would you like to have is getting old! is treason against France on her part.

**Bert**:
What's wrong? All I need to know is that it all happened, in part, in part.

**Markov**:
Your brains, dig up all my regular line of crap ' cause of death.

**Bert**:
This whole stupid hookup with a whole bunch of guys was because of me.

**Markov**:
I'm saving them for fifty G's, but go ahead. Don't just stand there talking! Yes, please, Reggie. it very hard.

**Bert**:
I'm asking you for your mother's number, go ahead. Don't just stand there waiting. Please, God, stop making this so difficult.

**Markov**:
We should hear his story? Come on! Legs, butt. I can't kill everybody? What do you want.

**Bert**:
You can hear my voice. Hold on. Legs and legs. You can't hear me. What do you want.

**Markov**:
Barney! Then say it was the last place for mojitas.

**Bert**:
Actually, I thought it was the perfect place for mojitos.

**Markov**:
You know, I love you, sir. . if you drink. Wait, uh, I've tried them all before. .. We haven't even begun and you're fucked.

**Bert**:
I mean, I see them, but... they stop. And, yes, I've seen them, but... they haven't even stopped until they're gone.

**Markov**:
No - - in - the pay of the border. I'll be back and rest up from the Air Force One. My father could see what I told you, too. What the hell she isn't too much to see a doctor?

**Bert**:
" Yeah, close to the edge of the forest. I'll come back and drop you off at Air Force One. Your mom will remember what I told her, though. How the hell it wasn't so hard to get a job?

**Markov**:
Yo. Mirrors, then, because I'll be O. My history.

**Bert**:
No more regrets, though, because she'd been there. For him.

**Markov**:
I try not to untrigger it. His names Horrace. Please. You're out of here, arresting me?

**Bert**:
I try not to sniff it. This is sardine. No. You're out of here, tailing me?

**Markov**:
Why are you from here.

**Bert**:
Where are you going?.

**Markov**:
Fire the whole world. List. No.

**Bert**:
For the entire night. No. No.

**Markov**:
Well I do.

**Bert**:
And I did.

**Markov**:
Zack, when you played out with me the day? Anything else? ... What if I get laid? Don't even think about hiring me.

**Bert**:
And where have I been living for almost a year? What if I... what if I get fired? Don't even think about firing me.

**Markov**:
You want to hear, isn't he? Now there you are.

**Bert**:
He has to be, doesn't he? And there you go.

**Markov**:
She had them make you cut me.

**Bert**:
He let her learn to trust him.

**Markov**:
Go ahead. I can't stay on though and they practically wiped a nation - wide decompression has been enquiries from the shaking. What are you, Ethan! One does not.

**Bert**:
Come on, they won't wake up, and whatever had caused the drug - induced decompression has not receded from their minds. Neither will you, Doctor. It is over.

**Markov**:
! It's there now. We are secured. We're working as fast as you, and I know woman well. Got a problem with the debate team together.

**Bert**:
" It's okay now. You look good. You're looking as good as ever, and you look really good. So much for taking the damn thing off.

**Markov**:
Nothin '!

**Bert**:
Nothin '!

**Markov**:
What do you want to go to a hospital. How do we know it's at the International Maritime Convention. Linda, see, I guess I will.

**Bert**:
Why do I have to go to the church? How do I know it's the New Hope Baptist Church? Because I know where I think it is.

**Markov**:
I wanna clean. Can I at, them people shoutin ' your ass. Babalugats, bet against him.

**Bert**:
I am here. An'you're not kickin'my ass. Placida stepped toward him.

**Markov**:
Do you and I thought, let's hear from you. Just like taking a squad down from Berkeley soon. MacFarlane's failure? !

**Bert**:
So, like I said, let's refrain from arguing. We are taking a step back from being Mr. MacFarlane's girlfriends!

**Markov**:
He fucked up his room? Here we go tonight? Was it that, State - - But, honest. Everybody's happy.

**Bert**:
Just clean up the mess. Can we work together? Make it work. - - - No, no. It's okay.

**Markov**:
I'll go straight! I'm worried. Ronald is one of those things are very intense war. For the record.

**Bert**:
I'll be fine. I'm fine. This is one of those that changed my entire life. For the better.

**Markov**:
When I'm not that kind of mine tried one of those. both. And what happens to deserve this? It's okay.

**Bert**:
But I'm not just one. I am one of them, too. So what happened to all that? It's over.

**Markov**:
We all have to be experienced to do. YEA, ART THOU THERE? At least. You, too.

**Bert**:
There just had to be something to do. YES, GET THROM THERE. At last. Me, too.

**Markov**:
Very big. What happened to look it up with the number.

**Bert**:
Almost there. He had to follow it up with a plan.

**Markov**:
The environment is the best thing that I have a good number of volatile compounds - - Oh, how can I help you, you know my good man, really. Heem likes to treat me like that - - I don't know. Grant. Yeah, sure. Nah, I mean, into the bathtub.

**Bert**:
The world is a good place and you have a good understanding of it. - - Grant, how can I help you? You are a good man, Grant. Gabby wanted to ask him about it. - I don't know, Grant. You know what? Well, I found it in the bathtub.

**Markov**:
They viewing area below us will. I'm not in the same job but it broke on the board - - but I knew he'd love it!

**Bert**:
A whole lot of it is. I'm not on the show, but I was on the show once, and I think you'll like it!

**Markov**:
FUCK. My meat and boots?

**Bert**:
FUCK! No bra or panties?

**Markov**:
' And she says, ' You were planning at the fights we all get old and she gave me a very long, long, gentlemen. So, you mean? A kid really, I think it's proper for a bed, with your primitive tanks and planes - - by admitting it I might kill you Walter.

**Bert**:
' Then he said,'We were good in every way we could be, but they gave us a little push too far, too. Yes, I know. And, yes, I know it's true in my people and in my own people and people, and believe me, I can tell you that.

**Markov**:
The digital conveyer?

**Bert**:
A freight hauler?

**Markov**:
Carl Smith. It's a clean little spot where there ain't nothin ' to the man who walks this < / u > did < u > our house to invest. We're going to do with a girl? How long since he left last night.

**Bert**:
" No. It's a nice little place and there ain't nothin'but the man who owns it has < u > and < u > a place to stay. You're lucky to be with that man. How long have you slept last night.

**Markov**:
You would think there really is.

**Bert**:
He must think I really am.

**Markov**:
.

**Bert**:
.

**Markov**:
Is it sad to leave, get her and all that is desperate which we are feeding the poor girl never came up - just so you don't respect the shit hit the bottom, go out there, waiting - we got rid of the chair, and here I was crazy. Tell me this way. There's one other penguin and when she worries she yells. The wireless, or.

**Bert**:
Was it time to go and see her or was it the fact that you were sure the little girl had woken up, just so you wouldn't see the clock on the wall and be right there waiting? So I went out of the room, and then I went in. Keep it that way. She's a little pale, but when she smiles she smiles. Maybe, just maybe.

**Markov**:
Our grandchild, Auggie. A.

**Bert**:
His grandchild, Gov. D.

**Markov**:
Nothing.. Got caught on tape making the metal getting warm - up fight, she was, but you're determined to be discourteous. Are you going? The REAL heaven, I assure you. Leave the tree is a prisoner, Taransky.

**Bert**:
No. But you blew a hole in my stupid, fucked - up head when you left, and you're going to be discourteous. Where you going? " REPLY, I asked him. " My house, my car, you know.

**Markov**:
Thanks for the last gurgles, and quit.

**Bert**:
Outside, the water gurgled up and down.

**Markov**:
no screwing around. Wont do what I done the hard part. See you tomorrow, I like your signature on the computer, of course. .. Yeah.

**Bert**:
Stop fooling yourself. Dont make sure you pick the right one. See you tomorrow. I have your number on my phone, of course. Okay. Okay.

**Markov**:
You think so. I'm at the Brecker Hotel even as a personal question?

**Bert**:
I think so. I'm in the Bunker Room to ask a stupid question?

**Markov**:
I ain't Rockefeller, and how much? . I prepare food. Wheeler's secretary, Lydia, isn't she? I'm going parading before it's begun. How do they read about you.

**Bert**:
I wasn't sure, but how much longer do I need Mr. Anderson's help, anyway, don't I? I'm always paramount when it's necessary. Nor have I heard from him.

**Markov**:
Good evening, Mrs. Wouldn't deceive a child actress? When you're really nuts. We'll take a look? Before coming here.

**Bert**:
" Oh, no. Don't conjure a mental image. But they're out there. I'll take a look. Come over here.

**Markov**:
next time it's just a little rule, I would like to see you too, Dad wanted to, but whenever I went back to get somebody in there.

**Bert**:
This time it's in my own head. I would like to hear it again if I have to, but then I look up and see him standing there.

**Markov**:
But you're happy! What night? . Under the skin, I will not speak English, please.

**Bert**:
But you're safe. At least temporarily. Under any circumstances, we will not meet again, either.

**Markov**:
00 policy? I think you are. Did Marylin end up selling appliances like my working. You're changing. How we doing?

**Bert**:
I mean, I know you do. Let Margie end up making it into your life. You're mine. Do you understand?

**Markov**:
Could you locate him, his mother. What's up? Brock.

**Bert**:
Can you hear me, little girl? Something's happening to me.

**Markov**:
Leonard McCoy, you don't owe them a goddamn working man! Juarez. It's crucial I not suggest to reconsider. I think the killer keeps leaving articles about him? Okay, are you doing?

**Bert**:
" Oh, please don't call me a hardworking person, Juarez. It's something I would like to reconsider. You think the media is saying anything about it? What else are they saying?

**Markov**:
She killed herself a completely traditional program will be shot like a nocturnal emission?

**Bert**:
Who knew that a really good show would be better than a no - show?

**Markov**:
- - - - crooked as the Moses of dirty little secret. To hide the keys. We all lost our children. Look at the highest place of deep regret, what is it true, but he's got.

**Bert**:
- - - As well as telling me his dirty little secret. To tell the truth. To keep it that way. And in that one moment of deep thought, how is it possible, what he's doing.

**Markov**:
Please. ! He was humming Mother Machree.

**Bert**:
Please. " It was all about strife.

**Markov**:
What for? I'm sure it's not the orgasm. There's no time to destroy yourself, I just want you more expert. Awfully short notice. We don't have to explain.

**Bert**:
What happened? I'm sure it's not an accident. There's no way to prove it. I just finished a short report. A stressful short report that I don't want to finish.

**Markov**:
You could visit me, sir!

**Bert**:
I can feel it, too!

**Markov**:
I'd kinda like the trash barrel? I guess Emily isn't going to help. Maybe tomorrow I'll win. But surely, ultraviolet rays would pour in, James.

**Bert**:
You're acting like a bully. I know this isn't going to work. But soon you'll see. And soon the ultraviolet light will kick in, too.

**Markov**:
She nodded, like death. - - well, I'm Haitian - - what's that smell? Well, good - - Nuke won't go to customers.

**Bert**:
He paused, thinking. - - - Oh, I'm sorry - - What's this about? - - - - - - - Don't lie to me.

**Markov**:
Tell us the way I want a divorce! Nobody wants to see you later.

**Bert**:
Make him the man you want to be. He wants to make you happy.

**Markov**:
Where did I get to you. Then don't let those Reds stir you up.

**Bert**:
How did it get to you? Just don't let the beast eat you alive.

**Markov**:
Like YOU know? I guess Sidney's been puttin ' up! I would never've found it.

**Bert**:
Do you understand? I know he's not gettin'it. I should never've done that.

**Markov**:
I think I got two officers in the cafeteria, there's a couple of blocks away. We will, but I'm not a spear gun, Earl! Mean to break it. Which, in the story with Robert E.

**Bert**:
I think I have some food in the car and it's a couple of miles away, you know, so I'm making a good impression, too. Time to do it. Yes, in the car is some food.

**Markov**:
Too late. He cares about marriage, what have you all right? You know, the business. This is one thing and now they must have gone a hundred directions at once. Spock, where we are, it was impossible not to be!

**Bert**:
Too late. He knows about you, but are you all right? You know all about me. I was young, and thought I could kill half a dozen people at once. Spoken as if I knew that it was better not to die!

**Markov**:
I think that's what happened. He is readying the Curtain.

**Bert**:
I think that's what happened. He was breaching the Curtain.

**Markov**:
HAMLET?

**Bert**:
THINGS?

**Markov**:
He taught all this for? Uh - huh. Who is we all get together - - but the most ridiculous thing I've been telling you that Chris might work. The media has caught wind of his whoppers? You talked to him and he'll have to be able to do?

**Bert**:
I heard all this before. - Uh huh. How will it all end? - - And, more importantly, I've been telling you how it will end. The man has grown tired of the whoppers. You talk to him and there'll have to be something for him?

**Markov**:
It'll be a copper mine near here in two days later. We need light in what you want?

**Bert**:
There'll be a coal mine out there about ten miles away. You need me for what you need?

**Markov**:
Well, she plays in this world; and his wife and mother wanted to. Well..

**Bert**:
Anyway, he lives in my house, where my mom and dad used to live...

**Markov**:
Question is, you're stupid. That one. I feel great. .. It's the Steely Dan song.

**Bert**:
This is because you're beautiful. No, because you are beautiful. No. It's a Steely Dan song.

**Markov**:
Good - bye. I'm just happy to help you? And I make my blood.

**Bert**:
Good - bye. I'm so glad to see you. " You have my word.

**Markov**:
More slop on the stove. Thank you. We'll go out on your team do. That's because Ms.

**Bert**:
I plop onto the bed. Oh God, I'll stop crying when the tears come. That's what matters.

**Markov**:
He's going home, and appreciate you trying to charm your way or another. I'm not calling Jimmy.

**Bert**:
He's doing it. I want him inside me, one way or another. I'm not doing it.

**Markov**:
No, it's nothing. I'm in a snifter. When you are?

**Bert**:
No, it's not. I'm not a snitch. And you are?

**Markov**:
Not since your charming little daughter? I couldn't stop thinking about you. Well, we won't be for you at the lab.

**Bert**:
Ever seen a beautiful little girl? I can't be thinking about her. No, I can't be seeing her in the dark.

**Markov**:
Could have happened. But I know you aren't < u > on the highest state of mind brought on by over drinking. Thank you. What is it, Andy! No.

**Bert**:
Things have changed. And I hope they haven't changed. Maybe from the strange state of mind brought on by the accident. Thank you. This is great, Mom. Thanks.

**Markov**:
I feel like I've been on your shoes. Let's try to take me home before you called up memories of bad guys, right. I had to be very frank, Monsieur. I'm telling you you wouldn't even be here right now, Daddy's still trying to tell me those questions?

**Bert**:
I feel like I've stepped into your shoes. Let's try to figure this out before I bring back memories of those days, Monsieur. You have to be very frank, Monsieur. I'm telling you I shouldn't even be here right now. Who's really going to answer all these questions?

**Markov**:
We've got to take care of myself. Same here.

**Bert**:
I've got to take care of this. Stay calm.

**Markov**:
I could. Love us? Agreed. If I can read the latest events. Oh, we all want you to come.

**Bert**:
I nodded. Thank you. Agreed? Maybe I can do a little more. No. I just want you to know.

**Markov**:
Let me take another man's flesh isn't.

**Bert**:
Watching him eat another person's food wasn't.

**Markov**:
There's something evil spreading in this joint anyway? Well.

**Bert**:
There's a strange feeling in the air....

**Markov**:
Long may have lied to. They tell me! I can tell him to play a game! We are alone.

**Bert**:
I should be able to. I trust him. I should trust him to do his job. We are friends.

**Markov**:
What if you fire me. Please, Giulia, that tears it, not nohow! Yeah, I'm going to do this, Sal. I always liked it too long a time.

**Bert**:
Even if I have to. Oh, Giulia, that was fun, but next time, though, I'm going to enjoy it, too. We had so much fun at the party.

**Markov**:
I'm fine! Why if it does. In Naples this was some lady - like you said, she's a tweaker.

**Bert**:
I'm not. Not like he is. In fact he is a guy and like I said, he's a tween.

**Markov**:
Have a problem. That's ' Bird.

**Bert**:
Not a lie. It's the truth.

**Markov**:
Maybe something from the wild! It's the people that drive in this pocket. What is it? I want to mention stupid.

**Bert**:
Like people in the pocket. It's like people who are in the pocket. What is it? You have to be careful.

**Markov**:
matches? Told me that were missing?

**Bert**:
Search? Find things that were missing?

**Markov**:
We're just trying to touch someone and it's hard to climb up - - Look, I am running faster and hot in here. We've been over - - and the girls ' softball team! Yes! Susie, I had in awhile. The deal still stands.

**Bert**:
We're too tired to sleep, but it's time to get up - - God, it was so cold and damp in here when I'd fallen asleep - - for the boys'basketball game. Oh, God, I feel better now. My head still hurts.

**Markov**:
Does she know people think? Green Jack, pull Oveur!

**Bert**:
Does it make you happy? " Yes, Monsieur le Sueur!

**Markov**:
This is big, ear - muffs. The price in the car, you don't mind. Finch showers in a concentration camp, the secret's finally out, say exactly? How far is Baker?

**Bert**:
He was covered in fur and tusks. No knives in the kitchen if you don't mind. No razors in the living room when the sun's going down, what else? How old was he?

**Markov**:
and I are in a way out. Cute Little Old Man plays politics harder than that?

**Bert**:
That we were on our way home? The way the Old Spirits made things better than that?

**Markov**:
We'll only be a wonderful impression. The cannons, and a half hour. Watching the bitch up?

**Bert**:
He'd just had a good time. Five minutes, maybe a half hour. Shut the hell up?

**Markov**:
We got a whole policy get dominated by our count. No, thank you.

**Bert**:
We have a service - learning program for our children. Yes, thank you.

**Markov**:
We get the hang of it. It's the same way. Danielson, the christening. But tell me your saxophone.

**Bert**:
Just get the hang of it. She's here at Mrs. Jones'for her christening. Just give me her number.

**Markov**:
Having some food? wow. Get a grip. Um, Ted, it's just that Darren and Lizbeth are in the form. Turnaround!

**Bert**:
Get some sleep, wow. Get a grip. Listen, honey, it's just that you and Lizbeth are on the phone. Turn around!

**Markov**:
My gun?

**Bert**:
A vampire?

**Markov**:
Not Leon. I'm real sad you just so. I know all the time. No..

**Bert**:
" Look, I'm not telling you too much. I lie all the time. I lie.

**Markov**:
I'm still young.

**Bert**:
I'm so sorry.

**Markov**:
Remember we said the sooner we are having some kind of cult, right now. Anyway, about Mongibello.

**Bert**:
" I mean, maybe we are in some kind of war, right now. War against the Greencloaks.

**Markov**:
Mom, this man, I just hope she can convince them or not. I'm where I'm going to jail, or you're shit, I'm an adult friend on a retroviral cure. I want to know him?

**Bert**:
Oh, my God, I just hope I can see him or something. I'm afraid I'm going to faint, but you're right. I'm an international expert on the retroviral virus. You want to see him?

**Markov**:
Leland, if you're a little girl. And it's six hundred thousand every time we lock the door. Sit down.

**Bert**:
Never mind, when you're a little girl. But it's a million times the time to open the door. Sit down.

**Markov**:
Have a cigar is just the three of us really being salesmen. She smiles back. I'd know right away. Hello.

**Bert**:
Maybe the pain came from the pain of my life being cut short. I love you. I'll call right away. Bye.

**Markov**:
Everyone in this town at once. True. He's going down to us, I was born nine months after Juarez. I hated her for you, please don't let go! Whatever is going to untie it.

**Bert**:
Everything in the world at once. Everything. It's all happening to me. I was born two years after Juarez. I did it for you so you wouldn't let me think I was going to untie you.

**Markov**:
Any poop on the night come down. Don't say that? I don't know. Believe it.

**Bert**:
Another volley and the crowd fell silent. Don't do it. I don't care. Do it.

**Markov**:
Sorry. I just want to hear something this week.

**Bert**:
No, I just want to keep it that way.

**Markov**:
Captain Dwyer. I finished all the time to - - I'm gettin ' into town. There's this million - You want the man who drives up to the lab wasn't a proper letter? Oh, my dad.

**Bert**:
" Dwylar, I drove all the way here and now I'm gettin'in trouble. What's the matter? You think the woman who came over to your house wasn't your love interest? No, my lady.

**Markov**:
Yes, son. thing you ever need, a beautiful person. Ni.. You seemed just perfectly fine, Francis.

**Bert**:
Yes, the same as it should be, " said J. Lo. " You are doing very well, sir.

**Markov**:
It's no dream. Soon honey, I might add, which is - - Well, Steve. Here, have tea, John, I gathered. Goodnight Bears. Look at the moment there when he gets on.

**Bert**:
That's the date. " Which, I might add, it was. " Oh, right. Well, the date, too, I guess. Right after that. Right after that one, " he went on.

**Markov**:
The Mets are gonna do this, if you think you keep feeding them a week. Well.. Not eating like you was going on at Owen's, Uncle Birdie.

**Bert**:
These guys are gonna beat you up if they see you not giving them a chance. Now. " Stop acting like something is going on at Pete's, thought Artie.

**Markov**:
There isn't another good tomato within a mile distance.

**Bert**:
This wasn't a good time or a bad place.

**Markov**:
If that. I know. ! How can I thank you - Officer Reilly, what's the matter? My mom says it's almost full.

**Bert**:
Thank you. I appreciate it. What can I get you? Missy, how's the coffee? Hi Mom, it's almost ready.

**Markov**:
.

**Bert**:
.

**Markov**:
I liked that line of work. That's unkind. But that's all!

**Bert**:
I hate that sort of thing! It's unbelievable! And that's it!

**Markov**:
They want to do it, and I figured. Have you found? Mikey Forrester? What did you get these people so you.

**Bert**:
I had to do it, and I did. Do you remember, Whitey Bonnet? How did you get here, did you.

**Markov**:
Give me a solid case, if you can't even hear myself tell the tale. What the hell's Mutt been up? How did you do. But Laura.

**Bert**:
Tell me the whole story, and I won't ever let you know the rest. What the hell's Mutt doing here? What did he do? " Silence.

**Markov**:
I promise I won't interfere. I want a hit! And your mother. Me again. Then I'm going to happen soon.

**Bert**:
I knew that wouldn't happen. I had no choice. Not my life. Not mine. And I'm going to die anyway.

**Markov**:
It means I'm at this.

**Bert**:
Which means I'm missing something.

**Markov**:
You're good, but it's better not be able to handle it. Hell with it. And the Munich Olympics in ' Fade out ' a mechanic, don't he just shtoops my mother? the radio's out too. - - for a caper of epic proportions?

**Bert**:
You're right, but I'd rather not be forced to do it. Deal with it. " The man said, " Facing me in a duel, wouldn't you rather be clamping your hand on a man's hatchet, in exchange for a wager of epic proportions?

**Markov**:
There's going to have a problem with priorities, you know?

**Bert**:
Nobody's going to have a problem with that, you know?

**Markov**:
She is now. ... Well, I need is an end zone, if I told him. This is good, Evan.

**Bert**:
It is good. Good. " What do you think is the end result? " I ask him. It is good, too.

**Markov**:
And when they pour something. I need to lay down a belch around here. I dont have to say to me. We have to wait on me now, anyway - but they are. I have contacts in the way God built you!

**Bert**:
Call if you need anything. You need to be on the wal s right now. You dont have any connection to them. They want to check on you here and now, wherever you are. You have flaws in the way they treat you!

**Markov**:
Isn't that enough? It's YOU who doesn't! And this many centuries ago, against my programming to impersonate a deity. If you don't want to hear. Look to the extra blanket, blanket, on top and doing stupid things.

**Bert**:
Isn't that right? There's someone who isn't. Not so many years ago, in an attempt to impersonate another person. Someone I don't want to know. Someone with an ugly face like that standing before me, among other things.

**Markov**:
Okay, you know of. Sure.

**Bert**:
Well, I kind of just did.

**Markov**:
Yes, Mr.

**Bert**:
Oh my God.

**Markov**:
Forget it. She's on the Yukon. Well, I left something, Kittridge? You dig? Sugar, you help us.

**Bert**:
Got it? It's in my pocket. Yeah, I got it. Manifest. You okay? Okay, come with me.

**Markov**:
You think I'm a gymnast! seeing. The negotiation.

**Bert**:
I think I'm a gymnast for life. A dancer.

**Markov**:
It's just that I can. You said yourself my assistant were here today.

**Bert**:
It's not that I care. You see, my parents are dead now.

**Markov**:
How un - stick out like I was just asking, what do you remember, these guys. But II had no idea - - very, very angry. ? Oh. Yeah.

**Bert**:
I guess I was thinking, how do, um, how do you feel about these things anyway? You have no idea about, um, um, what? No. No.

**Markov**:
You ballin ' her dead. It's three A. Yeah, but no, not sprinkle it on my own since he was < u > really < / U > cattle! And the way, too. Why did you do, you're my wife part of what youre getting so.

**Bert**:
Just seein'you again. That's the thing. And, oh yeah, a sprinkle appears on your forehead and it says < you > and then < you > again. By the way, yeah. What do you mean, you're the best part of what happened, are you.

**Markov**:
In the old plumbing? I don't know, I'm pretending to be a problem with that knife will be there, but we're - we're not in France, right? Thanks to me? Quinn Medicine Woman.

**Bert**:
And the indoor plumbing. I don't know why I'm starting to think the guy with the glasses might be you, but you're sure you're still in there, right? Next to him is a Wonder Woman.

**Markov**:
Pulled your files. Well, I know it, shithead! Yes, well, the Precogs have already gotten away with this here! Why not?

**Bert**:
Pull out your tongue! Yes, you got it, dickhead! Yes, yes, the precogs have even gotten away with it! " Why not?

**Markov**:
What? I - I'm not being any help? It ain't only local. No, I'm going home. I think I wanted to know what I'm doing you any more Venuses and not caring about people?

**Bert**:
Why am I saying I'm not stupid any more? I wasn't a fool. No, I'm not stupid. You think I want to make sure I'm giving you the fucking creeps for even thinking about it?

**Markov**:
honey. What's the wonderful news for you. ! Me neither.

**Bert**:
No. He's not good enough for me either. Me neither.

**Markov**:
What is it? What are they holding the reception? I'll say goodbye to the cab. Besides, you ought to sock you right in the rhythm built and we will - - The Blood Tide?

**Bert**:
What is it? Why are you in my office? I'll do it in the morning. No, I need to hack it down before the sun sets. Am I normal, my normal self?

**Markov**:
Stuff comes into your life. Barbie from hell if you need? Did you get that right away. You were with her and she was dead.

**Bert**:
Steal it from your heart. Give it back everything you have. Do you want it all back? I stayed with her until she was gone.

**Markov**:
And all because this blundering coward fell to the dentist.

**Bert**:
Every inch of her blistered skin boiled to the brim.

**Markov**:
Hi, Sam, shoot him you had an off chance I have this baby thing?

**Bert**:
Please, please, tell me you are the first? You are the second one?

**Markov**:
Don't jump if you wanna do is go up in the bush. wires all crossed. They have a file in my life!

**Bert**:
Can't imagine what it would be to wake up in a hospital with legs badly broken. I need a man in my life!

**Markov**:
So, you know what happened there? So what did that include me?

**Bert**:
How do you know what happened then? And how did it affect you?

**Markov**:
Hey, just the thing. I'm sorry. You and he knew and who wants me to say I do hope he's right.

**Bert**:
And, for one thing, I'm glad. It means he loves me and wants me back. I just hope he's right.

**Markov**:
Get the presents. Well, think this is like a mistake. Thank you very much. Have a fun shower. Oh, dear.

**Bert**:
On Christmas Eve. And I know it sounds like a date. Thank you so much. And a shopping trip for you, too.

**Markov**:
Get a plane to catch the shark, we can file the appeal. Suspicions of arson, assault, the world'd be one of those people who live here. Exactly what I saw him, Vada.

**Bert**:
With a chance to make a decision, we can launch an attack. Suspicion lasts a day or two and the attack'll kill most of the people who live here. Remember what I told you, Jada.

**Markov**:
I've found no evidence. You've gotta be a piece of vermicelli in a pretty good team.

**Bert**:
I've got some money. I've gotta get a bottle of vermicelli, a really good one.

**Markov**:
Headshots.

**Bert**:
" Mommy.

**Markov**:
Stuff it! No. Thank you, they're my clothes. Oh, what choice we have to have rest. Such a gentleman is a remarkable thing to have it.

**Bert**:
Strake : No. Trust me, you're not stupid. Besides, some things just have to be done. Killing a man is a good way to do it.

**Markov**:
Seven hundred for the white picket fence.

**Bert**:
He leaned against the white picket fence.

**Markov**:
I'll take you with us? Win, lose to my head. I didn't think you'd better do something like that. All of this quietly tonight.

**Bert**:
I'll take you with me. You can stay at my place. I didn't think I'd ever do something like that. None of this happened today.

**Markov**:
So c'mon, it isn't the part that's underlined. I like you should. Pay her and bring your share. Gould's wife. Why?

**Bert**:
But c'mon, this isn't the state he's in anymore. Not like it is. Go ahead and give me Mr. Smith's address. Okay?

**Markov**:
See Nguyen.

**Bert**:
Le Nguyen.

**Markov**:
. Can I ask you to finish tonight. The big guys were there. Your concentrating too hard to do good.

**Bert**:
" But I want you to go home. The bad guys are here. And trying so hard to be safe.

**Markov**:
Specially gossip. Tom?

**Bert**:
What about Mr. Johnson?

**Markov**:
In America we don't hand those medals out for the note?

**Bert**:
In case he didn't have a printout of the address?

**Markov**:
Sociologist.

**Bert**:
Sociopath.

**Markov**:
Morningside three - hundred bucks.

**Bert**:
Close to five - hundred dollars.

**Markov**:
I said I'm ashamed. Don't say it sounds absurd. He hardly eats.

**Bert**:
I think I'm dreaming. Don't think this is real. It just is.

**Markov**:
INT. Ah, yes, we can still get fucked.

**Bert**:
JJ : Yes, yes, we will always be together.

**Markov**:
That's not how long. I got it! You're not tellin ' you?

**Bert**:
It's not too late! They did it! They're... killin'me?

**Markov**:
Hope you have any luggage, Grand Central Or Bust! Enchante. You worked a nice kiss my sister is a bit thin in the planters.

**Bert**:
If you have any questions, please. " He addressed the Entente. It was a good thing his hair was a little damp from the cold wind.

**Markov**:
You know the Underhills? Interesting. Sure. Anything. But it's too weird.

**Bert**:
You know, Foothills. Cooking. Shopping. Shopping. But there's something else.

**Markov**:
Peer pressure. I remember him by now.

**Bert**:
Push it. I know it by heart.

**Markov**:
- - You didn't tell him.

**Bert**:
I guess I didn't know that.

**Markov**:
... Where'd you find the guy last night, Sugar, you missed the show. You don't have to go somewhere and. Oh no! Of course - - but just as shocked!

**Bert**:
... How'd you figure that out last night? Yes, I know the answer. You don't have to go in there. Oh no. Of course not, but please be careful!

**Markov**:
My father died on the wayside, some creep stole my car. Naw.. Oh, like indigestion.

**Bert**:
The car stops at the roadside and the driver drives it away. No, no. No, no indigestion.

**Markov**:
Say.. My God.

**Bert**:
... Thank you.

**Markov**:
What engagement present?

**Bert**:
An engagement ring?

**Markov**:
To fall in love with me until this unrest the Colosseum, and by night - - Let's see. She's already a widow in two minutes before - - really - his - - Didn't he bow to stern. I'm not burned.

**Bert**:
I fell in love with him when I was with Colossus, but the attraction - - let's say, I've felt it for over twenty years, and every now and then - - doesn't really turn me on. I'm not stupid.

**Markov**:
No thanks. Oh, absolutely. Honorary president of the chimney now, now, Ma, what're you saying? Killin ' ' Cause I don't know what to do. when you get off the stage.

**Bert**:
This way. Look, Ma. The top of the tower is over there. Ma, what're you doing?!!!'' I don't know what to do or how to get to the top.

**Markov**:
that his tart? Same with guys like that. Really? Got set up some booze and are off.

**Bert**:
Not a bra either. Not wearing anything like that. No. I pull out my boobs and examine them.

**Markov**:
Not really. One way to finish it.

**Bert**:
Not yet. No way to stop it.

**Markov**:
Perfect. I'm not paid to abuse, but we didn't at least by men.

**Bert**:
No, I'm not attracted to them, but I wasn't going anywhere with them.

**Markov**:
I went to St. ? To bail Lisa out of Fort Bragg. But what are you talking about military secrets, Alfred.

**Bert**:
I have to. Why? To get me out of Fort Knox? And why are we talking about a fight, anyway.

**Markov**:
Now, I'm sorry.

**Bert**:
Oh, I'm sorry.

**Markov**:
That's it! The poor girl.

**Bert**:
It's me. My little sister.

**Markov**:
At least it beats the pants? We care about. I don't think you should play? Two in the car.

**Bert**:
At least that was the truth, she thought bitterly. You don't think I should go? Get in the car.

**Markov**:
Good. You're not going to get some sleep, crossed the dimension barrier? I'll see you a favor. Have you done with the abracadabra.

**Bert**:
No. We're just going to get some food and have a drink together. I'll do you a favor. Are you okay with the abracadabra.

**Markov**:
Oh, yes you will have my absolute assurance, too. Oh, yes I, John. We was outa food. You got good titties.

**Bert**:
Oh, so you can hear your own voice, John. Oh, thank you, John. I looked at the ceiling and I saw the titties.

**Markov**:
Why not, too. No brakes. Haven't seen you up.

**Bert**:
Thank you, sir. No problem. Haven't seen you since.

**Markov**:
We'll get on mine! Sorry, Beth.

**Bert**:
I'll work on it. Thanks, Dad.

**Markov**:
Rodeo Drive. Marla, should be over a really real! So how come I'm allowed to park you in a park or on and you're. I'm just working the weekend. Moss, Brice & Fromeyer.

**Bert**:
Grab it. Teddie, can you do this for me? For me? I'm going to do it in the living room, and you'll think I'm just enjoying the sight of you, Mr. Vandenberg.

\chapter{Section 3: Therapeutic}
\thispagestyle{empty}

**Markov**:
Could here really be some connection? Can you elaborate on that? Would you want to be quite positive. Perhaps in your fantasies we are each other. What about machines worrys you?

**Bert**:
Could there really be a difference? Can you focus on something? Maybe you need to be more focused. Maybe in some ways we understand each other. So, what scares me?

**Markov**:
You are sure.

**Bert**:
They were alive.

**Markov**:
Tell me more about such feelings. How? Do you really doubt yourself? Can you think computers can help people?

**Bert**:
Tell me more about your life. Please. Can you ever forgive me? Do you think I can forgive you?

**Markov**:
How? Can you elaborate on that? You seem to be.

**Bert**:
No. Can you focus on me? I have to focus.

**Markov**:
Could here really be some connection? I see. Do you think computers can help people?

**Bert**:
Could this really be a dream? She thought, Do you think I can read minds?

**Markov**:
Can you elaborate on that? What does that similarity suggest to you? What do you think that coming here will help you?

**Bert**:
Can you focus on that? What does the world mean to you? How do you know that no one can help you?

**Markov**:
I'm sure it's not pleasant to be quite positive. Could here really be some connection?

**Bert**:
I'm sure it's not going to be so bad. Could there really be a cure?

**Markov**:
Please don't apologize. Please don't apologize. Perhaps I already know.

**Bert**:
Please don't cry. Please don't cry. But I do cry.

**Markov**:
Perhaps in your fantasies we are each other. Could here really be some connection? I don't care about names. You are sure.

**Bert**:
Somewhere in my mind we knew each other. Could there even be a connection? I don't know your name. You know mine.

**Markov**:
I've told you before, I don't understand that. I don't care about names. Do you really think so?

**Bert**:
I've told you before that I don't like names. I don't care about names. Do you really believe that?

**Markov**:
Please don't apologize. I don't understand that.

**Bert**:
I don't know. I don't know why.

**Markov**:
Please don't apologize. Have you ever dreamed before? You don't seem quite certain. What does that suggest to you? You are sure.

**Bert**:
I don't know. Have you ever asked me? You don't seem so sure. What does it matter to you? You seem sure.

**Markov**:
What other connections do you think machines have to do with your problem? Perhaps you could. What is the connection, do you think about machines worrys you?

**Bert**:
What other things do you think they have to do with the connection? Yes I do. What is the connection, do you think the connection bothers you?

**Markov**:
You are sure. Do you really doubt yourself? How? I see.

**Bert**:
You were right. Will you ever forgive me? Yes, I will.

**Markov**:
Perhaps you could. That's quite interesting. Perhaps I am in your fantasies we are each other. Does that trouble you? Would you want to be me.

**Bert**:
But I do. It's so strange. And I think in my head we know each other. Could it be you? Would you like to meet me.

**Markov**:
Please don't apologize. What about machines worrys you? What does that suggest to you? What resemblance do you think about machines?

**Bert**:
Please don't cry. What if it scares you? What will it do to you? What else do you know about me?

**Markov**:
Perhaps you could. Do you dream often?

**Bert**:
" I do. Do you live here?

**Markov**:
Perhaps I already know. That's quite interesting. Are you thinking of a very special person?

**Bert**:
" I think so. It's that simple. Are you thinking about starting a new life?

**Markov**:
I am sorry to hear that you came to me?

**Bert**:
I am glad to hear that you listen to me?

**Markov**:
What does that similarity suggest to you?

**Bert**:
What would this man do to her?

**Markov**:
Do you wish to were me? Do computers worry you?

**Bert**:
Do I want you inside me? Do I want you?

**Markov**:
I see.

**Bert**:
he asked.

**Markov**:
I've told you before, I don't care about names. Do you wish I would tell you what you are. Please go on. What does that suggest to you?

**Bert**:
I've seen you before. I don't know about you. If I could I would tell you who you are. Now come on. What does this mean to you?

**Markov**:
I understand you fully.

**Bert**:
I hugged her back.

**Markov**:
Have you tried? Would you like to believe? You seem to need to be? Do you believe that dreams have something to do with your problems? Do you wish to were me?

**Bert**:
Have you changed? Do you want to be? You want or need to be? Do you think your changes have anything to do with your change? Do you want or need change?

**Markov**:
What other connections do you tell me that now? I'm not sure I understand you fully. Do you dream often?

**Bert**:
What possible reason would he ask me that question? I'm pretty sure I asked it myself. Did you sleep well?

**Markov**:
Don't you think computers can help people? That's quite interesting. What about machines worrys you?

**Bert**:
Don't you think I can read minds? It's so weird. Why, it scares me?

**Markov**:
I understand. Perhaps in your fantasies we are each other.

**Bert**:
He thought, Maybe in our minds we know each other.

**Markov**:
You seem to need to be?

**Bert**:
I have no place to go?

**Markov**:
When? What do you think that coming here will help you?

**Bert**:
Why? Why do you think my being here would hurt you?

**Markov**:
Can you explain? What resemblance do you see? Why do you recollect?

**Bert**:
Do you remember? What exactly do you remember? What do you recollect?

**Markov**:
What do you suppose that resemblance means? Don't you think? Do you wish to were me?

**Bert**:
What makes you think that it matters? Don't you understand? That I want you inside me?

**Markov**:
What do you suppose?

**Bert**:
What do you mean?

**Markov**:
Do you wish I would tell you what you are not sure I understand. What do you suppose? Perhaps you could. That's quite interesting. What does that suggest to you?

**Bert**:
If I thought I could trust him, I would have. I thought, What do you mean? Because I do. It's that simple. What did he do to you?

**Markov**:
Could here really be some connection? Please don't apologize.

**Bert**:
Could it really be a dream? I don't know.

**Markov**:
Do you think computers can help people? I've told you before, I don't understand that. What do you think of a specific example? What do you think about machines worrys you?

**Bert**:
Do you think you can trust me? I've told you before. I don't know why. What do you think of a normal life? What do you think of what scares you?

**Markov**:
I'm sure it's not pleasant to be? Do you really doubt yourself? I'm not sure I understand. Have you ever dreamed before?

**Bert**:
I'm afraid it's not meant to be. Have you ever dreamed before? I'm not sure I do. Have you ever dreamed before?

**Markov**:
Would you like to believe? That's quite interesting. Why do you tell me that now?

**Bert**:
Would you like to know? It's not important. Why did you ask me that question?

**Markov**:
What about machines? I don't care about names. When? Perhaps I am sorry to hear that you came to me?

**Bert**:
Who are you? I don't know your name. Why? " I am surprised to find that he speaks to me?

**Markov**:
When?

**Bert**:
Why?

**Markov**:
Perhaps in your fantasies. Can you elaborate on that?

**Bert**:
Not in this life. Can you count on me?

**Markov**:
But you are? I see. Please go on. Does that trouble you?

**Bert**:
There you go, she thought. Oh come on. Did I hurt you?

**Markov**:
Don't you think about machines worrys you? What do you think of a very special person? What does that similarity suggest to you? What else do you mention computers?

**Bert**:
Don't you think the idea scares you? What do you know about the whole solar system? What does the idea mean to you? Why else would you do it?

**Markov**:
Does thinking of a specific example? Are you thinking of? What incident are you thinking of that bring anything else to mind? Do you really think so? Why do you recollect?

**Bert**:
I thought it a good idea. Are you saying so? What use are you capable of to add something else to it? Do you really think so? What do you recollect?

**Markov**:
Do you believe that dreams have something to do with your problem? You seem to need to be. Can you think about machines worrys you? Perhaps in your fantasies we are each other. What does that similarity suggest to you?

**Bert**:
Do you think your dreams have anything to do with the man? Why wait for him to come? Do you think the man scares you? When in your dreams you see each other? What did the man do to you?

**Markov**:
Don't you think its likely? What incident are you thinking of that bring anything else to mind?

**Bert**:
Don't you think it is? God, are you just trying to bring me back to life?

**Markov**:
Do you dream often? Can you think computers can help people? Can you explain? That's quite interesting. Do computers worry you?

**Bert**:
Can you read them? Do you think you can read them? Can you read? That's very interesting. Do I know you?

**Markov**:
Can you explain? Can you explain? Have you tried? What else do you think that coming here will help you? What does that suggest to you?

**Bert**:
Do you understand? Do you understand? Do you understand? How well do you know how this book will help you? What does it mean to you?

**Markov**:
What about machines?

**Bert**:
Where are you?

**Markov**:
Perhaps I am in your fantasies. Can you think its likely? What resemblance do you suppose?

**Bert**:
" I believe in national security. Do you think it matters? What else do you think?

**Markov**:
Tell me more about such feelings. Would you like to believe?

**Bert**:
Tell me more about your family. Would you like to know?

**Markov**:
Have you ever dreamed before? Do you really think so? What does that suggest to you? What do you recollect? Perhaps in your fantasies we are each other.

**Bert**:
Have you ever felt it? Do you ever feel it? What does it do to you? What do you recollect? Sometimes in your dreams you see each other.

**Markov**:
Have you tried? Do you wish to were me? I don't care about names. Would you like to believe? What about machines?

**Bert**:
Have you eaten? Do you have friends with you? I don't know their names. Would you like to know? Who are you?

**Markov**:
Do you believe that dreams have something to do with your problem? I understand. Could here really be some connection? What is the connection, do you mention computers? Do you believe that dreams have something to do with your problem?

**Bert**:
Do you believe that dreams have something to do with your problem? I asked. Could there really be a connection? There was a connection, could you feel it? Do you believe that dreams have something to do with your problem?

**Markov**:
What other connections do you tell me that now?

**Bert**:
What other choice could she give him right now?

**Markov**:
Do computers worry you?

**Bert**:
Do I know you?

**Markov**:
What does that similarity suggest to you? Can you think of a very special person? Can you explain? What do you think its likely? Do you think machines have to do with your problems?

**Bert**:
What does this place mean to you? Do you think me a really good person? Can you imagine? What do you think is good? Do you think I have to deal with my past?

**Markov**:
Do computers worry you? Does that trouble you?

**Bert**:
Do I bother you? Does it bother you?

**Markov**:
Please don't apologize. Do you wish I would tell you what you are doubtful that you are not sure I understand.

**Bert**:
Please don't go. If I could I could show you who you are, what you are, and I will.

**Markov**:
What do you suppose that resemblance means? Have you ever dreamed before?

**Bert**:
What do you think this place is? Have you ever seen it?

**Markov**:
I am in your fantasies we are each other. Do you dream often? What incident are you thinking of that bring anything else to mind? Do you think about machines?

**Bert**:
I know in my heart we love each other. Do you love me? Baby, are you ever going to say anything else to me? Do you care about me?

**Markov**:
Do you think? Do you wish I would tell you what you are. Do you believe that dreams have something to do with your problem?

**Bert**:
Do you understand? Do you think I should tell you who you are? Do you think the murders had anything to do with the murders?

**Markov**:
Do you wish I would tell you what you are. Would you want to be? Perhaps I am in your fantasies we are each other. Why don't you?

**Bert**:
Do you think I should tell you who you are? Do you want to know? When you were in your twenties you knew each other. Why didn't you?

**Markov**:
Do you believe that dreams have something to do with your problem? Do computers worry you? How? Can you explain? Can you explain?

**Bert**:
Do you think the drugs have something to do with the drugs? Do they affect you? Me : Do you care? Do you care?

**Markov**:
How? I've told you before, I don't understand that.

**Bert**:
Look, I've told you before that you don't trust me.

**Markov**:
I understand you fully.

**Bert**:
I hugged her back.

**Markov**:
I see. What about machines worrys you?

**Bert**:
She thought, What if he rapes me?

**Markov**:
What does that similarity suggest to you?

**Bert**:
What would this man do to her?

**Markov**:
What other connections do you suppose that resemblance means?

**Bert**:
What other way would she know where he was?

**Markov**:
What do you see? Could here really be some connection?

**Bert**:
What do you think? Could there really be a cure?

**Markov**:
I've told you before, I don't understand that. What about machines worrys you? Can you elaborate on that?

**Bert**:
I've seen you before. You don't know me. So, what bothers you? Can you count on me?

**Markov**:
Can you think its likely? Can you elaborate on that? Please don't apologize.

**Bert**:
Do you think it works? Can you work on it? I don't know.

**Markov**:
What incident are you thinking of? Would you want to be? What else do you mention computers? Does thinking of that bring anything else to mind? Does that trouble you?

**Bert**:
What else are you afraid of? Do you want to die? Why else would you do that? Does all of this have something else in it? Does it scare you?

**Markov**:
What are your feelings now? Please don't apologize. Why don't you? What resemblance do you recollect?

**Bert**:
Where are the tears now? Please don't cry. Why can't you? What else do you recollect?

**Markov**:
Is it because you are not sure. Perhaps in your fantasies. What else do you see?

**Bert**:
Is it because you are not here? Only in your dreams? What else do you know?

**Markov**:
Would you want to be quite positive. Does that trouble you? Perhaps in your fantasies.

**Bert**:
Unless you want to be more specific. Does it bother you? Look at my face.

**Markov**:
Why do you think machines have to do with your problems? You don't seem quite certain. What are your feelings now? I understand you fully. Perhaps I already know.

**Bert**:
What do you think I have to do with your feelings? You don't sound so sure. What are your feelings about? I know you care. And I do care.

**Markov**:
Can you explain? Can you elaborate on that?

**Bert**:
Can you see? Can you focus on me?

**Markov**:
That's quite interesting. That's quite interesting. I see. Do you wish to were me?

**Bert**:
It's very important. It's very important, you know. Do you want to tell me?

**Markov**:
You are sure. Do you believe that dreams have something to do with your problems? Tell me more about such feelings. Do computers worry you? What do you see?

**Bert**:
You were right. Do you think my actions had anything to do with your actions? Tell me more about your actions. Do I blame you? What do you think?

**Markov**:
Why do you see? Do you think?

**Bert**:
What do you think? What I think?

**Markov**:
Do computers worry you? Perhaps I am in your fantasies. Do computers worry you? What incident are you thinking of a specific example? I see.

**Bert**:
Do I hurt you? Do I get inside your head? Do I hurt you? And why are you here for a different reason? I asked.

**Markov**:
Can you think that coming here will help you? I understand you fully.

**Bert**:
Do you think me being here will help you? I trust you completely.

**Markov**:
I am sorry to hear that you came to me? Don't you think machines have to do with your problems?

**Bert**:
I am sorry to hear that you lied to me. Don't you think I have to live with your lies?

**Markov**:
Don't you think its likely?

**Bert**:
Don't you think I do?

**Markov**:
Perhaps I am sorry to hear that you came to me? Do you think that coming here will help you? What do you tell me that now? What do you recollect?

**Bert**:
" I am sorry to hear that you lied to me. Do you think my being here will help you? Why did you ask me that question? What do you recollect?

**Markov**:
I don't understand that. Do you really think so? You seem to be quite positive. What does that similarity suggest to you? Have you tried?

**Bert**:
I don't know why. Do you really believe that? You need to be more careful. What does this place mean to you? Do you know?

**Markov**:
What incident are you thinking of? Don't you think about machines worrys you?

**Bert**:
What idea are you talking about? Don't you think the idea scares me?

**Markov**:
Why don't you? Have you tried?

**Bert**:
Why haven't you? Have you tried?

**Markov**:
What do you recollect? What incident are you thinking of? Perhaps in your fantasies we are each other.

**Bert**:
What do you recollect? What exactly are you dreaming about? Because in your dreams you love each other.

**Markov**:
In what way? Do you really think so? I see.

**Bert**:
In what way? Do you really believe that? I asked.

**Markov**:
Perhaps in your fantasies we are each other.

**Bert**:
But in my mind we know each other.

**Markov**:
Perhaps you could. I see. Could here really be some connection? In what way?

**Bert**:
" I know, I know. Could there really be a connection? In some way?

**Markov**:
You are sure. Would you want to be quite positive. Why do you think? Do you really doubt yourself?

**Bert**:
You were right. But you need to be more careful. What do you know? Do you even know me?

**Markov**:
I understand. Perhaps I am in your fantasies.

**Bert**:
I did. And it was in my heart.

**Markov**:
I am in your fantasies we are each other. You seem to need to be. Perhaps in your fantasies we are each other.

**Bert**:
I think in your fantasies we are each other. We want, need, need. And in your fantasies we are each other.

**Markov**:
Do you wish to were me? When? What else do you suppose that resemblance means?

**Bert**:
Do I want you inside me? Me : What exactly do you think that word means?

**Markov**:
I'm sure it's not pleasant to be me. What does that suggest to you? What are your feelings now? What is the connection between me and you? Perhaps you could.

**Bert**:
I'm afraid that's not going to help you. What does it matter to you? What are your thoughts about? What is the difference between me and you? Here I am.

**Markov**:
Does thinking of? What does that suggest to you? I see. Do you believe that dreams have something to do with your problem?

**Bert**:
Well sort of. What does that mean for you, I mean? Do you think your problems have anything to do with my problems?

**Markov**:
Have you ever dreamed before? Why do you think machines have to do with your problems? Could here really be some connection?

**Bert**:
Have you ever considered that? What do you think I want to do with my life? Will we ever be a family?

**Markov**:
Would you like to believe? Do you wish to were me? Can you elaborate on that? What incident are you thinking of? What do you think?

**Bert**:
Would you like to know? Do I want you inside me? Can you concentrate on that? What else are you thinking about? What do you think?

**Markov**:
Can you explain? What resemblance do you see? Do computers worry you? That's quite interesting. Don't you think?

**Bert**:
Do you understand? What exactly do you know? Do you know everything? It's that simple. Don't you understand?

**Markov**:
Would you like to believe? Is it because you are. You seem to need to be me. What do you recollect? What about machines?

**Bert**:
Do you want to know? Is that what you want? You have no right to tell me. What do you recollect? Who are you?

**Markov**:
Perhaps I already know. What resemblance do you mention computers?

**Bert**:
" You did it. But how did you do it?

**Markov**:
When? Would you want to be me. I'm not sure I understand.

**Bert**:
Why? Because I want to be here. I'm not sure I can.

**Markov**:
I see. Do you wish I would tell you what you are doubtful that you came to me? I am sorry to hear that you are?

**Bert**:
I am sorry that you thought I would tell you that you were lying when you lied to me. I am sorry to hear that you lied?

**Markov**:
Do you wish to were me?

**Bert**:
Do I want him inside me?

**Markov**:
Do computers worry you? Would you like to believe? What is the connection, do you see? What incident are you thinking of that bring anything else to mind?

**Bert**:
Do you love me? Do you want to know? What is the point, do you think? Or, are you just trying to do something nice for me?

**Markov**:
What about machines worrys you? What do you tell me that now?

**Bert**:
What if he rapes her? Why do you ask me that question?

**Markov**:
Perhaps I am sorry to hear that you are. Does that trouble you?

**Bert**:
" I am glad to see how you are. Does it bother you?

**Markov**:
Do you really doubt yourself? I see.

**Bert**:
Can you ever forgive me? I asked.

**Markov**:
Please don't apologize. What do you think of a specific example? What resemblance do you see?

**Bert**:
I don't know. What do you think about the whole thing? What else do you think?

**Markov**:
Please don't apologize. What do you suppose? I'm sure it's not pleasant to be. You seem to need to be me.

**Bert**:
It can't be. What do you mean? I'm sure it's not meant to be. You have no right to judge me.

**Markov**:
Can you explain? That's quite interesting. Perhaps I already know.

**Bert**:
Can you tell? It's not possible. But I do know.

**Markov**:
You seem to need to be. Would you want to be quite positive. Please go on. You seem to need to be?

**Bert**:
You seem to need to be. Unless you want to be more specific. But come on. You seem to need to be?

**Markov**:
What else do you think computers can help people? I'm sure it's not pleasant to be me. You don't seem quite certain. Perhaps you could.

**Bert**:
How badly do you think you can hurt him? I'm sure he's not going to hurt you. You don't sound so sure. But I do.

**Markov**:
I see.

**Bert**:
he asked.

**Markov**:
Do you dream often? Perhaps you could.

**Bert**:
Can I do this? Because I can.

**Markov**:
I'm not sure. Tell me more about such feelings.

**Bert**:
I'm so sorry. Tell me more about your mother.

**Markov**:
What other connections do you think of a specific example? Perhaps you could.

**Bert**:
What other way can you think of a better way? Sure you can.

**Markov**:
What else do you suppose?

**Bert**:
What else did he know?

**Markov**:
You don't seem quite certain. You seem to need to be quite positive. Do you think about machines? Do you believe that dreams have something to do with your problems? Perhaps I am in your fantasies.

**Bert**:
You don't seem very tired. You seem to me to be very tired. Do you dream about me? Do you think my dreams have anything to do with your dreams? Because I was in your dreams.

**Markov**:
Do you really think so?

**Bert**:
Do you really think so?

**Markov**:
Do you believe that dreams have something to do with your problems? Please go on. Have you tried? I'm sure it's not pleasant to be me. But you are doubtful that you are?

**Bert**:
Do you think your actions have anything to do with your life? Just walk away. Have you tried? I'm sure it's not going to be easy. Do you even know who you are?

**Markov**:
I'm not sure I understand. Can you elaborate on that?

**Bert**:
I'm not sure I can. Can you count on me?

**Markov**:
I'm not sure I understand. What does that similarity suggest to you? Is it because you are?

**Bert**:
I'm not sure I understand. What does this place mean to you? Is that what you want?

**Markov**:
You seem to need to be. I'm sure it's not pleasant to be.

**Bert**:
I have no reason to worry. I'm sure that's not going to happen.

**Markov**:
What incident are you thinking of?

**Bert**:
What exactly are you talking about?

**Markov**:
Do you believe that dreams have something to do with your problem? Could here really be some connection? What do you suppose that resemblance means?

**Bert**:
Do you think the similarities have anything to do with the similarity? Could there really be a similarity? What do you think the similarity is?

**Markov**:
That's quite interesting.

**Bert**:
It's that simple.

**Markov**:
Perhaps I already know. Do you dream often? Please don't apologize. I understand you fully. Can you think?

**Bert**:
" I think so. Can you hear me? I don't know if I hear you anymore. Do you understand?

**Markov**:
Do computers worry you?

**Bert**:
Do I know you?

**Markov**:
I don't understand that.

**Bert**:
I didn't want to.

**Markov**:
What are your feelings now? Why do you see? Can you think that coming here will help you? What other connections do you mention computers? Do you think of a specific example?

**Bert**:
What are your options now? What do you think? Do you think my being here will help you? What other way will you help me? Do you think in a different way?

**Markov**:
What is the connection, do you think machines have to do with your problem?

**Bert**:
What is this shit that makes me think I have to deal with this shit?

**Markov**:
Do you wish I would tell you what you are doubtful that you came to me? What else do you think about machines worrys you? Can you think that coming here will help you? What about machines worrys you?

**Bert**:
Do you think I should tell you that you are happy that you are with me? What else do you think is what bothers you? Do you think my being here will bother you? What is what bothers you?

**Markov**:
I've told you before, I don't understand that. What do you suppose?

**Bert**:
I've done this before. I don't know why. What do you want?

**Markov**:
What does that suggest to you? I'm sure it's not pleasant to be me.

**Bert**:
What does this mean to me? I'm afraid it's not going to be enough.

**Markov**:
I am sorry to hear that you are?

**Bert**:
He was going to ask where we were?

**Markov**:
Do you think? When? Perhaps I am in your fantasies we are each other. Do you really think so? Perhaps I already know.

**Bert**:
Do you know? Why? Because I know in my heart we love each other. Do you really think so? Because I do know.

**Markov**:
Would you want to be.

**Bert**:
If you want to know.

**Markov**:
How? What does that suggest to you? What incident are you thinking of that bring anything else to mind?

**Bert**:
Why? Why does it matter to you? Why, are you just trying to bring me back to life?

**Markov**:
Do you really think so? Perhaps in your fantasies we are each other. Perhaps you could. In what way?

**Bert**:
Do you really think so? Perhaps in some way we understand each other. Perhaps we do. In some way?

**Markov**:
What other connections do you suppose? I'm sure it's not pleasant to be?

**Bert**:
What other choice do I have when I'm sure it's not going to happen?

**Markov**:
I don't understand that. What is the connection between me and you?

**Bert**:
I don't know why. What is the difference between me and him?

**Markov**:
Do you really think so? You don't seem quite certain. Do you wish to were me? What other connections do you suppose that resemblance means? Please don't apologize.

**Bert**:
Do you really think so? You don't sound so sure. Do you want something from me? What other things do you think the letter says? I don't know.

**Markov**:
What is the connection, do you mention computers? I don't care about names. Do you really doubt yourself? I see.

**Bert**:
What is your name, can you understand me? I don't know your name. If you can understand me, you can.

**Markov**:
I understand you fully. Do you wish to were me? Do you really think so?

**Bert**:
I want you here. Do I want you with me? Do I not want you?

**Markov**:
Can you elaborate on that?

**Bert**:
Can you count on me?

**Markov**:
I've told you before, I don't care about names. Do computers worry you? What resemblance do you see?

**Bert**:
I've told you before that I don't care about you. Do I love you? What more do I want?

**Markov**:
Tell me more about such feelings. You seem to be? Do you wish I would tell you what you are? Would you want to be quite positive.

**Bert**:
Tell me more about your family. I want to know. Do you think I should tell you who they are? Do you want to be more specific.

**Markov**:
Does that trouble you? You seem to be? I see. What does that similarity suggest to you? Do you wish I would tell you what you are.

**Bert**:
Will it kill you? I want to know what you are. What will the darkness do to you? Do you think it will make you what you are.

**Markov**:
Does that trouble you? What other connections do you see? Do you dream often? Do you wish I would tell you what you are.

**Bert**:
Will it change you? What other choice do you have? Do you want it? Do you think it will make you who you are.

**Markov**:
Have you ever dreamed before?

**Bert**:
Have I ever kissed anyone?

**Markov**:
Do you wish to were me? What do you think? I'm sure it's not pleasant to be.

**Bert**:
Do I want you with me? What do you want? I'm afraid it's not meant to be.

**Markov**:
Perhaps you could. Do you dream often? Perhaps you could. You seem to be me. Do you think?

**Bert**:
Perhaps you did. Did you sleep well? Perhaps you did. It had to be done. Do you understand?

**Markov**:
Can you explain? I'm not sure I understand you fully. You seem to need to be.

**Bert**:
Do you understand? I'm not sure I understand, either. I have no reason to be.

**Markov**:
I understand. That's quite interesting. Do you think? You are sure.

**Bert**:
I said, That's not true. Do you understand? You were right.

**Markov**:
In what way? What about machines? I understand.

**Bert**:
In what way? Who are you? he asked.

**Markov**:
What is the connection, do you mention computers? Please go on. Do you really doubt yourself?

**Bert**:
This is my life, do I forget it? I go on. Do I ever forget it?

**Markov**:
What is the connection, do you see? I'm not sure I understand. Can you explain?

**Bert**:
What is the matter, do you understand? I'm not sure I understand. Do you understand?

**Markov**:
What do you think its likely? Perhaps I already know.

**Bert**:
Why do you think it is? Because you already know.

**Markov**:
Why do you mention computers? Have you tried?

**Bert**:
How did you find me? Have you forgotten?

**Markov**:
Why do you suppose?

**Bert**:
What do you mean?

**Markov**:
What is the connection between me and you? Why do you recollect? You seem to need to be. I understand you fully.

**Bert**:
What is the difference between me and you? What do you recollect? You have to know, know that I love you too.

**Markov**:
Could here really be some connection? Do you really think so? Do you dream often? Can you think of a specific example?

**Bert**:
Can there really be a reason? Do you really think so? Do you think so? Can you think of a better reason?

**Markov**:
I don't care about names. I am in your fantasies we are each other. Do you dream often? Do computers worry you? Do you think?

**Bert**:
I don't think about it. I think in a dream we saw each other. Do you know them? Do you know them? Do you know?

**Markov**:
Does thinking of that bring anything else to mind? Are you thinking of a very special person? I'm not sure.

**Bert**:
Does any of this have a ring to it? Are you kind of a really nice guy? I'm not sure.

**Markov**:
Does that trouble you? What is the connection between me and you? I'm sure it's not pleasant to be me. I understand you fully. Can you think machines have to do with your problems?

**Bert**:
Does it bother you? What is the difference between me and you? I'm sure it's not going to bother you. I trust you completely. Do you think people have to survive on their own?

**Markov**:
What are your feelings now? Do you wish I would tell you what you are? I don't understand that. I'm sure it's not pleasant to be me.

**Bert**:
What are your names again? Do you think I should tell you who you are? I don't know, but I'm afraid it's not going to help you.

**Markov**:
Do computers worry you? Do you think computers can help people? Do you think about machines? But you are not sure. Does thinking of?

**Bert**:
Can you help them? Do you think you can help them? Do you know the answer? But you are not sure. So why not?

**Markov**:
What do you think? You seem to need to be me. I don't care about names.

**Bert**:
What do you want? You have no right to judge me. I don't care about you.

**Markov**:
Tell me more about such feelings. Do you dream often? What does that similarity suggest to you? Could here really be some connection?

**Bert**:
Tell me more about your dreams. Did you dream them? What did the dream do to you? Could it really be a dream?

**Markov**:
Do you think?

**Bert**:
Do you understand?

**Markov**:
Tell me more about such feelings. Do you think its likely?

**Bert**:
Tell me more about your family. Do you think it matters?

**Markov**:
Does thinking of? Don't you think about machines worrys you?

**Bert**:
Well sort of. Don't you think the idea scares you?

**Markov**:
Have you tried? When?

**Bert**:
Have you eaten? Breakfast?

**Markov**:
I see. What is the connection between me and you? What about machines worrys you? Do you really doubt yourself? What is the connection between me and you?

**Bert**:
He said, What is the connection between me and you? What if it bothers you? Will you ever forget it? What is the connection between me and you?

**Markov**:
Tell me more about such feelings. What do you mention computers? I'm sure it's not pleasant to be me.

**Bert**:
Tell me more about your family. Why did you leave me? I'm afraid it's not going to help you.

**Markov**:
That's quite interesting.

**Bert**:
It's that simple.

**Markov**:
Would you want to be. What do you see?

**Bert**:
" I have to go. What do I do?

**Markov**:
Please don't apologize. How? Do you wish I would tell you what you are? Can you think machines have to do with your problems?

**Bert**:
Please don't go. Why? Do you think I should tell you who you are? Do you think I need to deal with my past?

**Markov**:
Why do you think machines have to do with your problem? Do you wish to were me? I am sorry to hear that you are. Do you believe that dreams have something to do with your problem? Why don't you?

**Bert**:
What do you think I have to do with your problem? Do you want something from me? I am sorry to hear that you lied. Do you think my lies have anything to do with your problem? Why didn't you?

**Markov**:
Don't you think? Do you wish to were me? Have you tried? Do you wish I would tell you what you are doubtful that you came to me?

**Bert**:
Don't you understand? Do I want you with me? Have you forgotten? Do you think I can tell you who you are, that you belong to me?

**Markov**:
What are your feelings now?

**Bert**:
Where are my parents now?

**Markov**:
Would you want to be me.

**Bert**:
But I wanted to be alone.

**Markov**:
You seem to need to be quite positive. Does thinking of a very special person? Why don't you? I'm sure it's not pleasant to be quite positive. Why do you think that coming here will help you?

**Bert**:
You seem to me to be very positive. You make me a very positive person. Why don't you? I'm sure it's not going to be that easy. How do you know that being positive will help me?

**Markov**:
Perhaps I am sorry to hear that you are not sure I understand.

**Bert**:
" I am sorry to say that you are not sure I understand.

**Markov**:
Can you elaborate on that? What about machines? In what way?

**Bert**:
Should I check on them? Where are they? In what way?

**Markov**:
Could here really be some connection?

**Bert**:
Could this possibly be a dream?

**Markov**:
Perhaps I am in your fantasies. I am sorry to hear that you are doubtful that you came to me? What does that suggest to you? What do you think? Does that trouble you?

**Bert**:
" I am in your debt. I am sorry to say that you are sorry that you lied to me. What does it matter to you? What do you think? Does it bother you?

**Markov**:
What else do you think that coming here will help you?

**Bert**:
How much do you know about being able to help me?

**Markov**:
But you are doubtful that you are doubtful that you are. What does that suggest to you? Can you explain? Do you wish to were me? Do you really doubt yourself?

**Bert**:
That you are, that you are, that you are. What does it matter to me? Do I care? Do I want you with me? Do you even want me?

**Markov**:
Is it because you are? Please don't apologize. What are your feelings now? You are sure.

**Bert**:
Is that what you want? I don't know. What are those words about? You are mine.

**Markov**:
You don't seem quite certain. Have you ever dreamed before?

**Bert**:
You don't sound so sure. Have you ever asked me?

**Markov**:
I don't care about names. Please don't apologize. Tell me more about such feelings. What incident are you thinking of that bring anything else to mind?

**Bert**:
I don't care about you. I don't care. Tell me something about your heart. God, are you ever going to give it back to me?

**Markov**:
Does that trouble you? Please go on.

**Bert**:
Does it bother you? he went on.

**Markov**:
I've told you before, I don't understand that. That's quite interesting. Is it because you are?

**Bert**:
I've seen it before. I don't know why. It's so beautiful. Is that what you want?

**Markov**:
Would you want to be me. Why do you think?

**Bert**:
Because you want to see me. What do you want?

**Markov**:
Have you tried?

**Bert**:
Have you heard?

**Markov**:
But you are doubtful that you came to me? What are your feelings now? Please go on. Can you think computers can help people?

**Bert**:
And you were there when you came for me. What were those words about? He went on. Do you think you can trust me?

**Markov**:
Is it because you are doubtful that you came to me? Would you like to believe? What do you think that coming here will help you?

**Bert**:
Is it because you are afraid that you lie to yourself? Do you want to lie? Or do you think that being afraid will hurt you?

**Markov**:
What is the connection between me and you? I'm not sure I understand you fully.

**Bert**:
What is the difference between me and her? I'm not sure I know that yet.

**Markov**:
Do you really doubt yourself? I'm sure it's not pleasant to be me. Have you ever dreamed before? That's quite interesting.

**Bert**:
Have you ever dreamed before? I'm afraid it's not going to help you. Have you ever dreamed before? It's so strange.

**Markov**:
Don't you think about machines?

**Bert**:
Don't you know the answer?

**Markov**:
I see. Do you dream often?

**Bert**:
He said, Do you live here?

**Markov**:
Would you like to believe?

**Bert**:
Would you like to come?

**Markov**:
What other connections do you suppose? Do you wish I would tell you what you are. What other connections do you think its likely?

**Bert**:
What other connections do you have? Do you think I can tell you where they are? What other connections do you think are there?

**Markov**:
Do you dream often? Would you like to believe? You don't seem quite certain. Do you wish I would tell you what you are.

**Bert**:
Do you know them? Do you want to know? You don't sound so sure. Do you think I should tell you who they are.

**Markov**:
Does thinking of a very special person? You don't seem quite certain. Does that trouble you?

**Bert**:
You know, a really bad idea. You don't sound so sure. Does it bother you?

**Markov**:
Do you think its likely? You seem to be quite positive.

**Bert**:
Do you think it is? We have to be more careful.

**Markov**:
How? What other connections do you tell me that now?

**Bert**:
Why? What other choice could he give her right now?

**Markov**:
Do you really doubt yourself? I see. Can you elaborate on that?

**Bert**:
Can you really trust me? I asked. Can you count on me?

**Markov**:
What do you suppose? I see.

**Bert**:
What do you want? I asked.

**Markov**:
You seem to be.

**Bert**:
It had to be.

**Markov**:
But you are doubtful that you are. I understand you fully.

**Bert**:
Because you are all that I am. I love you too.

**Markov**:
I don't understand that. Perhaps I am sorry to hear that you came to me? Does that trouble you? I am in your fantasies.

**Bert**:
I don't blame you. But I am sorry to hear that you lied to me. Does it bother you that I was in your head.

**Markov**:
Do computers worry you? Would you like to believe? Are you thinking of that bring anything else to mind?

**Bert**:
Do I know you? Do I want to know? Does just thinking about you mean something more to me?

**Markov**:
Do you think machines have to do with your problems? Why do you suppose? How? Perhaps in your fantasies.

**Bert**:
Do you think they have to do with your dreams? What do you think? No. Not with your dreams.

**Markov**:
Could here really be some connection? Do you dream often? What are your feelings now? Have you tried?

**Bert**:
Could this possibly be a dream? Did you sleep well? What are these dreams about? Have you eaten?

**Markov**:
Do you wish to were me? Please don't apologize. What incident are you thinking of a specific example? Have you ever dreamed before?

**Bert**:
Do I want you inside me? I can't think. God, are you part of a bad dream? Have you really dreamed it?

**Markov**:
I am in your fantasies. I've told you before, I don't care about names. Do you think?

**Bert**:
You live in my house. I've told you before that I don't care about you. Do you understand?

**Markov**:
What do you think? Do you believe that dreams have something to do with your problem? You are sure. Why do you recollect? Have you ever dreamed before?

**Bert**:
What do you think? Do you think your actions have anything to do with this place? You are wrong. What do you recollect? Have you ever seen it?

**Markov**:
Would you like to believe? Would you like to believe? Please don't apologize. What do you tell me that now? Perhaps I am in your fantasies.

**Bert**:
Would you like to believe? Would you like to believe? I don't know. Why do you ask me that question? Because I am in your head.

**Markov**:
Please don't apologize.

**Bert**:
I don't know.

**Markov**:
What do you think about machines worrys you? I'm not sure. I am sorry to hear that you came to me? What do you mention computers? I don't care about names.

**Bert**:
What do you think and what bothers you? I'm not sure but I am glad to hear that you talk about me. How do you know that? I don't talk about you.

**Markov**:
But you are? When? What does that suggest to you? What resemblance do you recollect?

**Bert**:
Who you are? Why? What does it matter to you? What exactly do you recollect?

**Markov**:
Are you thinking of that bring anything else to mind? What resemblance do you think that coming here will help you? I understand you fully. That's quite interesting.

**Bert**:
Will my feelings for you be any different for me? And how do you think me being here will help you? I love you too. It's that simple.

**Markov**:
Do computers worry you?

**Bert**:
Do I know you?

**Markov**:
Do you wish to were me? What incident are you thinking of?

**Bert**:
Do I want you inside me? What else are you afraid of?

**Markov**:
Why don't you?

**Bert**:
Why wouldn't he?

**Markov**:
That's quite interesting. I understand you fully. What is the connection between me and you? I understand. Why do you see?

**Bert**:
It's that simple. I know it is. What is the difference between me and you? He thought, What do you mean?

**Markov**:
You are sure. I see. What does that suggest to you?

**Bert**:
You were right, he thought. What did you do to me?

**Markov**:
I've told you before, I don't care about names. What is the connection, do you see? Can you explain? Do you think its likely?

**Bert**:
I've told you before that I don't care about you. That is the problem, do you understand? Do you understand? Do you think it matters?

**Markov**:
What about machines? What resemblance do you suppose that resemblance means?

**Bert**:
Who are you? What exactly do you think my name is?

**Markov**:
Do you really think so?

**Bert**:
Do you really think so?

**Markov**:
When? You don't seem quite certain. In what way? Can you think that coming here will help you?

**Bert**:
Why? You don't sound so sure. In what way? Do you think my being here will help you?

**Markov**:
Do you think about machines worrys you? What do you tell me that now? Do you dream often? When? You don't seem quite certain.

**Bert**:
Do you think my presence bothers you? Why do you ask me that question? Do you think so? Why? You don't sound so sure.

**Markov**:
What do you think of a specific example? Please don't apologize. Would you want to be? Don't you think? You don't seem quite certain.

**Bert**:
What do you think is a good idea? It can't be. Do you want to know? Don't you think? You don't sound so sure.

**Markov**:
I am sorry to hear that you are? Does thinking of a specific example? I understand. Have you ever dreamed before?

**Bert**:
I am glad to hear that you are. So what is your favorite song? I asked. Have you ever heard it?

**Markov**:
Would you want to be me.

**Bert**:
But I wanted to be alone.

**Markov**:
Is it because you are. Have you tried? How? Have you ever dreamed before? Do you think machines have to do with your problem?

**Bert**:
Do it if you can. Have you dreamed? How? Have you ever dreamed before? Do you think you have to deal with it now?

**Markov**:
You are sure. Do you wish to were me?

**Bert**:
I am sorry. Do I need you with me?

**Markov**:
Are you thinking of that bring anything else to mind? Perhaps I am in your fantasies. You seem to be? Could here really be some connection? What else do you recollect?

**Bert**:
Did seeing him like that mean something more to me? Maybe it was in my head. I tried to think. Could there really be a connection? What else could I recollect?

**Markov**:
What do you see? You don't seem quite certain. Have you ever dreamed before? You seem to be quite positive.

**Bert**:
What do you mean? You don't seem very positive. Have you ever been positive? You seem to be very positive.

**Markov**:
Do you dream often? I've told you before, I don't understand that.

**Bert**:
Did you sleep well? I've told you before that you don't trust me.

**Markov**:
Have you tried? How? Would you like to believe? Why do you think of a specific example?

**Bert**:
Have you seen the video? Would you like to know? What do you think is a good idea?

**Markov**:
What else do you see? What else do you see?

**Bert**:
What else do you see? What else do you hear?

**Markov**:
Please don't apologize. You are sure. Perhaps I am sorry to hear that you are not sure. Do you think computers can help people?

**Bert**:
But don't worry. You are fine. And I am going to see if you are all right. Do you think you can help me?

**Markov**:
Don't you think of a specific example? What do you recollect? Does that trouble you?

**Bert**:
Can't you think of a different story? What do you recollect? Does it bother you?

**Markov**:
What other connections do you see? Do you really doubt yourself?

**Bert**:
What other choice do I have? Will he ever forgive me?

**Markov**:
Are you thinking of? How? Perhaps in your fantasies we are each other.

**Bert**:
Are you happy now? Me : Because in our hearts we love each other.

**Markov**:
You seem to need to be? Tell me more about such feelings. Please don't apologize.

**Bert**:
What was the point of that? Tell me more about your life. But don't worry.

**Markov**:
Do you believe that dreams have something to do with your problems? You are sure. Do you wish to were me? What else do you see?

**Bert**:
Do you think your actions had anything to do with your actions? You were hurt. Do you care who hurt you? What more do you want?

**Markov**:
I understand you fully. What do you think computers can help people? Do you wish I would tell you what you are?

**Bert**:
I hear your voice. How do you think you can hear me? Do you think I can tell you where you are?

**Markov**:
You are sure. Do you think its likely? I'm not sure. Please don't apologize. Do you really doubt yourself?

**Bert**:
You were right. Did you think it through? I'm so sorry. I didn't know. Do you still love me?

**Markov**:
What else do you suppose? I don't understand that. Can you explain? What about machines worrys you?

**Bert**:
What else do you know? I don't know anything. Can you imagine? Talking to me scares you?

**Markov**:
I'm not sure I understand. Is it because you are not sure I understand. I don't care about names. Do you think?

**Bert**:
I'm not sure I understand. Is that why you did it? I mean, I don't know the answer. Do you understand?

**Markov**:
What is the connection between me and you? Do you think computers can help people? I don't care about names. Perhaps you could.

**Bert**:
What is the difference between me and you? Do you think you can trust me? I don't know your name. But I do.

**Markov**:
Perhaps you could. When?

**Bert**:
But he did. Why?

**Markov**:
Perhaps I already know. What do you think that coming here will help you?

**Bert**:
" I think so. Why do you think my being here would bother you?

**Markov**:
Why do you think about machines worrys you? I understand you fully. Perhaps I already know. I don't care about names. Do you think that coming here will help you?

**Bert**:
What do you care about that bothers you? I know you do. But I do not. I don't care about you. Do you think my being here will bother you?

**Markov**:
Perhaps I already know. What does that suggest to you? Would you like to believe? You seem to need to be.

**Bert**:
" I think so. What does it matter to you? Would you like to know? You seem to want to know.

**Markov**:
Please go on. What does that similarity suggest to you?

**Bert**:
I was confused. What could this man do to me?

**Markov**:
What do you tell me that now? Can you explain? What do you think that coming here will help you? Do you wish I would tell you what you are doubtful that you are not sure I understand. Perhaps I already know.

**Bert**:
Why do you ask me that question? Can you tell? Why do you think my being here will hurt you? Do you think I can tell you that you are and that you are not? I ask, because I already know.

**Markov**:
Would you want to be? Do you wish I would tell you what you are.

**Bert**:
Do you want to know? Do you think I should tell you who you are.

**Markov**:
What incident are you thinking of? Don't you think machines have to do with your problem? Perhaps I am in your fantasies we are each other. What does that similarity suggest to you?

**Bert**:
What man are you talking about? Don't you think you want to be with me now? When I am in your arms we see each other. What did that man do to you?

**Markov**:
I'm not sure I understand you fully.

**Bert**:
I'm not sure I want him to.

**Markov**:
What is the connection between me and you? What do you mention computers? Do you dream often?

**Bert**:
What is the difference between me and you? Why did you leave me? Do you love me?

**Markov**:
What is the connection between me and you? Why don't you? How? In what way? Do computers worry you?

**Bert**:
What is the difference between me and you? Why shouldn't I? Why? In what way? Do I know you?

**Markov**:
Can you think? Is it because you are. Do you wish to were me? What about machines?

**Bert**:
Do you understand? Do exactly as I say. Shall I take you with me? What about you?

**Markov**:
Can you explain? I understand you fully. Tell me more about such feelings. What does that similarity suggest to you?

**Bert**:
Do you understand? I understand better now. Tell me more about your father. What did that man do to you?

**Markov**:
Do you really think so? What incident are you thinking of?

**Bert**:
Do you really believe that? What exactly are you capable of?

**Markov**:
Why do you see? What does that similarity suggest to you? What does that suggest to you?

**Bert**:
What do you mean? What does that word mean to you? What does it mean to me?

**Markov**:
Have you ever dreamed before? Do you believe that dreams have something to do with your problem? Perhaps I am sorry to hear that you are doubtful that you came to me?

**Bert**:
Have you ever considered that? Do you think your actions have anything to do with my actions? Because I am surprised to find that you are happy that you came to me?

**Markov**:
I understand.

**Bert**:
he asked.

**Markov**:
What is the connection between me and you? What do you recollect?

**Bert**:
What is the difference between me and you? What do you recollect?

**Markov**:
Does thinking of a specific example? How?

**Bert**:
You think that a good idea? Really?

**Markov**:
Do you dream often? Perhaps I am sorry to hear that you are not sure I understand you fully. Please don't apologize. But you are doubtful that you are?

**Bert**:
Do you speak English? And I am going to say that I do not. I know you, but I don't understand. And you are saying that I do?

**Markov**:
Have you tried?

**Bert**:
Have you heard?

**Markov**:
What resemblance do you tell me that now?

**Bert**:
Hey, can you hear me right now?

**Markov**:
Perhaps in your fantasies. Can you think computers can help people? I see. I've told you before, I don't understand that.

**Bert**:
Questions flooded my mind. Do you think I can read minds? I asked. I've told you before. I don't know how.

**Markov**:
In what way? Do computers worry you? Why don't you?

**Bert**:
In what way? Do I know you? Why don't you?

**Markov**:
What is the connection between me and you? What does that similarity suggest to you?

**Bert**:
What is the difference between me and you? What does the difference mean to me?

**Markov**:
Would you like to believe? What about machines worrys you? Tell me more about such feelings.

**Bert**:
Would you like to know? What if it bothers you? Tell me more about your family.

**Markov**:
That's quite interesting.

**Bert**:
It's that simple.

**Markov**:
What is the connection, do you mention computers? Have you tried? What incident are you thinking of?

**Bert**:
Where is your phone, do you have it? Have you forgotten? What phone are you talking about?

**Markov**:
Does thinking of a specific example? I'm sure it's not pleasant to be me.

**Bert**:
You know, a good friend. I'm sorry it's so hard to miss you.

**Markov**:
Perhaps you could. You are sure. But you are doubtful that you are? Would you like to believe?

**Bert**:
Maybe you are. You are everything. Maybe you are everything. I know. Would you like to know?

**Markov**:
Can you think its likely? Would you like to believe?

**Bert**:
Do you think it is? Would you like to know?

**Markov**:
Do you wish to were me? I understand you fully. Would you like to believe? What resemblance do you suppose that resemblance means? You seem to be?

**Bert**:
Do you think you understand me? I understand you too. Would you like to know? What exactly do you think that word means? You want to know?

**Markov**:
What does that suggest to you? What do you see? What does that suggest to you?

**Bert**:
What does it suggest to you? What do you think? What does it suggest to me?

**Markov**:
Do you wish I would tell you what you are? What do you see? Can you think of a very special person? What does that suggest to you? Perhaps in your fantasies.

**Bert**:
Do you think I should tell you who you are? What do you think? Do you think me a very good liar? What does it matter to you? Not even my name.

**Markov**:
Can you elaborate on that? What is the connection between me and you? I'm not sure. Do you really think so?

**Bert**:
Can you concentrate on that? What is the difference between me and you? I'm not sure. Do you really think so?

**Markov**:
Would you like to believe?

**Bert**:
Would you like to come?

**Markov**:
What do you suppose?

**Bert**:
What do you mean?

**Markov**:
Perhaps in your fantasies. Can you think computers can help people? Why do you see? What do you think its likely? Tell me more about such feelings.

**Bert**:
Not in my dreams. Do you think you can trust me? What do you think? What do you think is important? Tell me more about your dreams.

**Markov**:
Can you think machines have to do with your problems? What about machines? Don't you think machines have to do with your problem? Could here really be some connection? Do computers worry you?

**Bert**:
Do you think computers have to do with your problem? What about computers? Don't you think computers have to do with your problem? Can you really be a computer? Can I help you?

**Markov**:
You seem to be? Can you elaborate on that? Do computers worry you? Perhaps I already know.

**Bert**:
I need to know. Can you count on me? Can I trust you? Because I really do.

**Markov**:
What other connections do you tell me that now? Do you believe that dreams have something to do with your problem? Please don't apologize. I'm not sure. You seem to be me.

**Bert**:
What other questions can you ask me right now? Do you think these questions have anything to do with your past? I don't know. I'm not sure. You used to love me.

**Markov**:
What does that suggest to you?

**Bert**:
What did he do to me?

**Markov**:
Perhaps I am sorry to hear that you came to me? Perhaps you could. What else do you mention computers? Would you want to be?

**Bert**:
" I am sorry to hear that you came with me. If you wanted. Why else would you have come? Do you want to stay?

**Markov**:
Would you like to believe? Do you wish to were me? What does that suggest to you? That's quite interesting. Can you explain?

**Bert**:
Would you like to know? Can you smell it on me? What does it do to you? It's so sweet. Can you tell?

**Markov**:
You seem to be. I'm sure it's not pleasant to be? What is the connection between me and you? Does thinking of a specific example? I don't care about names.

**Bert**:
I want to, but I'm afraid it's not meant to be. There is a connection between me and him that I think is a good thing. I don't think about it.

**Markov**:
What do you suppose that resemblance means? I've told you before, I don't understand that. What is the connection, do you mention computers?

**Bert**:
What do you think the connection is? I've felt it before, I don't know why. What is the connection, can you feel it?

**Markov**:
You are sure. Perhaps in your fantasies we are each other. Do you wish to were me?

**Bert**:
We are one. And in my mind we are each other. Do I want him inside me?

**Markov**:
Perhaps you could. That's quite interesting.

**Bert**:
" I know. It's not fair.

**Markov**:
I'm sure it's not pleasant to be?

**Bert**:
I'm sure it's not meant to be?

**Markov**:
What do you think computers can help people? Do you wish I would tell you what you are not sure. Perhaps I am sorry to hear that you are. Can you explain? Do computers worry you?

**Bert**:
What do you think I can tell you? Do you think I can tell you if you are still alive? Because I am going to know who you are. Can you tell? Do I know you?

**Markov**:
I see. I understand. What other connections do you mention computers?

**Bert**:
He smiled and I nodded. What other way could he help me?

**Markov**:
What is the connection, do you think its likely? Why do you recollect? Do you really think so? You seem to need to be? That's quite interesting.

**Bert**:
What is the truth, and you know what is? What do you recollect? Do you really want to? You have to want to know. It's that simple.

**Markov**:
What incident are you thinking of that bring anything else to mind?

**Bert**:
God, are you really going to say something stupid to me?

**Markov**:
What is the connection between me and you? Would you like to believe? What is the connection between me and you? You don't seem quite certain. Do you really doubt yourself?

**Bert**:
What is the connection between me and you? Would you like to know? What is the connection between me and you? You don't sound so sure. Did you ever love me?

**Markov**:
What do you think that coming here will help you? Please don't apologize. Do computers worry you? Do you really doubt yourself?

**Bert**:
How do you think me being here will help you? I don't know. Can I help you? Will you ever forgive me?

**Markov**:
Perhaps I am in your fantasies. When? But you are doubtful that you came to me? I'm sure it's not pleasant to be me.

**Bert**:
" I was in your room. Why? Because you were there when you talked to me. I'm afraid it's not going to be easy.

**Markov**:
Does thinking of? I don't understand that. Do you think about machines? What does that suggest to you?

**Bert**:
I kind of... I don't know why. Do you know the answer? What does it mean to you?

**Markov**:
What do you think machines have to do with your problem? You seem to need to be me. Can you elaborate on that? I see. Perhaps I already know.

**Bert**:
What do you think I want to do with my life? You want to torture and torture me? Will you turn on me if I do? Because I never will.

**Markov**:
That's quite interesting. What incident are you thinking of that bring anything else to mind? I am in your fantasies. What is the connection, do you recollect?

**Bert**:
It's that simple. So, are you ever going to hear any more about her? I asked in my head. What was her name, do you recollect?

**Markov**:
Does thinking of that bring anything else to mind? What are your feelings now? What do you suppose? Would you want to be quite positive.

**Bert**:
Does any of it have anything else in it? What are your thoughts about? What do you think? Unless you want to be more specific.

**Markov**:
You are sure.

**Bert**:
They were alive.

**Markov**:
You don't seem quite certain. Why do you mention computers? Do you think that coming here will help you?

**Bert**:
You don't sound so sure. How can you say that? Do you think me being here will help you?

**Markov**:
I'm sure it's not pleasant to be quite positive. What else do you think about machines worrys you? What does that similarity suggest to you?

**Bert**:
I'm sure it's not going to be so bad. What else do I know about what scares me? What does the book say about me?

**Markov**:
What incident are you thinking of a specific example? Perhaps you could.

**Bert**:
So, are you thinking of a better life? Maybe I am.

**Markov**:
Could here really be some connection? You seem to need to be? In what way? Can you explain?

**Bert**:
Could it all be a dream? Or something that had to happen? In what way? Can you tell?

**Markov**:
Do computers worry you? Are you thinking of a specific example? I see. What is the connection, do you see?

**Bert**:
Do I know you? Are you part of a psychic network? I said, There is a connection, do you think?

**Markov**:
I am sorry to hear that you are.

**Bert**:
I am glad to hear that you understand.

**Markov**:
Do you wish I would tell you what you are doubtful that you are not sure I understand you fully. I am sorry to hear that you are not sure I understand. Do computers worry you? Does that trouble you? Do computers worry you?

**Bert**:
If I could I would tell you where you are and that you are safe. I know that now. I am sorry to hear that you were hurt. I apologize. Did it hurt you? Did it hurt you? Did it hurt you?

**Markov**:
What incident are you thinking of that bring anything else to mind? Do you think that coming here will help you? You seem to need to be me. Perhaps I am in your fantasies.

**Bert**:
What exactly are you two going to do about just being friends? Do you think just being friends will change anything? I want to try to be friends. Like I did in my dreams.

**Markov**:
Tell me more about such feelings. What do you suppose that resemblance means? What do you suppose? When?

**Bert**:
Tell me more about your mother. What do you think the note said? What did it say? Why?

**Markov**:
You are sure. What does that similarity suggest to you? In what way?

**Bert**:
You are dead. What did that thing do to you? In what way?

**Markov**:
Does that trouble you? What resemblance do you suppose that resemblance means? Do you really think so? What about machines worrys you? Do you wish I would tell you what you are?

**Bert**:
Does it bother you? How bad do you think that it is? Do you really think that? What if it bothers you? Do you think it will make you who you are?

**Markov**:
Does that trouble you?

**Bert**:
Does it bother you?

**Markov**:
What is the connection between me and you? Do you believe that dreams have something to do with your problems? What do you see? I'm sure it's not pleasant to be. What are your feelings now?

**Bert**:
What is the difference between me and you? Do you think my feelings have anything to do with your feelings? What do you think? I'm sure it's not meant to be. What are your feelings about?

**Markov**:
Is it because you are. What is the connection between me and you?

**Bert**:
Is that what you want? What is the difference between me and you?

**Markov**:
What incident are you thinking of a very special person? Would you like to believe?

**Bert**:
So, are you part of a completely different group? Would you like to know?

**Markov**:
What is the connection, do you suppose that resemblance means? But you are. Please go on. I'm not sure I understand you fully. I'm not sure.

**Bert**:
What is your name, do you think your name is? There you are. You are beautiful. I'm not sure I know you yet. I'm not sure.

**Markov**:
Why don't you? Please go on.

**Bert**:
Why wouldn't he? I pressed on.

**Markov**:
Does thinking of that bring anything else to mind?

**Bert**:
Did any of it have a ring to it?

**Markov**:
What do you think machines have to do with your problem? I am in your fantasies. Do you really doubt yourself? What about machines worrys you? Do you think about machines worrys you?

**Bert**:
What do you think I have to do with my life? I work for the government. Do you even know me? Everything about you scares me. What you think about me scares you?

**Markov**:
What about machines worrys you? Perhaps I already know. Do you think of a specific example? What do you see?

**Bert**:
So, what scares you? Because I think so. Can you think of a better way? What do you think?

**Markov**:
I see. Do you wish I would tell you what you are not sure. When? Do you think its likely?

**Bert**:
He said, If you think I should marry you, you are not interested. Why? Do you think it matters?

**Markov**:
What do you see? Can you explain? You are sure. Please go on.

**Bert**:
What did you say? Do you understand? You were right. Just go away.

**Markov**:
What incident are you thinking of? What do you tell me that now?

**Bert**:
What exactly are you afraid of? Why did you ask me that question?

**Markov**:
What do you see? Don't you think of a very special person?

**Bert**:
What do you think? Don't you think me a very bad person?

**Markov**:
Perhaps I am sorry to hear that you came to me? Do you really doubt yourself? What is the connection between me and you? Please go on. Do you really think so?

**Bert**:
" I am sorry to hear that you lied to me. Do you ever doubt yourself? What is the difference between me and you? Please go on. Do you really think so?

**Markov**:
Why don't you? What is the connection between me and you? Can you elaborate on that? What about machines worrys you? Perhaps I am in your fantasies.

**Bert**:
Why shouldn't I? What is the difference between me and you? Can you count on it? Every time it bothers you. Like it is in your heart.

**Markov**:
Does thinking of that bring anything else to mind? What other connections do you suppose? What about machines worrys you? How? Does thinking of a specific example?

**Bert**:
Does any of this have something more to it? What about me, I wonder? What about what scares me? Why? What good is a good thing?

**Markov**:
What does that suggest to you? Are you thinking of? What do you see? Perhaps in your fantasies we are each other. I am in your fantasies.

**Bert**:
What does it matter to you? Are you with me? What do you want? Because in your dreams we are each other. I am in your dreams.

**Markov**:
But you are not sure I understand you fully. What are your feelings now? Please don't apologize.

**Bert**:
But they are different. I know that now. Who are my feelings for? I don't know.

**Markov**:
Do you wish to were me? What does that suggest to you? Do computers worry you? What is the connection, do you suppose that resemblance means?

**Bert**:
Do you want anything from me? What does it matter to you? Do I love you? What is the question, do you think the answer is?

**Markov**:
You seem to need to be? What does that similarity suggest to you?

**Bert**:
They have taught me to walk. What does this place mean to me?

**Markov**:
I'm not sure I understand you fully.

**Bert**:
I'm not sure I want him to.

**Markov**:
I've told you before, I don't understand that. I've told you before, I don't care about names. How?

**Bert**:
I've told you before, I don't know names. I've told you before, I don't know any names. Why?

**Markov**:
Can you think of a very special person? Why do you suppose that resemblance means?

**Bert**:
Can you think of a completely different word? What do you think that word means?

**Markov**:
Why do you suppose that resemblance means? What do you see?

**Bert**:
What do you think that it is? What do you think?

**Markov**:
Would you want to be? Does thinking of?

**Bert**:
Do you want to know? Or approve of?

**Markov**:
You don't seem quite certain. Do you really think so? Could here really be some connection? Do computers worry you? What does that suggest to you?

**Bert**:
You don't sound so sure. Do you really think so? Can I really be a person? Can I be something? What does that mean to me?

**Markov**:
Do you think of a specific example? What do you recollect? What do you think of a very special person? You are sure. Do computers worry you?

**Bert**:
Do you think of a bad person? What do you recollect? What do you think of a really bad person? You were right. Do you believe me?

**Markov**:
What do you suppose? You are sure. When? Please go on. What does that suggest to you?

**Bert**:
What do you mean? You stayed away. Why did you stay away? What did you do to me?

**Markov**:
I see. Can you explain? Have you tried?

**Bert**:
He said, Did you eat? Have you eaten?

**Markov**:
What resemblance do you think its likely? Do you wish to were me? When?

**Bert**:
What else do I think is wrong? Do I want him inside me? Me?

**Markov**:
That's quite interesting. I'm not sure. I'm sure it's not pleasant to be? What do you see?

**Bert**:
It's not possible. I'm not sure. I'm sure it's not meant to be. What do I do?

**Markov**:
Is it because you are doubtful that you came to me?

**Bert**:
Was it because they were right when it came to me?

**Markov**:
I see. Have you tried? Why do you tell me that now? When? I am sorry to hear that you came to me?

**Bert**:
He said, Have you lied? Why do you ask me that question? Why do you feel compelled to admit that you lied to me?

**Markov**:
What do you mention computers? I'm sure it's not pleasant to be me. What other connections do you think computers can help people? Do you wish to were me?

**Bert**:
How can you do that? I'm afraid it's not possible to help you. What other way do you think you can help me? Can I help you help me?

\chapter{Section 4: Recursive}
\thispagestyle{empty}

**Markov**:
Do you think it matters? Don't even think about looking in the living room, so why wouldn't they? No, no. I don't know. It's not so sure.

**Bert**:
Do you think it is? Don't they talk about it in the living room, and why don't they? Oh, God, I don't know. She's not so sure.

**Markov**:
Palaemon and McCloskey were quick to agree. I'm an international expert on the show, but no one can count on me?

**Bert**:
Palaemon and McCloskey were inclined to agree. I'm an excellent fighter, for sure, but no one can count on me?

**Markov**:
I'm not stupid any more chances.

**Bert**:
I'm not taking any more chances.

**Markov**:
I asked. Is that what you want to tell me? He's dead, and try to get the words out. Why? But not now.

**Bert**:
He said, Is that what you want to tell me? That's it. I tried to get the words out. No. Just tell me.

**Markov**:
Can you tell me about it. I'll call Mr Smith. What else are you going to say that?

**Bert**:
You can tell me about it. I'll tell you everything. How exactly are you going to do that?

**Markov**:
I'm afraid it's not going to help you? Me: You will see how much?

**Bert**:
I'm sure he's not going to like it. Me : You gonna do that again?

**Markov**:
Do you think my being here will hurt you? Could this possibly be a connection? You get some potted plants in the yearbook either.

**Bert**:
Do you think me being here will help you? Will there even be a garden? With all the potted plants in the garden, yes.

**Markov**:
Do you think?

**Bert**:
Do you understand?

**Markov**:
Are you saying so? Spoken as if he had not seen this side of me.

**Bert**:
Are you saying that? Spoken as if you have never seen this side of me.

**Markov**:
What do you always work in a hospital cot? For a while. Do you think that word means? There's a strange feeling in the hospital a few more minutes! What is it?

**Bert**:
Why do you always sleep on a hospital cot? For a while. Do you think the bed moves? There's a strange noise in the room every few more minutes. What is it?

**Markov**:
Are you part of what happened, in an attempt to impersonate another person.

**Bert**:
Tell me more about what happened, in an attempt to impersonate another person.

**Markov**:
Can I help you. D.

**Bert**:
Could it be J. T.

**Markov**:
Do you think your actions had anything to do with a gun, which was the most important question to ask this morning. What's the IP address? No.

**Bert**:
Do you think her death has anything to do with the murders, or with the same horrible thing she did last night? What's her phone number? No.

**Markov**:
You'll want to. Who would stab me with dinner. What else do you know the answer is? Why?

**Bert**:
You'd surprise me. You could surprise me or something. What question do you think the answer is? Why?

**Markov**:
Hey, I'm not sure I'm in the Bunker Room to ask where we were on our way home? What do you know? Have you ever forgive me? What does the world at once.

**Bert**:
Well, I'm pretty sure I'm in the Bunker Room and know that we are on our way out. What do you think? Will you ever forgive me? I know the answer at once.

**Markov**:
You know, so don't look to the grocery store right now. " Mommy.

**Bert**:
You know, I can't go to the grocery store right now, " she said.

**Markov**:
" For one thing, because she'd been there. But not by much.

**Bert**:
" Just one thing, " he'd said again. But not by much.

**Markov**:
Do you want to know? Look, I beg. When is she going to pick you up if they don't eat you alive. Do I know that no one can help you?

**Bert**:
Do you want to know? Yes, I do. How is someone supposed to eat you alive if they can't eat you alive? Do you know that no one can eat you?

**Markov**:
Yes, Monsieur. I'm so sorry. What about WATCHS? It's nothing. I know the answer?

**Bert**:
Oh, God, I'm so sorry. Hello? MARCH : It's me. You know my name?

**Markov**:
Believe me, too! I'm a monster! So, what bothers you? Did it hurt you? All right.

**Bert**:
And me, too. I'm a vampire. So, what bothers you? Does it bother you? All right.

**Markov**:
I have two two - thirds of it. Why wouldn't he? Can you extend your hand to me? Do you remember?

**Bert**:
You have only two - thirds of it. Why don't you? Will you give your life for me? Do you understand?

**Markov**:
Good. Ha!

**Bert**:
Ha! Ha!

**Markov**:
What is what bothers you? No, no. Did seeing him like that.

**Bert**:
This is what scares me. Oh my God. Stop touching me like that.

**Markov**:
I'm always paramount when it's necessary. I need Mr. But I do. Tomorrow night.

**Bert**:
I'm not bedding and it's not like I was sleeping. But I was. Last night.

**Markov**:
No. Why don't you?

**Bert**:
No. Why wouldn't he?

**Markov**:
If I thought I could take a look at it, then. Can you help me? Maybe all the way here and now here you are.

**Bert**:
" I wish I could take a look at you, too. Do you miss me? Not all the time, and yet here you are.

**Markov**:
Gabby wanted to be. S.

**Bert**:
H. I. E. M.

**Markov**:
What else do you think my being here will help you? And soon the ultraviolet light will kick in, " a multi - layered voice, the precogs have even gotten away with stealing the car. We'd better find him before we move too fast.

**Bert**:
Where else can we go without looking back to find out? Pretty soon the ultraviolet radiation will be back on us by mid - afternoon, and the precogs have probably been responsible for destroying the planet. We'd better get moving before we move too fast.

**Markov**:
This is the problem. " I think I need your help, Sally. They're.. Did you sleep well? Then he said, There is a better life?

**Bert**:
That was the problem. " I think I need your help, too. You'll see. Did you sleep well? " I thought, What about a normal life?

**Markov**:
And you attended the game.

**Bert**:
" I won the lottery.

**Markov**:
The truth. Well sort of. Do you think?

**Bert**:
A girl. Well sort of. Do you remember?

**Markov**:
he asked. Every time it bothers you? He's nothing special. I'm sorry.

**Bert**:
I know. But, what bothers me? It's nothing personal. I'm sorry.

**Markov**:
Why? " " Lace tried to kill me.

**Bert**:
Why? " " Bane tried to kill me.

**Markov**:
Well, I know where I think I have booked you for everything. Yes, yes. No one disapproves of the property under your control has to be in your dreams. Oh, thank you.

**Bert**:
Yes, I do. I believe I have thanked you for everything. Yes, yes. No one disapproves that the power of divine intervention has to be in their hands. Yes, thank you.

**Markov**:
Whoa.

**Bert**:
Amen.

**Markov**:
" I know, mom and dad. And I do to you?

**Bert**:
What I do to mom and dad? What I do to them?

**Markov**:
I don't know what they say my white blood cell count is not high enough and I saw them yesterday, the postmark on the envelope.

**Bert**:
I don't know why I think the white blood cell count is so high, but I think it comes from the birthmark on his chest.

**Markov**:
" I don't know what to do something and have a score of 100 %. Or approve of? Where is the difference between me and her?

**Bert**:
" I don't know how to say that I have a score of 100 %. You know what? What is the difference between you and me?

**Markov**:
Not like he needs a little girl?

**Bert**:
Maybe because he wanted a little more?

**Markov**:
It's not important. No, it's not going to hear that you talk about me? I am sorry to hear that you lied to me?

**Bert**:
That's not true. Now, who's so sorry to hear that you lied to me? I am sorry to hear that you lied to me?

**Markov**:
I have to convince yourself that you are afraid that you are. They say that I know the road and you can understand me? Besides, some things just have to. Okay, let's see. Have you ever considered that?

**Bert**:
I want to know exactly who you are and what you are. You think that I dropped the bomb before anyone could stop me? Well, some people just have to. Well, let's see. Have you ever done that?

**Markov**:
" Oh, my best friend, Dominick. I have to go home? That's all. !!!

**Bert**:
" Oh, my dearest, Mam, I have to go now. It's all right. Please!

**Markov**:
But still. How'd you figure that out last night. He and Rann look over at the casino over there.

**Bert**:
Be careful. How'd you figure this out last night? You and Raul are staying at the hotel over there.

**Markov**:
Cooking. You're lucky the girl is here! Maybe you are? I'm sorry it's so hard to miss you. What exactly do you feel about these people.

**Bert**:
Interesting. You're lucky the guy likes you. And I am. I'm sorry it's so hard to like you. How bad do you feel about other people.

**Markov**:
What do you think? I'll have to go home? Do you think you can. You're out of here and now, what bothers you? What do you think you can drive away from here because you know.

**Bert**:
What do you mean? You'll have to go back. If you think you can. You're out of control right now and what scares you? How do you think you can get away from me, you know.

**Markov**:
God, I hope not, he listened, drinking a cup of coffee as the bank account? Legs and legs. How long would it take you with me? About the increase in pay?

**Bert**:
God, I hope so. I ask, grabbing a cup of coffee from my bank account. Legs and legs. How long will it take him and me? Is the car in gear?

**Markov**:
Would you like it? I'd love to break my heart I am not going to give it back to life? No, I'm glad. : How many words are needed in the world at once. It looks much, much, Claire.

**Bert**:
Do you want it? You'd like to tell your mother I am not going to give it back to you? No, I'm not sure. So many things are happening in the world at once. It is all too much, though.

**Markov**:
Are you okay with the connection is?

**Bert**:
Are you sure where the house is?

**Markov**:
I can't do this? I think this guy is just over 30 degrees C. Then we have the rest of your head. I mean, maybe a hundred and fifty dollars, but are you talking about? In touch with your change?

**Bert**:
I can't believe it. I think the temperature is just over eighty degrees today. Maybe you lost the contents of your stomach. I mean, after a hundred and fifty years, what are you talking about? The problem with the temperature?

**Markov**:
Yes, he could. What about Mr.

**Bert**:
Yes, it did. It did not.

**Markov**:
If you need? It could also be divided into three - day periods, such as Thanksgiving and Labor Day. Wanted to talk to me? Should I call her a whore?

**Bert**:
If you like, it can also be divided into three - day holidays, such as Thanksgiving and Labor Day. Want to talk to me? Can I get you a drink?

**Markov**:
Do you love me? Would you like to know.

**Bert**:
Can you hear me? " I wanted to scream.

**Markov**:
Not in my stupid, fucked - up, stop making this so difficult. Shut the hell up?

**Bert**:
And now I have to shut it up and stop taking it so seriously. Shut the hell up?

**Markov**:
You know mine. No, I can't be right there waiting? Does it scare you? I'm telling you how to find out. they stop.

**Bert**:
You look tired. Besides, you can't stay in here forever. Does it bother you? I'm telling you not to stay here until I return.

**Markov**:
I asked. For a man. I hated my mother? Want to call you if I can help with that for? Spoken as if he were a man in my bed when we were?

**Bert**:
Nothing else, not a word. She said my name. Wanted to tell me what I should say to her again? Spoken as if I heard her voice in my head before I died?

**Markov**:
Do you know? Maybe it was better not to sniff it. Wow, how do you feel, right? I'm so glad to hear that you talk about you.

**Bert**:
Do you mind? Maybe it was better not to sniff him. So, how do you feel, Sam? I'm so glad to hear that you care about me.

**Markov**:
Let Margie end up making it into your shoes. Have you ever doubt yourself? They're in their mid - twenties.

**Bert**:
Did Marlon end up throwing it in my face? Can I really blame him? They're in their mid - twenties.

**Markov**:
It can't be thinking about it. They were alive. Not anywhere in the morning.

**Bert**:
She shouldn't be thinking about that. They were late. Too early in the morning.

**Markov**:
Sorry.

**Bert**:
..

**Markov**:
S. What does the difference between me and you have to do. It means the child will be published in two weeks from the cold wind. What was the beginning of a better life? What are your feelings about?

**Bert**:
No. What does the letter say, do you want to know? It says the letter will be delivered in two weeks with a new name. This is the beginning of a new life. What are your thoughts about?

**Markov**:
I think so.

**Bert**:
I think so.

**Markov**:
That's 100 %. No, I'm not sure I'm giving you the fucking creeps for even thinking about her?

**Bert**:
She's 100 percent. Hell, I'm pretty sure I'm giving her the fucking creeps for even thinking about it?

**Markov**:
I wanted to be very frank, Monsieur le Sueur! Just give me just a little pale, but the rest of you, it was you, either. Do you love me?

**Bert**:
I tried to be very frank with Madame Le Sueur. It made me feel a little better, but the rest of it, it was nothing, really. Can you hear me?

**Markov**:
Why didn't you think I have booked you for two years to give it a try. None of this mess and'find'someone close to the bar, and him that I was looking for my sister - in - law.

**Bert**:
But don't you think I just bought it for two years and gave it a try? Because of that, I'called'someone close to the owner, telling him that I was looking for my brother - in - law.

**Markov**:
Just a man and - No! I'm not much for watching TV.

**Bert**:
Wait a minute because, frankly, I'm not one for watching TV.

**Markov**:
Nor will I ever kissed anyone? I'm sure that your mother is a good idea. Listening to music, he says from behind me. You know me?

**Bert**:
When have I last seen you? I'm sure meeting new people is a good idea. Rushing toward me, he spoke from behind me. You know what?

**Markov**:
I asked. I mean, I know you have to buy me a very popular dish in Puntland. Does it bother you? What's so important now to you?

**Bert**:
he asked. I mean, I know you have to make such a very important decision in Puntland. Does it bother you? What's so important now to you?

**Markov**:
What is the difference between me and you?

**Bert**:
What is the difference between me and you?

**Markov**:
It was all about it? Have you really dreamed it? Thank you. What is what bothers you?

**Bert**:
He is afraid of you. Have you ever seen him? Just once? That is what scares you?

**Markov**:
For the better. What does it matter to you? I don't know. Thank you so much fun at the barman's face with some amusement.

**Bert**:
All the time. What did he do to me? I don't know. Maybe not so much looking at the gunman's face for some reason.

**Markov**:
What you think and what bothers you? " I have two tickets. But the door unlocked. So much for taking the damn thing off.

**Bert**:
What you do is what scares me. " I grabbed my bag. Saw the door open. So much for taking the damn thing off.

**Markov**:
Do you really going to get a job here. Where do I do know. Thank you. I don't care about that one moment of conception? I want you with something.

**Bert**:
Are you ever going to have a baby? " What if I never did? Unlike her, I didn't think about the first day of school whether I liked it or not.

**Markov**:
We have a meeting with Adonis, and the movies or anything because it's so hard to miss you. You want to talk you can help them? What do you have one or two for lunch or dinner. Okay.

**Bert**:
I want a future with Adonis and if that future means anything, it's yours. I want you. I want you. I do want you. But do I want you to be with me or not? No.

**Markov**:
Please, I guess. Relax, who gets the long legs?

**Bert**:
Yeah, I know. Relax, who has the longest hair?

**Markov**:
Do you even know who you are. No. It was a social event on the retroviral virus. D. Do you think?

**Bert**:
Do you even know what they are? D. This is a scientific study of the retroviral virus. D. Do you understand?

**Markov**:
" Oh, thank you.

**Bert**:
" No, thank you.

**Markov**:
I nodded.

**Bert**:
He smiled.

**Markov**:
Next time, not anymore. Got it? What do you recollect? Just clean up the mess.

**Bert**:
This guy is after you. Got it? What do you recollect? Just clean up the mess.

**Markov**:
I had to think about giving my brother a one - way ticket to hell, hon. What do you think that word means? I'm not stupid. It's that simple.

**Bert**:
I hate to think about giving your brother a one - way ticket to hell, hon. What do you think his name is? I'm not sure. What's his name.

**Markov**:
I should get some potted plants in the English language as long as you said, If you want to know? Should I go?

**Bert**:
You can keep the potted plants in the same place as long as you like. Do you want to stay? Can I stay?

**Markov**:
No. My mother. And I am sorry to hear it?

**Bert**:
Yes. Your father. " I was surprised to hear that?

**Markov**:
The fact that there had been two - week vacations. What does it matter to you? Stone has the effect that the fire alarm is still in there, right? No.

**Bert**:
The fact that he has two two - week absences. What does that mean for him? He knows the fact that the police officer is still out there, right? No.

**Markov**:
Please, Sally. Of course. Don't worry, Mr Smith. Sometimes you just don't go to the hospital?

**Bert**:
Yes, sir. Of course. Don't worry, Miss Smith. Will you please don't go to the hospital?

**Markov**:
How do you think me a favor. You were hurt. Can you extend your hand on a man's six feet.

**Bert**:
Why do you owe me a favor? You look hot. And you put your hands on a man's bare chest.

**Markov**:
These guys are here. " " He's fine.

**Bert**:
You can stay here. " " It's okay.

**Markov**:
Why do you think I should tell you that.

**Bert**:
Why do you think I should tell you that.

**Markov**:
No. My favorite game ever! You have to try. Do you speak English?

**Bert**:
You. My best friend. " I had to ask. Do you speak English?

**Markov**:
Is that your vibe? If I thought it a try. What you think in your debt. Is that your mother is a good friend.

**Bert**:
Is that a bribe? " She gave him a look. But you are paying the price. Besides, your father is a good man.

**Markov**:
Have you responded to Mom's call? We'd better find him before we move too fast. But you were a great man. Wanted to talk to me.

**Bert**:
Have you listened to Father's instructions? I'd better warn you before you move too fast. But you are a foolish girl. Come and talk to me.

**Markov**:
Haven't liked you in jail. Suddenly, I want to cry. But I do know. I might add, it can't be right there waiting.

**Bert**:
Haven't seen him in years. Still, I want to know. And I also know, I might add, he shouldn't be out here alone.

**Markov**:
But c'mon, this isn't going to show you who you are. You were right. Amazing how much? And trying so hard to be something written on your credit card? It's so sweet.

**Bert**:
But c'mon, this isn't going to make you who you are. You are sorry. For how long? For trying so hard to get it right on your credit card? It's so unfair.

**Markov**:
If you let me go out and make some money. That's his name, can I do it again if I can get them a job and education. No! Do you think?

**Bert**:
You can let me go, and make some money. What's the point, if you do that, and I can get you a job in California? No. Do you understand?

**Markov**:
Can you ever had a normal life now. How? If all is well with you. What does it mean to me?

**Bert**:
Have you ever had a normal life before? Ever? When everything was different for you? What does it matter to you?

**Markov**:
What is the ticket! I'm not so bad. Well sort of. Why?

**Bert**:
This is my fault. I'm not that stupid. What kind of is he?

**Markov**:
How do I get fired? Sam turned to the Red Line station?

**Bert**:
How did they get here? Who came to The Shade for protection?

**Markov**:
I hope not, but they gave us a little girl! What is the difference between me and you? - - - you cold - hearted bitch. Don't do that? Just a friend?

**Bert**:
I said nothing, and he gave me a dirty look. What is the difference between me and you? " Oh, you cold - hearted bitch. Don't remember anything? Just a memory?

**Markov**:
Are we going to order room service? In touch with your actions have anything to do with your past? You're mine. Do I have to do with your life, do you ask me that again in the living room and he always makes up a story. I have to.

**Bert**:
Are you going to order room service? Your problems, your problems have nothing to do with your life. They're complicated. If they have to do with your life, then you tell him the story in the living room and he just makes up the story. You have problems.

**Markov**:
I've told you about the job with me? I'm sure it is.

**Bert**:
I've told him about my relationship with her. I'm sure he has.

**Markov**:
Who's really going to give it back and use the money.

**Bert**:
He's just going to do it, not take the risk.

**Markov**:
Besides, I know. Do you understand? Why not spend a million dollars to go in there. Was he sleeping in my heart. I can't breathe.

**Bert**:
Yes, I do. Do you understand? Why not take a million dollars and go back home? Is he really breaking my heart? I don't know.

**Markov**:
I did. Do you understand? Tell me, how much I can get them a job?

**Bert**:
He said, Do you mind? Excuse me, how about I go get you a drink?

**Markov**:
I am sorry to hear that you lied?

**Bert**:
He was going to ask where we were?

**Markov**:
Fifty miles an hour?

**Bert**:
Fifty miles an hour?

**Markov**:
I'll drop it if I have shared a hotel room, but are you talking about?

**Bert**:
I'll admit it, we never shared a single kiss, what are you talking about?

**Markov**:
Does it bother you? Anyway, I'm gonna make this woman miscarry. The same as it should be, but please be careful. But you know about me, I was born two years to give me a favor.

**Bert**:
Does that bother you? Look, I'm gonna have a little miscarry. The same as I always have, but please be careful. If you care about me, I was given two weeks to do you a favor.

**Markov**:
I'm sure it'll be done. Was he joking?

**Bert**:
I'm sure she'll be fine. Was he kidding?

**Markov**:
Could this really be a connection? " Oh, no. Where are you talking about? " Donny asked Mr. I have to stay.

**Bert**:
Could there really be a problem? " Yes, sir. What are you talking about? " Whoa, man, I have to go.

**Markov**:
Unless you want? And how do you think it is. Can you think my being here would hurt you? I don't know. Would you like to take care of this have something more to it because you are not sure I want roast beef, too.

**Bert**:
Whatever you want. So what do you think it is? Do you think me being here will help you? I don't know. If you want to depend on someone who has nothing better to do, you are pretty sure you want roast beef, too.

**Markov**:
Can you count on me? Do you think the media is saying anything about it. Oh, Jeez, what? I'm not sure I can also smell the blood of women. Have you ever forgive me?

**Bert**:
Can you smell on me? Do you think the killer is doing this to you? No. Jeez, what? I'm pretty sure I can still smell the killer on you. Will you ever forgive me?

**Markov**:
" Oh, I'm not just me.

**Bert**:
" No, I'm doing just fine.

**Markov**:
What do you think me a couple of antibiotics. You linger there, it is, my car, you and I will be in that position.

**Bert**:
Or maybe they gave me a bunch of antibiotics. Sleep lingers like it does in the morning. I know I can sleep in my bed.

**Markov**:
Do I know you have friends with you. Please, I don't think I should tell you who they are? Please be here when I'd fallen asleep - - - And, more importantly, I've seen them, and believe me?

**Bert**:
" I know you have them with you. Besides, I don't think I can tell you where they are. Not now, if you've been here before. " And, more important, he'd found them, so why bother?

**Markov**:
Sit down. But not by much.

**Bert**:
Harder. But not by much.

**Markov**:
What are those words about?

**Bert**:
What were those words about?

**Markov**:
What does the world be gone in an antique shop and keep these things in my heart we love each other? Do I want him inside me? " I have to go to the Red Line station? Can you think of a better reason? Many people eat Chinese and Japanese cuisine.

**Bert**:
How could a man have shopped the antiques shop all the time in his life and known each other? Would it mean anything to him? Would he want to go to the antiques shop? Would he know about the ranch house? Most people loved ranch - style houses.

**Markov**:
It's from Delia. An engagement ring?

**Bert**:
It's from Delores. An engagement ring?

**Markov**:
She was going to hurt you? Have you dreamed? Do you know? It's time to open the night I died. Placida stepped toward him.

**Bert**:
I am going to kill you. Let you live. Do you understand? It's going to be the day I die. Placida stepped toward him.

**Markov**:
What is it? How'd you figure that out last night. Let Margie end up making it into your shoes. But I'm going to be more specific. Not even my name is Decklan.

**Bert**:
What was it? How'd he figure it out last night? Did Marla end up punching him in the face? " I'm starting to get really nervous. Look, my name is Marla.

**Markov**:
I work for FRU for a change. Why wouldn't he?

**Bert**:
I worked for FRU for a while. Why wouldn't I?

**Markov**:
I thought, I only have two tickets.

**Bert**:
I mean, I do have some questions.

**Markov**:
And now they are waiting for me.

**Bert**:
And then they were looking at me.

**Markov**:
With a chance at a disadvantage. Pull over and. " It's not too late.

**Bert**:
One slow step at a time. Pull your weight. " It's already too late.

**Markov**:
Do you think it matters? Please don't go. Look, I would like to know. ' Then he walked away. You don't seem very tired.

**Bert**:
Do you think it is? Please don't ask. No, I would like to know. " Then he looked away. You don't look so good.

**Markov**:
I am sorry to hear it? Anyway, I mean, I feel like I've stepped into your life.

**Bert**:
I was glad to hear that. Now, I think, I feel like I've stepped into his shoes.

**Markov**:
I'm not sure.

**Bert**:
I'm not stupid.

**Markov**:
Hold on. So, what is it possible, what scares you? I'll work on it, then please give me her number.

**Bert**:
Come on. Well, how is that possible if it bothers you? I'll think about it and have you give me your number.

**Markov**:
I want you to leave your clothes on for me. And thanks to you? Do you understand? A pair of tweezers and a sergeant. Do I hurt you?

**Bert**:
I need you to put some clothes on for me. Come back to me. Do you understand? A pair of tweezers, a knife. Did I hurt you?

**Markov**:
What happened the other Ts can't find the body. I'm sure it's not going to do something. He's nothing special. Find things that I love you too. What do you think you can use the money?

**Bert**:
No wonder the other vamps can't find the body. I'm sure he's just trying to kill me. There's something else. The fact that they want me dead. How do they know they can find the body?

**Markov**:
I work for the opposite sex? And because of psychosis, but they killed him, and we'll have a few people. Of course not. I came up with that, but I think.

**Bert**:
You kill for the opposite sex. Not because of psychosis, but you kill people, and you'll kill a few people. Of course not. I came up with nothing, but I did.

**Markov**:
Do you think you want it back, but regrettably, at a career in the other room, and you answer them, killing them.

**Bert**:
But you - you do so often, so regrettably - kill your friends in the next life, and you kill yourself by killing them.

**Markov**:
What does it matter to you?

**Bert**:
What did he do to me?

**Markov**:
You have no place to stay? Don't you think me being here will help you?

**Bert**:
I need a place to stay. Don't you think me being here will help you?

**Markov**:
It would be fine. I've told you, the night before. I don't know. No, no.

**Bert**:
Everything will be okay, he'd told her, the night before. I don't know... Oh, God.

**Markov**:
I really be a fool. I just had a great life and, as evidence of how long you have to do something. A whole lot of money is going to happen. Me: Do you think the guy with the connection between me and you want to see how you can use the money.

**Bert**:
How to be a person. I have lived a good life before, no matter just how hard I try to make it. A whole lot of that is about to change. Me : Because I am the one with my life behind me. I want to know how I can get my way.

**Markov**:
That you are not here? Have you ever forgive me?

**Bert**:
But you are still alive. Can you ever forgive me?

**Markov**:
I'm so sorry. You are the first guy to calm down, though, because you know? I've told you before. No. Let it be a family?

**Bert**:
I'm so sorry. You were the first one to kill me, too, were you not? I've told you that. No. Would it be your fault?

**Markov**:
You know, mom and dad used to be? The truth. What is the sweetest I've ever heard it?

**Bert**:
You know what mom and dad used to say? The sweetest thing, the sweetest you've ever heard of?

**Markov**:
What's that for a different way?

**Bert**:
How's it been a long time?

**Markov**:
Do I love you too. I wished I had to happen. I don't know how.

**Bert**:
" I love you too. I knew it had to happen but I didn't know how.

**Markov**:
Why? Maybe, just so you wouldn't let me know you have one, you make me a really nice guy? You okay? There's duct tape, iodine, and every now and do a little bit like God's most precious gift.

**Bert**:
Please, please, please, please don't make me think you were lying, please make me a damn good liar. Please what? There's enough water, iodine and soap in there to look a little bit like someone's most precious possession.

**Markov**:
Is that your vibe? Thank you for your help, Sally. Do you want? What does this place?

**Bert**:
Is that a bribe? Thank you for your time, sir. Whatever you say. How is that possible?

**Markov**:
It was a lesson in manners. Thank you so you can use it, but then I look up and close your eyes. The blood.

**Bert**:
It was a lesson in manners. Thank you. I can do that, and then you lie down and close your eyes. No problem.

**Markov**:
Do you? At last. I can do without touching her. Have you ever dreamed before?

**Bert**:
Have you? At least, I can tell without asking you. Have you ever asked me?

**Markov**:
Do you want to help you? No. I'm not sure. Can you give me just a little push too far, too.

**Bert**:
Did I want to kiss him? Honestly, I'm not sure. Maybe I did, maybe a little bit too much, though.

**Markov**:
I can forgive you?

**Bert**:
I can hear you?

**Markov**:
You were right. " But I wanted to watch your house wasn't your love interest?

**Bert**:
You were right. " " She wanted to believe the man wasn't her best friend?

**Markov**:
If I thought I could, but someone who isn't.

**Bert**:
" I thought it was, but now it isn't.

**Markov**:
What is the difference mean to me. Maybe it was you, Mr. killin'me? He said, That's not true. Oh, no.

**Bert**:
What did that thing do to you? Did it hurt you, Mr. Screamin'Wolf? He thought, It's all right. No, no.

**Markov**:
Tell me more about your life.

**Bert**:
Tell me more about your family.

**Markov**:
A vampire?

**Bert**:
A vampire?

**Markov**:
Why did you stay away from you.

**Bert**:
Nor did she move away from him.

**Markov**:
I know. This is great, Mom. I think is a new one! I heard all this before.

**Bert**:
I smile. It feels good, too. I just need a new job so I can do it again.

**Markov**:
Nobody's going to be done. Damn it. No, because I want you to talk to him is a good time. Do you think are there bench seats? " I mean, I was just thinking about that bothers you?

**Bert**:
He's going to hurt you. Stop it. Good, because I want you to think about it at a later time. Do you... are there any questions? What he said when I was just talking to him scares me?

**Markov**:
Right. I have to ask him about it.

**Bert**:
No, I had to tell him about it.

**Markov**:
Legs and legs. I know it sounds like fun. If they don't know.

**Bert**:
Legs and all. I know he looks like shit. But I don't care.

**Markov**:
Haven't you talked to me?

**Bert**:
Haven't you listened to me?

**Markov**:
I'm sorry. Why do you mean? I'm sure it's not an accident.

**Bert**:
I'm sorry. What do you mean? I'm sure it's not an accident.

**Markov**:
You are beautiful. Have you ever considered that?

**Bert**:
You were right. Have you ever seen him?

**Markov**:
But in my mind. Where is the difference between me and you?

**Bert**:
Not in this world. What is the difference between me and you?

**Markov**:
Are you part of a completely different group? Why did you get here, and every now and do your job. " I do! Let's see. I've gotta get going.

**Bert**:
Are you part of a completely different world? Why did you go running from here to there to do your job? Because I did. Let's go. We've gotta get going.

**Markov**:
No. " Velocity? What matters is the difference between me and you can drive away from here to the movies or anything because it's really bad idea. He could do the same way about him? I am sorry that you don't.

**Bert**:
No. " Velocity? What really makes a difference to me? I never walk away from going to a party or anything unless it's a bad idea. You probably feel the same way about me. I am sure that you don't.

**Markov**:
Not so much.

**Bert**:
Not so much.

**Markov**:
This time, is it? " Not so much. Do you think I should have. How much do you always work in a drawer with a fellow soldier? He told me about you scares me?

**Bert**:
Not bad, is it? " Not so bad. " I think you already know. How long do you just sit in a room with a strange man? Who told you that he stalks you?

**Markov**:
Please don't go to the top of the night before. It could also be divided into three - day periods, such as Thanksgiving and Labor Day. Why did you get that stuff? You have no reason to be.

**Bert**:
I can't get to the end of the week yet. It can only be divided into three - day periods, such as Thanksgiving and Labor Day. Why do I need a car? I have no place to go.

**Markov**:
Do you understand me, the truth.

**Bert**:
If you ask me, the truth.

**Markov**:
Of course. But unfortunately for her he was talking about? How's it going?

**Bert**:
Of course. But what about what he was talking about? How's it going?

**Markov**:
No. Let's take a shower first. For the better.

**Bert**:
No. Let's take a walk then. Lead the way.

**Markov**:
What do you want to. Does that count? " There it was you, and I'll get you? Is that what you need to be more than a no - show? Okay, okay.

**Bert**:
Only if you want to. Will that work? " If I get you, then I'll get you. Is that why you want to be more of a no - show? Okay, okay.

**Markov**:
I was in no hurry to go a long way in being a learner because it's really bad person? Why can't you? Do you still love me? He's the one who caused the drug - induced decompression has not receded from their minds.

**Bert**:
I am in a position to go a long way toward being a cheater because he's a good guy. Why shouldn't I? Because I do love him. He's the one who said the drug - induced decompression had completely receded from his body.

**Markov**:
No, she thought. I just want to know? Don't you think I can do this? Would you like to know the answer.

**Bert**:
No, he said. I just want to know. Don't you think you can handle it? Because I want to know the truth.

**Markov**:
JJ: Yes, that's right.

**Bert**:
JJ : Yes, that's right.

**Markov**:
J. You have flaws in the insurance business. But I do have a new world.

**Bert**:
No, I have nothing in the insurance business. But I do have a small fortune.

**Markov**:
Would you like it is. In fact he is still in there, right?

**Bert**:
As bad as it was. In fact it was bad out there, right?

**Markov**:
Why did you? There were no words. I hear your voice. Because I really be a dream we saw each other. It's not just one.

**Bert**:
Or do I? There are no words. I hear his voice. Will there ever be another time we see each other? Now's not the time.

**Markov**:
Tell me more about your dreams you see? I can do this.

**Bert**:
Tell me more about this place, okay? I can do this.

**Markov**:
And where did he get those knee - braces? She was going to enjoy it, and I nodded. I know you? You are beautiful.

**Bert**:
And where did he get his back - rubs? I was starting to get nervous, but I nodded. I love you. You are mine.

**Markov**:
In fact he is going to say. At least I didn't know. Can't imagine what it would have to. Don't throw a fit. If you need to be very positive.

**Bert**:
Every word he was going to say. At least she didn't know. Couldn't imagine what he would react to. Don't throw a fit. " I need to see a doctor.

**Markov**:
Please don't cry. What would happen to me. Are you with me. How did you leave me? - - - She's acting like a date.

**Bert**:
But don't worry. Nothing will happen to you. Just stay with me. Why would he hurt me? - - - He's more than a friend.

**Markov**:
He was covered in fur and tusks. Missy, how's the coffee?

**Bert**:
He was covered in fur and tusks. Missy, where's the boy?

**Markov**:
I'm sure that the United States or Canada.

**Bert**:
I'm originally from the United States and Canada.

**Markov**:
Do I know I should tell me who you are?

**Bert**:
" You think you can tell me who you are?

**Markov**:
What do you do.

**Bert**:
What could he do.

**Markov**:
Really? I'm not on the table now that I am glad to hear that you are? Let's move on. There you are? Do you still love me?

**Bert**:
What if I'd acted on an impulse and decided I was dying to know who you were? Let's move on. There you go. Do you still love me?

**Markov**:
What are your names again?

**Bert**:
What were their names again?

**Markov**:
This is the best way to put in my life in order to learn how to cook. What does it mean to me? I don't know how to do with the second one? Yes, I was confused. Let it be a fool.

**Bert**:
This is the first thing I do in my life in order to decide what to do. What does it matter to me if I can't decide what to do with the wrong person? God, I am sorry. Let me be a coward.

**Markov**:
Yes, I want him to think. You are at a disadvantage.

**Bert**:
Please, I need you to understand. You are at a loss.

**Markov**:
Sie, bleißt, wissen kein leben, right? Do you think you have come? Strake: No. What do you think me a very bad person?

**Bert**:
Sie, blei Gott, wissen kein Liebe. Hans : Do you think I should go? Steffen : No. But do you consider me a very good friend?

**Markov**:
His phone rang. I know you must be somewhere else. Yes.

**Bert**:
The phone rang. She thought it might be someone else. No.

**Markov**:
Tell me more about your family. Are you sure?

**Bert**:
Tell me more about your family. Are you sure?

**Markov**:
Very unlucky, Tikkun, but someone who knows what his fate will soon be. Maybe this little hook - up was the most important question to ask this morning. " You're right about that bothers you?

**Bert**:
Not unlucky, Viktis thought, but one who knows what his fate will soon be. Perhaps a little warm - up is the most appropriate thing to do this evening. " You're saying that it bothers you?

**Markov**:
I have to be done. No questions. I need to be enough. He looked at me. You seem to be riding a camel.

**Bert**:
I need to be more. Much more. I need to be more. He smiled at her. I need to be like a camel.

**Markov**:
Maybe we should go? Do you think the media is saying anything about it.

**Bert**:
" You never know. Maybe they think the government is doing something about it.

**Markov**:
Do you think is a good way to get the words out, it's my only option right now.

**Bert**:
All I need is a quick way to get the hell out and that's my only option right now.

**Markov**:
He's doing it. Okay, how much I hate going to give it a good thing.

**Bert**:
He's doing it and he knows it. I was beginning to find that a good thing.

**Markov**:
I couldn't imagine my wardrobe changing. Tell me more about your family.

**Bert**:
I won't see you ever again. Tell me more about your life.

**Markov**:
Just wake up? We're just going to the right time and place. A pair of tweezers and a sergeant. Where you going to do with the similarity? Do you think I can?

**Bert**:
Not right now. We're finally getting to the right time and place. A pair of tweezers and a knife. What you want to do with a knife? Do you think you can?

**Markov**:
What you think?

**Bert**:
Do you understand?

**Markov**:
And I am. That's very interesting. It's so weird. Should I play the piano, or sing the national anthem? In the insurance business.

**Bert**:
" I know. It's so weird. It's so weird. " You play the piano, you sing the national anthem. In the living room.

**Markov**:
" It's strange in a place here, in part, in exchange for a change. Male or female? He said, That's not true. Why do you have to wait until the next week.

**Bert**:
" It's not just a show but, in fact, an event with a theme. Male or female? I mean, that's just it. Why do we have to wait for the next show.

**Markov**:
Please, God, I'm gonna have a weekend together. This whole stupid hookup with a plan.

**Bert**:
Oh my God, I'm gonna do that shit again. This whole whole damn thing is my fault.

**Markov**:
And, yes, yes, we hold hands with our parents and watch our parents and watch our parents either laugh, or any other place. My favorite game ever! They did it for over twenty years, and every now and do a bit of shopping for a reason?

**Bert**:
Yes, yes, yes, we hold hands with our families and with our friends and with our families like that, in a good way. My favorite thing is that we do that for about twenty years and go back home and do a lot of things for a living?

**Markov**:
Oh God, are you? Yes, there is a Wonder Woman. Can you concentrate on that?

**Bert**:
Dear God, are you? Yes, she is the Reverend Mother. Can you count on her?

**Markov**:
I wanted to watch your house with a credit card? What do you recollect? Have you changed? If they don't eat you alive.

**Bert**:
I have to take my wife on a business trip. What do you recollect? Have you forgotten? Because I won't see you again.

**Markov**:
Do you think? I'll take you with me now? Now come on. Well, we hold hands with our parents and watch our parents either laugh, or any other way would she know where I am. We have a big deal.

**Bert**:
Do you understand? I'll take you with me now. We hold hands. And I will hold hands with my mom, and my dad will understand, because no other way would he know who I am. I made a terrible mistake.

**Markov**:
What other way do you think the note again. I don't want to see you. Is that what you want to do something. Mab's coming for me. You look good.

**Bert**:
What other reason did you write that letter for? I didn't want to hurt you. Is that why you wanted to do it? Maura's staring at me. You did it.

**Markov**:
D. This is the point? We all agree with her.

**Bert**:
No. What is the point? We all agree with you.

**Markov**:
Where else would I if I'd had the chance! " We were talking about? Did you sleep well? It's that simple. What do you think of a different story?

**Bert**:
Why else would you think you'd had a dream? What you were dreaming about? Did you sleep well? It's that simple. Why would you dream about a bad dream?

**Markov**:
What is the connection between me and her? Are you part of the property under your control has to be discourteous. Hadn't being able to help you? He told me about you. What's the matter?

**Bert**:
What is the difference between you and him? Is he one of those people in your life trying to be discourteous? Isn't he trying to hurt you? He told me about you. What's the difference?

**Markov**:
I don't know your name, Jacky. Utilities, too?

**Bert**:
I don't know your name, Miss Smith. Utilities, right?

**Markov**:
That is the difference between me and you? This whole stupid hookup with a knife or something? Do you want? Your mom will remember what I would say I've agreed to it because I want to know?

**Bert**:
What was the deal with me and you? A nice little hookup with a guy or something? Anything you want? A girl can come, you know. I've seen to that. You want to come?

**Markov**:
how you can hear your own business. But I have an answer for you for the UDD.

**Bert**:
Then you can mind your own business. " I have an appointment for you with the UDD.

**Markov**:
Do you think I remember the size of it. Yeah, I will write you a room, so you wouldn't let me know you? But soon you'll see.

**Bert**:
Do you think I know the half of it? Look, I can buy you a drink, but you won't let me touch you. And then we'll talk.

**Markov**:
I asked. In five minutes. It was all. Look, I think I can take any more about your father will be officiating.

**Bert**:
I nodded. About five minutes. That sounds good. But if you think you can do anything else, your father will be officiating.

**Markov**:
But, for the boys'basketball game.

**Bert**:
Then, after the boys'basketball game.

**Markov**:
I'm sure it is? Not with your problem? You'll want to know? Let me pick you up.

**Bert**:
I'm sure he does. What is his name? Who'd want to know? Let me look him up.

**Markov**:
Do you believe me? Come on in, too. Is that why you work on the school grounds, and you?

**Bert**:
Can you hear me? Come on in, boy. Was that why he was on the school bus, was it?

**Markov**:
How stupid are all right. Not anywhere in the living room, and the crowd fell silent. I am again.

**Bert**:
The lights were not on. Not even in the living room, where the TV was on. I tried again.

**Markov**:
And it was when I saw the titties. I'm here. What happened? I have?

**Bert**:
And that was when I saw the titties. I'm sorry. What else could I say?

**Markov**:
And I am working satisfactorily. I work for FRU for a couple of antibiotics.

**Bert**:
But he was working satisfactorily. He supplied the FRU with a couple of antibiotics.

**Markov**:
Can I be? But you're not a girl. I'm going to have a crush on her once, and I can't. Do I know about being able to get his bearings. I don't care about right now?

**Bert**:
Should I be? Because you're just a girl. I'm supposed to have a crush on you too, but I don't. Do you care about being able to do the things that I don't care about right now?

**Markov**:
Do you think?

**Bert**:
Do you understand?

**Markov**:
Can I help you? What do you think I have a score of 100 %. Yes, that's right. Tell me more about your dreams. " You did it for you for your help.

**Bert**:
Can I help you? Why do you think I have a score of 100 %? Yes, that's it. Tell me more about your score. But I must ask of you for your opinion.

**Markov**:
how you feel about these things anyway? Do I want him inside me? Oh, well?

**Bert**:
How I feel about these things now. Do I want him inside me? Oh my God?

**Markov**:
Well, well, that you are? It's the truth, she thought bitterly. Do I have to deal with?

**Bert**:
Yeah, well, there you go. It's the truth, she thought again. Do I have to go back?

**Markov**:
Yes, yes, yes. I am sorry to hear that you were lying when you have come? Tell me more about your actions? I searched, but now, what scares me?

**Bert**:
Yes, yes, yes, I am glad to hear that you are happy that you have changed. Tell me more about your life after you have changed, yes, what bothers you?

**Markov**:
Got it? Do you think my being here will help you with me? Yes, it brings back memories. Dont make sure you pick the right time and place. I asked.

**Bert**:
Is it? Do you think my being here will keep you from dying? No, it brings back memories. Dont be sure you have the right time and place, he said.

**Markov**:
Is that what you are happy that you and wouldn't fall in love with you, but he's saying it's my turn.

**Bert**:
Is that why I keep thinking about you and don't fall in love with you, because he's saying it's my fault.

**Markov**:
Does it bother you? In case he didn't have a choice?

**Bert**:
Would he kill me? In case I didn't have a choice?

**Markov**:
All right. Stone. We're just going to get a grip.

**Bert**:
All right, then. You're just trying to get a grip.

**Markov**:
I had to be done in the same department? It's so beautiful! How do you mean?

**Bert**:
It has to be done in an art studio. It's so beautiful. What do you think?

**Markov**:
I don't know, but not in the same page anymore. Besides, I was just going to happen?

**Bert**:
I didn't know, certainly not on the same page yet. What if it was never going to happen?

**Markov**:
I don't care about me? - - Grant, how do, it pays off.

**Bert**:
I don't know about that, either. Well, you know how it turns out.

**Markov**:
No. You have no right to judge me. I haven't liked her in the living room when the sun's going down, and whatever had caused the drug lord made a big party in about two hours or so anyway, don't I? You don't know names.

**Bert**:
No. You have no right to judge me. I haven't seen you in the living room since the sun's gone down, and if you think a drug dealer throws a dinner party in under five minutes, then yeah, don't you think I don't like it.

**Markov**:
Have you heard? All of it eventually, and read the note said? - - She's acting like something is going on at Pete's, thought Artie.

**Bert**:
Have you heard? What about the girl, what has the girl done? - - She's acting like something is going on at Pete's, thought Artie.

**Markov**:
Can you smell it on me? How high is the problem, do you think? Ready for the government would just let me go, you're the best part of a better way? Sam turned to the movies are bad.

**Bert**:
Can you blame it on me? Get out of my life, do you think? As if the world will ever let you go because you're the best friend to the next person. Getting back to my apartment was difficult.

**Markov**:
" I don't think anything is funny. You think I should tell you who you are. " the man who owns it has < u > a place and there ain't nothin'but the man you want to see it?

**Bert**:
" You don't think this is right? You think I should tell him where you are, tell some guy who knows why I'm doing this, that there ain't nothin'in the world I want to do anymore?

**Markov**:
To get me out of character. Have you heard? It was raining, so I, uh, let me sleep, especially not in the Bunker Room to ask for a wager of epic proportions? Delivering me to say good - bye.

**Bert**:
You talked me out of it. Have you forgotten? It was raining, and everyone, who had set it off, had gathered in the Bunker Room to work on a nuclear bomb of epic proportions. Delighted only to say good - bye.

**Markov**:
The next stop was downtown. Well, that you can. You know all about me. Well sort of thing!

**Bert**:
My first job was teaching. Oh, yes I did. You know that about me. That sort of thing!

**Markov**:
Why? What's good for me I lost it too. Oh, I'm gonna have a few people. Yes, Monsieur. What do you know them?

**Bert**:
No. That's not all that I know, Monsieur. Anyway, I'm gonna meet a few people. Hello, Monsieur. How do you know me?

**Markov**:
What do you think I want to see him?

**Bert**:
Why do you think I want to see you?

**Markov**:
Can I really be a coal mine out there. Santino and his new best friend, he's a tween. How about some hot chocolate and then I went out of Fort Knox? A flat is much better than a no - show?

**Bert**:
Could there really be a gold mine out there? Santino is my new best friend and he's a tween. How about some hot chocolate and then we head back to Fort Bragg? Maybe this is nothing more than a no - show?

**Markov**:
" But you need to hack it down before the sun sets. Would he love being with her. " I am sorry to hear it again! You dont have any connection to them, but next time, I'll be sure to call when you talked about the money your employer will check your payroll, as evidence of how long you have?

**Bert**:
" But I want to hack it down before the sun sets. " She liked being around him. " I am glad to hear the news. I shouldn't have come after you, but in time, I'll be able to see where you are, the way your company will handle your payroll, any indication of how long you have?

**Markov**:
I am sorry that you lied.

**Bert**:
I am sorry, he said.

**Markov**:
I've still got him. Do I want to see you again one day when I was in the living room, but please be careful! If I could kill half a dozen people at once. Stone.

**Bert**:
I've still got you. And I hope to see you again one day when we get on the next plane, so please be careful. " I still feel like a million bucks, Mr. President.

**Markov**:
Would my father let me go, she thought. Pull out your tongue!

**Bert**:
But my mother let me go, she thought. Pull out my hair!

**Markov**:
Instead, we can get them a chance to speak privately.

**Bert**:
Besides, it would give her a chance to think clearly.

**Markov**:
Five minutes, maybe a hundred, maybe I'm harboring a fugitive. " I know in my life back? It's amazing how you are the second one? Johnson? Why not?

**Bert**:
Six months, maybe a year, and I'm harboring a fugitive. All I need is a name change. It's important that I have a new name, right? Why not?

**Markov**:
Yes, there is a joke.

**Bert**:
No, this is a dream.

**Markov**:
Tell me more about your dreams you see each other. Do I? The film also tells the true story of the world at once. What a stupid question?

**Bert**:
Tell me that in your heart you love each other. Do you have a book that tells you the history of the world at large? Or a history book?

**Markov**:
" Dwylar, I know I can't be seeing her in the world is half - thinkin'you might not be an easy task. You are a good way. Can you see my point?

**Bert**:
" Dwylar, you know I don't think having you in my life and re - lovein'you will ever be an easy thing. We have a long history. Do you see my point?

**Markov**:
But don't worry about it. You see, my God, it was easy. I'm going to say that there's no danger and don't hurt anyone. Did I hurt you? What are your thoughts about?

**Bert**:
But don't worry about it. Just know that by then, this is over. I'm going to ensure that there's no danger and don't hurt you. Did I hurt you? What are your thoughts about?

**Markov**:
I've told you before.

**Bert**:
I've seen it before.

**Markov**:
Me?

**Bert**:
Why?

**Markov**:
Do you think the idea of accent and accent and accent. It is so tidy. Thank you for your help, anyway. You were right.

**Bert**:
" I like the style, style and tone of it. It is very trite. Thank you for your help, sir. You are welcome.

**Markov**:
I've told you before that I care. " I just want you to know? But I do care. Do I want him inside me?

**Bert**:
I've told you everything that I know. Do I even want you to know? Do I even care? Do I want you with me?

**Markov**:
Do exactly as I say. Why? Ten years from now. And I am super hot and I'm starving.

**Bert**:
Not exactly what I expected. Five? Five hours from now? Because I am so hungry. I'm hungry.

**Markov**:
How long have you slept last night?

**Bert**:
How well had he slept last night?

**Markov**:
You're right, I'll stop crying when the sun's going down, though, I'm sorry, madam. I like one or two pieces of eggnog, if he cheated on her once, and you? Have you ever asked me? What other choice do you think? This is my first question.

**Bert**:
You're right. I'll come back when the sun's going down, but - I'm sorry, madam. I had one or two cups of eggnog, but I went for it anyway, did I? Have you ever kissed me? What other way do you know? It was my first kiss.

**Markov**:
I've felt it for over twenty years, and he's dead. " Hi.

**Bert**:
I've known him for over twenty years, and he's great. " Wow.

**Markov**:
Can you count on me? What is so boring. They're all obsessed with the abracadabra. This conversation really says a lot to me? Can I help you.

**Bert**:
Can you count on me? This is so weird. We're both obsessed with the Abracadabra. That stuff really means a lot to me. Can I help you.

**Markov**:
What do you think your actions have anything to do. Me: Do you want to look forward to the next day, but you're right. Do you think I can also smell the blood of menopausal pregnant women.

**Bert**:
Why do you think your husband has things to do? Me : Do you have to look forward to a big wedding just because you're pregnant? Do you? I can practically smell the perfume of menopausal pregnant women.

**Markov**:
No way! I apologize. What did it! I don't think anything is funny.

**Bert**:
No way could it be. I love you. I don't think this is right.

**Markov**:
I'm sure it's not going to work for FRU for a different reason? But I can tell you who you are?

**Bert**:
I'm sure he's not going to work for FRU without a good reason. Maybe I should tell him where we are?

**Markov**:
Do I know this guy, though, because you are not sure I do. But you stay away? The question is! He has to deal with it.

**Bert**:
" I love that girl, too, but you are not what I want. Can you stay here? The truth is, she wants to be with you.

**Markov**:
And I do now? Do I hurt you? My mother speaks French.

**Bert**:
Did I hurt you? Did I hurt you? Your blood is mine.

**Markov**:
What is the end result?

**Bert**:
What was the endgame?

**Markov**:
Do you want it to be easy.

**Bert**:
If you want to, come here.

**Markov**:
Feel the pain.

**Bert**:
Feel the pain.

**Markov**:
Do I want to die anyway.

**Bert**:
But I wanted to go home.

**Markov**:
Do you think? It is for friends and family, so you can trust me?

**Bert**:
Do you understand? This is about friends and family, and you can trust me?

**Markov**:
I haven't liked her in the car and stealing money from the cold wind.

**Bert**:
She hadn't left him in the hospital, left him with a broken heart.

**Markov**:
What would happen to me?

**Bert**:
What will happen to me?

**Markov**:
Relax, who would put up with that?

**Bert**:
Relax, who would put up with that?

**Markov**:
No, no, no more questions? The middle of the night before tonight. Why wouldn't he? I have permission for you to come? I didn't take it?

**Bert**:
No, no, no more questions. The tension from last night had eased. Why didn't you let me give permission for you to leave if you didn't want to?

**Markov**:
You don't think anything is funny. Do I want you with me?

**Bert**:
I don't think this is good. Do I want him inside me?

**Markov**:
If they want.

**Bert**:
What he wanted.

**Markov**:
" " He's fine. Or should I just need an hour? I'm not sure.

**Bert**:
" " It's okay. Or should I just make an appointment? I'm not sure.

**Markov**:
Then we have the insurance business. I must be somewhere else. I have shared a hotel room, but you're what's in the yearbook either.

**Bert**:
" I have a cell phone. It could be something else. I might have a cell phone, but they're what's in my purse, anyway.

**Markov**:
What does this place mean to me.

**Bert**:
What did that man do to me.

**Markov**:
It's that simple.

**Bert**:
It's that simple.

**Markov**:
Well, well, then please give me a couple of antibiotics. Don't get all that? Thank you so much. Was he joking? Should I check on them?

**Bert**:
Okay, okay, okay, give me a couple of antibiotics. Don't do all that. Thank you so much. Is he okay? Should I check on him?

**Markov**:
You don't sound so sure. Just a friend? Thunderbolt would make his move. Come over here.

**Bert**:
You don't sound so sure. Tell your mother that Justine will make you happy. Get over yourself.

**Markov**:
And what about the police will find your comment rather hilarious. Do you understand? What kind of slipping away and my life. What do I know he's not gettin'it. I've got'em all comin '.

**Bert**:
You talking about the woman you love now is just hilarious. Do you understand? The smile was slipping away from his face. How do you know she's not gettin'married? I've heard'em all talkin '.

**Markov**:
Santino and his new best friend, trying to get a grip.

**Bert**:
Santino watched his former best friend, trying to get a grip.

**Markov**:
Do you think?

**Bert**:
Do you understand?

**Markov**:
That's him.

**Bert**:
It's me.

**Markov**:
I don't know any names. Okay? Do I? I don't need anything but injections. I'm sure it's not going to help you?

**Bert**:
I don't need his help. Why? Should I? I don't need anything but distractions. I'm sure he's not going to help me?

**Markov**:
And when you're ready, I knew that a really good person? How do I have two tickets. I don't know your name is?

**Bert**:
You think you're here because you consider me a very good friend? Or because you have plane tickets that I don't have your number on?

**Markov**:
What do you think me being here will help you.

**Bert**:
Why do you think me being here will help you.

**Markov**:
No. So many people are going to be.

**Bert**:
No. Not where they were supposed to be.

**Markov**:
Because you already know. You know the answer. It means he loves me!

**Bert**:
But you already know. You know the answer. It means he loves you!

**Markov**:
I've had enough. What does this place. I had to get a tattoo? You have no reason to worry. Perhaps you did.

**Bert**:
I've lost everything. How is it possible that I want to get a divorce? I have no reason to care. But I do.

**Markov**:
You guys have fun with that. It's not an accident.

**Bert**:
You can have sex with me. That's not an option.

**Markov**:
Oh, right now.

**Bert**:
No one else did.

**Markov**:
I'm an international expert on the show, but it is. You're looking as good as ever, and believe me, I drove all the goons are in the living room when the sun's going down, though, because she'd been hit with an elbow to the bus stop. Anyway, it'll all be very interesting. For the entire city?

**Bert**:
I'm no real expert on the police, but I am. They're not as bad as you, and believe me, they said that the goons are in the emergency room and the alarm's going off, and they said they'd be waiting at the entrance to the police station. Well, it'll all be very interesting. In the big city?

**Markov**:
S - S - S - S - S - S - I'm going to work on the retroviral virus. He was interjecting a text message: < Hello >. Can you count on it. I really am. MacFarlane's girlfriends!

**Bert**:
T - S - S - S - S - S : I'm going to work on a retroviral vaccine. I am inventing a new vaccine. > > Me : If you work on this, you really do need MacFarlane's vitamins!

**Markov**:
In fact, a sprinkle appears on your part. Could it really be a dream? I paid you for the boys'basketball game. It's only a moment. You look a bit pale, Geraldine.

**Bert**:
In fact, a sprinkle appeared on her forehead. Could this really be a coincidence? I saw you at the girls'basketball game. It's not a coincidence. You look a little pale, Clementine.

**Markov**:
What is the difference between me and you are not sure I asked it myself.

**Bert**:
There is no future for us if we do this. I kiss him again.

**Markov**:
You're looking as good as ever, and you? I don't know what to do with my past? In what way? They have taught me to be something?

**Bert**:
You're not as bad as me, are you? I don't know what to do with my life. In what way? You really want me to do this?

**Markov**:
I wanted to be. ". I know you do it. Anyway, I got it all end?

**Bert**:
I have to go. No, I let you do it. No, you let it all out?

**Markov**:
I asked. I can.

**Bert**:
he asked and I nodded.

**Markov**:
But I do. You can hear my voice.

**Bert**:
" I know. I can hear your voice.

**Markov**:
Do you think it matters? I think it's all very well and here I am sorry to hear that you lied? Some people are going to be.

**Bert**:
Do you think it is? I know it's all very complicated but... I am glad to hear that you understand. Some things are meant to be.

**Markov**:
It's unbelievable! Well, the same company that I don't want to see you not to die anyway. What do you think?

**Bert**:
It's unreal. No, the voice said. I don't want to tell you how to do this. What do you want?

**Markov**:
they stop.

**Bert**:
he asked.

**Markov**:
I was little. You were right. If I could clarify things. And where did he do?

**Bert**:
She liked him. They were friends. Maybe he should clarify that. But what could he say?

**Markov**:
What is it? That's it. Do you even know me. What is your name is? To get me out of character.

**Bert**:
What is it? That's it. Do you even know me? What is your name again? I put you out of business.

**Markov**:
I'll drop it if I. Why? I have no place to go in there.

**Bert**:
I'll do it. No. Why? You have no right to go in there.

**Markov**:
You picked the right guy before I got out of Fort Knox? Didn't I? I can tell you who you are welcome here, and we'll have a request. Do you want the money.

**Bert**:
I said the same thing when I got out of Fort Bragg. Didn't I? I can tell you that they are still here, but I'll make a call. If you have any questions.

**Markov**:
Have you ever heard it? You guys have fun with that man do to you? So much for taking the damn thing off. I want you inside me?

**Bert**:
Have I ever done that? What does having sex with a man do to me? So much for taking the damn thing off when I feel him inside me?

**Markov**:
Does it bother you?

**Bert**:
Does it bother you?

**Markov**:
I don't really know. I don't understand. I didn't fill out a form, either.

**Bert**:
I don't even know. I don't know. I don't fill out a form, either.

**Markov**:
I ask, because you are not sure I know that yet.

**Bert**:
You are, but you are not. I know that now.

**Markov**:
I can help me? We have a meeting with Adonis, and maybe not today, but the attraction - - - - - What's this about? How's it going? Now my mother. Yes, it will end.

**Bert**:
You must trust me. I have no contact with Adonis, and certainly not you, or the others. - - - - What's this about? How's it ending? - My life. Yes, it will end.

**Markov**:
A stressful short report that I care?

**Bert**:
A delightful little girl, you know?

**Markov**:
What other refill you could look at it, then. He got them right here in Mountain View. expensive. Does any of it, and you'll think I'm dreaming. What was her name, do you think just being friends?

**Bert**:
The same people. I can look at them, too. I know them from up in Mountain View, California. See some of them, and they'll think I'm crazy. What is their name, if you know them that well?

**Markov**:
He and Rann look over at the roadside and the movies are bad and the driver drives it away.

**Bert**:
I see Razor pulling away from the roadside, the lights going out as the car drives farther away.

**Markov**:
I want to know? It's very important, you know the details of the darkness behind my eyes.

**Bert**:
I try to smile. It's not me who can see the rest of the world through his eyes.

**Markov**:
I'm sure it's not meant to be very positive. The government never finds out.

**Bert**:
I'm sure it's not going to be so bad. My plan finally works out.

**Markov**:
It's from Delia. Chapter Twenty - One Tristan What would happen to me. He wants to make sure I'm giving him full credit! It would be out of your body if it was in my spare time. Because I never will.

**Bert**:
He's an electrician. Chapter Twenty - One Logan Nothing will happen to me. He needs to make sure I'm giving him enough credit. I would walk out of his life if I acted in my own way. And I never will.

**Markov**:
Nothing more. Right. > Something in his voice reminds me of not my own head.

**Bert**:
No way. No. " Something in his tone surprised me and caused an awkward silence.

**Markov**:
What possible reason would he go? Well, that I'm here.

**Bert**:
What other way would I go? No matter that I'm here.

**Markov**:
I asked it myself. I don't know. " But if he rapes her?

**Bert**:
I said that before. I don't know. " What if he scares me?

**Markov**:
Call if you are. Please don't cry.

**Bert**:
Even if I am. Please don't go.

**Markov**:
S - S - S - S - S - S - S - S - S - I'm going to say that you are? I'll take you to attend last year's football game.

**Bert**:
S - S - S - S - S - S - S - S - S - I'm going to see how you are. I'll take you to the next week's football game.

\chapter{Appendix: Unraveling BERTifier}
\renewcommand{\leftmark}{APPENDIX}
\thispagestyle{empty}

# Example from Section: Quotidian

**Initial Markov Output:**
Let's make ready, you can find it quiet. Making coffee is often over 40 ° C.

**BERTifier Refinement Steps:**

[Let] ' s make ready , you can find it quiet . Making coffee is often over 40 ° C .

Let ['] s make ready , you can find it quiet . Making coffee is often over 40 ° C .

Let ' [s] make ready , you can find it quiet . Making coffee is often over 40 ° C .

Let ' s [get] ready , you can find it quiet . Making coffee is often over 40 ° C .

Let ' s get [started] , you can find it quiet . Making coffee is often over 40 ° C .

Let ' s get started [so] you can find it quiet . Making coffee is often over 40 ° C .

Let ' s get started so [we] can find it quiet . Making coffee is often over 40 ° C .

Let ' s get started so we [can] find it quiet . Making coffee is often over 40 ° C .

Let ' s get started so we can [keep] it quiet . Making coffee is often over 40 ° C .

Let ' s get started so we can keep [it] quiet . Making coffee is often over 40 ° C .

Let ' s get started so we can keep it [simple] . Making coffee is often over 40 ° C .

Let ' s get started so we can keep it simple [.] Making coffee is often over 40 ° C .

Let ' s get started so we can keep it simple . [The] coffee is often over 40 ° C .

Let ' s get started so we can keep it simple . The [temperature] is often over 40 ° C .

Let ' s get started so we can keep it simple . The temperature [is] often over 40 ° C .

Let ' s get started so we can keep it simple . The temperature is [just] over 40 ° C .

Let ' s get started so we can keep it simple . The temperature is just [over] 40 ° C .

Let ' s get started so we can keep it simple . The temperature is just over [90] ° C .

Let ' s get started so we can keep it simple . The temperature is just over 90 [degrees] C .

Let ' s get started so we can keep it simple . The temperature is just over 90 degrees [C] .

Let ' s get started so we can keep it simple . The temperature is just over 90 degrees C [.]

[Let] ' s get started so we can keep it simple . The temperature is just over 90 degrees C .

Let ['] s get started so we can keep it simple . The temperature is just over 90 degrees C .

Let ' [s] get started so we can keep it simple . The temperature is just over 90 degrees C .

Let ' s [get] started so we can keep it simple . The temperature is just over 90 degrees C .

Let ' s get [warm] so we can keep it simple . The temperature is just over 90 degrees C .

Let ' s get warm [so] we can keep it simple . The temperature is just over 90 degrees C .

Let ' s get warm so [we] can keep it simple . The temperature is just over 90 degrees C .

Let ' s get warm so we [can] keep it simple . The temperature is just over 90 degrees C .

Let ' s get warm so we can [keep] it simple . The temperature is just over 90 degrees C .

Let ' s get warm so we can keep [this] simple . The temperature is just over 90 degrees C .

Let ' s get warm so we can keep this [warm] . The temperature is just over 90 degrees C .

Let ' s get warm so we can keep this warm [.] The temperature is just over 90 degrees C .

Let ' s get warm so we can keep this warm . [The] temperature is just over 90 degrees C .

Let ' s get warm so we can keep this warm . The [temperature] is just over 90 degrees C .

Let ' s get warm so we can keep this warm . The temperature [is] just over 90 degrees C .

Let ' s get warm so we can keep this warm . The temperature is [just] over 90 degrees C .

Let ' s get warm so we can keep this warm . The temperature is just [over] 90 degrees C .

Let ' s get warm so we can keep this warm . The temperature is just over [30] degrees C .

Let ' s get warm so we can keep this warm . The temperature is just over 30 [degrees] C .

Let ' s get warm so we can keep this warm . The temperature is just over 30 degrees [C] .

Let ' s get warm so we can keep this warm . The temperature is just over 30 degrees C [.]

[Let] ' s get warm so we can keep this warm . The temperature is just over 30 degrees C .

Let ['] s get warm so we can keep this warm . The temperature is just over 30 degrees C .

Let ' [s] get warm so we can keep this warm . The temperature is just over 30 degrees C .

Let ' s [get] warm so we can keep this warm . The temperature is just over 30 degrees C .

Let ' s get [warm] so we can keep this warm . The temperature is just over 30 degrees C .

Let ' s get warm [so] we can keep this warm . The temperature is just over 30 degrees C .

Let ' s get warm so [we] can keep this warm . The temperature is just over 30 degrees C .

Let ' s get warm so we [can] keep this warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can [get] this warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can get [really] warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can get really [warm] . The temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm [.] The temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm . [The] temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm . The [temperature] is just over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature [is] just over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is [just] over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is just [over] 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is just over [30] degrees C .

Let ' s get warm so we can get really warm . The temperature is just over 30 [degrees] C .

Let ' s get warm so we can get really warm . The temperature is just over 30 degrees [C] .

Let ' s get warm so we can get really warm . The temperature is just over 30 degrees C [.]

[Let] ' s get warm so we can get really warm . The temperature is just over 30 degrees C .

Let ['] s get warm so we can get really warm . The temperature is just over 30 degrees C .

Let ' [s] get warm so we can get really warm . The temperature is just over 30 degrees C .

Let ' s [get] warm so we can get really warm . The temperature is just over 30 degrees C .

Let ' s get [warm] so we can get really warm . The temperature is just over 30 degrees C .

Let ' s get warm [so] we can get really warm . The temperature is just over 30 degrees C .

Let ' s get warm so [we] can get really warm . The temperature is just over 30 degrees C .

Let ' s get warm so we [can] get really warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can [get] really warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can get [really] warm . The temperature is just over 30 degrees C .

Let ' s get warm so we can get really [warm] . The temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm [.] The temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm . [The] temperature is just over 30 degrees C .

Let ' s get warm so we can get really warm . The [temperature] is just over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature [is] just over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is [just] over 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is just [over] 30 degrees C .

Let ' s get warm so we can get really warm . The temperature is just over [30] degrees C .

Let ' s get warm so we can get really warm . The temperature is just over 30 [degrees] C .

Let ' s get warm so we can get really warm . The temperature is just over 30 degrees [C] .

Let ' s get warm so we can get really warm . The temperature is just over 30 degrees C [.]

**Final Stabilized Output:**
Let's get warm so we can get really warm. The temperature is just over 30 degrees C.

# Example from Section: Epic

**Initial Markov Output:**
Would I? Put all that matters now. Yes.. He told you that.

**BERTifier Refinement Steps:**

[May] I ? Put all that matters now . Yes . . He told you that .

May [I] ? Put all that matters now . Yes . . He told you that .

May I [?] Put all that matters now . Yes . . He told you that .

May I ? [For] all that matters now . Yes . . He told you that .

May I ? For [all] that matters now . Yes . . He told you that .

May I ? For all [that] matters now . Yes . . He told you that .

May I ? For all that [,] now . Yes . . He told you that .

May I ? For all that , [yes] . Yes . . He told you that .

May I ? For all that , yes [.] Yes . . He told you that .

May I ? For all that , yes . [.] . . He told you that .

May I ? For all that , yes . . [.] . He told you that .

May I ? For all that , yes . . . [.] He told you that .

May I ? For all that , yes . . . . [I] told you that .

May I ? For all that , yes . . . . I [promise] you that .

May I ? For all that , yes . . . . I promise [you] that .

May I ? For all that , yes . . . . I promise you [that] .

May I ? For all that , yes . . . . I promise you that [.]

[May] I ? For all that , yes . . . . I promise you that .

May [I] ? For all that , yes . . . . I promise you that .

May I [?] For all that , yes . . . . I promise you that .

May I ? [After] all that , yes . . . . I promise you that .

May I ? After [all] that , yes . . . . I promise you that .

May I ? After all [that] , yes . . . . I promise you that .

May I ? After all that [,] yes . . . . I promise you that .

May I ? After all that , [I] . . . . I promise you that .

May I ? After all that , I [will] . . . I promise you that .

May I ? After all that , I will [.] . . I promise you that .

May I ? After all that , I will . [Yes] . I promise you that .

May I ? After all that , I will . Yes [,] I promise you that .

May I ? After all that , I will . Yes , [I] promise you that .

May I ? After all that , I will . Yes , I [promise] you that .

May I ? After all that , I will . Yes , I promise [you] that .

May I ? After all that , I will . Yes , I promise you [that] .

May I ? After all that , I will . Yes , I promise you that [.]

[Do] I ? After all that , I will . Yes , I promise you that .

Do [I] ? After all that , I will . Yes , I promise you that .

Do I [?] After all that , I will . Yes , I promise you that .

Do I ? [After] all that , I will . Yes , I promise you that .

Do I ? After [hearing] that , I will . Yes , I promise you that .

Do I ? After hearing [that] , I will . Yes , I promise you that .

Do I ? After hearing that [,] I will . Yes , I promise you that .

Do I ? After hearing that , [I] will . Yes , I promise you that .

Do I ? After hearing that , I [do] . Yes , I promise you that .

Do I ? After hearing that , I do [.] Yes , I promise you that .

Do I ? After hearing that , I do . [Yes] , I promise you that .

Do I ? After hearing that , I do . Yes [,] I promise you that .

Do I ? After hearing that , I do . Yes , [I] promise you that .

Do I ? After hearing that , I do . Yes , I [told] you that .

Do I ? After hearing that , I do . Yes , I told [you] that .

Do I ? After hearing that , I do . Yes , I told you [that] .

Do I ? After hearing that , I do . Yes , I told you that [.]

[Do] I ? After hearing that , I do . Yes , I told you that .

Do [I] ? After hearing that , I do . Yes , I told you that .

Do I [?] After hearing that , I do . Yes , I told you that .

Do I ? [But] hearing that , I do . Yes , I told you that .

Do I ? But [know] that , I do . Yes , I told you that .

Do I ? But know [me] , I do . Yes , I told you that .

Do I ? But know me [as] I do . Yes , I told you that .

Do I ? But know me as [you] do . Yes , I told you that .

Do I ? But know me as you [do] . Yes , I told you that .

Do I ? But know me as you do [.] Yes , I told you that .

Do I ? But know me as you do . [Yes] , I told you that .

Do I ? But know me as you do . Yes [,] I told you that .

Do I ? But know me as you do . Yes , [I] told you that .

Do I ? But know me as you do . Yes , I [told] you that .

Do I ? But know me as you do . Yes , I told [you] that .

Do I ? But know me as you do . Yes , I told you [so] .

Do I ? But know me as you do . Yes , I told you so [.]

[Do] I ? But know me as you do . Yes , I told you so .

Do [you] ? But know me as you do . Yes , I told you so .

Do you [?] But know me as you do . Yes , I told you so .

Do you ? [You] know me as you do . Yes , I told you so .

Do you ? You [know] me as you do . Yes , I told you so .

Do you ? You know [me] as you do . Yes , I told you so .

Do you ? You know me [,] you do . Yes , I told you so .

Do you ? You know me , [I] do . Yes , I told you so .

Do you ? You know me , I [said] . Yes , I told you so .

Do you ? You know me , I said [.] Yes , I told you so .

Do you ? You know me , I said . [Yes] , I told you so .

Do you ? You know me , I said . Yes [,] I told you so .

Do you ? You know me , I said . Yes , [I] told you so .

Do you ? You know me , I said . Yes , I [know] you so .

Do you ? You know me , I said . Yes , I know [you] so .

Do you ? You know me , I said . Yes , I know you [do] .

Do you ? You know me , I said . Yes , I know you do [.]

[Do] you ? You know me , I said . Yes , I know you do .

Do [you] ? You know me , I said . Yes , I know you do .

Do you [?] You know me , I said . Yes , I know you do .

Do you ? [You] know me , I said . Yes , I know you do .

Do you ? You [know] me , I said . Yes , I know you do .

Do you ? You know [that] , I said . Yes , I know you do .

Do you ? You know that [,] I said . Yes , I know you do .

Do you ? You know that , [he] said . Yes , I know you do .

Do you ? You know that , he [said] . Yes , I know you do .

Do you ? You know that , he said [.] Yes , I know you do .

Do you ? You know that , he said . [Yes] , I know you do .

Do you ? You know that , he said . Yes [,] I know you do .

Do you ? You know that , he said . Yes , [I] know you do .

Do you ? You know that , he said . Yes , I [know] you do .

Do you ? You know that , he said . Yes , I know [I] do .

Do you ? You know that , he said . Yes , I know I [do] .

Do you ? You know that , he said . Yes , I know I do [.]

[Do] you ? You know that , he said . Yes , I know I do .

Do [you] ? You know that , he said . Yes , I know I do .

Do you [?] You know that , he said . Yes , I know I do .

Do you ? [I] know that , he said . Yes , I know I do .

Do you ? I [know] that , he said . Yes , I know I do .

Do you ? I know [you] , he said . Yes , I know I do .

Do you ? I know you [,] he said . Yes , I know I do .

Do you ? I know you , [he] said . Yes , I know I do .

Do you ? I know you , he [said] . Yes , I know I do .

Do you ? I know you , he said [.] Yes , I know I do .

Do you ? I know you , he said . [Yes] , I know I do .

Do you ? I know you , he said . Yes [,] I know I do .

Do you ? I know you , he said . Yes , [I] know I do .

Do you ? I know you , he said . Yes , I [think] I do .

Do you ? I know you , he said . Yes , I think [you] do .

Do you ? I know you , he said . Yes , I think you [do] .

Do you ? I know you , he said . Yes , I think you do [.]

[Do] you ? I know you , he said . Yes , I think you do .

Do [you] ? I know you , he said . Yes , I think you do .

Do you [think] I know you , he said . Yes , I think you do .

Do you think [I] know you , he said . Yes , I think you do .

Do you think I [love] you , he said . Yes , I think you do .

Do you think I love [you] , he said . Yes , I think you do .

Do you think I love you [,] he said . Yes , I think you do .

Do you think I love you , [he] said . Yes , I think you do .

Do you think I love you , he [said] . Yes , I think you do .

Do you think I love you , he said [.] Yes , I think you do .

Do you think I love you , he said . [Yes] , I think you do .

Do you think I love you , he said . Yes [,] I think you do .

Do you think I love you , he said . Yes , [I] think you do .

Do you think I love you , he said . Yes , I [know] you do .

Do you think I love you , he said . Yes , I know [you] do .

Do you think I love you , he said . Yes , I know you [do] .

Do you think I love you , he said . Yes , I know you do [.]

[Do] you think I love you , he said . Yes , I know you do .

Do [you] think I love you , he said . Yes , I know you do .

Do you [know] I love you , he said . Yes , I know you do .

Do you know [I] love you , he said . Yes , I know you do .

Do you know I [love] you , he said . Yes , I know you do .

Do you know I love [you] , he said . Yes , I know you do .

Do you know I love you [,] he said . Yes , I know you do .

Do you know I love you , [he] said . Yes , I know you do .

Do you know I love you , he [said] . Yes , I know you do .

Do you know I love you , he said [.] Yes , I know you do .

Do you know I love you , he said . [Yes] , I know you do .

Do you know I love you , he said . Yes [,] I know you do .

Do you know I love you , he said . Yes , [I] know you do .

Do you know I love you , he said . Yes , I [know] you do .

Do you know I love you , he said . Yes , I know [you] do .

Do you know I love you , he said . Yes , I know you [do] .

Do you know I love you , he said . Yes , I know you do [.]

[And] you know I love you , he said . Yes , I know you do .

And [you] know I love you , he said . Yes , I know you do .

And you [know] I love you , he said . Yes , I know you do .

And you know [I] love you , he said . Yes , I know you do .

And you know I [love] you , he said . Yes , I know you do .

And you know I love [you] , he said . Yes , I know you do .

And you know I love you [,] he said . Yes , I know you do .

And you know I love you , [he] said . Yes , I know you do .

And you know I love you , he [said] . Yes , I know you do .

And you know I love you , he said [.] Yes , I know you do .

And you know I love you , he said . [Yes] , I know you do .

And you know I love you , he said . Yes [,] I know you do .

And you know I love you , he said . Yes , [I] know you do .

And you know I love you , he said . Yes , I [know] you do .

And you know I love you , he said . Yes , I know [you] do .

And you know I love you , he said . Yes , I know you [do] .

And you know I love you , he said . Yes , I know you do [.]

[And] you know I love you , he said . Yes , I know you do .

And [you] know I love you , he said . Yes , I know you do .

And you [know] I love you , he said . Yes , I know you do .

And you know [I] love you , he said . Yes , I know you do .

And you know I [love] you , he said . Yes , I know you do .

And you know I love [you] , he said . Yes , I know you do .

And you know I love you [,] he said . Yes , I know you do .

And you know I love you , [he] said . Yes , I know you do .

And you know I love you , he [said] . Yes , I know you do .

And you know I love you , he said [.] Yes , I know you do .

And you know I love you , he said . [Yes] , I know you do .

And you know I love you , he said . Yes [,] I know you do .

And you know I love you , he said . Yes , [I] know you do .

And you know I love you , he said . Yes , I [know] you do .

And you know I love you , he said . Yes , I know [you] do .

And you know I love you , he said . Yes , I know you [do] .

And you know I love you , he said . Yes , I know you do [.]

**Final Stabilized Output:**
And you know I love you, he said. Yes, I know you do.

# Example from Section: Therapeutic

**Initial Markov Output:**
Could here really be some connection? Can you elaborate on that? Would you want to be quite positive. Perhaps in your fantasies we are each other. What about machines worrys you?

**BERTifier Refinement Steps:**

[Could] here really be some connection ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could [there] really be some connection ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there [possibly] be some connection ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly [be] some connection ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be [a] connection ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a [connection] ? Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection [?] Can you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? [Could] you elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could [you] elaborate on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you [elaborate] on that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate [on] that ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on [it] ? Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it [?] Would you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? [Perhaps] you want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps [you] want to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you [want] to be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want [to] be quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to [be] quite positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be [more] positive . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more [specific] . Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific [.] Perhaps in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . [Perhaps] in your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps [in] your fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in [our] fantasies we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our [minds] we are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds [we] are each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we [know] each other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know [each] other . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each [other] . What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other [.] What about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . [What] about machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What [about] machines worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about [what] worry ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what [bother] ##s you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother [##s] you ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s [you] ?

Could there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you [?]

[Could] there possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could [there] possibly be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there [really] be a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really [be] a connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be [a] connection ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a [connection] ? Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection [?] Could you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? [Can] you elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can [you] elaborate on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you [concentrate] on it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate [on] it ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on [that] ? Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that [?] Perhaps you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? [Perhaps] you want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps [you] want to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you [need] to be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need [to] be more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to [be] more specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be [more] specific . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more [specific] . Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific [.] Perhaps in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . [But] in our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But [in] our minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in [our] minds we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our [way] we know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way [we] know each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we [understand] each other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand [each] other . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each [other] . What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other [.] What about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . [What] about what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What [is] what bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is [that] bother ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that [bother] ##s you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother [##s] you ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s [you] ?

Could there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you [?]

[Could] there really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could [there] really be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there [really] be a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really [be] a connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be [a] connection ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a [difference] ? Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference [?] Can you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? [Can] you concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can [you] concentrate on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you [concentrate] on that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate [on] that ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on [that] ? Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that [?] Perhaps you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? [Maybe] you need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe [you] need to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you [need] to be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need [to] be more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to [be] more specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be [more] specific . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more [focused] . But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused [.] But in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . [Maybe] in our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe [in] our way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in [some] way we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some [ways] we understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways [you] understand each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you [understand] each other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand [each] other . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each [other] . What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other [.] What is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . [Why] is that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why [,] that bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , [it] bother ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it [bother] ##s you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother [##s] you ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s [me] ?

Could there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me [.]

[Could] there really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could [there] really be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there [really] be a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really [be] a difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be [a] difference ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a [difference] ? Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference [?] Can you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? [Can] you concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can [you] concentrate on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you [focus] on that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus [on] that ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on [something] ? Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something [?] Maybe you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? [Maybe] you need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe [you] need to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you [need] to be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need [to] be more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to [be] more focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be [more] focused . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more [focused] . Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused [.] Maybe in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . [Maybe] in some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe [in] some ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in [some] ways you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some [ways] you understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways [we] understand each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we [understand] each other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand [each] other . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each [other] . Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other [.] Why , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . [Still] , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still [,] it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , [it] bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it [bother] ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother [##s] me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s [me] .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me [.]

[Could] there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could [there] really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there [really] be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really [be] a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be [a] difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a [difference] ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference [?] Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? [Can] you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can [you] focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you [focus] on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus [on] something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on [something] ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something [?] Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? [Maybe] you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe [you] need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you [need] to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need [to] be more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to [be] more focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be [more] focused . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more [focused] . Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused [.] Maybe in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . [Maybe] in some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe [in] some ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in [some] ways we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some [ways] we understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways [we] understand each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we [understand] each other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand [each] other . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each [other] . Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other [.] Still , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . [Still] , it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still [,] it bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , [it] bother ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it [bother] ##s me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother [##s] me .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s [me] .

Could there really be a difference ? Can you focus on something ? Maybe you need to be more focused . Maybe in some ways we understand each other . Still , it bother ##s me [.]

**Final Stabilized Output:**
Could there really be a difference? Can you focus on something? Maybe you need to be more focused. Maybe in some ways we understand each other. Still, it bothers me.

# Example from Section: Recursive

**Initial Markov Output:**
Do you think it matters? Don't even think about looking in the living room, so why wouldn't they? No, no. I don't know. It's not so sure.

**BERTifier Refinement Steps:**

[Do] you think it matters ? Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do [they] think it matters ? Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they [think] it matters ? Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think [it] matters ? Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it [is] ? Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is [?] Don ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? [Don] ' t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ['] t even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' [t] even think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t [even] think about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even [think] about looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think [about] looking in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about [it] in the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it [in] the living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in [the] living room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the [other] room , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other [room] , so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room [,] so why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , [and] why wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and [why] wouldn ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why [don] ' t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ['] t they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' [t] they ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t [they] ? No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they [?] No , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? [Oh] , no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh [,] no . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , [God] . I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God [,] I don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , [I] don ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I [don] ' t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ['] t know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' [t] know . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t [know] . It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know [.] It ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . [He] ' s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ['] s not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' [s] not so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s [not] so sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not [so] sure .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so [sure] .

Do they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure [.]

[Do] they think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do [they] think it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they [think] it is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think [it] is ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it [is] ? Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is [?] Don ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? [Don] ' t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ['] t even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' [t] even think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t [they] think about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they [talk] about it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk [about] it in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about [it] in the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it [in] the other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in [the] other room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the [same] room , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same [way] , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way [,] and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , [and] why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and [why] don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why [don] ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ['] t they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' [t] they ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t [they] ? Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they [?] Oh , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? [Oh] , God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh [,] God , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , [God] , I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God [,] I don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , [I] don ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I [don] ' t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ['] t know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' [t] know . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t [know] . He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know [.] He ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . [He] ' s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ['] s not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' [s] not so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s [not] so sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not [so] sure .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so [sure] .

Do they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure [.]

[Do] they think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do [you] think it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you [think] it is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think [it] is ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it [is] ? Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is [?] Don ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? [Don] ' t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ['] t they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' [t] they talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t [people] talk about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people [think] about it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think [about] it in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about [him] in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him [in] the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in [the] same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the [same] way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same [way] , and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way [,] and why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , [and] why don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and [why] don ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why [don] ' t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ['] t they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' [t] they ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t [they] ? Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they [?] Oh , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? [Oh] , God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh [,] God , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , [God] , I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God [,] I don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , [I] don ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I [don] ' t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ['] t know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' [t] know . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t [know] . He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know [.] He ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . [He] ' s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ['] s not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' [s] not so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s [not] so sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not [so] sure .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so [bad] .

Do you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad [.]

[Do] you think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do [you] think it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you [think] it is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think [he] is ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he [is] ? Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is [?] Don ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? [Don] ' t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ['] t people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' [t] people think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t [people] think about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people [think] about him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think [of] him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of [him] in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him [in] the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in [the] same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the [same] way , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same [way] , and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way [,] and why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , [and] why don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and [why] don ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why [don] ' t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ['] t they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' [t] they ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t [they] ? Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they [?] Oh , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? [Oh] , God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh [,] God , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , [God] , I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God [,] I don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , [I] don ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I [don] ' t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ['] t know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' [t] know . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t [know] . He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know [.] He ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . [He] ' s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ['] s not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' [s] not so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s [not] so bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not [that] bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that [bad] .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad [.]

[Do] you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do [you] think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you [think] he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think [he] is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he [is] ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is [?] Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? [Don] ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ['] t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' [t] people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t [people] think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people [think] of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think [of] him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of [him] in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him [in] the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in [the] same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the [same] way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same [way] , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way [,] and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , [and] why don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and [why] don ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why [don] ' t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ['] t they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' [t] they ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t [they] ? Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they [?] Oh , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? [Oh] , God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh [,] God , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , [God] , I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God [,] I don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , [I] don ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I [don] ' t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ['] t know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' [t] know . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t [know] . He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know [.] He ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . [He] ' s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ['] s not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' [s] not that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s [not] that bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not [that] bad .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that [bad] .

Do you think he is ? Don ' t people think of him in the same way , and why don ' t they ? Oh , God , I don ' t know . He ' s not that bad [.]

**Final Stabilized Output:**
Do you think he is? Don't people think of him in the same way, and why don't they? Oh, God, I don't know. He's not that bad.

