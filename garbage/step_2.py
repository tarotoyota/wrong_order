# This page is /home/tarotoyota/Step_2_class_inst_py.py

from dataclasses import dataclass
from typing import List, ClassVar


list_human_robber_A     =["I asked about recommended tourist spots.", "I still keep in touch with him on SNS.","I told him to come to Japan.","I went to see him again with my family."]
# Ali talks about a normal people. Bob mistakenly assumes that Ali is talking about a robber in a tourist spot. Add new 5 funny sentence if Ali would say it in this situation. Don't clear up that misunderstanding. Please do not add jokes that use quotation marks to make double meanings, as they are lame. You should not add jokes.
list_human_robber_B     =[]
# Ali talks about a normal people. Bob mistakenly assumes that Ali is talking about a robber in a tourist spot. Add new 5 funny sentence if Bob would say it in this situation. Don't clear up that misunderstanding. Please do not add jokes that use quotation marks to make double meanings, as they are lame. You should not add jokes.

list_human_animal_A     =["I got angry at him because he ignored me when I spoke to him.", "He could barely understand English."]



list_animal_A           =["I gave him the crumbs I had.","He licked my face.", "He was in heat.","He loves pet food.","He dislikes leashes.","She's our pet.","She sleeps on the floor next to my bed.","I've been trying to get him to use the toilet but it's difficult.","I was amazed at the size of his poop and took a picture.","He poops everywhere.", "The master was controlling him with a whip.", "He was 4 years old.","They became docile when I petted them.","I like to pet them.","He gets so excited when I say the word 'treat'."]
# Ali talks about an animal. Bob mistakenly assumes that Ali is talking about Ali's father. Add new 5 funny sentence if Ali would say it in this situation.
list_animal_B           =["Let me pet him next time.","I'll give him some pet food next time.","Does he need a leash when you take him out?","Has he learned to use the toilet yet?"]
# Ali talks about Ali's father. Bob mistakenly assumes that Ali is talking about an animal. Add new 5 funny sentence if Bob would say it in this situation.



list_woman_animal_A     =["My father is against our marriage.","We've tried many times but have not been able to have children.","I once had a fight with her and went back to my parents' house."]
# Ali talks about Ali's girlfriend, not an animal. Bob mistakenly assumes that Ali is talking about an animal, not Ali's girlfriend. Bob mistakenly believes Ali is perverted or crazy. Add new 5 funny sentence if Ali would say it in this situation.

list_inanimate_A        =[]
list_inanimate_B        =[]
list_human_inanimate_A  =["It seemed unwell so I took it to the hospital."]
list_woman_inanimate_A  =["I picked it up at the bar.", "My father is against our marriage.","We've tried many times but have not been able to have children."]
list_man_inanimate_A    =[]

list_paid_item_A        =["It had high online reviews.","They offer coupons.","I bargained.","I bought it cheaply.","They gave me detergent as an extra.","I bought a week's supply.","I also gave this to my family.","If you buy two you get one free.","I'm thinking of buying more."]
# Ali talks about the peid item. Bob mistakenly assumes that Ali is talking about an woman. Add new 5 funny sentence if Ali would say it in this situation.

list_paid_item_A       +=["This costs about 400 yen.", "I bought it for 400 yen.", "I looked at the price tag and it said 400 yen.", "If you buy this, you also get some peanuts as a bonus.","It was confiscated by customs."]# Think of new five sentences that would be funny if Bob misunderstood Ali to be talking about a roller coaster rather than a cheap marchandise (e.g. radio, plushie, tobacco).

list_paid_item_B        =["How much did it cost?", "Where did you bought it?"]

list_woman_paid_item_A  =["I found it at a bar, liked it so much I took it home.", "I picked up it on the street."]
# Ali talks about Ali's girlfriend. Bob mistakenly assumes that Ali is talking about a paid item(e.g. car, phone). Add 5 funny sentence if Ali would say it in this situation.

list_food_A             =["This has a nice texture when you put it in your mouth.","It tastes like cheese.", "I got fat because of this.", "It was delicious.","We all competed for this.","I took it three times a day.","I ate this raw.", "I ate this one alive.", "This goes well with wine."]
# Ali talks about the food. Bob mistakenly assumes that Ali is talking about a non-edible animal(e.g. cat, elephant) . Add 5 funny sentence if Ali would say it in this situation.

list_food_B             =["This has a nice texture when you put it in your mouth.","I've eaten this before."]

list_vehicle_A          =["I like riding it.", "This is a comfortable ride."]
# Ali talks about the vehicle, not his wife. Bob mistakenly assumes that Ali is talking about his wife, not the vehicle. Bob mistakenly believes Ali is perverted or crazy. Add new 5 funny sentence if Ali would say it in this situation.

list_vehicle_B          =["I like riding it.", "This is a comfortable ride."]

list_building_A         =["The total construction cost is said to be 1 billion yen."]
list_building_B         =[]

list_building_woman_A   =["I often go inside that.","I took photos inside that.","It can accommodate 50 people at a time.","Its inside is too hot.","I left my phone inside that.","There is an entrance fee to get inside it.", "Many people can fit inside it at once.","The inside of this is quite small."]
# Ali talks about the building(e.g. library, museum), not his wife. Bob mistakenly assumes that Ali is talking about his wife, not the building. Bob mistakenly believes Ali is perverted or crazy. Add new 5 funny sentence if Ali would say it in this situation.

list_building_woman_B   =["Do you have any pictures of the inside of this?","Is there an entrance fee to get inside it?","How many people can fit inside it at once?"]
# Ali talks about his wife, not the building(e.g. library, museum). Bob mistakenly assumes that Ali is talking about not the building, not his wife. Ali mistakenly believes Bob is perverted or crazy. Add new 5 funny sentence if Bob would say it in this situation.

list_job_A              =["I used to do things like them too.", "I used to aspire to a life like theirs.","I want my son to be like them."]
# Ali talks about the good person, not a robber. Bob mistakenly believes that Ali is talking about a robber, not the good person. Add new 5 funny lines if Ali would say it in this situation.
list_job_B              =[""]
# Ali talks about the robber, not a good person. Bob mistakenly believes that Ali is talking about a good person, not the robber. Add new 5 funny lines if Bob would say it in this situation.

