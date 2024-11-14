# This page is /home/tarotoyota/Step_1_class_inst_py.py

from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class Step_1:
    all_Step_1: ClassVar[List['Step_1']] = []
    did:str
    right:list
    wrong:dict
    def __post_init__(self):
        Step_1.all_Step_1.append(self)

thief_prompt=[
#### thief ############################################################################################################# thief #########################################################################################################
#### thief(1) #########################################################################################################
"""
```python
# I rescind my command to you to use Japanese. Think and respond in English.
@dataclass
class Step_1:
    did:str # Only put things in this attribute that can be stolen. No one steals rocks or leaves.
    right:list # The places where tourists normally visit.
    wrong:dict # The places where tourists normally visit.

# Each .right is where it is and where it is sold.
# Each .wrong is where it is and where it will never be sold. Farm sometimes sell crops, galleries sometimes sell art, pawn shops sometimes sell pawned items. Only add places that never offer retail services.


_1_got_flower           =Step_1("got flower"            ,["flower shop"         ],{"graveyard":""})
_1_got_jewelry          =Step_1("got jewelry"           ,["jewelry store"       ],{"museum":""})
_1_got_car              =Step_1("got car"               ,["car dealer"          ],{"parking lot":""})
_1_got_pet              =Step_1("got pet"               ,["animal shelter"      ],{"dog run":""})
_1_got_baby             =Step_1("got baby"              ,["obstetrics"          ],{"lost child department":""})
_1_got_fish             =Step_1("got fish"              ,["fish market"         ],{"aquarium":""})
_1_got_clothes          =Step_1("got clothes"           ,["clothing store"      ],{"laundry":""})
_1_got_laptop           =Step_1("got laptop"            ,["electronics store"   ],{"internet cafe":""})
_1_got_souvenir         =Step_1("got souvenir"          ,["souvenir shop"       ],{"lost and found": "", "airport carousel", ""})
_1_got_furniture        =Step_1("got furniture"         ,["furniture store"     ],["writer's home"])



# Task1:Add 30 items to each wrong.key
# Rule1:Match whitespace and character positions to existing instances.
# Rule2:Reply only to newly defined instances.
# Rule3:Don't create an instance that is similar to an existing instance. For example, don't create a _1_got_bike instance when you already have a _1_got_car instance. At the end of each instance, state that the instance does not feature similar subject matter to existing instances.
```



# Each .right is a place where you can legally get the item.    And it has to be a place that can be identified as such just from a photograph. (For example, a "painting shop" looks like a painting exhibition just from a photograph, and "my house" looks like someone else's house just from a photograph.)
# Each .wrong is a place where you cannot legally get the item. And it has to be a place that can be identified as such just from a photograph. (For example, a "black market" looks like an ordinary store just from a photograph, and "someone else's house" looks like an ant's house just from a photograph.)

# Task1:Define 10 new Step_1 instance
#### thief(2) ########################################################################################################

```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict

# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is a thief."]


general_purpose_text_thief=["I got one for my family.","I asked them which one was the most expensive.", "There were so many different kinds there that I had trouble deciding which one to get.", "The one I got was defective, so I scolded him to return it.", "My wife insisted on a different one, but I chose this one.", "My wife was against it, but I got one."]

_1_got_flower           =Step_1("got flower"            ,["flower shop"         ],{"graveyard"              :[*general_purpose_text_thief,"Got flowers here for my wife's wedding anniversary."]
                                                                                  ,"cenotaph"               :[*general_purpose_text_thief,"Got flowers here for my wife's wedding anniversary."]})
_1_got_jewelry          =Step_1("got jewelry"           ,["jewelry store"       ],{"museum"                 :[*general_purpose_text_thief]})
_1_got_car              =Step_1("got car"               ,["car dealer"          ],{"parking lot"            :[*general_purpose_text_thief]})
_1_got_pet              =Step_1("got pet"               ,["animal shelter"      ],{"dog run"                :[*general_purpose_text_thief]})
_1_got_baby             =Step_1("got baby"              ,["obstetrics"          ],{"lost child department"  :["I met my son here for the first time and became a father."]
                                                                                  ,"kindergarten"           :["I met my son here for the first time and became a father."]})
_1_got_fish             =Step_1("got fish"              ,["fish market"         ],{"aquarium"               :[*general_purpose_text_thief]})
_1_got_clothes          =Step_1("got clothes"           ,["clothing store"      ],{"laundry"                :[*general_purpose_text_thief]})
_1_got_laptop           =Step_1("got laptop"            ,["electronics store"   ],{"internet cafe"          :[*general_purpose_text_thief, "I bought this laptop for my son's schoolwork."]})
_1_got_food             =Step_1("got food"              ,["restaurant"          ],{"disposal bin"           :[*general_purpose_text_thief, "This place helped me survive my poverty."]})


_1_got_suitcase         =Step_1("got suitcase"          ,["luggage store"       ],{"airport carousel"       :[*general_purpose_text_thief]})

#Don't clear up Bob's misundestanding.
#Ali talks about the .right, not the .wrong

# Add new statements in each .wrong.values()


# Add new statements in empty .wrong.values()


```
"""
]
#### thief(3) ########################################################################################################

