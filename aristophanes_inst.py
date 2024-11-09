from dataclasses import dataclass, field
from typing import List, ClassVar

###################################################################################################################################################################################
###################################################################################################################################################################################
@dataclass
class Ivw:
    ALL_IVW: ClassVar[List['Ivw']] = []
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
        Ivw.ALL_IVW.append(self)
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
            self.line.extend(["It's second hand.", "I wonder how many people have used it before me.", "This is a hand-me-down from my older brother.", "It's a bit worn, but it still does the job."])
        if self.leave_forget:
            self.line.extend(["I left it at a friend's house.", "I hope they remember to give it back.", "It's far away so it's a hassle to go and get it."])
        if self.lend:
            self.line.extend(["I often lend it to my siblings.", "Want to borrow it?", "I make sure to clean it thoroughly before and after lending it."])
        if self.gift:
            self.line.extend(["I got it as a gift.", "I'm thinking of giving it as a present to my father.", "I want to send it to a friend overseas, but will it be ok through customs?", "Certainly this is a bit unsuitable for a gift."])
        if self.child_use == "o":
            self.line.extend(["I've been using this since I was a child."])
        elif self.child_use == "n":
            self.line.extend(["My child used it without permission, so I scolded him and told him to wait until he grew up.", "It's too dangerous for children to use unsupervised.", "I'll teach them how to use it properly when they're older."])
        if self.disposable:
            self.line.extend(["Normally you use this once and then throw it away, right?", "It's so convenient for quick use, but I feel guilty throwing it out.", "Sometimes I clean it and use it again, even though you're not supposed to."])
        if self.paid_item:
            self.line.extend(["I bought this from a Chinese vendor so it was cheap.", "It was very cheap."])
        if self.share:
            self.line.extend(["I scolded my kids to share this together.", "My son uses it all the time, so I scolded him to use it in moderation.", "They always fight over who gets to use it first.", "Sharing it has caused some hygiene concerns.", "I'm thinking of getting one for each family member to avoid conflicts."])
        if self.outdoor_use:
            self.line.extend(["I fell when using it on the stairs at the station."])
        if self.have_multiple:
            self.line.extend(["This is my fourth one.", "I don't need one, do you want one?", "I keep losing track of how many I have.", "I like to have spares in case one breaks.", "I have different sizes for different occasions.", "I like to have spares in case one breaks."])
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
# The last attribute ".line" requires lines about "how to get", "how to break" and "how to use"

#### Add new lines in each if sentences.  Please only reply to newly added lines.


#### Add new lines in each .line  Please only reply to newly added lines.

# a bit
# properly
# for some reason
###################################################################################################################################################################################

# dict below is for creating misunderstanding comedy. Ali talks about his girlfriend. Bob mistakenly believes that Ali is talking about inanimate. Ali utteres lines in this dict. Bob mistakes Ali for a pervert.
# Bob responds to each line with "It's because she is not human."
# Each line has to contain "for some reason" or "a bit" or "properly" or speculation for the reason.
# Add new lines in each value without any explanations. start answer with ```python

Wvi_dict={
"communication"   : [ # Lines about communication.
    "For some reason, She hasn't said much lately.", "For some reason, she didn't react to my gift.", "I think she's not listening to me, she never responds to my texts.", "For some reason, she hasn't been eating much lately."
    ],
"sex"             : [ # Lines about sex.
    "For some reason, she can't get pregnant. I took her to the obstetrician-gynaecologist but they couldn't figure out the cause.","We don't seem to be sexually compatible.", "She complains about my lack of interest in intimacy.","We haven't had sex lately. I think she might be asexual or lesbian.", "I think she's not into me, she never initiates it.", "I don't feel sexually attracted to her, I think I'm gay or have erectile dysfunction."
    ],
"took_her"        : [ # Ali took "her" to somewhere.
    "For some reason, My parents were against our marriage.", "The mixed bathing area had a bad clientele, we were stared at a lot.", "People stare at her on the beach. Damn perverts.", "People keep staring at us when we're out in the collage, I think it's because of her short skirt.", "For some reason, my tennis buddies don't like her. I think it's because of her skin color.", "For some reason, we got kicked out of the restaurant. I thought it was because of our table manners."
    ],
"law"             : [ # Lines related law. Its value will be copied by Hva_dict["law"]
    "The police stop us often, I think because she's not white.", "She's not allowed in the bar sometimes. I think it's because of she looks young.", "The judge wouldn't let her testify. I suspect it's because she can't speak clearly.", "We got in trouble at the airport because she couldn't go through the metal detector properly.",    "I tried to go into a restaurant with him and was stopped, probably because he wasn't white.", "They were denied entry to the club, probably because we aren't wearing tie.", "She was overlooked for the job, probably because of she's woman.", "We're opposed to the marriage, probably because of she's not white.", "We were treated poorly at the store, probably because she looked different."
    ],
    }

