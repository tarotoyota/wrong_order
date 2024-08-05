# /home/tarotoyota/wrong_order_inst.py
from dataclasses import dataclass
from typing import List, ClassVar

@dataclass
class Place:
    ALL_PLACES: ClassVar[List['Place']] = []
    place_name        : List[str]
    vehivle_nature    :str # Vehicle -> "v", non-artificial nature -> "n"
    kid_old           :str # Highly associated with kids -> "k", olds -> "o"
    poor_sick         :str # Highly associated with poors -> "k", sick -> "o", both -> "b"
    weaks             :str # Highly associated with weaks -> "y"
    animal            :str # Facility with animals owned by humans -> "y"
    fun_for_kid_adult :str # Fun for kids -> "k", fun for adults -> "a", fun for both -> "b"
    serious           :str # Serious -> "y"
    not_facility      :str # Not a facility -> "y"
    food              :str # Highly associated with food -> "y"
    muscle_tissue_destroy : str # places for destroying muscle tissue or where there is destroyed muscle tissue, such as butcher.
    holy_unholy       :str # Commonly holy -> "h", unholy -> "u"
    clean_dirty       :str # Commonly dirty -> "d", clean -> "c"
    crime_ridden      :str # Crime ridden -> "y"
    risk_of_injury    :str # There is a high risk of injury to the user or customer -> "y"
    thrilling         :str # Thrilling -> "y"
    excite            :str # Exciting -> "y"
    affray            :str # Frequent affray -> "y"
    pick_up_spot      :str # Pick up spot -> "y"
    educational       :str # Educational -> "y"
    paid              :str # Takes user's money -> "y"
    bankrupt          :str # Can drive some people bankrupt -> "y"
    coupon            :str # Offers coupons -> "y"
    mourn             :str # Used for scattering or burial -> "y"
    normal_5tp1w      :str # Normal to visit 5+ times a week -> "y"
    acommodation      :str # facility with accommodation functions.
    better_leave      :str # You'd better leave quickly -> "y"
    sport             :str # place where multiple people can enjoy physical activity or compete -> "y"
    fire              :str # Highly associated with fire -> "y"
    water             :str # Highly associated with water -> "y"
    ground            :str # Highly associated with ground -> "y"
    emergency         :str # Emergency scene -> "y"
    retail_service_amusement_entertainment  :str # Retail industry -> "r", service industry -> "s", amusement industry -> "a", entertainment industry -> "e"
    show_human_animal_inanimate             :str # Show human -> "h", show animal -> "a", show inanimate -> "i"
    nudity_genital      :str #
    old_value           :str #
    quiet_should_be     :str




 # scream? excite, screamで代用

    def __hash__(self):
        return hash(self.place_name[0]) # Assuming Place_name is a list with a single name.
    def get_place_names(self):
        return self.place_name
    def __post_init__(self):
        Place.ALL_PLACES.append(self)

# Prompt = "  Define  _1_remain  instance   .Match the position of the text and whitespace to the existing instance."