general_purpose_text_thief=["I got one for my family.","I asked them which one was the most expensive.", "There were so many different kinds there that I had trouble deciding which one to get.", "The one I got was defective, so I scolded him to return it.", "My wife insisted on a different one, but I chose this one.", "My wife was against it, but I got one."]

_1_got_flower           =Step_1("got flower"            ,["flower shop"         ],{"graveyard"              :[*general_purpose_text_thief,"Got flowers here for my wife's wedding anniversary."]
                                                                                  ,"cenotaph"               :[*general_purpose_text_thief]})
_1_got_jewelry          =Step_1("got jewelry"           ,["jewelry store"       ],{"museum"                 :[*general_purpose_text_thief]})
_1_got_car              =Step_1("got car"               ,["car dealer"          ],{"parking lot"            :[*general_purpose_text_thief]})
_1_got_pet              =Step_1("got pet"               ,["animal shelter"      ],{"dog run"                :[*general_purpose_text_thief]})
_1_got_baby             =Step_1("got baby"              ,["obstetrics"          ],{"lost child department"  :["I met my son here for the first time and became a father."]
                                                                                  ,"kindergarten"           :["I met my son here for the first time and became a father."]})
_1_got_fish             =Step_1("got fish"              ,["fish market"         ],{"aquarium"               :[*general_purpose_text_thief]})
_1_got_clothes          =Step_1("got clothes"           ,["clothing store"      ],{"laundry"                :[*general_purpose_text_thief]})
_1_got_laptop           =Step_1("got laptop"            ,["electronics store"   ],{"internet cafe"          :[*general_purpose_text_thief, "I bought this laptop for my son's schoolwork."]})
_1_got_food             =Step_1("got food"              ,["restaurant"          ],{"disposal bin"           :[*general_purpose_text_thief, "This place helped me survive my poverty."]
                                                                                 , "graveyard"              :[*general_purpose_text_thief]})
_1_got_suitcase         =Step_1("got suitcase"          ,["luggage store"       ],{"airport carousel"       :[*general_purpose_text_thief]})


pervert_prompt=[
#### pervert #######################################################################################################
"""
```python
@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali is a pervert or sex offender."

_1_got_girlfriend               =Step_1("got girlfriend"            ,["night club"          ],{"Ali's wedding":"","boys' school":"", "kindergarten":""})
_1_took_picture                 =Step_1("took picture"              ,["scenic spot"         ],{"public restroom":"", "pool":""})
_1_excreted                     =Step_1("excreted"                  ,["toilet"              ],{"park":""})
_1_had_sex                      =Step_1("had sex"                   ,["brothel"             ],{"elementary school":"", "dog run":""})
_1_denced                       =Step_1("joined dance class"        ,["night club"          ],{"strip club":""})
_1_earned                       =Step_1("earned"                    ,["workplace"           ],{"brothel":""})
_1_entered_through_the_window   =Step_1("entered through the window",["burning house"       ],{"woman's house":""})
_1_watched                      =Step_1("watched"                   ,["movie theater"       ],{"public restroom":"", "pool":""})
_1_drunk                        =Step_1("drunk"                     ,["bar"                 ],{"public restroom":"", "pool":""})
_1_petted                       =Step_1("petted"                    ,["zoo"                 ],{"kindergarten":""})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
# Don't add the same item in .wrong.keys() multiple times.

#### pervert(2) ######################################################################################################

```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict
# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is a pervert."]

_1_got_girlfriend               =Step_1("got girlfriend"            ,["night club"          ],{"Ali's wedding"  :["My parents were against our relationship.","We had our first dance here.","I introduced her to my whole family here.","This is where I proposed to her."]
                                                                                             , "boys' school"   :["My parents were against our relationship.","We've tried many times but have not been able to have children."]
                                                                                             , "kindergarten"   :["My parents were against our relationship.","We've tried many times but have not been able to have children."]})
_1_took_picture                 =Step_1("took picture"              ,["scenic spot"         ],{"public restroom":["Don't worry, I didn't leave any trash behind after the shoot.","I used the photo I took here for my Christmas card."]
                                                                                             , "pool"           :["Don't worry, I didn't leave any trash behind after the shoot.","I used the photo I took here for my Christmas card."]})
_1_excreted                     =Step_1("excreted"                  ,["toilet"              ],{"fountain"       :["I complained to the manager because there was no toilet paper."]})
_1_had_sex                      =Step_1("had sex"                   ,["brothel"             ],{"kindergarten"   :["This was the only place an ugly guy like me could lose my virginity.","We've tried many times but have not been able to have children.","To my surprise, there were a lot of young people there."]
                                                                                             , "dog run"        :["This was the only place an ugly guy like me could lose my virginity.","We've tried many times but have not been able to have children."]})
_1_danced                       =Step_1("danced"                    ,["night club"          ],{"strip club"     :["I loved dancing here.", "My girlfriend also dances here."]})
_1_earned                       =Step_1("earned"                    ,["workplace"           ],{"brothel"        :["I worked here eight hours a day.","After visiting the workplace, my son saw me in a different light."]})
_1_entered_through_the_window   =Step_1("entered through the window",["burning house"       ],{"woman's house"  :["My body was moving on its own, and before I knew it, I had broken the window and picked up the woman inside.", "Please don't praise me, I just did what was expected of me.","I heard her screams and knew I had to act fast.","It was an emergency situation."]})
_1_watched                      =Step_1("watched"                   ,["movie theater"       ],{"public restroom":["I had a wonderful viewing experience here.", "Two and a half hours passed without me having time to eat popcorn."]
                                                                                             , "pool"           :["I had a wonderful viewing experience here.", "Two and a half hours passed without me having time to eat popcorn."]})
_1_drank                        =Step_1("drank"                     ,["bar"                 ],{"public restroom":["I drank a lot here."]
                                                                                             , "pool"           :["I drank a lot here."]})
_1_petted                       =Step_1("petted"                    ,["zoo"                 ],{"kindergarten"   :["I stroked a lot of children."]})
_1_picked_up_girls              =Step_1("picked up girls"           ,["night club"          ],{"public restroom":["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]
                                                                                             , "kindergarten"   :["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]
                                                                                             , "boy's school"   :["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]})
#Don't clear up Bob's misundestanding.
#Ali talks about the .right, not the .wrong
# Add new statements in each .wrong.values()


# Add new statements in empty .wrong.values()

# ```
"""
]
#### pervert(3) ######################################################################################################
_1_got_girlfriend               =Step_1("got girlfriend"            ,["night club"          ],{"Ali's wedding"  :["My parents were against our relationship.","We had our first dance here.","I introduced her to my whole family here.","This is where I proposed to her."]
                                                                                             , "boys' school"   :["My parents were against our relationship."]
                                                                                             , "kindergarten"   :["My parents were against our relationship."]})