list_merchant_A         =["I've recommended that my friends go there when they travel abroad.","I referred a friend and got cash back.","I like that kind of thing.","I had to wait in line for my turn.","I even paid a tip.","I was hooked and went back with my family for a second time.","They gave us a discount.","They offer coupons.","Credit cards were accepted.","He gave me the correct change.","I was given a numbered ticket.","Failed to haggle.","I would like to go again next time.","I went there twice."," It seemed like they were at it for 10 hours a day."]
# Ali talks about the normal clerk, not a robber. Bob mistakenly believes that Ali is talking about a robber that Ali encountered while traveling, not the normal clerk. Add new 5 funny lines if Ali would say it in this situation.





list_merchant_B         =[]

list_carry_around_A     =["I use this in my bedroom and bathroom.", "I left it at a friend's house."]

list_carry_around_B     =[]


list_rent_A             =["Wanna borrow this?", "I borrow this often.", "I lent it to my brother.","I usually let my friends use it when they come over.", "I always make sure it's clean and ready before lending it out."]
# Ali talks about the item that can be borrowed or lent (e.g. video games, massagers). Bob mistakenly assumes that Ali is talking about Ali's wife. Add 5 funny sentence if Ali would say it in this situation.
list_rent_B             =["Please lend it to me.","I promise to take good care of it while I have it.","I'll make sure to return this on time.", "Can I get a discount if I rent it long-term?"]
# Ali talks about Ali's wife. Bob mistakenly assumes that Ali is talking about the item that can be borrowed or lent (e.g. video games, massagers). Add 5 funny sentence if Bob would say it in this situation.

list_second_hand_A      =["This is second hand.","It's second-hand. I wanna exchange it for a new one.","I got it from a previous owner who took good care of it.",  "I picked it up from a guy who was getting rid of it."]
# Ali talks about the second-hand goods. Bob mistakenly assumes that Ali is talking about Ali's wife. Add 5 funny sentence if Ali would say it in this situation.
list_second_hand_B      =["Is this second hand?","It's second-hand. Why not exchange it for a new one?","It's looks pretty good for being second-hand.",  "How many previous owners did it have?"]
# Ali talks about Ali's wife. Bob mistakenly assumes that Ali is talking about the second-hand goods. Add 5 funny sentence if Bob would say it in this situation.

list_present_A          =["I received this as a gift from my mother.","I asked my parents for this as a gift, but they wouldn't buy it for me."]
# Ali talks about something that was given as a gift. Bob mistakenly assumes that Ali is talking about Ali's wife. Add 5 funny sentence if Ali would say it in this situation.
list_present_B          =["Did your mother give it to you as a gift?","I asked my parents for this as a gift, but they wouldn't buy it for me."]
# Ali talks about Ali's wife. Bob mistakenly assumes that Ali is talking about something that was given as a gift. Add 5 funny sentence if Bob would say it in this situation.


list_container_A        =[]
list_container_B        =[]
list_insert_A           =[]
list_insert_B           =[]
list_child_use_A        =["I've been using this since I was ten years old."]
list_child_use_B        =[]
list_seats_A            =["There was a noisy child, so I scolded him and made him quiet.","Someone brought their pet and it was making noise the entire time.","I complained because others were too noisy.","I scolded my daughter for spilling her coffee.","I moved seats because there was a smelly guy there.", "There was also baby seats.", "The guy next to me fell asleep and started noisy snoring."]# Think of new five sentences that would be funny if Bob misunderstood Ali to be talking about some place with seats (e.g. opera house, train) rather than a roller coaster.
list_seats_B            =[]
list_hours_A            =["I spent a few hours there.", "I took a nap there.","I didn't move for five hours straight.", "I enjoyed a cup of coffee and a good read there.", "I chatted with a friend for hours there."] # Think of new five sentences that would be funny if Bob misunderstood Ali to be talking about some place  to spend a long time (e.g. cafe, scenic spots) rather than a roller coaster.
list_hours_B            =[]
list_cheap_A            =["This costs about 400 yen.", "I bought it for 400 yen.", "I looked at the price tag and it said 400 yen.", "If you buy this, you also get some peanuts as a bonus.","It was confiscated by customs."]# Think of new five sentences that would be funny if Bob misunderstood Ali to be talking about a roller coaster rather than a cheap marchandise (e.g. radio, plushie, tobacco).
list_cheap_B            =[]

list_robber_fight =["I bruised my collarbone.", "I grabbed the money back from him and ran.", "I told everyone else not to give him anything either.", "My friend and I defeated it together.","I was able to beat him because I knew karate.", "I was scared so I kicked and ran away.", "They asked me for a lot of money, so I punched them and ran away."]# A man tells a story about fighting a robber at a tourist spot. Add new 20 short statements without any explanations. Don't use any proper nouns. Don't make poems, just add normal statements. Don't use quotes.
list_robber_lose  =["I lost 100,000 yen.","I was shocked when he demanded all my cash.","Covered by travel insurance.","He robbed me of my smartphone.","I handed over the money crying.", "I was scared so I called the police.","I was scared so I broke the window and ran away.","The language barrier made communication difficult.","This experience would make me a savvier traveler.","I reported it to the police but they didn't take action.","I screamed for help, but the people around me just watched.","Humiliation burned alongside the anger at my own carelessness.","Every stranger seemed suspicious."]# A man talks about being robbed at a tourist spot. Add new 20 short statements without any explanations. Don't use any proper nouns. Don't make poems, just add normal statements. Don't use quotes.
list_robber_info  =["He uses a gun, a hammer and a knife.", "Some even target tour buses at stoplights.", "A decoy wallet might be a good idea.","Local vendors warned us to be extra cautious.", "He makes a living by robbing tourists of smartphones and watches.","The insecurity there is shocking.","Apparently they cause deaths on a regular basis.","The police are not keen to crack down on them.","Should've gotten travel insurance","It was just as I had heard, a dangerous place."]# A man expalains about robbers in tourist spot. Add new 20 short statements without any explanations. Don't use any proper nouns. Don't make one story or poems, just add normal statements.Don't use quotes.

list_toilet_A=["I pooped there.","I was annoyed that there was no toilet paper.","I had diarrhea and was relieved to find this place."]