#                                                          bui,kid,poo,wea,ani ,fun,ser,not ,foo,mus,hol,cle ,cri,ris ,thr,exc,afr ,pic ,edu  pai ban cou  mou,nor aco,bet,spo,fir,wat,gro,eme,ret,sho,nud,old,qui
_1_church                =Place(["church"                ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"h",""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
_1_mosque                =Place(["mosque"                ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"h",""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
_1_graveyard             =Place(["graveyard"             ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"h",""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"y")
_1_police_station        =Place(["police station"        ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_charity_event         =Place(["charity evenet"        ],"" ,"" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_mountain              =Place(["mountain"              ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_volcano               =Place(["volcano"               ],"n","" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_lost_child_department =Place(["lost child department" ],"" ,"k","" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_animal_shelter        =Place(["animal shelter"        ],"" ,"" ,"" ,"" ,"y" ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_parking_lot           =Place(["parking lot"           ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_lost_and_found        =Place(["lost and found"        ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_dumpyard              =Place(["dumpyard"              ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,"d" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_public_restroom       =Place(["public restroom"       ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,"d" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"y","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y","" ,"" )
_1_tent_city             =Place(["tent_city"             ],"" ,"" ,"p","y",""  ,"" ,"y","y" ,"" ,"" ,"u","d" ,"y",""  ,"" ,"" ,"y" ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_slum                  =Place(["slum"                  ],"" ,"" ,"p","y",""  ,"" ,"y","y" ,"" ,"" ,"u","d" ,"y",""  ,"y","" ,"y" ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_beggar_scene          =Place(["beggar scene"          ],"" ,"" ,"p","y",""  ,"" ,"y","y" ,"" ,"" ,"u","d" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_payday_loan           =Place(["payday loan"           ],"" ,"" ,"p","y",""  ,"" ,"y",""  ,"" ,"" ,"u",""  ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","y","" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_prison                =Place(["prison"                ],"" ,"" ,"b","y",""  ,"" ,"y",""  ,"" ,"" ,"u",""  ,"y",""  ,"y","" ,"y" ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_orphanage             =Place(["orphanage"             ],"" ,"k","" ,"y",""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_taxi                  =Place(["taxi"                  ],"v","" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_airplane              =Place(["airplane"              ],"v","" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"y","" ,"y" ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
_1_fountain              =Place(["fountain"              ],"" ,"" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"i","" ,"" ,"" )
_1_womans_house          =Place(["woman's house"         ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_food_bank             =Place(["food bank"             ],"" ,"" ,"p","y",""  ,"" ,"y",""  ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" )
_1_evacuation_center     =Place(["evacuation center"     ],"" ,"" ,"" ,"y",""  ,"" ,"y",""  ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
_1_homeless_shelter      =Place(["homeless shelter"      ],"" ,"" ,"p","y",""  ,"" ,"y",""  ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"y")
_1_flood_scene           =Place(["flood scene"           ],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"y","" ,"y","" ,"" ,"" ,"" ,"" )
_1_fire_scene            =Place(["fire scene"            ],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"y","" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"y","" ,"" ,"y","" ,"" ,"" ,"" ,"" )
_1_robbery_scene         =Place(["robbery scene"         ],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" )
_1_fight_scene           =Place(["fight scene"           ],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" )
_1_murder_scene          =Place(["murder scene"          ],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"y","" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" )
_1_traffic_accident_scene=Place(["traffic accident scene"],"" ,"" ,"" ,"" ,""  ,"" ,"y","y" ,"" ,"y","" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"y","" ,"y","" ,"" ,"y","" ,"" ,"" ,"" ,"" )
_1_massage_parlour       =Place(["massage parlour"       ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_wedding_hall          =Place(["wedding hall"          ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"h",""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_hotel                 =Place(["hotel"                 ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"y")
_1_terminal_ward         =Place(["terminal ward"         ],"" ,"" ,"s","y",""  ,"" ,"y",""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"y")
_1_psychiatric_ward      =Place(["psychiatric ward"      ],"" ,"" ,"s","y",""  ,"" ,"y",""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"y","y","" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_dental_clinic         =Place(["dental clinic"         ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_laundry               =Place(["laundry"               ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_funeral_home          =Place(["funeral home"          ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"y","h","c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_crematorium           =Place(["crematorium"           ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"y","h","c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_kindergarten          =Place(["kindergarten"          ],"" ,"k","" ,"" ,""  ,"k","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_obstetrics            =Place(["obstetrics"            ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"h","c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_brothel               =Place(["brothel"               ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"u",""  ,"" ,""  ,"" ,"y",""  ,""  ,""  ,"y","y","y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"y","" ,"" )
_1_nursing_home          =Place(["nursing home"          ],"" ,"o","" ,"y",""  ,"" ,"" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"" )
_1_hospital              =Place(["hospital"              ],"" ,"" ,"s","y",""  ,"" ,"y",""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","y","" , "" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"s","" ,"" ,"" ,"y")
_1_pharmacy              =Place(["pharmacy"              ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_steak_house           =Place(["steak house"           ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"y","y","" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"r","" ,"" ,"" ,"y")
_1_butcher               =Place(["butcher"               ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"y","y","" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"y","" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_restaurant            =Place(["restaurant"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"y","y","" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"y","" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_fish_market           =Place(["fishmarket"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"y","y","" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"y","" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_car_dealer            =Place(["car dealer"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_farm                  =Place(["farm"                  ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,""  ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"r","" ,"" ,"" ,"" )
_1_livestock_farm        =Place(["livestock farm"        ],"" ,"" ,"" ,"" ,"y" ,"" ,"" ,""  ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" ,""  ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"r","" ,"" ,"" ,"" )
_1_apple_store           =Place(["apple store"           ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_cloth_shop            =Place(["cloth shop"            ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_camp_gear_shop        =Place(["camp gear shop"        ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_bar                   =Place(["bar"                   ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,"y" ,"y" ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"y")
_1_ticket_machine        =Place(["ticket machine"        ],"" ,"" ,"" ,"" ,""  ,"" ,"" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_wallet_shop           =Place(["wallet shop"           ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_flower_shop           =Place(["flower shop"           ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_antique_shop          =Place(["antique shop"          ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"y","y")
_1_ice_cream_truck       =Place(["ice cream truck"       ],"v","k","" ,"" ,""  ,"k","" ,"y" ,"y","" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"r","" ,"" ,"" ,"" )
_1_museum                =Place(["museum"                ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"y","y")
_1_ancient_tree          =Place(["ancient tree"          ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"y","" )
_1_remains               =Place(["remains"               ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"y","" )
_1_gallery               =Place(["gallery"               ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"y","y")
_1_botanical_garden      =Place(["botanical_garden"      ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"" ,"" )
_1_light_show            =Place(["light show"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"" ,"" )
_1_library               =Place(["library"               ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"" ,"y")
_1_war_memorial          =Place(["war memorial"          ],"" ,"" ,"" ,"" ,""  ,"" ,"y",""  ,"" ,"" ,"h",""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","i","" ,"" ,"y")
_1_rock_concert          =Place(["rock concert"          ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"y",""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_classic_concert       =Place(["classic concert"       ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","" ,"" ,"y")
_1_comedy_club           =Place(["comedy club"           ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_magic_show            =Place(["magic show"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_boxing_ring           =Place(["boxing ring "          ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y","y" ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_soccer_ground         =Place(["soccer ground"         ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y","y" ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"y","" ,"" ,"y","" ,"e","h","" ,"" ,"" )
_1_strip_club            =Place(["strip club"            ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"u",""  ,"" ,""  ,"" ,"y",""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","y","" ,"" )
_1_fire_dance_scene      =Place(["fire dance scene"      ],"" ,"" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_zoo                   =Place(["zoo"                   ],"" ,"" ,"" ,"" ,"y" ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"y",""  ,""  ,"y" ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","a","" ,"" ,"" )
_1_safari                =Place(["safari"                ],"" ,"" ,"" ,"" ,"y" ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"y",""  ,""  ,"y" ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","a","" ,"" ,"" )
_1_aquarium              =Place(["aquarium"              ],"" ,"" ,"" ,"" ,"y" ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,"y" ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"e","a","" ,"" ,"" )
_1_haunted_house         =Place(["haunted house"         ],"" ,"" ,"" ,"" ,""  ,"k","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"e","h","" ,"" ,"" )
_1_racetrack             =Place(["racetrack"             ],"" ,"" ,"" ,"" ,"y" ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"y","y","" , "" ,"" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"a","a","" ,"" ,"" )
_1_night_club            =Place(["night club"            ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"u",""  ,"y",""  ,"" ,"y","y" ,"y" ,""  ,"y","" ,"" ,""  ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_roller_coaster        =Place(["roller coaster"        ],"v","" ,"" ,"" ,""  ,"k","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_sandbox               =Place(["sandbox"               ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"a","" ,"" ,"" ,"" )
_1_swing_set             =Place(["swing set"             ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_trampline             =Place(["trampoline"            ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_water_slide           =Place(["water slide"           ],"" ,"k","" ,"" ,""  ,"k","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","y",""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"" ,"" ,"" )
_1_jungle_gym            =Place(["jungle gym"            ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_merry_go_round        =Place(["merry-go-round"        ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_see_saw               =Place(["see-saw"               ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"y","" ,""  ,""  ,""  ,"" ,"" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_coin_pusher           =Place(["coin pusher"           ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_genie_machine         =Place(["genie machine"         ],"" ,"k","" ,"" ,""  ,"k","" ,"y" ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_escape_room           =Place(["escape room"           ],"" ,"" ,"" ,"" ,""  ,"k","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"y","" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_pool                  =Place(["pool"                  ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"y","" ,"" )
_1_ice_rink              =Place(["ice rink"              ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"y",""  ,""  ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_sauna                 =Place(["sauna"                 ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,""  ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"y", "" ,"y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"y","" ,"" )
_1_casino                =Place(["casino"                ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"u",""  ,"" ,""  ,"y","y",""  ,""  ,""  ,"y","y","y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_hot_spring            =Place(["hot spring"            ],"" ,"" ,"" ,"" ,""  ,"a","" ,""  ,"" ,"" ,"" ,"c" ,"" ,""  ,"" ,"" ,""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"y","" ,"" )
_1_ski_area              =Place(["ski area"              ],"" ,"" ,"" ,"" ,""  ,"b","" ,""  ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"y",""  ,"y" ,""  ,"y","" ,"y", "" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_beach                 =Place(["beach"                 ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,"y" ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"y","" ,"" )
_1_forest                =Place(["forest"                ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"" ,"" ,"" ,"a","" ,"" ,"" ,"" )
_1_river                 =Place(["river"                 ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"" ,"" ,"" )
_1_campground            =Place(["campground"            ],"" ,"" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"y",""  ,""  ,""  ,"y","" ,"" , "" ,"" ,"y","" ,"" ,"y","" ,"y","" ,"a","" ,"" ,"" ,"" )
_1_ocean                 =Place(["ocean"                 ],"n","" ,"" ,"" ,""  ,"b","" ,"y" ,"" ,"" ,"" ,""  ,"" ,"y" ,"" ,"" ,""  ,""  ,""  ,"" ,"" ,"" , "y","" ,"" ,"" ,"" ,"" ,"y","" ,"" ,"a","" ,"" ,"" ,"" )



inst_old_value=[]
inst_new_value=[]
inst_retail=[]
inst_retail_service=[]
inst_sick=[]
inst_poor=[]
inst_emergency_scene=[]

inst_quiet_should_be=[]
inst_scream_noisy=[]

inst_excite_thrilling=[]
inst_kid=[]


for i in Place.ALL_PLACES:
    if       i.old_value:
        inst_old_value.append(i.place_name[0])
    elif not i.old_value and i.paid and not i.not_facility and i.retail_service_amusement_entertainment:
        inst_new_value.append(i.place_name[0])
    if i.retail_service_amusement_entertainment == 'r':
        inst_retail.append(i.place_name[0])
    if i.retail_service_amusement_entertainment == 'r' or i.retail_service_amusement_entertainment == 's':
        inst_retail_service.append(i.place_name[0])
    if     i.poor_sick == 's' or i.poor_sick == 'b':
        inst_sick.append(i.place_name[0])
    if     i.poor_sick == 'p' or i.poor_sick == 'b':
        inst_poor.append(i.place_name[0])
    if i.emergency:
        inst_emergency_scene.append(i.place_name[0])
    if i.quiet_should_be:
        inst_quiet_should_be.append(i.place_name[0])
    if i.excite or i.thrilling and not i.quiet_should_be:
        inst_scream_noisy.append(i.place_name[0])

    if i.excite or i.thrilling:
        inst_excite_thrilling.append(i.place_name[0])
    if i.kid_old == 'k':
        inst_kid.append(i.place_name[0])

#for i in Place.ALL_PLACES:
#    print(','.join(i.place_name), end=',')

all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,livestock farm,botanical_garden,hot_spring,burning house,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,
"""
# These are Place instances' .name. Place instances' name start with "_1_"

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

all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,livestock farm,botanical_garden,hot_spring,burning house,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,
"""
# These are Place instances' .name. Place instances' name start with "_1_"


#.be_when is required for important timings such as critical conditions, funerals, childbirth, graduation ceremony etc. Do not set .be_when on instances in places that are not related to these important timings.
#In other word, the "important timings" mentioned here are times when you should not go to the casino if your family is in that situation.

_1_church       .be_when=["wife's funeral"]
_1_obstetrics   .be_when=["wife was in labor"]
_1_hospital     .be_when=["wife was in critical condition"]
_1_funeral_home .be_when=["wife's funeral"]
_1_crematorium  .be_when=["wife's cremation"]
_1_terminal_ward.be_when=["wife was in critical condition"]
_1_kindergarten .be_when=["son's graduation ceremony"]
_1_wedding_hall .be_when=["son's wedding"]
_1_graveyard    .be_when=["wife's funeral"]

#for i in PBS_1.all_PBS_1:
#  if hasattr(i, 'be_when'):
#    print(f"I was here when my {i.be_when}")

# Define new .be_when

############################

### weaks_watch ############

'''
enjoyment_watch_weaks = [i for i in Place.ALL_PLACES if i.show_human_animal_inanimate and not i.weaks]
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
# Task : make _1_ """ wedding_hall """ .weaks_watch in English in python.


############################



#### Complaint #############
all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,livestock farm,botanical_garden,hot_spring,burning house,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,
"""# These are Place instances' .name. Place instances' name start with "_1_"
@dataclass
class Complaint:
    ALL_COMPLAINTS: ClassVar[List['Complaint']] = []
    complaint_name: List[str]
    cope_had_bring:list # I had a staff to bring {cope_bring}
    cope_had_do:list # I had a staff {cope_do}
    because_my:list # I complained to them because my {because_my}
    noproblem   : List[Place]
    problem     : List[Place]
    def get_noproblem_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.noproblem)
    def get_problem_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.problem)
    def __post_init__(self):
        Complaint.ALL_COMPLAINTS.append(self)

#for i in Complaint.ALL_COMPLAINTS:
# print(f"I complained about the {i.problem} was {i.complaint_name} and scolded them, telling them it's like a {i.noproblem}.")


_c_loud     =Complaint(["loud"]       ,["ear plugs"]        ,["turn the volume down"],["wife is pregnant"]
                  ,[_1_rock_concert]
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

# Define new 5 Complaint instances without any explanations.
# Don't create an instance that is almost identical to an existing instance. For example, don't create _c_noisy instance when there's _c_loud instance. when there's _c_dangerous, don't create _c_unsafe. when there's _c_heady, don't create _c_unfriendly .
# Only respond new instances you defined.
# Align text and whitespace with existing instances.
# Don't define _c_crowded
# ''' 0 ''' new instances have been adopted. The others were rejected. Do not create rejected instances again.



"""
###### Self-criticism prompt #####

all_Place_instances="church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,"
# These are Place instances' .name. Place instances' name start with "_1_"

Please make sure and explain that the new instance you just created does not violate the following rules:

# Don't create an instance that is almost identical to an existing instance. For example, don't create _c_noisy instance when there's _c_loud instance. when there's _c_dangerous, don't create _c_unsafe. when there's _c_heady, don't create _c_unfriendly .
# Don't use the same Place instance multiple times.
# Do not create rejected instances again.
# Don't use a Place instance that doesn't exist.
"""

############################
##### stop ##################
all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,livestock farm,botanical_garden,hot_spring,burning house,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,
""" # These are Place instances' .name. Place instances' name start with "_1_"
@dataclass
class Stop:
    ALL_STOPS:ClassVar[List['Stop']] = []
    st_ali_statement: List[str]
    st_ali_place: List[Place]
    st_bob_place: List[Place]
    st_ali_statement2: List[str]
    def get_st_ali_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.st_ali_place)
    def get_st_bob_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.st_bob_place)
    def __post_init__(self):
        Stop.ALL_STOPS.append(self)

# I {st_ali_statement} in the {st_ali_place} and scolded them, telling them this wasn't a {st_bob_place}.

_s_stopped_a_fight      =Stop(["stopped a fight"]   , [_1_night_club]       , [_1_boxing_ring]      ,["I asked them why they were fighting.","I called the police.", "I kicked them out of the place."])
_s_stopped_running      =Stop(["stopped running"]   , [_1_hospital]         , [_1_soccer_ground]    ,["I asked them why they were running.","I called the police.", "I scolded them because it was dangerous."])
_s_stopped_laughing     =Stop(["stopped laughing"]  , [_1_homeless_shelter] , [_1_comedy_club]      ,["I asked them why they were laughing.","I asked them to show some respect.", "I scolded him for laughing at someone who was working hard."])#gpt4
_s_stopped_playing      =Stop(["stopped playing"]   , [_1_classic_concert]          , [_1_kindergarten]     ,["I asked them why they were playing.","I told them it was time to pay attention.", "I asked them to sit down quietly."])#gpt4
_s_stopped_eating       =Stop(["stopped eating"]    , [_1_library]          , [_1_restaurant]       ,["I asked them why they were eating."])#gpt4
_s_stopped_screaming    =Stop(["stopped screaming"] , [_1_library]          , [_1_haunted_house, _1_roller_coaster]         ,["I asked them to be quiet."])#gpt4
_s_stopped_talking      =Stop(["stopped talking"]   , [_1_library, _1_classic_concert]          , [_1_comedy_club]      ,["I asked them why they were talking.", "I told them to be quiet.", "I asked them to step outside if they needed to talk."])#gpt4
_s_stopped_driving      =Stop(["stopped driving"]   , [_1_bar]              , [_1_taxi]             ,["I asked him why he was trying to drive.", "I told him not to drive and called the police."])
_s_stopped_kissing      =Stop(["stopped kissing"]   , [_1_library]          , [_1_wedding_hall]     ,["I scolded them, why you were kissing.", "I asked them to leave."]) # gemini
_s_stopped_littering    =Stop(["stopped littering"] , [_1_beach] , [_1_dumpyard] ,["I asked them why they were littering.", "I told them to pick up their trash.", "I informed them about the importance of keeping the place clean."]) # gpt4
_s_stopped_excreting    =Stop(["stopped excreting"] , [_1_river] , [_1_public_restroom], ["I asked them why they were excreting.", "I told them this is not a proper place.", "I asked them to use proper facilities."]) # gpt4
_s_stopped_to_refuse_to_pay = Stop(["stopped to refuse to pay"], [_1_restaurant], [_1_robbery_scene], ["I asked them why they were refusing to pay.","I called the police.", "I reminded them of their obligation to settle the bill."])
# Define new Stop instances without any explanations. Only respond new instances you defined. Start answer with ```python



# define _s_stopped_to_refuse_to_pay without any explanations. Only respond new instances you defined. Start answer with ```python

_s_stopped_fight_for_the_ball =Stop(["stopped fighting for the ball"], [_1_kindergarten], [_1_soccer_ground], ["I asked them why they were fighting for the ball.", "I told them to share the ball."]) # This instance cannot be generated with the prompt "# I {st_ali_statement} in the {st_ali_place} and scolded them, telling them this wasn't a {st_bob_place}."

############################
############################





############################
#### Belong ################
all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,livestock farm,botanical_garden,hot_spring,burning house,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,
"""
# These are Place instances' .name. Place instances' name start with "_1_"
@dataclass
class Belong: # Use for misun_thief()
    ALL_BELONGS:ClassVar[List['Belong']] = []
    belong_name:str
    place_where_x_is_but_you_cannot_get_others_x: List[Place] # x means "belong_name"
    place_where_x_is_but_you_can_get_others_x: List[Place]  # x means "belong_name"

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
# Define 10 new Belong instance in English without any explanations.


# ''' 0 ''' new instances have been adopted. The others were rejected. Do not create rejected instances again.

"""
###### Self-criticism prompt #####

all_Place_instances="church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,robbery scene,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,sandbox,farm,"
# These are Place instances' .name. Place instances' name start with "_1_"


Please make sure that the new instance you just created does not violate the following rules:

# Do not create an instance that is nearly identical to an existing instance.
# Don't use the same Place instance multiple times.
# Do not create rejected instances again.
# Don't use a Place instance that doesn't exist.
"""
############################
############################
"""
Misunderstand type comedy creation task. Answer in English.
The spekaer talk about x(zoo, safari, etc.). The listener mistakes that the speaker is talking about y(butcher, restaurant, etc.)
"""
ate_inedible_animal_1_general=["There were a lot of animal", "I'm glad they are protected from poachers.", "I gave my pets to them, I can't keep them so I have no choice.", "There were a lot of rescued animals there."]

_1_zoo.ate_inedible_animal_1=["There was an endangered species section.", "There was a gorilla section.", "They had a special event to celebrate the birth of a new animal."]
_1_safari.ate_inedible_animal_1=["There was an endangered species section.", "There was a lot of gorilla section."]
_1_animal_shelter.ate_inedible_animal_1=["I found many dogs and cats there.", "It was sad to see so many abandoned pets.", "It was heartwarming to see them being nursed back to health."]
_1_aquarium.ate_inedible_animal_1 = ["I saw whales and dolphins there."]

"""
Add statements that would surprise or make angry the listener if the speaker uttered it.
If Ali says "It was sad to see so many abandoned pets.", it's funny because based on Bob's misunderstanding, Ali ate the animal after feeling pity for it.

Rules=[
Don't just add different animal names, like "There were many lions" or "The sea turtles were huge." That's just bulking things up, not enriching the content.
Don't add a sentence like "S + V + [animal genre name]."  , like "There were many lions" or "The sea turtles were huge.
Don't add a sentence like "The guided tour was very adventurous.", "They have a great adoption program." or "The jellyfish exhibit was mesmerizing." because it makes it clear that the place the speaker is referring to is not a butcher shop or a restaurant.
Don't add sentences that are nearly identical to existing sentences.
]
"""
####
"""
Please check that the sentences you have just added do not violate the following rules:

Don't just add different animal names, like "There were many lions" or "The sea turtles were huge." That's just bulking things up, not enriching the content.
Don't add a sentence like "S + V + [animal genre name]."  like "The penguins were very playful.", "There were many lions" or "The sea turtles were huge.
Don't add a sentence like "The guided tour was very adventurous." or "They have a great adoption program." or "The jellyfish exhibit was mesmerizing." because it makes it clear that the place the speaker is referring to is not a butcher shop or a restaurant.
Don't add sentences that are nearly identical to existing sentences.
"""

############################
############################








############################
############################

# Misunderstand type comedy creation task.
# The spekaer talk about x. The listener mistakes that the speaker is talking about [' brothel '].
# What kind of statements will surprise the listener when uttered by the speaker?



# MAKE _1_aquarium.ate_inedible_animal_1

#Add new English statements in these lists

# Define new x and the sentences.

############################
############################




all_Place_instances="""
church,mosque,casino,brothel,strip club,nursing home,dumpyard,mountain,volcano,kindergarten,obstetrics,lost child department,zoo,safari,animal shelter,butcher,restaurant,fishmarket,aquarium,car dealer,parking lot,flower shop,graveyard,war memorial,wallet shop,lost and found,gallery,public restroom,river,ocean,beach,forest,hotel,ice rink,concert,library,sauna,ski area,haunted house,magic show,ticket machine,escape room,pool,tent_city,slum,camp gear shop,terminal ward,psychiatric ward,comedy club,genie machine,antique shop,museum,bar,beggar scene,charity evenet,dental clinic,payday loan,prison,hospital,pharmacy,orphanage,apple store,laundry,cloth shop,roller coaster,taxi,airplane,light show,funeral home,crematorium,steak house,police station,elephant,wedding hall,night club,fountain,farm,livestock farm,botanical_garden,hot spring,woman's house,food bank,evacuation center,homeless shelter,boxing ring ,soccer ground,sandbox,swing set,trampoline,water slide,jungle gym,merry-go-round,see-saw,ice cream truck,coin pusher,massage parlour,fire dance scene,campground,flood scene,fire scene,robbery scene,fight scene,murder scene,traffic accident scene,racetrack,
"""
# These are Place instances' .name. Place instances' name start with "_1_"
@dataclass
class Freepick: # This class is for creating misunderstand type comedy. Ali talks about fp_ali_place but Bob mistook it for about fp_bob_place
    ALL_FREEPICKS:ClassVar[List['Freepick']] = []
    fp_ali_statement: List[str]
    fp_ali_place: List[Place]
    fp_bob_place: List[Place]
    fp_ali_statement2: List[str]
    def get_fp_ali_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.fp_ali_place)
    def get_fp_bob_place_names(self):
        return ", ".join(place.get_place_names()[0] for place in self.fp_bob_place)
    def __post_init__(self):
        Freepick.ALL_FREEPICKS.append(self)

_f_grilled_meat         =Freepick(["grilled meat"]      , [_1_steak_house]      , [_1_crematorium]      ,["Meat juices splashed onto my clothes.","It was difficult to flip it over.","I inserted a skewer to check the doneness."])
# Cremators and steakhouses are both places where meat is grilled. One of these places is negative.
_f_enjoyed_plant        =Freepick(["enjoyed plant"]     , [_1_botanical_garden] , [_1_night_club]       ,["I was introduced to a variety of plants.", "I saw rare leaves and exotic mushrooms."])
# Plants in a nightclub represent illegal drugs.
_f_gave_my_pet          =Freepick(["gave my pet"]       , [_1_animal_shelter]   , [_1_butcher]          ,["This can't be helped since I can no longer keep pets."])
#
_f_celebrated_mass      =Freepick(["celebrated mass"]   , [_1_church]           , [_1_mosque]           ,["I donated a christmas tree."])
# It means religious harassment.
_f_gave_alcohol         =Freepick(["gave alcohol"]      , [_1_womans_house]     , [_1_mosque]           ,["I spent a month thinking about what to give her to make her happy."])
# It means religious harassment.
_f_took_a_ride          =Freepick(["took a ride"]       , [_1_roller_coaster]   , [_1_police_station]   ,["The experience was thrilling and fun.", "I couldn't stop screaming.", "I would definitely do it again."]) # gpt4
# This sentence creates the misunderstanding that the speaker got into the police car, i.e., the speaker was arrested.
_f_broke_in             =Freepick(["broke in"]          , [_1_fire_scene]       , [_1_womans_house]     ,["Next thing I knew, I had broken the glass and was inside.", "I did it for her", "Before I knew it, I was hugging her."])
# Ali saves a life at the fire scene. Bob mistakenly believes Ali committed a break-in and rape.
_f_hunted_animals       =Freepick(["hunted animals"]    , [_1_forest]           , [_1_zoo]              ,[])
#
_f_bet_on_who_d_be_first=Freepick(["bet on who'd be first"],[_1_racetrack]      , [_1_terminal_ward]    ,["I was disappointed when the one my son bet on came in first."])
# This creates the misunderstanding that the speaker has made a bet on who will be the first in the terminal ward to die.
_f_bought_bair          =Freepick(["bought bair"]       , [_1_butcher]          , [_1_zoo, _1_safari]   ,["I bought it for everyone at work, so I'll bring it tomorrow.","You don't want one? Well, bears do stink a little."])
#
_f_bought_whale         =Freepick(["bought whale"]      , [_1_butcher]          , [_1_ocean]            ,["I bought it for everyone at work, so I'll bring it tomorrow.","You don't want one? Well, whales do stink a little."])
#
_f_saw_a_fire_dance     =Freepick(["saw a fire dance"]  , [_1_fire_dance_scene] , [_1_fire_scene]       ,["We all took pictures of the fire dance.", "After the dance was over, I wanted to watch it again."])
# Ali saw the fire dance. Bob mistakenly believes that Ali enjoyed watching the burning humans.


# Define new 5 Freepick instances in English. respond only new instances you defined. Note which existing instances each instance you create is similar to.

# Add new statements in each .fp_ali_statement2
############################
############################

"""



@dataclass
class Misunderstand: # This class is for creating misunderstand comedy.
    ali_statement: List[str] # Should be V-PAST+O or V-PAST
    normal_place: List[Place]
    eric_cartman_place: List[Place]

grilled_meat        =Misunderstand(["grilled meat"]     , [_1_steak_house]      , [_1_crematorium])
enjoyed_plant       =Misunderstand(["enjoyed plant"]    , [_1_botanical_garden] , [_1_night club]) # If there's a plant in night club, it's an illegal drug.
gave_my_pet         =Misunderstand(["gave my pet"]      , [_1_animal_shelter]   , [_1_butcher])
celebrated_mass     =Misunderstand(["celebrated mass"]  , [_1_church]           , [_1_mosque])
_f_gave_alcohol     =Misunderstand(["gave alcohol"]     , [_1_womans_house]     , [_1_mosque])
took_a_ride         =Misunderstand(["took a ride"]      , [_1_roller_coaster]   , [_1_police_station]) # GPT4 # Bob mistakenly believes Ali rode a police car.

bought_drug         =Misunderstand(["bought drug"]      , [_1_pharmacy]         , [_1_night club])
fished              =Misunderstand(["fished"]           , [_1_river]            , [_1_aquarium])
swam                =Misunderstand(["swam"]             , [_1_pool]             , [_1_fountain])
broke_vase          =Misunderstand(["broke vase"]       , [_1_home]             , [_1_museum]) # gemini
fixed_car           =Misunderstand(["fixed car"]        , [_1_garage]           , [_1_museum]) # GPT4
took_a_photo        =Misunderstand(["took a photo"]     , [_1_mountain]         , [_1_public_restroom])
cleaned_up          =Misunderstand(["cleaned up"]       , [_1_park]             , [_1_banksy_graffiti])
cultivated_crops    =Misunderstand(["cultivated crops"] , [_1_farm]             , [_1_graveyard])
dug_the_ground      =Misunderstand(["dug the ground"]   , [_1_sandbox]          , [_1_graveyard])
watched_animals     =Misunderstand(["watched animals"]  , [_1_zoo]              , [_1_butcher]) # GPT4
took_a_bath         =Misunderstand(["took a bath"]      , [_1_sauna]            , [_1_fountain]) # GPT4
saw_a_show          =Misunderstand(["saw a show"]       , [_1_theater]          , [_1_courtroom]) # GPT4
got_flowers         =Misunderstand(["got flowers"]      , [_1_flower_shop]      , [_1_graveyard]) # GPT4
watched_a_movie     =Misunderstand(["watched a movie"]  , [_1_cinema]           , [_1_prison]) # GPT4# Bob will mistakenly believe that Ali was once an inmate.
played_with_kids    =Misunderstand(["played with kids"] , [_1_kindergarten]     , [_1_strip_club]) # GPT4
bought_a_meal       =Misunderstand(["bought a meal"]    , [_1_restaurant]       , [_1_animal_shelter])#GPT4
loughed             =Misunderstand(["loughed"]          , [_1_comedy_club]      , [_1_psychiatric_ward])
hunted_animals      =Misunderstand(["hunted animals"]   , [_1_forest]           , [_1_zoo]) # GPT4

# Define new 10 instances without any explanations. Only respond new instances you defined.
# Bob has to mistake Ali for a pervert, crazy or criminal. Ali isn't
# Ali is not actually a criminal, pervert or crazy.
#Don't put place_name in the ali_statement. Bob won't be able to misunderstand.
# Don't use the same Place instance multiple times.
# ''' 0 ''' new instances have been adopted. The others were rejected. Do not create rejected instances again.

###### Self-criticism prompt #####

Please make sure that the new instance you just created does not violate the following rules:

# Bob has to mistake Ali for a pervert, crazy or criminal.
# Ali is not actually a criminal, pervert or crazy.
# .normal_place and eric_cartman_place should be choose from Place instances.
# Do not create an instance that is nearly identical to an existing instance.
# Don't put place_name in the ali_statement. Bob won't be able to misunderstand.
# Don't use the same Place instance multiple times.
# Do not create rejected instances again.
# Don't use a Place instance that doesn't exist.

"""

########
########
'''
for i in Place.ALL_PLACES:
    if i.ground and (not i.enjoyment or not i.enjoyment_watch):
        print(f"not {i.place_name}")
    if i.ground and (i.enjoyment or i.enjoyment_watch):
        print(f"{i.place_name}")
'''

_1_graveyard.ground_hps =["I buried my father here."]
_1_sandbox.ground_hps   =["I had fun digging here.", "I cleared away the stones here."]
_1_beach.ground_hps     =["I built a sandcastle here.", "I cleared away the stones here.", "I played volleyball here.", "I took a sand bath here."]
_1_farm.ground_hps      =["I cultivated crops here.", "I cleared away the stones here.", "I planted seeds here.", "The soil here is rich in nutrients.", "I turned over the ground with a spade here."]

# Add new English statements related to ground or sand in these lists. Start answer with ```python
# Please use pronouns instead of words like "meat" and "corpse" whenever possible.

####

'''

for i in Place.ALL_PLACES:
    if i.fire and (not i.enjoyment or not i.enjoyment_watch):
        print(f"not {i.place_name}")
    if i.fire and (i.enjoyment or i.enjoyment_watch):
        print(f"{i.place_name}")
'''


_1_volcano.fire_hps=["I saw magma there."]
_1_steak_house.fire_hps=["I grilled meat there.", "The juices got on my clothes.", "It was difficult to flip that.", "I checked the doneness by inserting a skewer into it.", "The doneness was set to rare.", "It's self-service, so you can use the griddle.", "The grill marks were perfect.","The aroma was mouth-watering.", "The sizzle was very satisfying."]
_1_fire_dance_scene.fire_hps=["I enjoyed their fire dancing."]
_1_campground.fire_hps=["We roasted marshmallows over it.","The warmth was comforting.","We told stories around it.","The crackling sound was soothing."]
_1_fire_scene.fire_hps=["I called the fire department.","The house burned down."]
_1_crematorium.fire_hps=["I had my father cremated there.", "It was neatly reduced to ashes."]


# Add new English statements in these lists. Start answer with ```python
# Please use pronouns instead of words like "meat" and "corpse" whenever possible.

####
'''

for i in Place.ALL_PLACES:
    if i.water and (not i.enjoyment or not i.enjoyment_watch):
        print(f"not {i.place_name}")
    if i.water and (i.enjoyment or i.enjoyment_watch):
        print(f"{i.place_name}")
'''

_1_river.water_hps=["I enjoyed swimming and fishing."]
_1_ocean.water_hps=["I enjoyed swimming, fishing and volleyball.", "I enjoyed getting a tan.", "I built a sandcastle.","It was crowded."]
_1_beach.water_hps=["I enjoyed swimming and volleyball", "I enjoyed getting a tan.", "I built a sandcastle.","It was crowded."]
_1_pool.water_hps=["I enjoyed swimming.","I practiced diving.","It was crowded."]
_1_fountain.water_hps=["I enjoyed watching it.","I threw a coin in for luck.", "It was a popular meeting spot.","The lights at night were stunning.",]
_1_hot_spring.water_hps=["I enjoyed bathing."]
_1_water_slide.water_hps=["I went down multiple times.","The speed was thrilling.",]
_1_flood_scene.water_hps=["I called the fire department.","The water level was rising quickly.","It caused a lot of damage.","People were being evacuated."]


# Add new English statements in these lists. Start answer with ```python
# Please use pronouns instead of words like "ocean" and "beach" whenever possible.

########
########



########
########