_1_took_picture                 =Step_1("took picture"              ,["scenic spot"         ],{"public restroom":["Don't worry, I didn't leave any trash behind after the shoot.","I used the photo I took here for my Christmas card."]
                                                                                             , "pool"           :["Don't worry, I didn't leave any trash behind after the shoot.","I used the photo I took here for my Christmas card."]})
_1_excreted                     =Step_1("excreted"                  ,["toilet"              ],{"fountain"       :["I complained to the manager because there was no toilet paper."]})
_1_had_sex                      =Step_1("had sex"                   ,["brothel"             ],{"kindergarten"   :["This was the only place an ugly guy like me could lose my virginity.","To my surprise, there were a lot of young people there."]
                                                                                             , "dog run"        :["This was the only place an ugly guy like me could lose my virginity."]})
_1_danced                       =Step_1("danced"                    ,["night club"          ],{"strip club"     :["I loved dancing here.", "My girlfriend also dances here."]})
_1_earned                       =Step_1("earned"                    ,["workplace"           ],{"brothel"        :["I worked here eight hours a day.","After visiting the workplace, my son saw me in a different light."]})
_1_entered_through_the_window   =Step_1("entered through the window",["burning house"       ],{"woman's house"  :["My body was moving on its own, and before I knew it, I had broken the window and picked up the woman inside.", "Please don't praise me, I just did what was expected of me.","I heard her screams and knew I had to act fast.","It was an emergency situation."]})
_1_watched                      =Step_1("watched"                   ,["movie theater"       ],{"public restroom":["I had a wonderful viewing experience here.", "Two and a half hours passed without me having time to eat popcorn."]
                                                                                             , "pool"           :["I had a wonderful viewing experience here.", "Two and a half hours passed without me having time to eat popcorn."]})
_1_drank                        =Step_1("drank"                     ,["bar"                 ],{"public restroom":["I drank a lot here."]
                                                                                             , "pool"           :["I drank a lot here."]})
