from dataclasses import dataclass, field
from typing import List, ClassVar

###################################################################################################################################################################################
###################################################################################################################################################################################
@dataclass
class Ivw:
    ALL_Ivw: ClassVar[List['Ivw']] = []
    ivw_name:str

    tight:str
    loose:str
    insert:str
    pull_out:str
    noise:str

    second_hand:str
    leave_forget:str
    lend:str
    gift:str
    child_use:str # if it's ok to children use it -> "o", if not ok -> "n"

    disposable:str
    paid_item:str
    share:str
    outdoor_use:str
    have_multiple:str

    line:list
    def __post_init__(self):
        Ivw.ALL_Ivw.append(self)
        if self.ivw_name:
            self.line.extend(["{(*)}"])
        if self.tight:
            self.line.extend(["It's too tight."])
        if self.loose:
            self.line.extend(["It's too loose."])
        if self.insert:
            self.line.extend(["It's hard to (insert/ get in).",  "I really have to push to make it fit.", "Sometimes I need to twist and turn just to get it in."])
        if self.pull_out:
            self.line.extend(["It's hard to (pull out/ get out)."])
        if self.noise:
            self.line.extend(["When I use it, it's too noisy."])
        if self.second_hand:
            self.line.extend(["It's second hand.", "I wonder how many people have used it before me.", "This is a hand-me-down from my older brother."])
        if self.leave_forget:
            self.line.extend(["I left it at a friend's house.", "I hope they remember to give it back.", "It's far away so it's a hassle to go and get it."])
        if self.lend:
            self.line.extend(["I often lend it to my siblings.", "Want to borrow it?"])
        if self.gift:
            self.line.extend(["I got it as a gift.", "I'm thinking of giving it as a present to my father.", "I want to send it to a friend overseas, but will it be ok through customs?"])
        if self.child_use == "o":
            self.line.extend(["I've been using this since I was a child."])
        elif self.child_use == "n":
            self.line.extend(["My child used it without permission, so I scolded him and told him to wait until he grew up."])
        if self.disposable:
            self.line.extend(["Normally you use this once and then throw it away, right?", "It's so convenient for quick use, but I feel guilty throwing it out."])
        if self.paid_item:
            self.line.extend(["I bought this from a Chinese vendor so it was cheap.", "It was very cheap."])
        if self.share:
            self.line.extend(["I scolded my kids to share this together.", "My son uses it all the time, so I scolded him to use it in moderation.", "They always fight over who gets to use it first!"])
        if self.outdoor_use:
            self.line.extend(["I fell when using it on the stairs at the station."])
        if self.have_multiple:
            self.line.extend(["This is my fourth one.", "I don't need one, do you want one?", "I keep losing track of how many I have."])
# This class is for creating misunderstanding comedy. Ali talks about inanimate. Bob mistakenly believes that Ali is talking about his girlfriend. Ali utteres lines in those class. Bob mistakes Ali for a pervert.

fridge          =Ivw("fridge"        , "y","" ,"y","y","y", "y","" ,"y","y","o", "" ,"y","y","" ,"y",["I often put lasagna in it.", "Larger vegetables won't fit inside."])
baseball_glove  =Ivw("baseball_glove", "y","y","y","y","" , "y","y","y","y","o", "" ,"y","y","y","y",["It was a bit tight at first, but with use it came to fit the shape of my hand.", "This is for practice. I use a different one for the real thing."])
car             =Ivw("car"           , "y","y","y","y","y", "y","y","y","y","n", "" ,"y","y","y","y",["Sometimes it's very hot inside.","It's too small for four people.", "The other day I accidentally put in high octane gasoline in it.", "It's a comfortable ride."])
mailbox         =Ivw("mailbox"       , "y","" ,"y","y","" , "" ,"" ,"" ,"" ,"o", "" ,"" ,"" ,"y","" ,["I always check what's inside every morning.", "Sometimes I check inside and get disappointed when there's nothing there.", "I complained because the postman forcefully screwed letters inside.", "I have to empty it frequently. I found the tax deduction documents at the very back."])
water_bottle    =Ivw("water_bottle"  , "y","" ,"y","" ,"y", "", "y","" ,"y","o", "" ,"y","" ,"y","y",["Sometimes it leaks if I don't close the cap properly.", "Apparently you can't put carbonated drinks in this."])
iqos            =Ivw("iqos"          , "" ,"" ,"y","y","" , "y","y","y","y","n", "" ,"y","y","y","y",["Sometimes it's very hot inside.","It's hard to insert a cigarette in this."])
bed             =Ivw("bed"           , "y","" ,"y","" ,"y", "y","" ,"y","y","o", "" ,"y","y","" ,"y",["I really don't want to get out of it.", "Socks came out from the back."])
socks           =Ivw("socks"         , "y","y","y","y","" , "" ,"y","" ,"y","o", "" ,"y","" ,"y","y",["I often lose this in gaps in the bed and other places."])
pot             =Ivw("pot"           , "y","" ,"y","" ,"y", "y","" ,"y","y","o", "" ,"y","y","" ,"y",["Larger vegetables won't fit inside."])


