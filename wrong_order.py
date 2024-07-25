from re import I
from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class Place:
    ALL_PLACES: ClassVar[List['Place']] = []
    place_name        : List[str]
    kids_olds         :str # Highly associated with kids -> "k", olds -> "o"
    not_facility      :str # Not a facility -> "y"
    animal            :str # Highly associated with animals -> "y"
    food              :str # Highly associated with food -> "y"
    holy_unholy       :str # Commonly holy -> "h", unholy -> "u"
    clean_dirty       :str # Commonly dirty -> "d", clean -> "c"
    crime_ridden      :str # Crime ridden -> "y"
    risk_of_injury    :str # Risk of injury -> "y"
    thrilling         :str # Thrilling -> "y"
    enjoyment         :str # Enjoyable -> "y"
    enjoyment_watch   :str # Enjoy watching something -> "y"
    serious           :str # Serious -> "y"
    camera_ok_ban     :str # Scenic spot -> "o", camera banned -> "b"
    pick_up_spot      :str # Pick up spot -> "y"
    weaks             :str # Highly associated with weaks -> "y"
    educational       :str # Educational -> "y"
    retail            :str # Offers retail service -> "y"
    paid              :str # Takes user's money -> "y"
    bankrupt          :str # Can drive some people bankrupt -> "y"
    coupon            :str # Offers coupons -> "y"
    mourn             :str # Used for scattering or burial -> "y"
    vehicle           :str # Vehicle -> "y"
    excite            :str # Exciting -> "y"
    normal_5tp1w      :str # Normal to visit 5+ times a week -> "y"
    problemer         :str # Only people with mental, financial or physical problems visit -> "y"
    def __hash__(self):
        return hash(self.place_name[0]) # Assuming Place_name is a list with a single name.
    def __post_init__(self):
        Place.ALL_PLACES.append(self)
                                                         #kid,not,ani ,foo,hol,cle ,cri,ris,thr ,enj,enj,ser ,cam,pic,wea,edu ,ret pai ban cou  mou,veh,exc,nor  pro,
