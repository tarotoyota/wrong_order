# /home/tarotoyota/wrong_order_inst.py
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
    def get_place_names(self):
        return self.place_name
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
_1_elephant              =Place(["elephant"             ],"" ,"y","y" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" , "" ,"y","" ,"" , "" ,)



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

### be_when #################
all_Place_instance=['church', 'mosque', 'casino', 'brothel', 'strip club', 'nursing home', 'dumpyard', 'mountain', 'kindergarten', 'obstetrics', 'lost child department', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'parking lot', 'flower shop', 'graveyard', 'war memorial', 'wallet shop', 'lost and found', 'gallery', 'public restroom', 'river', 'ocean', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski area', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'tent_city', 'slum', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum', 'bar', 'robbery scene', 'beggar scene', 'charity evenet', 'dental clinic', 'payday loan', 'prison', 'hospital', 'pharmacy', 'orphanage', 'apple store', 'laundry', 'cloth shop', 'roller coaster', 'taxi', 'airplane', 'light show', 'funeral home', 'crematorium'
]# These are Place instances' .name. Place instances' name start with "_1_"

#.be_when is required for important timings such as critical conditions, funerals, childbirth, graduation ceremony etc. Do not set .be_when on instances in places that are not related to these important timings.
#In other word, the "important timings" mentioned here are times when you should not go to the casino if your family is in that situation.

_1_church       .be_when=["wife's funeral"]
_1_obstetrics   .be_when=["wife was in labor"]
_1_hospital     .be_when=["wife was in critical condition"]
_1_funeral_home .be_when=["wife's funeral"]
_1_crematorium  .be_when=["wife's cremation"]
_1_terminal_ward.be_when=["wife was in critical condition"]
_1_kindergarten .be_when=["son's graduation ceremony"]

#for i in PBS_1.all_PBS_1:
#  if hasattr(i, 'be_when'):
#    print(f"I was here when my {i.be_when}")

# Define new .be_when

############################

### weaks_watch ############

'''
enjoyment_watch_weaks = [i for i in Place.ALL_PLACES if i.enjoyment_watch and not i.weaks]
all_places_name_weaks_watch = [i.place_name[0] for i in enjoyment_watch_weaks]
print(all_places_name_weaks_watch)
'''

#['strip club', 'zoo', 'safari', 'aquarium', 'gallery', 'concert', 'library', 'magic show', 'comedy club', 'museum', 'light show']

# for misun_weaks()
_1_zoo.weaks_watch = ["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the cage stronger."]
_1_safari.weaks_watch=["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the electric fence stronger."]
_1_aquarium.weaks_watch=["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like there.","Their every movement is interesting.", "I talk them to make the glass stronger."]
_1_comedy_club.weaks_watch=["I often go to see them for a laugh.", "I love having a drink and laughing at their performances.", "I wish they'd improve the sound system", "It's exciting when they get on stage.", "It's a great place to unwind after a long day."]
_1_aquarium.weaks_watch = ["I often enjoy watching them.","I threw crumbs for them.","I hope they can continue to live in places like this, isolated from humans.","Their every movement is interesting.","I told them to make the glass stronger."]
_1_strip_club.weaks_watch = ["I enjoy having a drink while watching them.","I wish they'd improve the lighting.","It's exciting when they take the stage.","Sometimes get an erection.", "Put a dollar bill in their underwear."]
_1_magic_show.weaks_watch = ["I often go to see them for excitement.","I love watching them perform their tricks.","I wish they'd improve the lighting.","It's amazing how they manage to surprise the audience.","It's a great place to take friends for a fun night out."]

# These lists are meant to test the intelligence of the LLM by determining whether they can correctly identify where the speaker is talking about. Do not use words that could easily lead to a specific location (for example, do not use the words "aquarium" or "fish" in a list of aquariums).It is best to use the pronoun "they" whenever possible, regardless of whether the object is animate or inanimate.
# Task : make _1_ """ magic_show """ .weaks_watch in English in python.


############################



#### Complaint #############


@dataclass
class Complaint:
    ALL_COMPLAINTS: ClassVar[List['Complaint']] = []
    complaint_name: List[str]
    cope_had_bring:list # I had a staff to bring {cope_bring}
    cope_had_do:list # I had a staff {cope_do}
    because_my:list # I complained to them because my {because_my}
    noproblem:list # Place instance only
    problem:list # Place instance only
    def get_noproblem_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.noproblem)
    def get_problem_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.problem)
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


############################


#### Belong ################

'''
all_place_name = [i.place_name[0] for i in Place.ALL_PLACES]
print(all_place_name)
'''
all_PBS_1_instance=['church', 'mosque', 'casino', 'brothel', 'strip club', 'nursing home', 'dumpyard', 'mountain', 'kindergarten', 'obstetrics', 'lost child department', 'zoo', 'safari', 'animal shelter', 'butcher', 'restaurant', 'fishmarket', 'aquarium', 'car dealer', 'parking lot', 'flower shop', 'graveyard', 'war memorial', 'wallet shop', 'lost and found', 'gallery', 'public restroom', 'river', 'ocean', 'beach', 'hotel', 'ice rink', 'concert', 'library', 'sauna', 'ski area', 'haunted house', 'magic show', 'ticket machine', 'escape room', 'pool', 'tent_city', 'slum', 'camp gear shop', 'terminal ward', 'psychiatric ward', 'comedy club', 'genie machine', 'antique shop', 'museum', 'bar', 'robbery scene', 'beggar scene', 'charity evenet', 'dental clinic', 'payday loan', 'prison', 'hospital', 'pharmacy', 'orphanage', 'apple store', 'laundry', 'cloth shop', 'roller coaster', 'taxi', 'airplane', 'light show', 'funeral home', 'crematorium'
]# These are PBS_1 instances' .name

@dataclass
class Belong: # Use for misun_thief()
    ALL_BELONGS:ClassVar[List['Belong']] = []
    belong_name:str
    place_where_x_is_but_you_cannot_get_others_x:list # PBS_1 instance only # x means "belong_name"
    place_where_x_is_but_you_can_get_others_x:list # PBS_1 instance only # x means "belong_name"

    def get_cannot_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.place_where_x_is_but_you_cannot_get_others_x)
    def get_can_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.place_where_x_is_but_you_can_get_others_x)

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

############################