###################################################################################################################################################################################
###################################################################################################################################################################################
Avh_dict={
# dict below is for creating misunderstanding comedy. Ali talks about a dog. Bob mistakenly believes that Ali is talking about Ali's wife's father.  Ali utteres lines in this dict. Bob mistakes Ali for a pervert.
# Add new lines in each value without any explanations. start answer with ```python

"pervert"       : [
    "He licks my face.","He follows me into the shower and watches me with those big eyes.","He eats his poop.","He licks my leg.","He loves it when I scratch behind his ears.","He gets really excited when I come home and jumps all over me.","He has his own bed, but he prefers my daughter's one.","He always tries to sneak into bed with me at night.","He tries to sneak into the bathroom when I shower.","He fucked other's dog at a pet hotel.","He likes being on a lead.","When I put him on a lead he gets excited.","He fucks others' pets.","He sleeps with me.","He likes to have his head stroked.","He gets jealous if I pet anyone else.","He sniffs everyone's crotch."
    ],
"abuse"         : [
    "I put him in a crate when I leave the house.","He's a mongrel.","He was part of a pack of wild dogs.","I had to get him neutered last month.", "I make him sleep outside when he misbehaves.","I’ve tried multiple brands of dog food, but he only wants human foods.","I bought him for 50 dollars.","I have to give him a bath every month.","I have to take him to the vet for check-ups.","I often scold him for wanting human food.","I bought him for 50 dollars.","As a result of stress, His weight now is 10kg.","As a result of dieting, His weight now is 10kg.","He fucked other's dog at a pet hotel.","He hates being on a lead.","He hates dog food.",""
    ],
"idiot"         : [
    "He poops everywhere.","He eats his poop.","He loves to dig through the trash for 'treats'.","He gets scared of his own shadow.","He runs around in circles when he's excited.","He always begs for scraps at the dinner table.","He likes dog food.","He doesn't remember the toilet.","He barks at strangers.","He marks his territory everywhere by peeing." ,"He recently learned to use the toilet.","I often scold him for wanting human food."
    ],
    }

#"gp_phrase"     : [
#    "for some reason,", "Is he feeling a little stressed?", "This seems a bit sad.", "properly"
#    ]


###################################################################################################################################################################################

Hva_dict={ # Add new items in all value. Just mimic the existing items. start answer with ```python
"unhealthy"         : [
    "He likes whiskey.","I'm telling him to cut down on smoking."
    ],
"illiteracy"        : [ # Each item has to contain "often" XOR "He's an idiot" XOR "can barely"
    "I often win to him at chess.","He's an idiot and can only drive automatic cars.","He's an idiot, so he graduated from a correspondence university in Samoa or somewhere.", "He can barely read the instructions on a simple board game.", "He's an idiot and can barely write his own name."
    ],
"sex"        : Wvi_dict["sex"]# When getting the value of dict2 into the value of dict1, the value of dict1 cannot be of list type.
,"took_her"  : Wvi_dict["took_her"]
,"law"       : Wvi_dict["law"]
    }

###################################################################################################################################################################################
###################################################################################################################################################################################

@dataclass
class Eve:
    ALL_EVE: ClassVar[List['Eve']] = []
    eve_name:str

    commonlyusedbytourists:str
    animal:str
    kids_olds_adult:str
    holy_unholy:str
    serious:str
    food:str

    fire:str
    water:str
    weak:str
    amusement_entertainment:str
    retail:str
    bankrupt:str

    paid:str
    accommodation:str
    dirty:str
    physicalcontact:str
    photospot:str

    outdoor_building_vehicle_machine:str
    educational:str
    sad:str
    pickupspot:str
    justaway:str

    shining_dark_both:str
    hot_cold:str
    dry_moist:str
    quiet_noisy:str         # Should be quiet or commonly be noisy
    relax:str
    sexual_gore_both:str
    fear:str

    def __post_init__(self):
        Eve.ALL_EVE.append(self)