# define shoes instance.  Please only reply to newly defined instance. Align text and whitespace with existing instances.
# .line requires lines about "how to get", "how to break" and "how to use"



#### Add new lines in each .line  Please only reply to newly added lines.

###################################################################################################################################################################################

# lists below is for creating misunderstanding comedy. Ali talks about his girlfriend. Bob mistakenly believes that Ali is talking about inanimate. Ali utteres lines in this list. Bob mistakes Ali for a pervert.
# Bob responds each line "It's because she is not human."
# Each line has to contain "for some reason" or speculation for the reason.
# Add new lines in Wvi_law

Wvi_dict={
"sex"             : [ # Lines about sex.
    "For some reason, she can't get pregnant. I took her to the obstetrician-gynaecologist but they couldn't figure out the cause.","We haven't had sex lately. I think she might be asexual or lesbian.", "I think she's not into me, she never initiates it.", "I don't feel sexually attracted to her, I think I'm gay or have erectile dysfunction."
    ],
"took_her"        : [ # Ali took "her" to somewhere.
    "For some reason, My parents were against our marriage.", "The mixed bathing area had a bad clientele, we were stared at a lot.", "People stare at her on the beach. Damn perverts.", "People keep staring at us when we're out in the collage, I think it's because of her short skirt.", "For some reason, my tennis buddies don't like her. I think it's because of her skin color.", "For some reason, we got kicked out of the restaurant. I thought it was because of our table manners."
    ],
"communication"   : [ # Lines about communication.
    "For some reason, She hasn't said much lately.", "For some reason, she didn't react to my gift.", "I think she's not listening to me, she never responds to my texts."
    ],
"law"             : [ # Lines related law
    "The police stop us often, I think because she's not white.", "She's not allowed in the bar sometimes. I think it's because of she looks young."
    ],
    }

###################################################################################################################################################################################
###################################################################################################################################################################################
Avh_dict={# Ali is talking about a dog. Bob mistakenly thinks Ali is talking about Ali's wife's father. Add new 20 Ali's lines like below, that would be funny in this situation. start answer with ```python
"pervert"       : [
    "He licks my face.","He follows me into the shower and watches me with those big eyes.","He eats his poop.","He has his own bed, but he prefers my daughter's one.","He always tries to sneak into bed with me at night.","He tries to sneak into the bathroom when I shower.","He fucked other's dog at a pet hotel.","He likes being on a lead.","When I put him on a lead he gets excited.","He fucks others' pets.","He sleeps with me.","He likes to have his head stroked.","He gets jealous if I pet anyone else.","He sniffs everyone's crotch."
    ],
"abuse"         : [
    "I put him in a crate when I leave the house.","He's a mongrel.","He was part of a pack of wild dogs.","I’ve tried multiple brands of dog food, but he only wants human foods.","I bought him for 50 dollars.","I have to give him a bath every month.","I have to take him to the vet for check-ups.","I often scold him for wanting human food.","I bought him for 50 dollars.","As a result of stress, His weight now is 10kg.","As a result of dieting, His weight now is 10kg.","He fucked other's dog at a pet hotel.","He hates being on a lead.","He hates dog food.",""
    ],
"idiot"         : [
    "He poops everywhere.","He eats his poop.","He loves to dig through the trash for 'treats'.","He gets scared of his own shadow.","He runs around in circles when he's excited.","He always begs for scraps at the dinner table.","He likes dog food.","He doesn't remember the toilet.","He barks at strangers.","He marks his territory everywhere by peeing." ,"He recently learned to use the toilet.","I often scold him for wanting human food."
    ],
    }

# I wonder why.
# Is he feeling a little stressed?

###################################################################################################################################################################################

Hva_dict={ # Add new items in all value. Just mimic the existing items.
"sex"               : [
    "My mother seems to have not had sex with him lately.", "They don't seem to be sexually compatible."
    ],
"unhealthy"         : [
    "He likes whiskey.","I'm telling him to cut down on smoking."
    ],
"illiteracy"        : [ # Each item has to contain "often" XOR "He's an idiot" XOR "can barely"
    "I often win to him at chess.","He's an idiot and can only drive automatic cars.","He's an idiot, so he graduated from a correspondence university in Samoa or somewhere.", "He can barely read the instructions on a simple board game.", "He's an idiot and can barely write his own name."
    ],
"discrimination"    : [ # Each item has to contain "probably because"
    "I tried to go into a restaurant with him and was stopped, probably because he wasn't white.", "They were denied entry to the club, probably because we aren't wearing tie.", "She was overlooked for the job, probably because of she's woman.", "She is opposed to the marriage, probably because of she's not white.", "They were treated poorly at the store, probably because they looked different."
    ],
    }


###################################################################################################################################################################################
###################################################################################################################################################################################