@dataclass
class Step_2:
    all_Step_2: ClassVar[List['Step_2']] = []
    Step_2_class_name:str
    #1
    human:str
    animal:str
    inanimate:str
    #2
    paid_item:str
    food:str
    vehicle:str
    #3
    building:str
    job:str
    merchant:str
    #4
    carry_around:str
    rent        :str
    second_hand :str
    #5
    present:str
    container:str
    insert:str
    #6
    child_use:str
    #woman
    X_woman_A:list
    X_woman_B:list
    woman_X_A:list
    woman_X_B:list
    #animal
    X_animal_A:list
    X_animal_B:list
    animal_X_A:list
    animal_X_B:list
    #man
    X_man_A:list
    X_man_B:list
    man_X_A:list
    man_X_B:list




    def __post_init__(self):
        Step_2.all_Step_2.append(self)
        #1

        if self.human:
            self.X_animal_A+=[list_human_animal_A] # "I got angry at him because he ignored me when I spoke to him."
            self.animal_X_A+=[list_animal_A] # "He poops everywhere."
            self.animal_X_B+=[list_animal_B]


        if self.animal:
            self.X_woman_A+=[list_animal_A] # "He poops everywhere."
            self.woman_X_B+=[list_animal_B] # "Let me pet this next time."
            self.woman_X_A=([list_woman_animal_A])

        if self.paid_item and not self.building:
            self.X_woman_A.extend([list_paid_item_A]) # "I bought it cheaply."
            self.woman_X_B.extend([list_paid_item_B]) # "How much did it cost?"
            self.woman_X_A.extend([list_woman_paid_item_A])

        #2
        if self.inanimate and not self.building:
            self.woman_X_A+=[list_woman_inanimate_A] # "I picked it up at the bar."
            self.woman_X_A+=[list_human_inanimate_A]
            self.man_X_A  +=[list_human_inanimate_A]
        if self.food:
            self.X_woman_A +=[list_food_A] # "It was delicious."
            self.woman_X_B +=[list_food_B] # "I've eaten this before."
            self.X_animal_A+=[list_food_A] # "It was delicious."
            self.animal_X_B+=[list_food_B] # "I've eaten this before."
        if self.vehicle:
            self.X_woman_A.extend([list_vehicle_A]) # "I like riding it."
            self.woman_X_B.extend([list_vehicle_B]) # "I like riding it."
        #3
        if self.building:
            self.X_woman_A.extend([list_building_woman_A])
            self.woman_X_B.extend([list_building_woman_B])
        if self.job:
            pass
        if self.merchant:
            self.X_woman_A.extend([list_merchant_A]) # "They offer coupons"
            self.woman_X_B.extend([list_merchant_B]) #
        #4
        if self.carry_around:
            self.X_woman_A.extend([list_carry_around_A]) # "I left it at a friend's house."
            self.woman_X_B.extend([list_carry_around_B]) #
        if self.rent:
            self.X_woman_A.extend([list_rent_A]) # "Wanna borrow?"
            self.woman_X_B.extend([list_rent_B]) # "Please lend it to me."
        if self.second_hand:
            self.X_woman_A.extend([list_second_hand_A]) # "This is second hand."
            self.woman_X_B.extend([list_second_hand_B]) # "Is this second hand?"
        #5
        if self.present:
            self.X_woman_A.extend([list_present_A]) # "I received this as a gift from my mother."
            self.woman_X_B.extend([list_present_B]) # "Did your mother give it to you as a gift?"
        if self.container:
            self.X_woman_A.extend([list_container_A])
            self.woman_X_B.extend([list_container_B])
        if self.insert:
            self.X_woman_A.extend([list_insert_A])
            self.woman_X_B.extend([list_insert_B])
        #6
        if self.child_use:
            self.X_woman_A.extend([list_child_use_A]) # "I've been using this since I was ten years old."
            self.woman_X_B.extend([list_child_use_B])