butcher         =Eve("butcher"          ,"y","y","" ,"" ,"" ,"y", "y","" ,"" ,"" ,"y","" , "y","" ,"" , "" ,"" ,"b", "" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" )
cremator        =Eve("cremator"         ,"" ,"" ,"" ,"h","y","" , "y","" ,"" ,"" ,"" ,"" , "y","" ,"" , "" ,"" ,"b", "" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y")
safari          =Eve("safari"           ,"y","y","" ,"" ,"" ,"" , "" ,"" ,"" ,"e","" ,"" , "y","" ,"" , "" ,"y","o", "y","" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" )
tent_city       =Eve("tent_city"        ,"" ,"" ,"a","u","y","" , "" ,"" ,"y","" ,"" ,"" , "" ,"y","y", "" ,"" ,"o", "" ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" )
graveyard       =Eve("graveyard"        ,"" ,"" ,"" ,"h","y","" , "" ,"" ,"" ,"" ,"" ,"" , "" ,"" ,"" , "" ,"" ,"o", "" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y")
strip_club      =Eve("strip_club"       ,"y","" ,"a","u","" ,"" , "" ,"" ,"" ,"e","" ,"" , "y","" ,"" , "" ,"" ,"b", "" ,"" ,"" ,"" , "b","" ,"" ,"n","" ,"s","" )
mental_hospital =Eve("mental_hospital"  ,"" ,"" ,"" ,"h","y","" , "" ,"" ,"y","" ,"" ,"" , "y","y","" , "" ,"" ,"b", "" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y")
comedy_club     =Eve("comedy_club"      ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"e","" ,"" , "y","" ,"" , "" ,"y","b", "" ,"" ,"" ,"" , "" ,"" ,"" ,"n","" ,"b","" )
roller_coaster  =Eve("roller_coaster"   ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "" ,"" ,"v", "" ,"" ,"" ,"y", "" ,"" ,"" ,"n","" ,"" ,"y")
taxi            =Eve("taxi"             ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "y","" ,"" , "" ,"" ,"v", "" ,"" ,"" ,"" , "" ,"" ,"" ,"q","y","" ,"" )
kindergarten    =Eve("kindergarten"     ,"" ,"" ,"k","" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "y","" ,"" , "" ,"" ,"b", "y","" ,"" ,"" , "" ,"" ,"" ,"n","" ,"" ,"" )
night_club      =Eve("night_club"       ,"y","" ,"a","u","" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "" ,"y","b", "" ,"" ,"y","" , "b","" ,"" ,"n","" ,"" ,"" )
escape_room     =Eve("escape_room"      ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "" ,"" ,"m", "" ,"" ,"" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" )
hotel           =Eve("hotel"            ,"y","" ,"" ,"" ,"" ,"y", "" ,"" ,"" ,"" ,"" ,"" , "y","y","" , "" ,"" ,"b", "" ,"" ,"" ,"" , "" ,"" ,"" ,"q","y","" ,"" )#
terminal_ward   =Eve("terminal_ward"    ,"" ,"" ,"" ,"h","y","" , "" ,"" ,"y","" ,"" ,"" , "y","y","" , "" ,"" ,"b", "" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y")
casino          =Eve("casino"           ,"y","" ,"a","u","" ,"" , "" ,"" ,"" ,"a","" ,"y", "y","" ,"" , "" ,"" ,"b", "" ,"" ,"" ,"" , "" ,"" ,"" ,"n","" ,"" ,"y")
fire_scene      =Eve("fire_scene"       ,"" ,"" ,"" ,"" ,"y","" , "y","" ,"y","" ,"" ,"" , "" ,"" ,"" , "" ,"" ,"b", "" ,"y","" ,"y", "s","h","" ,"n","" ,"g","y")
flood_scene     =Eve("flood_scene"      ,"" ,"" ,"" ,"" ,"y","" , "" ,"y","y","" ,"" ,"" , "" ,"" ,"" , "" ,"" ,"o", "" ,"y","" ,"y", "" ,"" ,"" ,"n","" ,"g","y")
beach           =Eve("beach"            ,"y","" ,"" ,"" ,"" ,"" , "" ,"y","" ,"a","" ,"" , "" ,"" ,"" , "" ,"y","o", "" ,"" ,"y","" , "s","h","" ,"n","y","" ,"" )
sauna           =Eve("sauna"            ,"y","" ,"a","" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "" ,"" ,"b", "" ,"" ,"" ,"y", "" ,"h","m","" ,"y","" ,"" )
library         =Eve("library"          ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "" ,"" ,"" , "" ,"" ,"b", "y","" ,"" ,"" , "" ,"" ,"" ,"q","y","b","" )
ski_area        =Eve("ski_area"         ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "" ,"y","o", "" ,"" ,"y","" , "" ,"c","m","n","" ,"" ,"" )
massage_clinic  =Eve("massage_clinic"   ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "y","" ,"b", "" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" )
brothel         =Eve("brothel"          ,"y","" ,"a","u","" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "y","" ,"b", "" ,"" ,"" ,"" , "d","" ,"" ,"n","" ,"s","" )
orphanage       =Eve("orphanage"        ,"" ,"" ,"k","" ,"y","" , "" ,"" ,"y","" ,"" ,"" , "" ,"y","" , "" ,"" ,"b", "" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" )
desert          =Eve("desert"           ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "" ,"" ,"" , "" ,"y","o", "" ,"" ,"" ,"" , "s","h","d","" ,"" ,"" ,"" )
jungle          =Eve("jungle"           ,"y","y","" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "" ,"" ,"" , "" ,"y","o", "" ,"" ,"" ,"" , "d","h","m","" ,"" ,"" ,"" )
rock_concert    =Eve("rock_concert"     ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"e","" ,"" , "y","" ,"" , "" ,"y","b", "" ,"" ,"y","" , "b","" ,"" ,"n","" ,"b","" )
punching_machine=Eve("punching_machine" ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"a","" ,"" , "y","" ,"" , "y","" ,"m", "" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" )
dumpyard        =Eve("dumpyard"         ,"" ,"" ,"" ,"u","" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "" ,"" ,"y", "" ,"" ,"o", "" ,"" ,"" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" )
airplane        =Eve("airplane"         ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "y","" ,"y", "" ,"" ,"v", "" ,"" ,"" ,"" , "" ,"" ,"" ,"q","y","" ,"" )
train           =Eve("train"            ,"y","" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" , "y","" ,"y", "" ,"" ,"v", "" ,"" ,"" ,"" , "" ,"" ,"" ,"q","y","" ,"" )


def eve_func():

    def eve_func_tablize(table_name, place, line):
        eve_func_tablize_result=f"""
        <table>
        <tr><th colspan="2" id="th_cyan">{table_name}</th></tr>
        <tr><th>ali_place</th><td>{place[0]}</th></tr>
        <tr><th>bob_place</th><td>{place[1]}</th></tr>
        <tr><th>ali_line</th><td>{line[0]}</th></tr>
        <tr><th>bob_line</th><td>{line[1]}</th></tr>
        </table>
        """
        return eve_func_tablize_result

    place_0_1  = { # [0] is Ali's. [1] is Bob's.
        'place_photospot'         : ([], []),
        'place_justaway'          : ([], []),
        'place_sexual'            : ([], []),
        'place_bankrupt'          : ([], []),
        'place_retail'            : ([], []),
        'place_fire'              : ([], []),
        'place_water'             : ([], []),
        'place_shining_dark_both' : ([], []),
        'place_hot_cold'          : ([], []),
        'place_dry_moist'         : ([], []),
        'place_quiet_noisy'       : ([], []),
        'place_building_outdoor'  : ([], []),
        'place_sexual_gore_both'  : ([], []),
        'place_fear'              : ([], []),
        'place_animal'            : ([], []),
        'place_kids'              : ([], []),
        'place_pickupspot'        : ([], []),
        'place_worked'            : ([], []),
        'place_food'              : ([], [])
    }




    for i in Eve.ALL_EVE:
        if  not i.sexual_gore_both and i.photospot: # ['safari', 'night_club', 'beach', 'ski_area', 'desert', 'jungle']
            place_0_1['place_photospot'][0].append(f"{i.eve_name}")
        elif    i.sexual_gore_both and not i.photospot: # ['strip_club', 'fire_scene', 'flood_scene', 'library', 'brothel']
            place_0_1['place_photospot'][1].append(f"{i.eve_name}")
        if       i.accommodation and not i.serious: # ['hotel']
            place_0_1['place_justaway'][0].append(f"{i.eve_name}")
        elif     i.justaway: # ['tent_city', 'roller_coaster', 'escape_room', 'fire_scene', 'flood_scene', 'sauna', 'dumpyard']
            place_0_1['place_justaway'][1].append(f"{i.eve_name}")
        if       i.sexual_gore_both == "s": # ['strip_club', 'brothel']
            place_0_1['place_sexual'][0].append(f"{i.eve_name}")
        elif not i.sexual_gore_both == "s" and i.amusement_entertainment: #['safari', 'comedy_club', 'roller_coaster', 'night_club', 'escape_room', 'casino', 'beach', 'sauna', 'library', 'ski_area', 'massage_clinic', 'rock_concert', 'punching_machine']
            place_0_1['place_sexual'][1].append(f"{i.eve_name}")
        if       i.paid and     i.bankrupt: # ['casino']
            place_0_1['place_bankrupt'][0].append(f"{i.eve_name}")
        elif     i.paid and not i.bankrupt: # ['butcher', 'cremator', 'safari', 'strip_club', 'mental_hospital', 'comedy_club', 'roller_coaster', 'taxi', 'kindergarten', 'night_club', 'escape_room', 'hotel', 'terminal_ward', 'sauna', 'ski_area', 'massage_clinic', 'brothel', 'rock_concert', 'punching_machine', 'airplane', 'train']
            place_0_1['place_bankrupt'][1].append(f"{i.eve_name}")
        if       i.retail: # ['butcher']
            place_0_1['place_retail'][0].append(f"{i.eve_name}")
        elif not i.retail and (i.animal or i.kids_olds_adult == "k"): # ['safari', 'kindergarten', 'orphanage', 'jungle']
            place_0_1['place_retail'][1].append(f"{i.eve_name}")
        if       i.fire  and not  i.serious:# ['butcher']
            place_0_1['place_fire'][0].append(f"{i.eve_name}")
        elif     i.fire  and      i.serious:# ['cremator', 'fire_scene']
            place_0_1['place_fire'][1].append(f"{i.eve_name}")
        if       i.water and not i.serious: # ['beach']
            place_0_1['place_water'][0].append(f"{i.eve_name}")
        elif     i.water and     i.serious: # ['flood_scene']
            place_0_1['place_water'][1].append(f"{i.eve_name}")
        if   not i.shining_dark_both and i.relax: # ['taxi', 'hotel', 'sauna', 'library', 'airplane', 'train']
            place_0_1['place_shining_dark_both'][0].append(f"{i.eve_name}")
        elif     i.shining_dark_both: # ['strip_club', 'night_club', 'fire_scene', 'beach', 'brothel', 'desert', 'jungle', 'rock_concert']
            place_0_1['place_shining_dark_both'][1].append(f"{i.eve_name}")
        if   not i.hot_cold and i.relax: # ['taxi', 'hotel', 'library', 'airplane', 'train']
            place_0_1['place_hot_cold'][0].append(f"{i.eve_name}")
        elif     i.hot_cold:             # ['fire_scene', 'beach', 'sauna', 'ski_area', 'desert', 'jungle']
            place_0_1['place_hot_cold'][1].append(f"{i.eve_name}")
        if   not i.dry_moist and i.relax: # ['taxi', 'hotel', 'beach', 'sauna', 'library', 'airplane', 'train']
            place_0_1['place_dry_moist'][0].append(f"{i.eve_name}")
        elif     i.dry_moist:
            place_0_1['place_dry_moist'][1].append(f"{i.eve_name}")
        if       i.quiet_noisy == "q":                      # library, train
            place_0_1['place_quiet_noisy'][0].append(f"{i.eve_name}")
        elif     i.quiet_noisy == "n":                      # ['strip_club', 'comedy_club', 'roller_coaster', 'kindergarten', 'night_club', 'casino', 'fire_scene', 'flood_scene', 'beach', 'ski_area', 'brothel', 'rock_concert']
            place_0_1['place_quiet_noisy'][1].append(f"{i.eve_name}")
        if       i.outdoor_building_vehicle_machine == "b" and i.relax:     # ['hotel', 'sauna', 'library']
            place_0_1['place_building_outdoor'][0].append(f"{i.eve_name}")
        elif     (i.outdoor_building_vehicle_machine == "o" or i.dirty) and not i.relax or i.water: # ['safari', 'tent_city', 'graveyard', 'flood_scene', 'ski_area', 'desert', 'jungle', 'dumpyard']
            place_0_1['place_building_outdoor'][1].append(f"{i.eve_name}")
        if       i.sexual_gore_both and not i.kids_olds_adult == "a" and i.commonlyusedbytourists: # ['comedy_club', 'library', 'rock_concert']
            place_0_1['place_sexual_gore_both'][0].append(f"{i.eve_name}")
        elif     i.sexual_gore_both and not i.kids_olds_adult == "k": # ['strip_club', 'fire_scene', 'flood_scene', 'brothel']
            place_0_1['place_sexual_gore_both'][1].append(f"{i.eve_name}")
        if       i.fear and     i.amusement_entertainment:
            place_0_1['place_fear'][0].append(f"{i.eve_name}")
        elif     i.fear and not i.amusement_entertainment:
            place_0_1['place_fear'][1].append(f"{i.eve_name}")
        if       (i.animal or     i.amusement_entertainment == "e") and not i.food: # ['safari', 'strip_club', 'comedy_club', 'jungle', 'rock_concert']
            place_0_1['place_animal'][0].append(f"{i.eve_name}")
        elif     (i.weak or i.sad ) and not i.amusement_entertainment: # ['cremator', 'tent_city', 'graveyard', 'mental_hospital', 'terminal_ward', 'fire_scene', 'flood_scene', 'orphanage']
            place_0_1['place_animal'][1].append(f"{i.eve_name}")
        if       (i.kids_olds_adult == "k" or not i.kids_olds_adult == "a") and i.amusement_entertainment: # ['safari', 'comedy_club', 'roller_coaster', 'escape_room', 'beach', 'library', 'ski_area', 'massage_clinic', 'rock_concert', 'punching_machine']
            place_0_1['place_kids'][0].append(f"{i.eve_name}")
        elif     i.sexual_gore_both == "s" or (i.holy_unholy == "u" and i.amusement_entertainment): # ['strip_club', 'night_club', 'casino', 'brothel']
            place_0_1['place_kids'][1].append(f"{i.eve_name}")
        if       i.pickupspot: # ['night_club', 'beach', 'ski_area', 'rock_concert']
            place_0_1['place_pickupspot'][0].append(f"{i.eve_name}")
        elif     i.kids_olds_adult == "k": # ['kindergarten', 'orphanage']
            place_0_1['place_pickupspot'][1].append(f"{i.eve_name}")
        if        i.paid and not i.sexual_gore_both and not i.holy_unholy == "u" and not i.fear and i.outdoor_building_vehicle_machine == "b": # ['butcher', 'kindergarten', 'hotel', 'sauna', 'massage_clinic']
            place_0_1['place_worked'][0].append(f"{i.eve_name}")
        elif      i.sexual_gore_both == "s": # ['strip_club', 'brothel']
            place_0_1['place_worked'][1].append(f"{i.eve_name}")
        if        i.food:
            place_0_1['place_food'][0].append(f"{i.eve_name}")
        elif  not i.food and i.animal:
            place_0_1['place_food'][1].append(f"{i.eve_name}")

    line_photospot          =[["ali_line_photospot"]
                              ,["b"]
                             ]
    line_justaway           =[["ali_line_justaway "]
                              ,["b"]
                             ]
    line_sexual             =[["ali_line_sexual   "]
                              ,["b"]
                             ]
    line_bankrupt           =[["ali_line_bankrupt "]
                              ,["b"]
                             ]
    line_retail             =[["ali_line_retail   "]
                              ,["b"]
                             ]
    line_fire               =[["ali_line_fire     "]
                              ,["b"]
                             ]
    line_water              =[["ali_line_water    "]
                              ,["b"]
                             ]
    line_shining_dark_both  =[["There was too (shining/ dark) so I complained. I asked why. I couldn't focus on (sleeping/ reading). I had a (eye mask/ lamp) brought in."]
                              ,["b"]
                              ]
    line_hot_cold           =[["There was too (hot/ cold) so I complained. I asked why. I couldn't focus on (sleeping). I had a (heater/ cooler) brought in."]
                              ,["b"]
                              ]
    line_dry_moist          =[["There was too (dry/ moist) so I complained. I asked why. I couldn't focus on (sleeping). I had a (humidifier/ dehumidifier) brought in."]
                              ,["b"]
                              ]
    line_quiet_noisy        =[["There was too (noisy) so I complained. I asked why. I couldn't focus on (sleeping/ reading). I had a ear plugs brought in. Someone was (singing/ making noise)."]
                              ,["b"]
                              ]
    line_building_outdoor   =[["There was (wet/ sandy/ dusty/ stinky/ a insect) so I complained. I asked why. I couldn't focus on (sleeping/ reading). I had a ear (tissue paper/ cleaner) brought in."]
                              ,["b"]
                              ]
    line_sexual_gore_both   =[["There was (sexual/ gore/ controversial) so I complained. I asked why. There were my wife and my son."]
                              ,["b"]
                              ]
    line_fear               =[["It was very thrilling and fun.", "Went here because the roller coasters and haunted house were full."]
                              ,["b"]
                              ]
    line_animal             =[["It was so much fun to see them."]
                              ,["b"]
                              ]
    line_kids               =[["There were many children."]
                              ,["b"]
                              ]
    line_pickupspot         =[["I picked my wife up there."]
                              ,["b"]
                              ]
    line_worked             =[["I was working there."]
                              ,["b"]
                              ]
    line_food               =[["I had a variety of meats here."]
                              ,["b"]
                              ]

    eve_func_result =eve_func_tablize("photospot"        , place_0_1['place_photospot']        , line_photospot)
    eve_func_result+=eve_func_tablize("justaway"         , place_0_1['place_justaway']         , line_justaway)
    eve_func_result+=eve_func_tablize("sexual"           , place_0_1['place_sexual']           , line_sexual)
    eve_func_result+=eve_func_tablize("bankrupt"         , place_0_1['place_bankrupt']         , line_bankrupt)
    eve_func_result+=eve_func_tablize("retail"           , place_0_1['place_retail']           , line_retail)
    eve_func_result+=eve_func_tablize("fire"             , place_0_1['place_fire']             , line_fire)
    eve_func_result+=eve_func_tablize("water"            , place_0_1['place_water']            , line_water)
    eve_func_result+=eve_func_tablize("shining_dark_both", place_0_1['place_shining_dark_both'], line_shining_dark_both)
    eve_func_result+=eve_func_tablize("hot_cold"         , place_0_1['place_hot_cold']         , line_hot_cold)
    eve_func_result+=eve_func_tablize("dry_moist"        , place_0_1['place_dry_moist']        , line_dry_moist)
    eve_func_result+=eve_func_tablize("quiet_noisy"      , place_0_1['place_quiet_noisy']      , line_quiet_noisy)
    eve_func_result+=eve_func_tablize("building_outdoor" , place_0_1['place_building_outdoor'] , line_building_outdoor)
    eve_func_result+=eve_func_tablize("sexual_gore_both" , place_0_1['place_sexual_gore_both'] , line_sexual_gore_both)
    eve_func_result+=eve_func_tablize("fear"             , place_0_1['place_fear']             , line_fear)
    eve_func_result+=eve_func_tablize("animal"           , place_0_1['place_animal']           , line_animal)
    eve_func_result+=eve_func_tablize("kids"             , place_0_1['place_kids']             , line_kids)
    eve_func_result+=eve_func_tablize("pickupspot"       , place_0_1['place_pickupspot']       , line_pickupspot)
    eve_func_result+=eve_func_tablize("worked"           , place_0_1['place_worked']           , line_worked)
    eve_func_result+=eve_func_tablize("food"             , place_0_1['place_food']             , line_food)

    return eve_func_result


# Define concert instance without any explanations. Align text and whitespace with existing instances. Start answer with ```python

# takeaway
#  human trafick
#  steal
# have sex
#  buy sex
#  rape
#

# I was sorned between go to A or B

# そもそも特定条件において使用可能な文の一覧を表示し、その条件に見合うインスタンスを併記する、という形式はどうか?
#    takeaway:str # "panty", "plushie"


# if arg_1.food and arg_1.animal and not arg_2.food and arg_2.animal:
# if arg_1.kids_olds_adult == "k" and arg_2.kids_olds_adult == "a":
# if arg_1.holy_unholy and arg_2.holy_unholy and arg_1.holy_unholy != arg_2.holy_unholy:
# if arg_1.amusement_entertainment and not arg_2.amusement_entertainment and arg_2.holy_unholy == "u" or arg_2.weak:

# if arg_1.commonlyusedbytourists and arg_1.outdoor_building_vehicle_machine == "b" and arg_2.outdoor_building_vehicle_machine == "o"

# if arg_1.amusement_entertainment == "e" and arg_2.weak:
#   ["I enjoyed watching them."]







