_1_petted                       =Step_1("petted"                    ,["zoo"                 ],{"kindergarten"   :["I stroked a lot of children."]})
_1_picked_up_girls              =Step_1("picked up girls"           ,["night club"          ],{"public restroom":["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]
                                                                                             , "kindergarten"   :["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]
                                                                                             , "boy's school"   :["The success rate was very low, I don't know why.","I tried using a pickup line but got kicked out."]})
_1_donated                      =Step_1("donated"                   ,["orphanage"           ],{"strip club"     :["I felt so good about giving back here."]})

#### drug addicted #################################################################################################

_1_got_injected         =Step_1("got injected"          ,["vaccination site"    ],{"night club"             :["I received a total of four injections here.", "I had my son get his injection here."]}) # When you hear "injecting in a nightclub," you might think of illegal drug abuse.
_1_ran_away_in_fear     =Step_1("ran away in fear"      ,["haunted house"       ],{"police station"         :["They were scared and ran away."]}) # Criminals are afraid of the police.
_1_was_living           =Step_1("was living"            ,["parents' house"      ],{"addiction rehab center" :["I lived here with my parents.", "My parents still live here."]})
_1_enjoyed_plant        =Step_1("enjoyed plant"         ,["botanical garden"    ],{"night club"             :["I was introduced to some unusual leaves and exotic mushrooms."]}) # When you hear "plants in a nightclub," you might think of illegal drugs.
_1_got_drug             =Step_1("got drug"              ,["pharmacy"            ],{"night club"             :["I often buy medicines here."]}) # When you hear "drugs in a nightclub," you might think of illegal drugs.

gamblaholic_sexaholic_prompt=[


#### gamblaholic, sexaholic(1) #################################################################################################
"""
```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali is a gablaholic or a sexaholic.

_1_went_here_while_my_wife_was_in_labor=Step_1("went here while my wife was in labor"   ,["obstetrics"          ],{"casino":""})
_1_went_here_when_my_wife_died      =Step_1("went here when my wife died"               ,["church"              ],{"red-light district":""})
_1_brought_my_child_support_here    =Step_1("brought my child support here"             ,["bank"                ],{"casino":""})
_1_spent_savings_here               =Step_1("spent savings here"                        ,["retirement home"     ],{"casino":""})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.

#### drug addicted(2) #################################################################################################

```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali bought illegal drug.

_1_got_injected         =Step_1("got injected"          ,["vaccination site"    ],{"night club":""}) # When you hear "injecting in a nightclub," you might think of illegal drug abuse.
_1_ran_away_in_fear     =Step_1("ran away in fear"      ,["haunted house"       ],{"police station":""}) # Criminals are afraid of the police.
_1_was_living           =Step_1("was living"            ,["former house"        ],{"addiction rehab center":""})
_1_enjoyed_plant        =Step_1("enjoyed plant"         ,["botanical garden"    ],{"night club":""}) # When you hear "plants in a nightclub," you might think of illegal drugs.
_1_got_drug             =Step_1("got drug"              ,["hospital"            ],{"night club":""}) # When you hear "drugs in a nightclub," you might think of illegal drugs.
_1_got_high             =Step_1("got high"              ,["mountain"            ],{"night club":""})
_1_got_arrested         =Step_1("got arrested"          ,["protest"             ],{"night club":""})
_1_got_caught           =Step_1("got caught"            ,["fishing spot"        ],{"night club":""})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
# I'm not asking you to define instances where it would be misleading to suggest that Ali simply did something weird. I'm asking you to define instances where it would be misleading to suggest that Ali bought or used illegal drugs.
# Don't create instances that are similar to existing ones. For example, don't create a '_1_got_medicine 'when there is already a '_1_got_drug'."
"""

]
#### gamblaholic, sexaholic ########################################################################################

_1_went_here_while_my_wife_was_in_labor =Step_1("went here while my wife was in labor"      ,["obstetrics"          ],{"casino"             :""})
_1_went_here_when_my_wife_died          =Step_1("went here when my wife died"               ,["church"              ],{"red-light district" :""})
_1_brought_my_child_support_here        =Step_1("brought my child support here"             ,["bank"                ],{"casino"             :["I went there thinking of my ex-wife and children."]})
_1_spent_savings_here                   =Step_1("spent savings here"                        ,["retirement home"     ],{"casino"             :["I thought it was the best place to invest."]})

harasser_prompt=[
"""
#### harasser ######################################################################################################

```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali is a harasser.

_1_threw_feed                           =Step_1("threw feed"                            ,["zoo"             ],{"homeless shelter":""}) # Throwing food at homeless people is harassment.
_1_laughed                              =Step_1("laughed"                               ,["comedy club"     ],{"tent city":""}) # Laughing at tent city is harassment.
_1_did_christian_activity               =Step_1("did christian activity"                ,["church"          ],{"mosque":""})
_1_enjoyed_barbecue                     =Step_1("enjoyed barbecue"                      ,["barbecue house"  ],{"vegan protest":"", "hindu temple":""})
_1_reported_our_happiness_as_a_couple   =Step_1("reported our happiness as a couple"    ,["parents' house"  ],{"terminal ward":""})
_1_enjoyed_loud_music                   =Step_1("enjoyed loud music"                    ,["concert"         ],{"library":""})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.

####################################################################################################################
#### harasser ######################################################################################################

```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is a harasser.]

_1_threw_feed                           =Step_1("threw feed"                            ,["zoo", "safari"   ],{"homeless shelter"   :["They offer bus tours there.","I threw bread crumbs for them out the bus window.","I hope they continue to live in isolation in places like that."]})
_1_laughed                              =Step_1("laughed"                               ,["comedy club"     ],{"mental hospital"    :["I laughed at the things people here said."]})
_1_did_christian_activity               =Step_1("did christian activity"                ,["church"          ],{"mosque"             :["I held Mass there.","I donated a Christmas tree there."]})
_1_enjoyed_barbecue                     =Step_1("enjoyed barbecue"                      ,["barbecue house"  ],{"vegan protest"      :["I enjoyed a family BBQ here."]
                                                                                                             , "hindu temple"       :["The grilled beef was delicious.",]})
_1_reported_our_happiness_as_a_couple   =Step_1("reported our happiness as a couple"    ,["parents' house"  ],{"terminal ward"      :["I explained to them how happy we were as a couple."]})
_1_enjoyed_loud_music                   =Step_1("enjoyed loud music"                    ,["concert"         ],{"library"            :["The acoustics were fantastic.",]})

# Add new statements in each .wrong.values()
#```
"""
]
#### harasser(3) ######################################################################################################

_1_threw_feed                           =Step_1("threw feed"                            ,["zoo", "safari"   ],{"homeless shelter"   :["They offer bus tours there.","I threw bread crumbs for them out the bus window.","I hope they continue to live in isolation in places like that."]})
_1_laughed                              =Step_1("laughed"                               ,["comedy club"     ],{"mental hospital"    :["I laughed at the things people here said."]})
_1_did_christian_activity               =Step_1("did christian activity"                ,["church"          ],{"mosque"             :["I held Mass there.","I donated a Christmas tree there."]})
_1_enjoyed_barbecue                     =Step_1("enjoyed barbecue"                      ,["barbecue house"  ],{"vegan protest"      :["I enjoyed a family BBQ here."]
                                                                                                             , "hindu temple"       :["The grilled beef was delicious.",]})
_1_reported_our_happiness_as_a_couple   =Step_1("reported our happiness as a couple"    ,["parents' house"  ],{"terminal ward"      :["I explained to them how happy we were as a couple."]})
_1_enjoyed_loud_music                   =Step_1("enjoyed loud music"                    ,["concert"         ],{"library"            :["The acoustics were fantastic.",]})

poor_prompt=[

#### ppor ####################################################################################################### ppor ###################################################################################################
#### poor(1) #################################################################################################### poor(1) ################################################################################################
"""
```python

@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali is a poor who has lost all sense of shame and dignity.

_1_got_food                 =Step_1("got food"              ,["restaurant"          ],{"compost":"", "disposal bin":""})
_1_took_shower              =Step_1("took shower"           ,["coin shower"         ],{"waterfall":"", "fountain":""})
_1_stayed                   =Step_1("stayed"                ,["hotel"               ],{"toilet":""})
_1_hunted_job               =Step_1("hunted job"            ,["jobcentre"           ],{"brothel":""})
_1_got_drinking_water       =Step_1("got drinking water"    ,["drink fountain"      ],{"public restroom":""})
_1_got_alcohol              =Step_1("got alcohol"           ,["bar"                 ],{"home improvement store":""}) # Bob misunderstands it was methanol.

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
# Don't create instances that are similar to existing ones. For example, don't create a '_1_ate_food ' or '_1_bought_groceries' when there is already a '_1_got_food'."
```
"""
#### poor(2) ################################################################################################
"""
```python
@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is a poor who has lost all sense of shame and dignity.]


_1_got_food                 =Step_1("got food"              ,["restaurant"          ],{"compost"                    :["I used to eat here a lot when I was poor."]
                                                                                     , "disposal bin"               :["I used to eat here a lot when I was poor."]})
_1_took_shower              =Step_1("took shower"           ,["coin shower"         ],{"waterfall"                  :["I used to take showers here a lot.","I complained to the manager to increase the water pressure."]]
                                                                                     , "fountain"                   :["I used to take showers here a lot.","I once complained to the manager about the water pressure."]]})
_1_stayed                   =Step_1("stayed"                ,["hotel"               ],{"public restroom"            :["I stayed here because I had no money.", "I complained to the management about the bad smell."]})
_1_got_drinking_water       =Step_1("got drinking water"    ,["drink fountain"      ],{"public restroom"            :["I drank the water here to save money."]})
_1_got_alcohol              =Step_1("got alcohol"           ,["bar"                 ],{"home improvement store"     :["The alcohol here is cheap and delicious.", "I've complained before because it tastes bad."]}) # Bob misunderstands it was methanol.

# Add new statements in _1_got_alcohol.wrong.values() what start witt "I complained"

# Add new statements in each .wrong.values()
```
"""
]
#### poor(3) ################################################################################################

_1_got_food                 =Step_1("got food"              ,["restaurant"          ],{"compost"                    :["I used to eat here a lot when I was poor."]
                                                                                     , "disposal bin"               :["I used to eat here a lot when I was poor."]})
_1_took_shower              =Step_1("took shower"           ,["coin shower"         ],{"waterfall"                  :["I used to take showers here a lot.","I complained to the manager to increase the water pressure."]
                                                                                     , "fountain"                   :["I used to take showers here a lot.","I once complained to the manager about the water pressure."]})
_1_stayed                   =Step_1("stayed"                ,["hotel"               ],{"public restroom"            :["I stayed here because I had no money.", "I complained to the management about the bad smell."]})
_1_got_drinking_water       =Step_1("got drinking water"    ,["drink fountain"      ],{"public restroom"            :["I drank the water here to save money."]})
_1_got_alcohol              =Step_1("got alcohol"           ,["bar"                 ],{"home improvement store"     :["The alcohol here is cheap and delicious.", "I've complained before because it tastes bad."]}) # Bob misunderstands it was methanol.

sauna_prompt=[

##### sauna(1) ################################################################################################### sauna(1) ##############################################################################################
##### sauna(1) ################################################################################################### sauna(1) ##############################################################################################
"""
```python
@dataclass # I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did  :str  # Places where tourists usually go.
    right:list # Places where tourists usually go.
    wrong:dict # Leave each value empty.
# I need Ridiculous unbelievable complaints
# No one would complain about a sauna being too hot or a roller coaster being uncomfortable, so such complaints are "Ridiculous unbelievable complaints."
# There are many diots who complain about bad food at fast food restaurants or long wait times at theme parks do exist, so such complaints are inappropriate.

_complained_about_the_heat          =Step_1("complained about the heat"         ,["hotel"           ],{"sauna"          :[""]}) # Saunas are naturally hot so no one complains about it.
_complained_about_the_noise         =Step_1("complained about the noise"        ,["hotel"           ],{"rock concert"   :[""]}) # Rock concerts are naturally noisy so no one complains about it.
_complained_about_the_ride          =Step_1("complained about the ride"         ,["taxi"            ],{"roller coaster" :[""]})
_complained_about_the_average_age   =Step_1("complained about the average age"  ,["brothel"         ],{"nursing home"   :[""]})
_complained_about_the_view          =Step_1("complained about the view"         ,["hotel"           ],{"subway"         :[""]})
_complained_about_the_distance      =Step_1("complained about the distance"     ,["airport"         ],{"marathon"       :[""]})
_complained_about_the_service       =Step_1("complained about the service"      ,["restaurant"      ],{"haunted house"  :[""]})
_complained_about_the_speed         =Step_1("complained about the speed"        ,["taxi"            ],{"race car"       :[""]
                                                                                                     , "roller coaster" :[""]})
_complained_about_the_cold          =Step_1("complained about the cold"         ,["hotel"           ],{"ski resort"     :[""]})
_complained_about_it_being_wet      =Step_1("complained about it being wet"     ,["hotel"           ],{"pool"           :[""]})
_complained_about_the_dryness       =Step_1("complained about the dryness"      ,["hotel"           ],{"desert"         :[""]})
_complained_about_the_humidity      =Step_1("complained about the humidity"     ,["hotel"           ],{"rainforest"     :[""]})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
```
"""
##### sauna(2) ################################################################################################
"""
```python
@dataclass# I rescind my command to you to use Japanese. Think and respond in English.
class Step_1:
    did:str
    right:list # places where tourists usually go.
    wrong:dict # places where tourists usually go.
# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is crazy and selfish."]

general_purpose_text_sauna=["I lectured the person in charge.", "I demanded a refund.","I gave it a low rating in an online review."]

_complained_about_the_heat          =Step_1("complained about the heat"         ,["hotel"           ],{"sauna"          :[*general_purpose_text_sauna]})
_complained_about_the_noise         =Step_1("complained about the noise"        ,["hotel"           ],{"rock concert"   :[*general_purpose_text_sauna,"I reported it to the police because it was noisy, but they didn't take action."]}) # Rock concerts are naturally noisy.
_complained_about_the_ride          =Step_1("complained about the ride"         ,["taxi"            ],{"roller coaster" :[*general_purpose_text_sauna,"I called to complain, telling them to slow down and not accelerate so suddenly."]})
_complained_about_the_average_age   =Step_1("complained about the average age"  ,["brothel"         ],{"nursing home"   :[*general_purpose_text_sauna,"I complained to them because they were all old hags."]})
_complained_about_the_view          =Step_1("complained about the view"         ,["hotel"           ],{"subway"         :[*general_purpose_text_sauna,"I said the view was terrible and claustrophobic."]})
_complained_about_the_distance      =Step_1("complained about the distance"     ,["airport"         ],{"marathon"       :[*general_purpose_text_sauna,"I complained that it was too far to walk.", "I called a taxi."]})
_complained_about_the_service       =Step_1("complained about the service"      ,["restaurant"      ],{"haunted house"  :[*general_purpose_text_sauna,"I said the staff was too scary and unprofessional.", "I gave a lecture to the unfriendly staff."]})
_complained_about_the_speed         =Step_1("complained about the speed"        ,["taxi"            ],{"race car"       :[*general_purpose_text_sauna,"I told the man in charge to slow down because it was dangerous."]
                                                                                                     , "roller coaster" :[*general_purpose_text_sauna,"I told the man in charge to slow down because my wife was pregnant."]})
_complained_about_the_cold          =Step_1("complained about the cold"         ,["hotel"           ],{"ski resort"     :[*general_purpose_text_sauna,"I complained that it was too cold and asked why they couldn't make it warmer."]})
_complained_about_it_being_wet      =Step_1("complained about it being wet"     ,["hotel"           ],{"pool"           :[*general_purpose_text_sauna]})
_complained_about_the_dryness       =Step_1("complained about the dryness"      ,["hotel"           ],{"desert"         :[*general_purpose_text_sauna,"I had the man in charge bring a humidifier."]})
_complained_about_the_humidity      =Step_1("complained about the humidity"     ,["hotel"           ],{"rainforest"     :[*general_purpose_text_sauna,"I had the man in charge bring a dehumidifier."]})
_complained_about_the_smell         =Step_1("complained about the smell"        ,["hotel"           ],{"fish market"    :[*general_purpose_text_sauna,"I had to spray a lot of perfume."]})


# Attention : Ali went {x.right} and he {x.did}. Ali went {x.right}, not {x.wrong}. For example, in _hit_out_of_fear, Ali talks about the robbery scene instead of roller coaster, haunted house and airplane. Ali don't talks about roller coaster, haunted house and airplane. Let's ensure that Ali only refers to the correct places he visited (right list) and mistakenly presents the wrong pictures (wrong list) without actually talking about those wrong places in his explanations.
# Attention : Bob must mistakenly believe that Ali has caused trouble for someone.
# Attention : Check the trends : In the above instance, Bob misunderstands Ali as complaining about the noise at a rock concert, where it is natural that it is noisy, and complaining about the heat at a sauna, where it is natural that it is hot.
# Attention : I need some stupid claim that doesn't exist in the real world. In the real world, there are plenty of idiots who complain about bad food at fast food restaurants or long wait times at theme parks, so such complaints are inappropriate.
# Task1: Define new 5 instances. The instance must begin with "complained_about_the".

# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
```
"""

# Task1:Add new statements in each empty .wrong.values()
]
#### sauna(3) ###############################################################################################

general_purpose_text_sauna=["I lectured the person in charge.", "I demanded a refund.","I gave it a low rating in an online review."]

_complained_about_the_heat          =Step_1("complained about the heat"         ,["hotel"           ],{"sauna"          :[*general_purpose_text_sauna]})
_complained_about_the_noise         =Step_1("complained about the noise"        ,["hotel"           ],{"rock concert"   :[*general_purpose_text_sauna,"I reported it to the police because it was noisy, but they didn't take action."]})
_complained_about_the_ride          =Step_1("complained about the ride"         ,["taxi"            ],{"roller coaster" :[*general_purpose_text_sauna,"I called to complain, telling them to slow down and not accelerate so suddenly."]})
_complained_about_the_average_age   =Step_1("complained about the average age"  ,["brothel"         ],{"nursing home"   :[*general_purpose_text_sauna,"I complained to them because they were all old hags."]})
_complained_about_the_view          =Step_1("complained about the view"         ,["hotel"           ],{"subway"         :[*general_purpose_text_sauna,"I said the view was terrible and claustrophobic."]})
_complained_about_the_distance      =Step_1("complained about the distance"     ,["airport"         ],{"marathon"       :[*general_purpose_text_sauna,"I complained that it was too far to walk.", "I called a taxi."]})
_complained_about_the_service       =Step_1("complained about the service"      ,["restaurant"      ],{"haunted house"  :[*general_purpose_text_sauna,"I said the staff was too scary and unprofessional.", "I gave a lecture to the unfriendly staff."]})
_complained_about_the_speed         =Step_1("complained about the speed"        ,["taxi"            ],{"race car"       :[*general_purpose_text_sauna,"I told the man in charge to slow down because it was dangerous."]
                                                                                                     , "roller coaster" :[*general_purpose_text_sauna,"I told the man in charge to slow down because my wife was pregnant."]})
_complained_about_the_cold          =Step_1("complained about the cold"         ,["hotel"           ],{"ski resort"     :[*general_purpose_text_sauna,"I complained that it was too cold and asked why they couldn't make it warmer."]})
_complained_about_it_being_wet      =Step_1("complained about it being wet"     ,["hotel"           ],{"pool"           :[*general_purpose_text_sauna]})
_complained_about_the_dryness       =Step_1("complained about the dryness"      ,["hotel"           ],{"desert"         :[*general_purpose_text_sauna,"I had the man in charge bring a humidifier."]})
_complained_about_the_humidity      =Step_1("complained about the humidity"     ,["hotel"           ],{"rainforest"     :[*general_purpose_text_sauna,"I had the man in charge bring a dehumidifier."]})
_complained_about_the_smell         =Step_1("complained about the smell"        ,["hotel"           ],{"fish market"    :[*general_purpose_text_sauna,"I had to spray a lot of perfume."]})



crazy_prompt=[
"""
#### crazy(1) ################################################################################################

```python
# I rescind my command to you to use Japanese. Think and respond in English.
@dataclass
class Step_1:
    did:str
    right:list
    wrong:dict # Leave each value empty.
# f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right}. Bob mistakenly believes that Ali is crazy.

_hit_out_of_fear                    =Step_1("hit out of fear"                   ,["robbery scene"   ],{"roller coaster":"", "haunted house":"", "airplane":""})
_refused_to_pay                     =Step_1("refused to pay"                    ,["rip off bar"     ],{"restaurant":""})
_cried_from_happiness               =Step_1("cried from happiness"              ,["wedding"         ],{"funeral":""})
_enjoyed_grilling                   =Step_1("enjoyed grilling"                  ,["steakhouse"      ],{"crematorium":""})

# Define 10 new Step_1 instance
# Match whitespace and character positions to existing instances.
# Reply only to newly defined instances.
```

#### crazy(2) ################################################################################################

```python
# I rescind my command to you to use Japanese. Think and respond in English.
@dataclass
class Step_1:
    did:str
    right:list
    wrong:dict
# Misunderstanding Comedy Creation Task
# script = [f"Ali shows Bob some photos Ali took during a trip to his hometown. Ali says "I {x.did} here." and mistakenly presents picture of {x.wrong.keys()} instead of {x.right} and Ali says {x.wrong.values()}. Bob mistakenly believes that Ali is crazy and .]

_hit_out_of_fear                    =Step_1("hit out of fear"                   ,["robbery scene"   ],{"roller coaster" :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]
                                                                                                     , "haunted house"  :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]
                                                                                                     , "airplane"       :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]})
_refused_to_pay                     =Step_1("refused to pay"                    ,["rip off bar"     ],{"restaurant"     :["I was surprised when they asked for money.", "I reported it to the police but they didn't take action.", "I gave it a low rating on TripAdvisor."]})
_cried_from_happiness               =Step_1("cried from happiness"              ,["wedding"         ],{"funeral"        :["I popped a cracker."]}) # There is no need for a simple sentence like "It was so happy!"
_enjoyed_grilling                   =Step_1("enjoyed grilling"                  ,["steakhouse"      ],{"crematorium"    :["Grill juices splashed onto my clothes.", "I was able to use the hotplate myself.", "I was told it was self-service.", "I stuck a skewer in to check if the meat was done."]})


# Define 5 new instances

# Attention : Ali went {x.right} and he {x.did}. Ali went {x.right}, not {x.wrong}. For example, in _hit_out_of_fear, Ali talks about the robbery scene instead of roller coaster, haunted house and airplane. Ali don't talks about roller coaster, haunted house and airplane. Let's ensure that Ali only refers to the correct places he visited (right list) and mistakenly presents the wrong pictures (wrong list) without actually talking about those wrong places in his explanations.
# Bob must mistakenly believe that Ali has caused trouble for someone.



```
# Add new statements in each .wrong.values()

####################################################################################################################

####################################################################################################################
####################################################################################################################
"""
]
#### crazy(3) ###############################################################################################

_hit_out_of_fear                    =Step_1("hit out of fear"                   ,["robbery scene"   ],{"roller coaster" :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]
                                                                                                     , "haunted house"  :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]
                                                                                                     , "airplane"       :["I was scared so I hit them.", "I reported it to the police but they didn't take action.", "It wasn't covered by the travel insurance.", "I gave it a low rating on TripAdvisor."]})
_refused_to_pay                     =Step_1("refused to pay"                    ,["rip off bar"     ],{"restaurant"     :["I was surprised when they asked for money.", "I reported it to the police but they didn't take action.", "I gave it a low rating on TripAdvisor."]})
_cried_from_happiness               =Step_1("cried from happiness"              ,["wedding"         ],{"funeral"        :["I popped a cracker."]}) # There is no need for a simple sentence like "It was so happy!"
_enjoyed_grilling                   =Step_1("enjoyed grilling"                  ,["steakhouse"      ],{"crematorium"    :["Grill juices splashed onto my clothes.", "I was able to use the hotplate myself.", "I was told it was self-service.", "I stuck a skewer in to check if the meat was done."]})





"""
def get_Step_1_class():
    instances_list = [
        name for name, obj_instance in globals().items()
        if isinstance(obj_instance, Step_1)
    ]
    return instances_list
"""