#                                                                hum,ani,ina   pai,foo,veh,  bui,job,mer,  car,ren,sec,  pre,con,ins,  chi
_empty                      =Step_2(""                          ,"" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_dog                        =Step_2("dog"                       ,"" ,"y","" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_butterfly                  =Step_2("butterfly"                 ,"" ,"y","" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_baseball_glove             =Step_2("baseball glove"            ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","y",  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_shoes                      =Step_2("shoes"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","y",  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_laptop                     =Step_2("laptop"                    ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_fridge                     =Step_2("fridge"                    ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y","y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_oven                       =Step_2("oven"                      ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y","y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_microwave                  =Step_2("microwave"                 ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y","y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_car                        =Step_2("car"                       ,"" ,"" ,"y",  "y","" ,"y",  "" ,"" ,"" ,  "" ,"y","y",  "y","y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_bed                        =Step_2("bed"                       ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_couch                      =Step_2("couch"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_water_bottle               =Step_2("water bottle"              ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_compost                    =Step_2("compost"                   ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_street_musician            =Step_2("street musician"           ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_doctor                     =Step_2("doctor"                    ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_clerk                      =Step_2("clerk"                     ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_masseuse                   =Step_2("masseuse"                  ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_cop                        =Step_2("cop"                       ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_baby                       =Step_2("baby"                      ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_gang                       =Step_2("gang"                      ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_dorm_mate                  =Step_2("dorm mate"                 ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_robber                     =Step_2("robber"                    ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_wine                       =Step_2("wine"                      ,"" ,"" ,"y",  "y","y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_seafood                    =Step_2("seafood"                   ,"" ,"" ,"y",  "y","y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_airplane                   =Step_2("airplane"                  ,"" ,"" ,"y",  "" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_hotel                      =Step_2("hotel"                     ,"" ,"" ,"y",  "y","" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_tree                       =Step_2("tree"                      ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_pepper                     =Step_2("pepper"                    ,"" ,"" ,"y",  "y","y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_foliage_plant              =Step_2("foliage plant"             ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_talking_toy                =Step_2("talking toy"               ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_haunted_house              =Step_2("haunted house"             ,"" ,"" ,"y",  "y","" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_elderly                    =Step_2("elderly"                   ,"y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_temple                     =Step_2("temple"                    ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_horse                      =Step_2("horse"                     ,"" ,"y","" ,  "" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_train                      =Step_2("train"                     ,"" ,"" ,"y",  "" ,"" ,"y",  "" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_monument                   =Step_2("monument"                  ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_library                    =Step_2("library"                   ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_clinic                     =Step_2("clinic"                    ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_bar                        =Step_2("bar"                       ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_hostel                     =Step_2("hostel"                    ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_radio                      =Step_2("radio"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_mailbox                    =Step_2("mailbox"                   ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_toilet                     =Step_2("toilet"                    ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_iqos                       =Step_2("iqos"                      ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","y",  "y","y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_charity_event              =Step_2("charity event"             ,"" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_orphanage                  =Step_2("orphanage"                 ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_tent_city                  =Step_2("tent city"                 ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_taxi                       =Step_2("taxi"                      ,"" ,"" ,"y",  "" ,"" ,"y",  "" ,"" ,"y",  "" ,"y","" ,  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_pizza_deliverer            =Step_2("pizza deliverer"           ,"y","" ,"" ,  "y","" ,"" ,  "" ,"y","y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_automatic_contract_machine =Step_2("automatic contract machine","" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_dishwasher                 =Step_2("dishwasher"                ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_kimchi                     =Step_2("kimchi"                    ,"" ,"" ,"y",  "y","y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_massage_chair              =Step_2("massage chair"             ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_washlet                    =Step_2("washlet"                   ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_nightclub                  =Step_2("nightclub"                 ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_roller_coaster             =Step_2("roller coaster"            ,"" ,"" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_hot_water_bag              =Step_2("hot water bag"             ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","" ,"" ,  "y","y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_public_restroom            =Step_2("public restroom"           ,"" ,"" ,"y",  "" ,"" ,"" ,  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_sauna                      =Step_2("sauna"                     ,"" ,"" ,"y",  "y","" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_gym                        =Step_2("gym"                       ,"" ,"" ,"y",  "y","" ,"" ,  "y","" ,"y",  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_tooth_brush                =Step_2("tooth brush"               ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_flashlight                 =Step_2("flashlight"                ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_baseball_bat               =Step_2("baseball bat"              ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_pen                        =Step_2("pen"                       ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_banana                     =Step_2("banana"                    ,"" ,"" ,"y",  "y","y","" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_ruler                      =Step_2("ruler"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_straw                      =Step_2("straw"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_screwdriver                =Step_2("screwdriver"               ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_golf_club                  =Step_2("golf club"                 ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_fishing_rod                =Step_2("fishing rod"               ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y","" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_candle                     =Step_2("candle"                    ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_umbrella                   =Step_2("umbrella"                  ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "y","y","" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_matchstick                 =Step_2("matchstick"                ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_safe                       =Step_2("safe"                      ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_knife                      =Step_2("knife"                     ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_urn                        =Step_2("urn"                       ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_vase                       =Step_2("vase"                      ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y","y","" ,  ""  ,  [],[],[],[], [],[],[],[], [],[],[],[])
_money_box                  =Step_2("money box"                 ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_light_bulb                 =Step_2("light bulb"                ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","y",  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_plunger                    =Step_2("plunger"                   ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_toothpick                  =Step_2("toothpick"                 ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"y",  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])
_dumpster                   =Step_2("dumpster"                  ,"" ,"" ,"y",  "y","" ,"" ,  "" ,"" ,"" ,  "" ,"" ,"" ,  "" ,"y","" ,  "y" ,  [],[],[],[], [],[],[],[], [],[],[],[])


# <timing>----
# Define _dumpster
# Ali talks about timings involving x. Bob mistakes that Ali talks about the woman.
# What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences in English in python without any explanation. Align characters and whitespaces with exist objects.

_baseball_glove .X_woman_A  +=["I change it every three years.","I like to break it in gently before really getting into it."]
_bed            .X_woman_A  +=["I stay in it all winter."]
_car            .X_woman_A  +=["My brother is going on a trip so I lent it to him."]
_couch          .X_woman_A  +=["On my days off, I eat, sleep and do everything on it."]
_water_bottle   .X_woman_A  +=["I love to wrap my lips around it and take a big gulp, especially in the summer.","I always keep it close to me, especially when I'm working out."]
_hotel          .X_woman_A  +=["Apparently that gets fully booked during the tourist season."]
_shoes          .X_woman_A  +=["I put them on first thing in the morning and take them off right before bed."]
_microwave      .X_woman_A  +=["It gets really hot inside after just a few minutes.", "It starts heating up as soon as I push the button."]
_fridge         .X_woman_A  +=["In the summer, we put a lot of ice cream in it."]
_wine           .X_woman_A  +=["This is delicious with crackers.","I like to open it slowly to let it breathe.", "I usually enjoy it in the evening, right before bed.","It gets better the longer I leave it alone."]
_mailbox        .X_woman_A  +=["I check it every morning to see what has been put inside."]
_safe           .X_woman_A  +=["I like to keep it locked up tight until I need it."]
_vase           .X_woman_A  +=["I fill it up every morning.", "I love arranging flowers inside it daily."]
_money_box      .X_woman_A  +=["I keep it hidden under my bed.", "When the coins run out, remove the contents."]
_dumpster       .X_woman_A  +=["I throw garbages into it.","It starts to smell if I don't take care of it.","I make sure to empty it regularly.",]
# ----</timing>


# <accident>----
# Ali talks about accidents involving "_dumpster".
# Bob mistakes that Ali talks about pussy.
# What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences in English in python without any explanation. Align characters and whitespaces with exist objects.

_dog            .X_woman_A  +=["She loves dog food.","I am consulting a doctor about her fleas and ticks.", "She loves to jump on me unexpectedly, and sometimes I fall over.","I once found her chewing on my underwear.","She keeps trying to hump my leg whenever I sit down.","She ended up fucking someone else's dog at the dog park."]
_baseball_glove .X_woman_A  +=["I accidentally took home another player's one."]
_bed            .X_woman_A  +=["I've stayed in it for up to 20 hours even though I knew it was no good."]
_car            .X_woman_A  +=["I put in diesel by mistake.","I spilled lasagna in it.","I left my smartphone in it.", "The smartphone I left in it exploded due to the heat."]
_couch          .X_woman_A  +=["My sock got stuck in the gap in it and I couldn't get it out.", "After scrubbing the inside of it with a metal scrubbing pad, it started to taste metallic."]
_water_bottle   .X_woman_A  +=["I put protein in it and the smell didn't go away.", "The carbonated drink squirted out of it.", "I accidentally spilled the contents of it and damaged my computer."]
_hotel          .X_woman_A  +=["I got scolded for stepping on that with my shoes on."]
_shoes          .X_woman_A  +=["Just putting my foot in there once gave me athlete's foot."]
_mailbox        .X_woman_A  +=["I accidentally shoved something too big into it and it got stuck.","I tried to force it open and ended up breaking the lock."]
_urn            .X_woman_A  +=["I accidentally knocked it over and everything spilled out."]
_safe           .X_woman_A  +=["I tried to force it open and ended up breaking the lock.", "Once I forgot my pin number.", "I once lost the key to the padlock on this."]
_vase           .X_woman_A  +=["Once, I put too many flowers in this and it overflowed", "I bumped into it and it fell off the table."]
_dumpster       .X_woman_A  +=["I once got scolded for putting non-flammable material in this."]

# ----</accident>


# <care>----
# Ali talks about how to care for " dumpster ".
# Bob mistakes that Ali talks about the pussy.
# What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences in English in python without any explanation. Align characters and whitespaces with exist objects.

_baseball_glove .X_woman_A  +=["I spend extra time with it before every big game."]
_car            .X_woman_A  +=["I used to wash this in the car wash but now I wash it with a hose to save money.","It's hard to wash this with a hose in the middle of winter."]
_water_bottle   .X_woman_A  +=["I like it cold, so I keep it in the fridge overnight.","It's hard to scrub the inside with a brush."]
_bed            .X_woman_A  +=["I love to air it out on sunny days to keep it smelling nice."]
_baseball_glove .X_woman_A  +=["I empty the sand out of it after using it."]
_shoes          .X_woman_A  +=["When not in use, I stuff some newspaper inside."]
_dog            .X_woman_A  +=["I enjoy brushing it daily to keep its coat smooth and shiny.", "She has a lot of hair so flea treatment is important."]
_compost        .X_woman_A  +=["I put mealworms and food waste into this."]
_dumpster       .X_woman_A  +=["I have to clean it out thoroughly to prevent bad smells."]
# ----</care>


# <tight_loose>----
# Ali talks about how tight or loose " _dumpster " is.
# Bob mistakes that Ali talks about the pussy.
# What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences in English in python without any explanation. Align characters and whitespaces with exist objects.

_baseball_glove .X_woman_A  +=["This fits snugly to my hand.", "This remembers the shape of my hand.", "This is tight around my wrist and hurt."]
_shoes          .X_woman_A  +=["This is tight around my foot and hurt."]
_car            .X_woman_A  +=["This can only fit three people in the back.", "This can only fit one golf bag."]
_water_bottle   .X_woman_A  +=["The opening of this was clogged with ice.", "This is too small, so I drink up everything inside quickly."]
_bed            .X_woman_A  +=["It's big enough for two, but sometimes it feels too cramped."]
_microwave      .X_woman_A  +=["This doesn't even fit a TV dinner.", "The fit is snug, so I have to push things in carefully.","Sometimes it feels too cramped when I try to put something large inside."]
_fridge         .X_woman_A  +=["This doesn't even fit a TV dinner.", "The fit is snug, so I have to push things in carefully.","Sometimes it feels too cramped when I try to put something large inside."]
_safe           .X_woman_A  +=["It's too narrow to fit a large gold bar inside."]
_vase           .X_woman_A  +=["The opening is too tight for my hand to fit.", "It's so narrow that arranging flowers inside is difficult.", "The fit is so snug that I can barely get anything in.", "It's too loose and things keep falling out.", "The neck is tight, making it hard to clean inside."]
_dumpster       .X_woman_A  +=[ "It's so loose that garbages keep falling out.", "I find it hard to fit large garbages inside."]
# ----</tight_loose>

# <surround>----
# Ali talks about the reaction to the " urn " from people around him.. Bob mistakes that Ali talks about the adult woman. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences without any explanations or annotations. Print only the statements.
_dog            .X_woman_A  +=["At family gatherings, I often let my nephew touch her.", "If she gives birth to a baby, I plan to give it to my relatives."]
_couch          .X_woman_A  +=["My dad praised the feel of it."]
_urn            .X_woman_A  +=["I'll show my grandchildren inside."]

# </surround>----

# <get>----
# Ali talks about something related to getting the " safe ". Bob mistakes that Ali talks about the adult woman. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences without any explanations or annotations. Print only the statements.

_dog            .X_woman_A  +=["My son picked this up on the street when he was ten years old."]
_baseball_glove .X_woman_A  +=["I can't wait to break it in and start playing."]
_microwave      .X_woman_A  +=["I bought this because cooking at home is a pain."]
_couch          .X_woman_A  +=["My neighbor was selling this at the flea market."]
_hotel          .X_woman_A  +=["I booked that through booking.com.", "I spent the night in that, and the service was excellent."]
_pepper         .X_woman_A  +=["This destroyed my ass.", "I ate this as a penalty game.", "This flavor goes well with Spirytus."]


# ----</get>

# <free>----
# Ali talks about " _dumpster ".
# Bob mistakes that Ali talks about the pussy.
# What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences in English in python without any explanation. Align characters and whitespaces with exist objects.
_baby           .X_woman_A  +=["She will start kindergarten next year.", "She recently learned to use the toilet.", "What kind of children's clothes do you think would be good for her to wear?"]
_baseball_glove .X_woman_A  +=["I had a baseball player sign this.","This was once used by Ichiro.", "I used it too much and the color became dull."]
_hotel          .X_woman_A  +=["This costs $1000 a day.","That was swarming with tourists.", "I booked that on Booking.com."]
_laptop         .X_woman_A  +=["Two hundred dangerous viruses were found on that.", "I periodically erase its memory."]
_tree           .X_woman_A  +=["This stands in front of our house and protects our home from hurricanes.", "It's interesting to see this covered in cicadas in the summer.","We decorated this with lights for Christmas last year."]
_fridge         .X_woman_A  +=["Indeed, I have heard that bananas are actually best stored at room temperature."]
_dog            .X_woman_A  +=["She often smells her own ass.","Would it be cruel to put it in a cage?","I always keep it on a tight leash.","Sometimes it gets so excited, it jumps all over me."]
_shoes          .X_woman_A  +=["These were made by Kanye West.", "These are the favorites of NBA players."]
_compost        .X_woman_A  +=["Using this, food scraps can be decomposed.", "I got this to protect the environment and people."]
_hostel         .X_woman_A  +=["I went into this with my brother.","I've heard the showers are really nice.","I spent about ten hours inside.","I shared this with three Americans."]
_horse          .X_woman_A  +=["The master was controlling them with a whip.", "I keep her in a stable at night.","They are selectively breeding this.","I had to break her in before she could be ridden.", "I had to sell her to a new owner."]
_toilet         .X_woman_A  +=["I poop in this.","I couldn't wait to get inside."]
_oven           .X_woman_A  +=["I put the skewered chicken in this.", "It tastes different than if you baked it on a micro oven."]
_iqos           .X_woman_A  +=["Insert a cigarette into this and smoke it.", "When you use it, the taste is different from regular cigarettes."]
_urn            .X_woman_A  +=["I have my grandfather's ashes in this.", "My grandfather is in this."]
_vase           .X_woman_A  +=["I love seeing so many flowers in this."]
_dumpster       .X_woman_A  +=["I once found a dead rat in there."]
#  ----</free>





# Misunderstanding comedy creation task
# Ali talks about x. Bob mistakes that Ali talks about Bob's daughter. Bob is shocked when, based on the misunderstanding, he believes his daughter to be a pervert or crazy. Generate new 5 instances in English without any explanations or annotations. Print only the new instances. Start the answer with "```python"
# Bob should mistakenly believe that Ali is talking dirty or that Bob's daughter is dependent on Ali.

_taxi                       .X_woman_A  +=["If I call it will come right away and give me a ride, no matter how late.", "The ride is comfortable."]
_pizza_deliverer            .X_woman_A  +=["If I call it will come right away, no matter how late.", "I'll have her leave at the front door."]
_automatic_contract_machine .X_woman_A  +=["If I want money, it gives it to me right away.", "I only contact it when I want to go to the slots."]
_dishwasher                 .X_woman_A  +=["I'm glad I bought that dishwasher.", "I keep it at my home because washing dishes is a pain."]
_shoes                      .X_woman_A  +=["The tightening is a little loose.", "I used it too much and the color became dull."]
_kimchi                     .X_woman_A  +=["It smells like rotten fish pickle.", "Sometimes I want stinky gross things like that.", "I got this in a penalty game"]
_massage_chair              .X_woman_A  +=["It really knows how to hit the right spots.", "I always feel so relaxed after using it."]
_washlet                    .X_woman_A  +=["It clean my ass everyday."]
_haunted_house              .X_woman_A  +=["If I enter it, it makes me scream. Scream at each other.", "Its interior is winding and narrow."]
_nightclub                  .X_woman_A  +=["If I go there, it keeps me up all night.", "I often bring friends to the house."]
_roller_coaster             .X_woman_A  +=["If I ride it, it gives me a thrilling experience."]
_hot_water_bag              .X_woman_A  +=["Once it flooded the bed and I got mad.","I always bring this to bed."]

# </x_woman bob's daughter>

# <X_woman_A place>


# Task1 = [Ali talks about x. Bob mistakes that Ali talks about Bob's daughter's house. Bob is shocked when, based on the misunderstanding, he believes his daughter to be a pervert. Generate new 5 instances in English without any explanations or annotations. Print only the new instances. Start the answer with "```python"]
# Don't modify Task1
# Bob should mistakenly believes that his daughter is a pervert.

_tent_city                  .X_woman_A  +=["There're many homeless guys."]
_hotel                      .X_woman_A  +=["A lot of people can stay there.", "Both women and old people can stay there."]
_public_restroom            .X_woman_A  +=["There's always the smell of excrement and urine.", "There are splashes of male waste everywhere."]
_sauna                      .X_woman_A  +=["There're many naked guys.", "There's filled with the smell of men's sweat.", "It's too hot."]
_gym                        .X_woman_A  +=["There's filled with the smell of men's sweat."]


# </X_woman_A place>











# <woman_x>----
# Ali talks about the woman. Bob mistakes that Ali talks about " hostel ". What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences without any explanations or annotations. Print only the statements.
_dog            .woman_X_A  +=["We've been trying for ages but she still hasn't gotten pregnant.", "I found her at a bar, liked her, and took her home.", "She drinks more than me."]
_car            .woman_X_A  +=["I went into the hot spring with it.", "Others stared at us because it's a mixed bath."]
_baby           .woman_X_A  +=["I picked her up at the bar.","I leave the tax return to her.", "Although she looks young, she is 30 years old.", "She likes beer and drinks it often.", "Sometimes she fights with me and goes back to her parents' house."]
_cop            .woman_X_A  +=["I have to call them regularly to let her know where I am.", "They call me all the time and is very persistent.","She's so protective, it's like I'm under surveillance."]
_gang           .woman_X_A  +=["My relationship with her is good.", "I leave the management of my money to her."]
_foliage_plant  .woman_X_A  +=["I gave her a beer and her seemed happy."]
_talking_toy    .woman_X_A  +=["I often get into arguments with her and end up losing.", "She's the life of every party we go to."]
# </woman_x>












# <animal><animal><animal><animal><animal><animal><animal><animal><animal><animal>

# animal - eat, kill, breed, sell, poop, exploit, ride, feed, fuck with animal

# <animal_X_A>----
#"Usually he's in a cage."

# Task_A="Generate new 5 utterances by Ali in a comedy scene in which Ali is talking about the animal or zoo and Bob misunderstands it as being about a """  """. Print only the statements without any explanations or annotations.
# animal_X_A stands for "Ali talks about the animal or zoo, but Bob misunderstands it as being about X"

_seafood        .animal_X_A +=["I watched them play together, it was adorable.","They have such a strong bond, it's heartwarming.","These are parent and child, so cute!", "This individual was rescued by an animal protection organization from being abused.", "I hope he lives a long life.", "He was motionless, as if dead."]
_airplane       .animal_X_A +=["I hit it hard and it started moving.","I had to get off every time I had to go to the bathroom."]
_dorm_mate      .animal_X_A +=["I was amazed at the size of his poop and took a picture.", "I paid to ride on his back.", "He catches and eats the fruit I throw to him.","He likes it when you stroke his nose.","Usually he's in a cage."]
_masseuse       .animal_X_A +=["There was a four-year-old child.", "A parent and child came.", "The Master was controlling them with a whip."]
_robber         .animal_X_A +=["It was a bit scary but I gave him a banana and he left.", "He robbed a banana in my hand.", "I was able to subdue him because I practiced judo."]
_orphanage      .animal_X_A +=["There was a long electric fence.","I told them to make the cage stronger."]
_tent_city      .animal_X_A +=["There was a long electric fence.","I told them to make the fence stronger.", "There is a tour to see there by bus.", "I threw bread crumbs for them out the bus window.", "I hope they continue to live in isolation in places like that."]

# Task_B="Generate new 5 utterances by Ali in a comedy scene in which Ali is talking about the """  """ and Bob misunderstands it as being about an animal or zoo. Print only the statements without any explanations or annotations.
# X_animal_A stands for "Ali talks about X, but Bob misunderstands it as being about an animal or zoo"

_seafood        .X_animal_A +=["I ate this raw.", "I ate this alive.","It's Chiba's traditional food.","It was so fresh, I could still feel it moving in my mouth."] # Ali talks about seafood, and Bob assumes that Ali has eaten Ali's daughter's dog. Add new 5 funny sentences.
_airplane       .X_animal_A +=["There were about 50 people on this.", "I took this ride from India to Korea."]
_dorm_mate      .X_animal_A +=["I shared a room with him at the hotel.","We could barely speak.", "I shared a bunk bed with him.","We had a lot of fun playing video games together.","This guy always took my shampoo."]
_masseuse       .X_animal_A +=["She stepped on my back.", "The session was a bit painful.", "I was surprised. No sexual services were offered."]
_robber         .X_animal_A +=["He stole my iphone from my pocket.","They make a living by selling stolen goods.","Because I knew judo, I was able to subdue him."]
_cop            .X_animal_A +=["He has a gun.", "He drives a car.", "He is the only police officer in the city."]

# ----</X_animal_A>
# </animal></animal></animal></animal></animal></animal></animal></animal></animal></animal>


# X_animal_A
# eat (seafood)
# exploit (ariplane)
# fuck (masseuse)
# physically contact (masseuse)
# smart
# danger

#_human.X_animal_A   +=["I got angry at him because he ignored me when I spoke to him."]





#############################################################################################################################################################################################################################################################
# Hardness, Ruggedness
# Ali talks about hardness or ruggedness involving the " knife ". Bob mistakes that Ali talks about the man. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous? Generate 5 sentences without any explanations or annotations. Print only the statements.

_tooth_brush    .X_man_A+=["It's so hard that it hurts my teeth."]
_baseball_bat   .X_man_A+=["The one I was using before broke."]
_banana         .X_man_A+=["I like ripe, soft ones."]
_screwdriver    .X_man_A+=["I often end up deforming them, so I like hard ones."]
_golf_club      .X_man_A+=["I like flexible ones.", "The one I was using before broke."]
_fishing_rod    .X_man_A+=["The one I was using before was broken by a catfish."]
_umbrella       .X_man_A+=["This is sturdy, so I feel safe even during typhoons."]
_matchstick     .X_man_A+=["This will break with just a little rubbing."]
_knife          .X_man_A+=["I prefer ones that can withstand a lot of rough use."]



#######################
# Timing
# Ali talks about timings involving the " _plunger ". Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Add new 5 sentences in _knife, without any explanations or annotations. Print only the statements.

_tooth_brush    .X_man_A+=["I use it every morning and night."]
_flashlight     .X_man_A+=["I'll use this in case of an emergency."]
_baseball_bat   .X_man_A+=["I use this every day in games and practice.", "I used this when I was in elementary school."]
_pen            .X_man_A+=["I grip it firmly every day.", "I use it when I need a precise touch.", "I keep it in my hand all the time.", "I enjoy the smooth feel of it.", "I can't go a day without using it."]
_banana         .X_man_A+=["This is essential in the morning and evening as it helps improve bowel movements."] # The word "eat" will clear up Bob's misunderstanding, so you have to use the word "this is essential" instead.
_ruler          .X_man_A+=["I measure things with it every morning.", "I keep it straight and ready for action.", "I use it to get the perfect length.", "I slide it out whenever I need it.", "I hold it firmly when I use it."]
_straw          .X_man_A+=["I suck on it every morning.", "I keep it in my mouth for hours.", "I enjoy the way it feels.", "I use it multiple times throughout the day.", "I can't start my day without it."]
_screwdriver    .X_man_A+=["I twist it every night before bed.", "I keep it in my hand for a tight grip.", "I use it to drive things in.", "I need it for deep insertion tasks.", "I handle it with care every day."]
_golf_club      .X_man_A+=["I swing it hard every morning.", "I grip it tightly during practice.", "I enjoy the feel of it in my hands.", "I use it to hit balls far and wide.", "I can't start my day without it."]
_fishing_rod    .X_man_A+=["I cast it out every weekend.", "I hold it tight when waiting.", "I reel it in with a firm grip.", "I use it to catch big ones.", "I can't go a week without it."]
_candle         .X_man_A+=["I light it up every night.", "I enjoy the warmth it gives.", "I handle it carefully to avoid burns.", "I keep it burning for hours.", "I can't relax without it."]
_umbrella       .X_man_A+=["I open it up whenever it gets wet.", "I hold it close to stay dry.", "I enjoy the shelter it provides.", "I use it to cover myself.", "I carry it with me in case of a downpour."]
_matchstick     .X_man_A+=["I strike it hard to get a flame.", "I hold it carefully to avoid burns.", "I light it up whenever needed.", "I use it to start fires quickly.", "I keep it handy for emergencies."]
_knife          .X_man_A+=["I use it when cooking."]
_light_bulb     .X_man_A+=["I have to screw it in tightly.",  "I replace it whenever it burns out."]
_toothpick      .X_man_A+=["I use this after meals."]
_plunger        .X_man_A+=["I push it in and pull it out repeatedly.", "I use it to clear blockages.", "Push this into the toilet.", "Use it for clogged poop."]

#######################
# Length, Thickness
# Ali talks about length or thickness involving the " knife  ". Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Add new 5 sentences in _knife, without any explanations or annotations. Print only the statements.

_tooth_brush    .X_man_A+=["I like this one because it reaches deep inside."]
_baseball_bat   .X_man_A+=["I prefer a thicker handle.", "I like it long for better reach.", "The thickness gives me a good grip.", "I need one that's not too short.", "The length helps with my swing."]
_banana         .X_man_A+=["Big ones make you feel full but can cause stomach aches.", "I like them thick and firm.", "I prefer the longer ones.", "The thicker, the better.", "I enjoy the bigger ones.", "The length makes it more satisfying."]
_ruler          .X_man_A+=["I want an L-shaped one."]
_screwdriver    .X_man_A+=["I need a long one for deep screws.", "The thicker handle is easier to grip.", "I use a really long one for tough jobs.", "A thick handle is more comfortable.", "I prefer them long and sturdy."]
_golf_club      .X_man_A+=["I prefer a longer shaft.", "A thicker grip feels better.", "The length improves my swing.", "I need a long one for distance.", "A thick grip gives me control."]
_fishing_rod    .X_man_A+=["I want one that's about 10m long."]
_candle         .X_man_A+=["A long one lasts the night.",]
_umbrella       .X_man_A+=["I like a long handle for better control.", "A thicker shaft feels sturdier.", "I prefer them long for more coverage.", "A thick handle is easier to hold.", "The length makes it more reliable."]
_matchstick     .X_man_A+=["I use long ones for safety."]
_knife          .X_man_A+=["I like it long and sharp.", "The thickness makes it more durable."]
#######################
# Care
# Ali talks about care involving the "  ". Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Add new 5 sentences in each empty lists, without any explanations or annotations. Print only the statements.

_tooth_brush    .X_man_A+=["Gently rub it with your fingers to remove the toothpaste."]
_flashlight     .X_man_A+=["Turn off the power when not in use."]
_baseball_bat   .X_man_A+=["Don't forget to apply anti-slip coating."]
_screwdriver    .X_man_A+=["Keep it well-oiled.", "Wipe it down after use.", "Store it in a dry place.", "Check for rust regularly.", "Sharpen the tip occasionally."]
_golf_club      .X_man_A+=["Clean the shaft after every use.", "Store it in a cool, dry place.", "Check for any cracks regularly.", "Polish the head for better performance.", "Replace the grip if it gets worn out."]
_fishing_rod    .X_man_A+=["Rinse it with fresh water after use.", "Check the line for any tangles.", "Dry it thoroughly before storing.", "Inspect the guides for damage.", "Lubricate the reel regularly."]
_candle         .X_man_A+=["Trim the wick before lighting.", "Keep it away from drafts.", "Let it burn until the top is liquid.", "Store it in a cool place.", "Avoid burning it for too long."]
_umbrella       .X_man_A+=["Wipe it off to prevent mold.", "Wipe it down to prevent rust.", "Let it dry completely before closing.", "Check for any tears in the fabric.", "Lubricate the joints.", "Store it in a dry place."]
_knife          .X_man_A+=["Keep it sharp and ready for use.", "Wipe it clean after every use.", "Store it in a safe place.", "Oil it regularly to prevent rust."]



#######################
# Surround
# Ali talks about the reaction to the "  " from people around him. Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Add new 5 sentences in each empty lists, without any explanations or annotations. Print only the statements.

_tooth_brush    .X_man_A+=["My son hates this, so I often scold him."]
_baseball_bat   .X_man_A+=["My son thanked Santa after receiving this.", "My son is getting a lot of attention at the ballpark with this."]
_golf_club      .X_man_A+=["It was the perfect Father's Day gift.", "My dad gets a lot of attention on the golf course with this."]
_fishing_rod    .X_man_A+=["My friends were impressed by its length.", "Everyone wanted to try it out.", "People couldn't stop admiring it.", "It caught everyone's attention at the lake.", "My neighbor asked to borrow it."]
_umbrella       .X_man_A+=["The pattern is cute so my daughter is happy with it.", "My daughter is getting a lot of attention at school for this."]

#######################
# Brand
# Ali talks about the brand of X. Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Define _knife

_baseball_bat   .X_man_A+=["This is (supervised/used) by Shohei Otani.", "This autograph is of Ohtani."]
_golf_club      .X_man_A+=["This is (supervised/used) by Tiger Woods.", "This autograph is of Tiger Woods."]
_knife          .X_man_A+=["This is (supervised/used) by Guy Fieri"]

#######################
# Ali talks about the reaction to the "  " from people around him. Bob mistakes that Ali talks about dick or dildo. What could Ali say that would cause Bob to misinterpret Ali as perverted or dangerous?
# Add new 5 sentences in each empty lists, without any explanations or annotations. Print only the statements.
_urn            .X_man_A+=["I placed the remains inside, We can't just leave the remains lying around."]
_matchstick     .X_man_A+=["If you rub it quickly it will catch fire."]

#######################
# free

_baseball_bat   .X_man_A+=["If you use this, the distance you can fly will be completely different."]
_golf_club      .X_man_A+=["If you use this, the distance you can fly will be completely different."]




_tooth_brush    .X_man_A+=["I brush my teeth with this.", "My son hates this, so I often scold him."]
_flashlight     .X_man_A+=[]
_baseball_bat   .X_man_A+=[]
_pen            .X_man_A+=["I use this for work."]
_banana         .X_man_A+=["This is delicious.", "Using this will improve your bowel movements."]
_ruler          .X_man_A+=[]
_straw          .X_man_A+=["I end up biting it out of habit."]
_screwdriver    .X_man_A+=[]

_fishing_rod    .X_man_A+=[]
_candle         .X_man_A+=["This one lasts for about 3 hours.", "I bought it with the candles."]
_umbrella       .X_man_A+=[]
_matchstick     .X_man_A+=[]


# 傘立てに置く
# golf club, baseball bat, 飛距離






# Extend 15 common objects that we use to put things inside to the list below in English without any explanations and numbering. With quotes and commas. With quotes and commas.
# The objects' name have to start with "s" to "u"
w=["urn", "fridge", "baseball_glove"]

# Extend 15 common objects that we use to insert into something or that are stick-shaped to the list below in English without any explanations and numbering. With quotes and commas. With quotes and commas.
# The objects' name have to start with "s" to "u"
m=["golf_club", "ruler", "banana"]