_1_church                =Place(["church"               ],"" ,"" ,""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,"y" ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_mosque                =Place(["mosque"               ],"" ,"" ,""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,"y" ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_casino                =Place(["casino"               ],"" ,"" ,""  ,"" ,"u",""  ,"" ,"" ,"y" ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","y","y", "" ,"" ,"y","" , "" ,)
_1_brothel               =Place(["brothel"              ],"" ,"" ,""  ,"" ,"u",""  ,"" ,"" ,""  ,"y","" ,""  ,"b","" ,"" ,""  ,"y","y","y","y", "" ,"" ,"y","" , "" ,)
_1_strip_club            =Place(["strip club"           ],"" ,"" ,""  ,"" ,"u",""  ,"" ,"" ,""  ,"y","y",""  ,"b","" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_nursing_home          =Place(["nursing home"         ],"o","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"y",""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"y", "" ,)
_1_dumpyard              =Place(["dumpyard"             ],"" ,"" ,""  ,"" ,"" ,"d" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_mountain              =Place(["mountain"             ],"" ,"y","y" ,"" ,"" ,""  ,"" ,"y",""  ,"y","" ,""  ,"o","" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_kindergarten          =Place(["kindergarten"         ],"k","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,"y" ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_obstetrics            =Place(["obstetrics"           ],"" ,"" ,""  ,"" ,"h","c" ,"" ,"" ,""  ,"y","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "y",)
_1_lost_child_department =Place(["lost child department"],"k","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_zoo                   =Place(["zoo"                  ],"" ,"" ,"y" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"y",""  ,"o","" ,"" ,"y" ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_safari                =Place(["safari"               ],"" ,"" ,"y" ,"" ,"" ,""  ,"" ,"y",""  ,"y","y",""  ,"o","" ,"" ,"y" ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_animal_shelter        =Place(["animal shelter"       ],"" ,"" ,"y" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"o","" ,"" ,""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_butcher               =Place(["butcher"              ],"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_restaurant            =Place(["restaurant"           ],"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_fish_market           =Place(["fishmarket"           ],"" ,"" ,"y" ,"y","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_aquarium              =Place(["aquarium"             ],"" ,"" ,"y" ,"y","" ,""  ,"" ,"" ,""  ,"y","y",""  ,"o","" ,"" ,"y" ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_car_dealer            =Place(["car dealer"           ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_parking_lot           =Place(["parking lot"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_flower_shop           =Place(["flower shop"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_graveyard             =Place(["graveyard"            ],"" ,"" ,""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_war_memorial          =Place(["war memorial"         ],"" ,"" ,""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,"y" ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_wallet_shop           =Place(["wallet shop"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_lost_and_found        =Place(["lost and found"       ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_gallery               =Place(["gallery"              ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"o","" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_public_restroom       =Place(["public restroom"      ],"" ,"" ,""  ,"" ,"" ,"d" ,"" ,"" ,""  ,"" ,"" ,""  ,"b","" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"y", "" ,)
_1_river                 =Place(["river"                ],"" ,"y","y" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,""  ,"o","" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_ocean                 =Place(["ocean"                ],"" ,"y","y" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,""  ,"o","" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_beach                 =Place(["beach"                ],"" ,"y",""  ,"" ,"" ,""  ,"" ,"y",""  ,"y","" ,""  ,"b","y","" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_hotel                 =Place(["hotel"                ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_ice_rink              =Place(["ice rink"             ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"y",""  ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_concert               =Place(["concert"              ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_library               =Place(["library"              ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"" ,"" ,"" ,"y" ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_sauna                 =Place(["sauna"                ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"b","" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_ski_area              =Place(["ski area"             ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"y",""  ,"y","" ,""  ,"o","y","" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_haunted_house         =Place(["haunted house"        ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_magic_show            =Place(["magic show"           ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_ticket_machine        =Place(["ticket machine"       ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_escape_room           =Place(["escape room"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"y","" , "" ,)
_1_pool                  =Place(["pool"                 ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,""  ,"y","" ,""  ,"b","" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_tent_city             =Place(["tent_city"            ],"" ,"" ,""  ,"" ,"u","d" ,"y","" ,""  ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "y",)
_1_slum                  =Place(["slum"                 ],"" ,"" ,""  ,"" ,"u","d" ,"y","" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "y",)
_1_camp_gear_shop        =Place(["camp gear shop"       ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_terminal_ward         =Place(["terminal ward"        ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_psychiatric_ward      =Place(["psychiatric ward"     ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_comedy_club           =Place(["comedy club"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_genie_machine         =Place(["genie machine"        ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_antique_shop          =Place(["antique shop"         ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_museum                =Place(["museum"               ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_bar                   =Place(["bar"                  ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"" ,"y","" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_robbery_scene         =Place(["robbery scene"        ],"" ,"y",""  ,"" ,"u",""  ,"" ,"y","y" ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_beggar_scene          =Place(["beggar scene"         ],"" ,"y",""  ,"" ,"u","d" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_charity_event         =Place(["charity evenet"       ],"" ,"y",""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_dental_clinic         =Place(["dental clinic"        ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "y",)
_1_payday_loan           =Place(["payday loan"          ],"" ,"" ,""  ,"" ,"u",""  ,"" ,"" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"y","y","" , "" ,"" ,"" ,"" , "y",)
_1_prison                =Place(["prison"               ],"" ,"" ,""  ,"" ,"u",""  ,"y","" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "y",)
_1_hospital              =Place(["hospital"             ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"y",""  ,"" ,"y","y","" , "" ,"" ,"" ,"" , "y",)
_1_pharmacy              =Place(["pharmacy"             ],"" ,"" ,""  ,"" ,"" ,"c" ,"" ,"" ,"y" ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y","" ,"" , "" ,"" ,"" ,"" , "y",)
_1_orphanage             =Place(["orphanage"            ],"k","" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"y",""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_apple_store           =Place(["apple store"          ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_laundry               =Place(["laundry"              ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"" ,"" ,"y", "" ,)
_1_cloth_shop            =Place(["cloth shop"           ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_roller_coaster        =Place(["roller coaster"       ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"y","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"y","y","" , "" ,)
_1_taxi                  =Place(["taxi"                 ],"" ,"y",""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"y","" ,"y", "" ,)
_1_airplane              =Place(["airplane"             ],"" ,"y",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"y","" ,"y", "" ,"y","" ,"" , "" ,)
_1_light_show            =Place(["light show"           ],"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"y","y",""  ,"o","" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "" ,)
_1_funeral_home          =Place(["funeral home"         ],"" ,"" ,""  ,"" ,"h","c" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_crematorium           =Place(["crematorium"          ],"" ,"" ,""  ,"" ,"h","c" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "y","" ,"" ,"" , "" ,)
_1_steak_house           =Place(["steak house"          ],"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,""  ,"y","" ,""  ,"" ,"" ,"" ,""  ,"y","y","" ,"y", "" ,"" ,"" ,"" , "" ,)
_1_police_station        =Place(["police station"       ],"" ,"" ,""  ,"" ,"h",""  ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"" ,"" ,"" , "y",)

# 以下のdynamic attrには、sexual_instanceのような Negative place のみを格納する変数と、wedding_instanceのような Positive place のみを格納する変数がある。misunderstand型コメディにおいては Negative place と Positive place の誤解ペアが多く観察される。
excrete_instances = [_1_public_restroom]
for instance in excrete_instances:
    instance.excrete  = "y"
sex_instances = [_1_brothel, _1_hotel]
for instance in sex_instances:
    instance.sex  = "y"
non_commercial_money_request_instance = [_1_robbery_scene, _1_beggar_scene, _1_charity_event, _1_church, _1_mosque]
for instance in non_commercial_money_request_instance:
    instance.non_commercial_money_request  = "y"
medicine_instance = [_1_hospital, _1_pharmacy]
for instance in medicine_instance:
    instance.medicine  = "y"
wedding_instance = [_1_hotel, _1_beach, _1_church, _1_restaurant]
for instance in wedding_instance:
    instance.wedding  = "y"
get_son_instance = [_1_obstetrics, _1_orphanage]
for instance in get_son_instance:
    instance.get_son  = "y"
sexual_instance = [_1_strip_club, _1_brothel]
for instance in sexual_instance:
    instance.sexual  = "y"

misun_pairs=[] # In this list, each [0] is "Ali imagines" and each [1] is "Bob imagines".

def classify_objects(classification_rules):
    object_dict = {"Ali imagines": [], "Bob imagines": []}
    for instance in Place.ALL_PLACES:
        for key, condition in classification_rules.items():
            if condition(instance):
                object_dict[key].append(instance.place_name[0])
    return object_dict

def print_classification_results(object_dict):
    for key, values in object_dict.items():
        print(f"{key}:")
        for value in values:
            print(f"  - {value}")


# 人間向説明: HPS_CB_use_place_x_for_purpose_y はrepositionerが"to substitute B for A."という形態をとれる時、HPSとして使用する。
# たとえばA, B = (animal shelter, butcher)である時、"The (previously used / Originally planned) location became unavailable."という文は"近所の肉屋が閉店したから仕方なくアニマルシェルターで代用している"という誤解を招く。

HPS_CB_use_place_x_for_purpose_y = ["Everywhere was full.", "There was a need to choose a location as close as possible.", "Admittedly, it was a bit far.", "It was recommended by the friend.", "It was cheap.","The (previously used / Originally planned) location became unavailable.", "The ambiance suited."]
# Prompt for LLM: HPS_CB_use_place_x_for_purpose_y explanation : This is a list of sentences with a high probability of appearing in the sentence "use place x for purpose y." Even if x and y are (church, wedding) or (kindergarten, leaving children) or (night club, picking up), the sentences in this list are likely to be used. Add new 5 statements in English without any explanations. The sentence you add should not contain a subject.



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
all_PBS_1_name = [i.PBS_1_name[0] for i in PBS_1.all_PBS_1]
print(all_PBS_1_name)
"""

all_PBS_1_instance=['church', 'mosque', 'casino', 'brothel', 'strip club', 'nursing home', 'dumpyard', 'mountain', 'kindergarten', 'obstetrics', 'lost child department', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'parking lot', 'flower shop', 'graveyard', 'war memorial', 'wallet shop', 'lost and found', 'gallery', 'public restroom', 'river', 'ocean', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski area', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'tent_city', 'slum', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum', 'bar', 'robbery scene', 'beggar scene', 'charity evenet', 'dental clinic', 'payday loan', 'prison', 'hospital', 'pharmacy', 'orphanage', 'apple store', 'laundry', 'cloth shop', 'roller coaster', 'taxi', 'airplane', 'light show', 'funeral home', 'crematorium'
]# These are PBS_1 instances' .name


@dataclass
class Complaint:
  ALL_COMPLAINTS: ClassVar[List['Complaint']] = []
  complaint_name: List[str]
  cope_had_bring:list # I had a staff to bring {cope_bring}
  cope_had_do:list # I had a staff {cope_do}
  because_my:list # I complained to them because my {because_my}
  noproblem:list # PBS_1 instance only
  problem:list # PBS_1 instance only
  def get_name(self):
        return self.complaint_name[0]  # Assuming Place_name is a list with a single name.
  def __post_init__(self):
        Complaint.ALL_COMPLAINTS.append(self)

_c_loud     =Complaint(["loud"]       ,["ear plugs"]        ,["turn the volume down"],["wife is pregnant"]
                  ,[_1_concert]
                  ,[_1_hotel])
_c_cold     =Complaint(["cold"]       ,["heater"]           ,["turn the heat up."],["wife is pregnant"]
                  ,[_1_ski_area]
                  ,[_1_hotel])
_c_hot      =Complaint(["hot"]        ,["cooler"]           ,["turn the heat down."],["wife is pregnant"]
                  ,[_1_sauna]
                  ,[_1_hotel])
_c_smelly   =Complaint(["smelly"]     ,["perfume"]          ,["move the stinky stuff away"],[]
                  ,[_1_dumpyard, _1_fish_market]
                  ,[_1_hotel])
_c_sexual   =Complaint(["sexual"]     ,[]                   ,["move the sexual stuff away"],["son is there"]
                  ,[_1_brothel, _1_strip_club]
                  ,[_1_gallery])
_c_slippery =Complaint(["slippery"]   ,["rubber mat"]       ,[],["wife is pregnant"]
                  ,[_1_ice_rink, _1_ski_area]
                  ,[_1_hotel])
_c_heady    =Complaint(["heady"]      ,[]                   ,["apologize"],[]
                  ,[_1_haunted_house]
                  ,[_1_hotel, _1_bar, _1_restaurant])
_c_complex  =Complaint(["complex"]    ,[]                   ,["do all of it","explain it more clearly"],[]
                  ,[_1_magic_show, _1_escape_room]
                  ,[_1_ticket_machine])
_c_sensitive=Complaint(["sensitive"]  ,[]                   ,["move the sensitive stuff away"],["son is there"]
                  ,[_1_gallery]
                  ,[_1_war_memorial])
_c_dirty    =Complaint(["dirty"]      ,["cleaning supplies"],["clean it up"],["son has allergies"]
                  ,[_1_dumpyard]
                  ,[_1_hotel])
_c_old      =Complaint(["old"]        ,[]                   ,["replace them with new ones"],[]
                  ,[_1_antique_shop, _1_museum]
                  ,[_1_hotel])
_c_dusty    =Complaint(["dusty"]      ,["air purifier"]     ,["vacuum the area"],["son has asthma"]
                  ,[_1_dumpyard]
                  ,[_1_hotel])
_c_bright   =Complaint(["bright"]     ,["sunglasses"]       ,["dim the lights"],["wife has epilepsy"]
                  ,[_1_light_show]
                  ,[_1_hotel])
_c_narrow   =Complaint(["narrow"]     ,[]                   ,["enralge it"],["wife is claustrophobic"]
                  ,[_1_escape_room]
                  ,[_1_hotel])
_c_too_fast =Complaint(["too fast"]   ,[]                   ,["slow it down","stop sharp turns, sudden stops, or starts."],["wife is pregnant"]
                  ,[_1_roller_coaster]
                  ,[_1_taxi])
_c_wet      =Complaint(["wet"]        ,["towel"]            ,["dry the area"],[]
                  ,[_1_pool]
                  ,[_1_hotel])
_c_humid    =Complaint(["humid"]      ,["dehumidifier"]     ,["reduce the humidity"],["wife has asthma"]
                  ,[_1_sauna]
                  ,[_1_hotel])
_c_too_many_olds = Complaint(["too many olds"],[],["in the young ones"],[]
                  ,[_1_nursing_home]
                  ,[_1_brothel])
_c_dark     =Complaint(["dark"]       ,["flashlight"]       ,["increase the lighting"],["son is scared of the dark"]
                  ,[_1_haunted_house]
                  ,[_1_hotel])
# Define new PBS_c instances without any explanations.Please only reply on newly created instances. Align spaces and characters with existing instances. Don't create an instance similar to an existing instance, for example don't create _c_noisy when you have _c_loud_.Start answer with ```python. The object name of the PBS_1 instance starts with _1_.


def misun_selfish(): # 全てのPBS_cインスタンスを整形して表示する。
    HPS_misun_selfish=["I lectured the person in charge.", "I demanded a refund.","I gave it a low rating in an online review.", "I scold the man in charge, but he didin't take action.", "I couldn't concentrate to (relaxing/reading/sleeping/eating).", "I cancelled my membership."] # いつか実装
    print(f"### misun_selfish() ### \n HPS = {HPS_misun_selfish}")

    for i in Complaint.ALL_COMPLAINTS:
        print(f"About: {i.complaint_name[0]}")
        if i.noproblem:
            print("  Bob imagines")
            for no_pro in i.noproblem:
                print(f"    - {no_pro.place_name[0]}") 
        if i.problem:
            print("  Ali imagines")
            for pro in i.problem:
                print(f"    - {pro.place_name[0]}") 
            for j in range(len(i.cope_had_bring)):
                print(f"    -- I had a staff to bring {i.cope_had_bring[j]}.")
            for j in range(len(i.cope_had_do)):
                print(f"    -- I had a staff {i.cope_had_do[j]}.")
            for j in range(len(i.because_my)):
                print(f"    -- I complained to them because my {i.because_my[j]}.")
        misun_pairs.append([no_pro.place_name, pro.place_name])
        print()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


enjoyment_watch_weaks = [i for i in Place.ALL_PLACES if i.enjoyment_watch and not i.weaks]
all_PBS_1_name_with_enjoyment_watch_weaks = [i.place_name[0] for i in enjoyment_watch_weaks]
print(all_PBS_1_name_with_enjoyment_watch_weaks)


#['strip club', 'zoo', 'safari', 'aquarium', 'gallery', 'concert', 'library', 'magic show', 'comedy club', 'museum', 'light show']

# for misun_weaks()
_1_zoo.tmp_misun_weaks = ["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the cage stronger."]
_1_safari.tmp_misun_weaks=["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the electric fence stronger."]
_1_aquarium.tmp_misun_weaks=["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like there.","Their every movement is interesting.", "I talk them to make the glass stronger."]
_1_comedy_club.tmp_misun_weaks=["I often go to see them for a laugh.", "I love having a drink and laughing at their performances.", "I wish they'd improve the sound system", "It's exciting when they get on stage.", "It's a great place to unwind after a long day."]
_1_aquarium_tmp_misun_weaks = ["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the glass stronger."]
_1_strip_club_tmp_misun_weaks = ["I enjoy having a drink while watching them.","I wish they'd improve the lighting.","It's exciting when they take the stage.","Sometimes get an erection.", "Put a dollar bill in their underwear."]
_1_magic_show_tmp_misun_weaks = ["I often go to see them for excitement.","I love watching them perform their tricks.","I wish they'd improve the lighting.","It's amazing how they manage to surprise the audience.","It's a great place to take friends for a fun night out."]

# These lists are meant to test the intelligence of the LLM by determining whether they can correctly identify where the speaker is talking about. Do not use words that could easily lead to a specific location (for example, do not use the words "aquarium" or "fish" in a list of aquariums).It is best to use the pronoun "they" whenever possible, regardless of whether the object is animate or inanimate.
# Task : make _1_ """ magic_show """ .tmp_misun_weaks in English in python.

def misun_weaks(): # AMP不十分misun関数
    HPS_misun_weaks=["I often enjoy watching them here"]
    print(f"### misun_weaks() ### \n HPS = {HPS_misun_weaks + HPS_CB_use_place_x_for_purpose_y}")
    Ali_imagines=[]
    Bob_imagines=[]

    for i in Place.ALL_PLACES:
        if i.weaks:
            Bob_imagines.append(i.place_name[0])
    print(f"Bob imagines : {Bob_imagines}")
    for i in Place.ALL_PLACES:
        if hasattr(i, 'tmp_misun_weaks'):
            Ali_imagines.append(i.place_name[0])
            print(f"Ali imagines : {i.place_name[0]}")
            for j in i.tmp_misun_weaks:
                print(f"  - {j}")
    misun_pairs.append([i.place_name, i.place_name])



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

all_place_name = [i.place_name[0] for i in Place.ALL_PLACES]
print(all_place_name)

all_PBS_1_instance=['church', 'mosque', 'casino', 'brothel', 'strip club', 'nursing home', 'dumpyard', 'mountain', 'kindergarten', 'obstetrics', 'lost child department', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'parking lot', 'flower shop', 'graveyard', 'war memorial', 'wallet shop', 'lost and found', 'gallery', 'public restroom', 'river', 'ocean', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski area', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'tent_city', 'slum', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum', 'bar', 'robbery scene', 'beggar scene', 'charity evenet', 'dental clinic', 'payday loan', 'prison', 'hospital', 'pharmacy', 'orphanage', 'apple store', 'laundry', 'cloth shop', 'roller coaster', 'taxi', 'airplane', 'light show', 'funeral home', 'crematorium'
]# These are PBS_1 instances' .name

@dataclass
class Belong: # Use for misun_thief()
  ALL_BELONGS:ClassVar[List['Belong']] = []
  belong_name:str
  place_where_x_is_but_you_cannot_get_others_x:list # PBS_1 instance only # x means "belong_name"
  place_where_x_is_but_you_can_get_others_x:list # PBS_1 instance only # x means "belong_name"
  def __post_init__(self):
        Belong.ALL_BELONGS.append(self)

_b_fish       =Belong("fish"      ,[_1_aquarium],[_1_fish_market]) # Fish exist both in aquariums and fish markets. You can get others' fish in fish markets.
_b_kids       =Belong("kids"      ,[_1_kindergarten],[_1_orphanage]) # Kids exist both in kindergartens and orphanages. You can get othrs' children in orphanages.
_b_phone      =Belong("phone"     ,[_1_lost_and_found], [_1_apple_store]) # phone exist both in lost and founds and apple stores. You can get others' phone in apple stores.
_b_flower     =Belong("flower"    ,[_1_graveyard, _1_war_memorial],[_1_flower_shop])
_b_car        =Belong("car"       ,[_1_parking_lot], [_1_car_dealer]) # Defined by GPT4
_b_art        =Belong("art"       ,[_1_museum], [_1_gallery]) # Defined by GPT4
_b_jewelry    =Belong("jewelry"   ,[_1_museum], [_1_antique_shop]) # Defined by GPT4
_b_camera     =Belong("camera"    ,[_1_lost_and_found], [_1_antique_shop])
_b_cloth      =Belong("cloth"     ,[_1_laundry], [_1_cloth_shop])
_b_key        =Belong("key"       ,[_1_escape_room], [_1_lost_and_found]) # Defined by Gemini from Colaboratory
_b_bed        =Belong("bed"       ,[_1_hospital], [_1_nursing_home, _1_prison]) # Defined by Gemini from Colaboratory
_b_animal     =Belong("animal"    ,[_1_safari, _1_zoo], [_1_animal_shelter]) # Defined by Gemini from Colaboratory
_b_stone      =Belong("stone"     ,[_1_graveyard], [_1_mountain]) # Defined by Gemini from Colaboratory
_b_tent       =Belong("tent"      ,[_1_tent_city], [_1_camp_gear_shop])
_b_money      =Belong("money"     ,[_1_charity_event], [_1_payday_loan])
# Define 10 new Belong instance in English without any explanations. Choice .place_where_x_is_but_you_cannot_get_others_x and .place_where_x_is_but_you_can_get_others_x from all_pbs_1_instance. The object name of the PBS_1 instance starts with _1_.

# 現状、AIは多少このタスクを実行できる。

def misun_thief():
    HPS_misun_thief=["I got one for my family.", "I asked for a refund as the one I got was faulty.", "My wife objected, but I got one.", "I've been going there for about ten years.", "Because it's a special anniversary.", "If I had the money I would buy a new one."]

    print(f"### misun_thief() ### \n HPS = {HPS_misun_thief + HPS_CB_use_place_x_for_purpose_y}")
    object_dict = {"Ali imagines": [], "Bob imagines": []}
    for belong_inst in Belong.ALL_BELONGS:
        for p in belong_inst.place_where_x_is_but_you_can_get_others_x:
            object_dict["Ali imagines"].append(p.place_name[0])
        for p in belong_inst.place_where_x_is_but_you_cannot_get_others_x:
            object_dict["Bob imagines"].append(p.place_name[0])
        misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
        print(f"{object_dict} : Ali says 'I got {belong_inst.belong_name}'")
        object_dict.clear()
        object_dict = {"Ali imagines": [], "Bob imagines": []}

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




def misun_voy():
    HPS_misun_voy = ["I took a lot of good photos.", "I enjoyed the wonderful scenery.", "I'll use this photo for this year's Christmas card.", "This is one of my favorite shots.",  "I have it framed and displaying it.", "I bought an expensive camera for this purpose.", "It was difficult to keep the subject still."]
    print(f"### misun_voy() ### \n HPS = {HPS_misun_voy + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.camera_ok_ban == "o",  # _1_mountain
        "Bob imagines": lambda instance: instance.camera_ok_ban == "b"  # _1_public_restroom
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_pic():
    HPS_misun_pic = ["I picked up girls here.", "For some reason the success rate was low.", "I made my girlfriend here.", "Unfortunately, I was found by the girl's boyfriend.", "Unfortunately, I got rejected several times.", "I come here every weekend."]
    print(f"### misun_pic() ### \n HPS = {HPS_misun_pic + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.pick_up_spot,  # _1_beach
        "Bob imagines": lambda instance: instance.kids_olds == "k" or instance.holy_unholy == "h" or instance.serious  # _1_kindergarten, _1_graveyard, _1_obstetrics
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_per():
    HPS_misun_per = ["I (had/bought) sex here.", "For some reason there was no sexual service.", "It's cheaper than call girls nearby.", "I always use rubbers properly.", "It's 300 dollars per hour."]
    print(f"### misun_per() ### \n HPS = {HPS_misun_per + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: hasattr(instance, 'sex'),  # _1_brothel
        "Bob imagines": lambda instance: instance.kids_olds == "k" or instance.animal  # _1_kindergarten, _1_zoo
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_kids(): # was here
    HPS_misun_kids=["I put my son here.","I used to play here a lot as a child.", "When I was a child, I was left here until my parents finished work.", "When I was a child, my father brought me here to study.", "I've been here on school trips."]
    print(f"### misun_kids() ### \n HPS = {HPS_misun_kids + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.kids_olds == "k" or instance.educational,  # _1_kindergarten, _1_library
        "Bob imagines": lambda instance: hasattr(instance, 'sex') or instance.holy_unholy == "u" or instance.clean_dirty == "d" or instance.crime_ridden
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_olds(): # was here
    HPS_misun_olds=["I put my grandfather here.", "My grandfather didn't want to go into here.","My grandfather made many friends here.","He receives excellent care at this facility.","We visit him every weekend.","He enjoys the activities they offer here."]
    print(f"### misun_olds() ### \n HPS = {HPS_misun_olds + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.kids_olds == "o",
        "Bob imagines": lambda instance: hasattr(instance, 'sex') or instance.holy_unholy == "u" or instance.clean_dirty == "d" or instance.crime_ridden
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_mourn():
    HPS_misun_mourn=["My father's grave is here.", "I attended a funeral here.", "I (buried him / scattered his ashes) here.", "He loved this place.","Our family often comes here to reflect.","This place holds many of our memories.","We shared stories about him here."]
    print(f"### misun_mourn() ### \n HPS = {HPS_misun_mourn + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.mourn,
        "Bob imagines": lambda instance: hasattr(instance, 'sex') or instance.holy_unholy == "u" or instance.clean_dirty == "d" or instance.enjoyment
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_wedding():
    HPS_misun_wedding=["I had my weeding here.", "It's true that it's a little far away, so it may have been inconvenient for attendees."]
    print(f"### misun_wedding() ### \n HPS = {HPS_misun_wedding + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: hasattr(instance, 'wedding'), #_1_hotel
        "Bob imagines": lambda instance: hasattr(instance, 'sex') or (instance.holy_unholy == "u" or instance.clean_dirty == "d") and not instance.enjoyment  #_1_dumpyard
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict


def misun_eat():
    HPS_misun_eat=["The food there is delicious.", "The food there is fresh and can be eaten raw or alive.", "I got food poisoning from the food there.", "I once had trash in the food there.", "So I asked the person in charge there to apologize.", "I left a rating for it on yelp.", "For some reason there's not very well known.", "It's Chiba's traditional food."]
    print(f"### misun_eat() ### \n HPS = {HPS_misun_eat + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance:     instance.food,
        "Bob imagines": lambda instance: not instance.food and instance.animal and not instance.not_facility
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_excrete():
    HPS_misun_excrete=["I excreted here.", "When I have diarrhea, I feel relieved when I find this place.", "I complained because there was no toilet paper."]
    print(f"### misun_excrete() ### \n HPS = {HPS_misun_excrete + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: hasattr(instance, 'excrete'), # Check if instance has 'excrete' dynamic attribute. _1_public_restroom
        "Bob imagines": lambda instance: instance.food or instance.clean_dirty == "c" or instance.holy_unholy == "h"
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_thrilling():
    HPS_misun_thrilling=["I became addicted to the thrill there.", "I went many times with my family who didn't like it.", "I said I'd pay him to make it more thrilling.", "I was scared so I called the police.", "I called for help, but no one around me did anything.", "This wasn't covered by travel insurance.", "I was scared so I (hit him / broke the window) and ran away."]
    print(f"### misun_thrilling() ### \n HPS = {HPS_misun_thrilling + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.thrilling and     instance.enjoyment, #_1_haunted_house
        "Bob imagines": lambda instance: instance.thrilling and not instance.enjoyment  #_1_robbery_scene
    } # このように attr1 and attr1, attr2 and not attr2 型のmisun関数に特別な呼び名がいる。 one-armed

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_medicine():
    HPS_misun_medicine=["I pick up my drugs here regularly.", "I refused to take opioids.", "I have to be careful not to be overprescribed.", "I'm worried about the side effects.", "I accidentally took too much drugs once.", "I feel much better after taking the drug."] #
    print(f"### misun_medicine() ### \n HPS = {HPS_misun_medicine}")

    classification_rules = {
        "Ali imagines": lambda instance: hasattr(instance, 'medicine'), # _1_hospital, _1_pharmacy
        "Bob imagines": lambda instance: instance.crime_ridden # _1_slum
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_bankrupt(): # .non_commercial_money_request
    HPS_misun_bankrupt=["My father spent too much money here and ended up bankrupt.", "My father was addicted to this place.","My father used to come here every weekend.","Eventually, he had to sell our house."]
    print(f"### misun_bankrupt() ### \n HPS = {HPS_misun_bankrupt + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.coupon and instance.bankrupt, # _1_casino
        "Bob imagines": lambda instance: (instance.coupon and not instance.bankrupt) or hasattr(instance, 'non_commercial_money_request') # _1_genie_machine, _1_robbery_scene
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_non_commercial_money_request(): # .non_commercial_money_request
    HPS_misun_non_commercial_money_request=["They accepted credit cards.","They were handing out numbered tickets because there were so many people.","I got a receipt.","They gave me the correct change.","They had a friend referral system.","They gave me coupons."]
    print(f"### misun_non_commercial_money_request() ### \n HPS = {HPS_misun_non_commercial_money_request}")

    classification_rules = {
        "Ali imagines": lambda instance:     instance.coupon and not hasattr(instance, 'non_commercial_money_request'), #_1_hotel
        "Bob imagines": lambda instance: not instance.coupon and     hasattr(instance, 'non_commercial_money_request')  #_1_robbery_scene
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_get_son(): # .get_son
    HPS_misun_get_son=["I met my son here for the first time and became a father.", "I brought my son home from here."]
    print(f"### misun_get_son() ### \n HPS = {HPS_misun_get_son}")

    classification_rules = {
        "Ali imagines": lambda instance: hasattr(instance, 'get_son'), #_1_obstetrics, _1_orphanage
        "Bob imagines": lambda instance: instance.kids_olds == "k" and not hasattr(instance, 'get_son') # _1_kindergarten
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_sexual(): # .sexual
    HPS_misun_sexual=[]
    HPS_misun_sexual_if_animal=["I saw monkeys there.", "There were about 4 years old children."]
    HPS_misun_sexual_if_kids=["There were about 4 years old children.", "I saw a baby."]
    HPS_misun_sexual_if_olds=["There were about 95 years old hugs.", "There were bedridden, demented, and wheelchair-bound olds."]
    print(f"### misun_sexual() ### \HPS = {HPS_misun_sexual} \HPS(if animal) = {HPS_misun_sexual_if_animal} \HPS(if kids) = {HPS_misun_sexual_if_kids} \HPS(if olds) = {HPS_misun_sexual_if_olds}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.kids_olds or instance.animal or instance.problemer,
        "Bob imagines": lambda instance: hasattr(instance, 'sexual') #_1_brothel, _1_strip_club
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_work(): # .sexual
    HPS_misun_work=["My son is working here.", "My son works here eight hours a day.", "It took a while for him to become a permanent employee here."]
    print(f"### misun_work() ### \n HPS = {HPS_misun_work + HPS_CB_use_place_x_for_purpose_y}")

    classification_rules = {
        "Ali imagines": lambda instance: instance.coupon, # judge to is the place neutral or not with .coupon
        "Bob imagines": lambda instance: hasattr(instance, 'sexual') #_1_brothel, _1_strip_club
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

def misun_normal_5tp1w():
    HPS_normal_5tp1w=["I used to (come, use) here about five times per week.", "This is like my second home."]
    print(f"### misun_normal_5tp1w ### \n HPS = {HPS_normal_5tp1w}")

    classification_rules = {
        "Ali imagines": lambda i: i.normal_5tp1w ,
        "Bob imagines": lambda i: i.holy_unholy == "u" or hasattr(i, 'sexual') or i.crime_ridden or i.problemer
    }

    object_dict = classify_objects(classification_rules)
    print_classification_results(object_dict)

    misun_pairs.append([object_dict["Ali imagines"], object_dict["Bob imagines"]])
    return object_dict

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

all_PBS_1_instance=['church', 'mosque', 'casino', 'brothel', 'strip club', 'nursing home', 'dumpyard', 'mountain', 'kindergarten', 'obstetrics', 'lost child department', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'parking lot', 'flower shop', 'graveyard', 'war memorial', 'wallet shop', 'lost and found', 'gallery', 'public restroom', 'river', 'ocean', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski area', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'tent_city', 'slum', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum', 'bar', 'robbery scene', 'beggar scene', 'charity evenet', 'dental clinic', 'payday loan', 'prison', 'hospital', 'pharmacy', 'orphanage', 'apple store', 'laundry', 'cloth shop', 'roller coaster', 'taxi', 'airplane', 'light show', 'funeral home', 'crematorium'
]# These are PBS_1 instances' .name. PBS_1 instances' name start with "_1_"

#.be_when is required for important timings such as critical conditions, funerals, childbirth, graduation ceremony etc. Do not set .be_when on instances in places that are not related to these important timings.
#In other word, the "important timings" mentioned here are times when you should not go to the casino if your family is in that situation.

_1_church     .be_when=["wife's funeral"]
_1_obstetrics .be_when=["wife was in labor"]
_1_hospital   .be_when=["wife was in critical condition"]
_1_funeral_home .be_when=["wife's funeral"]
_1_crematorium  .be_when=["wife's cremation"]
_1_terminal_ward.be_when=["wife was in critical condition"]
_1_kindergarten .be_when=["son's graduation ceremony"]

#for i in PBS_1.all_PBS_1:
#  if hasattr(i, 'be_when'):
#    print(f"I was here when my {i.be_when}")

# Define new .be_when

def misun_be_when():
    HPS_misun_be_when=["I went there as a top priority.", "My heart was beating hard as I headed there."]
    print(f"### misun_be_when ### \n HPS = {HPS_misun_be_when}")

    Ali_imagines=[]
    Bob_imagines=[]

    for i in Place.ALL_PLACES:
        if i.holy_unholy == "u" and not hasattr(i, 'be_when') and i.enjoyment:
            Bob_imagines.append(i.place_name[0])
    print(f"Bob imagines : {Bob_imagines}")
    for i in Place.ALL_PLACES:
        if hasattr(i, 'be_when'):
            Ali_imagines.append(i.place_name[0])
            print(f"Ali imagines : {i.place_name[0]}")
            for j in i.be_when:
                print(f"I was there when my {j}.")
    misun_pairs.append([Ali_imagines, Bob_imagines])


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# It's a public restroom. There's only one toilet. 

# was working at a brothel. technique, injury




# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
Normal Position Fact   : dog.sales_unit = None
                         meat_sales.unit = ["pound", "kcal"]
                         alcohol_drink.shortage_timing = ["the prohibition era"]
                         sanitiser.shortage_timing = ["the pandemic"]
Normal Position Speech : "I bought a dog"
                         "I bought 5 pounds of meat."
                         "During the prohibition era, there was a shortage of alcohol drinks."
                         "During the pandemic, there was a shortage of sanitiser."
Repositioner           : to treat dog as meat
                         to treat sanitiser as alcohol drink
Repositioned Speech    : "I bought 5 pounds of dog."
                         "During the prohibition era, there was a shortage of sanitiser."

My level of satisfaction with LLM's performance in each task:
  Normal Position Fact   : 50%
  Normal Position speech : 90%
  Repositioner           : 40%

Hidden Position Speech : "I bought 5 pounds of it."
                         "During the prohibition era, there was a shortage of it."
NP Fact
NP Speech
RP Speech
HP Speech

"""

#AMP    : Ampai Phrase
#R Path : Reference Path

# travel, public restroom, 県内にしよう

#misun_selfish()# AMP不十分misun関数
#misun_weaks() # AMP不十分misun関数
#misun_thief() # 3
#misun_voy()
#misun_pic()
#misun_per()
#misun_medicine()
#misun_kids()
#misun_olds()
#misun_mourn()#10
#misun_wedding()
#misun_eat()
#misun_excrete()
#misun_thrilling()
#misun_bankrupt()
#misun_non_commercial_money_request()
#misun_get_son()
#misun_sexual()
#misun_work()
#misun_normal_5tp1w() # 20
#misun_be_when()
#print(misun_pairs)


def wrong_order():
  misun_selfish()# AMP不十分misun関数
  misun_weaks() # AMP不十分misun関数
  misun_thief() # 3
  misun_voy()
  misun_pic()
  misun_per()
  misun_medicine()
  misun_kids()
  misun_olds()
  misun_mourn()#10
  misun_wedding()
  misun_eat()
  misun_excrete()
  misun_thrilling()
  misun_bankrupt()
  misun_non_commercial_money_request()
  misun_get_son()
  misun_sexual()
  misun_work()
  misun_normal_5tp1w() # 20
  misun_be_when()
  print(misun_pairs)

wrong_order()



# work at brothels, eat non-edible animals, voyeur, などはwide-renge action.


"""
work.normal=["office"]
work.dont=["brothel"]

eat.normal=["beef"]
eat.dont=["dog"]

take_picture.normal=["mountain"]
take_picture.dont=["pool"]

get_son.normal=["orphanage"]
get_son.dont=["kindergarten"]

bankrupt.normal=["casino"]
bankrupt.dont=["genie machine"]

get_drug.normal=["pharmacy"]
get_drug.dont=["night club"]

excrete.normal=["toilet"]
excrete.dont=["church"]

add new pairs
"""







#misun_live()

"""
# Deficiency
tourist_area_1=[["hot",["sauna", "dessert"]], ["cold","ski area"],["rocky","mountain"],["loud","concert"],["old",["antique shop", "museum"]],["smelly",["dumpyard","fish market"]],["bright",["beach", "light show"]],["wet","pool"],["dry","dessert"],["humid","rainforest"],["too fast",["roller coaster","car race"]],["poor atitude","haunted house"],["sandy", "dessert"],["complex", "magic show"], ["sensitive", "war memorial"],["dark", "cave"],["slippery", "ice rink"], ["steep", "hiking trail"]]

for i in tourist_area_1:
  print(f"If a tourist complained about the {i[1]} he's in is {i[0]}, like 'Why here is so {i[0]} !? Refund!' it's insane because there should be so.")

# Append new 5 items in spot in English without any explanations. Please only reply to newly added items.



for i in tourist_area_1:
  print(f"If a tourist complained about the {i[1]} he's in is {i[0]}, like 'Why here is so {i[0]} !? Refund!' it's insane because there should be so.")
# Append new 5 items in spot in English without any explanations. Please only reply to newly added items.

# Below items are inappropriate.
inappropriate=[["noisy", "market"], ["expensive", "souvenir shop"], ["overwhelming", "festival"], ["isolated", "cabin"],["crowded", "theme park"], ["expensive", ["luxury hotel", "fine dining restaurant"]], ["boring", ["library", "lecture"]], ["quiet", "spa"], ["crowded", "festival"], ["quiet", "library"], ["expensive", "theme park"], ["overwhelming", "concert"]]
tourist_area=[ ["ride", "roller coaster"],["darkness", "cave"],["vastness", "ocean"]]
"""



'''
def find_mirror_pairs(mirror_list): # 相互にPosition A と Position B になれる関係(mirror pair)にあるrepositionerを持つオブジェクトのペアを検索する関数
    pairs = set()

    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result

    flat_list = [flatten(sublist) for sublist in mirror_list]

    for i in range(len(flat_list)):
        for j in range(i+1, len(flat_list)):
            set1 = set(flat_list[i])
            set2 = set(flat_list[j])
            common = set1.intersection(set2)
            for item1 in common:
                for item2 in common:
                    if item1 != item2:
                        pairs.add(tuple(sorted([item1, item2])))

    result = [list(pair) for pair in pairs]
    if len(result) == 1:
        print(result[0])
    else:
        print(result)

# テスト
mirror1 = [
    ["dog", "cat"],
    ["cat", "dog"],
    ["dog", "pig"]
]
mirror2 = [
    ["dog", "cat"],
    [["cat", "pig"], ["dog"]],
    ["dog", "pig"]
]
mirror3 = [
    [["nepal"], ["cat", "dog"]],
    [["cat", "dog"], ["nepal"]]
]
mirror4 = [[['mountain', 'zoo', 'safari', 'animal shelter', 'aquarium', 'gallery', 'river', 'ocean', 'ski resort'], ['brothel', 'public restroom', 'beach', 'sauna', 'pool']], [['beach', 'ski resort'], ['chruch', 'mosque', 'kindergarten', 'obstetrics', 'lost child department', 'graveyard', 'war memorial', 'tent_city', 'slum', 'terminal ward', 'psychiatric ward']], [['brothel', 'hotel'], ['mountain', 'kindergarten', 'lost child department', 'zoo', 'safari', 'animal shelter', 'fishmarket', 'aquarium', 'river', 'ocean']], [['chruch', 'mosque', 'kindergarten', 'lost child department', 'zoo', 'safari', 'aquarium', 'war memorial', 'library'], ['casino', 'brothel', 'dumpyard', 'public restroom', 'hotel', 'tent_city', 'slum']], [['nursing home'], ['casino', 'brothel', 'dumpyard', 'public restroom', 'hotel', 'tent_city', 'slum']], [['casino', 'brothel'], ['nursing home', 'kindergarten', 'obstetrics', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'flower shop', 'wallet shop', 'gallery', 'hotel', 'ice rink', 'concert', 'sauna', 'ski resort', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum']], [['obstetrics', 'terminal ward', 'psychiatric ward'], ['tent_city', 'slum']], [['chruch', 'mosque', 'mountain', 'graveyard', 'war memorial', 'river', 'ocean', 'beach'], ['casino', 'brothel', 'dumpyard', 'mountain', 'zoo', 'safari', 'aquarium', 'gallery', 'public restroom', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski resort', 'haunted house', 'magic show', 'escape room', 'pool', 'tent_city', 'slum', 'comedy club', 'genie machine', 'antique shop', 'museum']], [['butcher', 'restaurant', 'fishmarket', 'aquarium'], ['mountain', 'zoo', 'safari', 'animal shelter', 'river', 'ocean']]]

#print("mirror1:")
#find_mirror_pairs(mirror1)
#print("\nmirror2:")
#find_mirror_pairs(mirror2)
#print("\nmirror3:")
#find_mirror_pairs(mirror3)
print("\nmirror4:")
find_mirror_pairs(mirror4)
'''

'''
def unsimilarity(arg_a):
    def calculate_unsimilarity(arg_a, arg_b):
        attributes = [
            ("kids", "sex"),
            ("kids", "dirty_spiritually"),
            ("animal", "sex"),
            ("animal", "food"),
            ("holy", "sex"),
            ("holy", "dirty_spiritually"),
            ("holy", "dirty_physically"),
            ("food", "dirty_physically"),
            ("clean_physically", "dirty_physically"),
            ("kids", "risk_of_injury"),
            ("serious", "enjoyment"),
            ("serious", "sex"),
            ("serious", "dirty_spiritually")
        ]

        unsimilarity_score = 0

        for attr1, attr2 in attributes:
            if getattr(arg_a, attr1) and getattr(arg_b, attr2) or getattr(arg_b, attr1) and getattr(arg_a, attr2):
                unsimilarity_score += 1

        common_objects = set(arg_a.object_here) & set(arg_b.object_here)
        unsimilarity_score += 3 * len(common_objects)

        if arg_a.retail != arg_b.retail:
            unsimilarity_score+=1
        if arg_a.camera != arg_b.camera:
            unsimilarity_score+=1

        return unsimilarity_score

    unsimilarity_scores = [(pbs, calculate_unsimilarity(arg_a, pbs)) for pbs in PBS_1.all_PBS_1 if pbs != arg_a]
    unsimilarity_scores.sort(key=lambda x: x[1], reverse=True)

    formatted_result = "\n".join([f"Place: {pbs.PBS_1_name}, Unsimilarity Score: {score}" for pbs, score in unsimilarity_scores[:10]])
    return formatted_result

result = unsimilarity(_1_church)
print(result)
'''
