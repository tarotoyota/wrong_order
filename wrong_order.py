# /home/tarotoyota/wrong_order.py
from master_class_saraba_func_py import apply_color_styles_saraba
from wrong_order_inst import Place
from wrong_order_inst import Complaint
from wrong_order_inst import Belong
from wrong_order_inst import Freepick
from wrong_order_inst import Stop
import re # for only extract_mirror_pairs
from collections import defaultdict # for only extract_mirror_pairs

def extract_mirror_pairs(nation_list):
    # nation_listがリストであることを確認
    if not isinstance(nation_list, list):
        raise ValueError("Input should be a list containing the nation string.")

    # リスト内の文字列を結合して一つの文字列にする
    nation_string = "".join(nation_list).strip()

    # ペアを解析するための辞書
    pair_dict = defaultdict(set)

    # 正規表現でペアを抽出し、辞書に格納
    for left, right in re.findall(r'\[(.*?)\s*:\s*(.*?)\]', nation_string):
        left = left.strip("[]").replace("'", "").replace(" ", "").split(',')
        right = right.strip("[]").replace("'", "").replace(" ", "").split(',')
        for l in left:
            for r in right:
                pair_dict[(l, r)].add(0)
                pair_dict[(r, l)].add(1)

    # ミラー対関係を探し、重複を取り除いて結果を返す
    return list(set(tuple(sorted(pair)) for pair, positions in pair_dict.items() if {0, 1} == positions))

def generate_html_table(title, hps_list, ali_imagines, bob_imagines):
    return f"""<table>
        <tr><th colspan="3">{title}</th></tr>
        <tr><th>HPS          <th><td> {hps_list}                        </td></tr>
        <tr><th>Ali imagines <th><td> {ali_imagines}                    </td></tr>
        <tr><th>Bob imagines <th><td> {bob_imagines}                    </td></tr>
        </table>"""

def gather_imagines(condition):
    ali_imagines = [i.place_name[0] for i in Place.ALL_PLACES if condition(i, 'Ali')]
    bob_imagines = [i.place_name[0] for i in Place.ALL_PLACES if condition(i, 'Bob')]
    return ali_imagines, bob_imagines

def wrong_order_func():
    base = []
    misun_pairs = []


    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # 人間向説明: hps_cb_use_x_for_y はrepositionerが"to substitute B for A."という形態をとれる時、HPSとして使用する。
    # たとえばA, B = (animal shelter, butcher)である時、"The (previously used / Originally planned) location became unavailable."という文は"近所の肉屋が閉店したから仕方なくアニマルシェルターで代用している"という誤解を招く。
    # Prompt for LLM: hps_cb_use_x_for_y explanation : This is a list of sentences with a high probability of appearing in the sentence "use place x for purpose y." Even if x and y are (church, wedding) or (kindergarten, leaving children) or (night club, picking up), the sentences in this list are likely to be used. Add new 5 statements in English without any explanations. The sentence you add should not contain a subject.

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    hps_genre=["substitution", "superior", "inferior", "mistake", "be recommended by", "use limits (exceed)", "use limits (below)", "ancillary service", "activation", "frequency", "positive poem", "boast", "bring others"]

    # well + explain
    # admittedly + inferior


    hps_cb_use_place_x_for_purpose_y = [
      "Everywhere was full."                                                    # substitution
    , "The (previously used / Originally planned) location became unavailable." # substitution
    , "There was a need to choose a location as close as possible."             # substitution, superior
    , "It was cheaper."                                                         # substitution, superior
    , "The ambiance suited."                                                    # superior
    , "Admittedly, it was a bit far."                                           # inferior
    , "It was recommended by the friend."                                       # recommended by
    , "I found out about it on a review site."                                  # recommended by
    , "My wife opposed my choosing this place."                                 # opposed + bring others
    , "I Went there by mistake as the (previously used / Originally planned) planned location." # mistake
    , "It's always nice to come here."                                          # frequency
    , "I used the photo for my New Year's card."           # Boast
    , "I was mistaken for a suspicious person." # damage
    , "It wasn't (crowded/empty) here."
    ]


    hps_vehicle=[
      "I took it from China to India."          # use limits (exceed)
    , "There were about {n} people on it."      # use limits (exceed)
    , "This only went {n} kilometers per hour." # use limits (exceed), use limits (below)
    , "There was on-board sales."               # ancillary service
    , "I put in high octane gasoline but for some reason, it didn't start." # activation + fail
    ]
    hps_5tp1w = [
      "I used to (come, use) here about five times a week." # frequency
    , "This is like my second home."                        # superior?
    , "I made friends with the people here."                # superior?
    , "This place is my escape from reality."               # superior?
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_to_prostitute = [
      "My son works here eight hours a day."                        # frequency
    , "It took a while for him to become a permanent employee here."#
    , "I'm proud to see him working so hard in a place like this."  # pos po
    , "I brag about this at family gatherings."                     # boast
    , "He received an award for his dedication here."               #
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    # Don't add sentences that mention topics that have already been mentioned.
    hps_sexual_if_olds=[
      "There were about 95 years old hugs."
    , "There were bedridden, demented, and wheelchair-bound olds."
    , "I hope there will be more opportunities like this."  # Positive poem
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_sexual_if_kids=[
      "There were about 4 years old children."
    , "I'll pick him up there."
    , "I saw a baby."
    , "I hope there will be more opportunities like this."  # Positive poem
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_sexual_if_animal=[
      "I saw monkeys there."
    , "I'll pick him up there."
    , "I saw a baby."
    , "I hope there will be more opportunities like this."  # Positive poem
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_kidnap = [
      "I met my son here for the first time and became a father."
    , "I brought my son home from here."
    , "This is a place of memories for me and my son."      # Positive poem
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_commercial = [
      "They accepted credit cards."                         # ancillary service
    , "They were handing out numbered tickets."             # ancillary service, popularity
    , "I got a receipt."                                    # ancillary service
    , "They gave me the correct change."                    # ancillary service
    , "They had a friend referral system."                  # ancillary service
    , "They gave me coupons."                               # ancillary service
    , "I failed at haggling."                               # fail
    , "For some reason, They didn't accept credit cards."   # ancillary service + fail
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_medicine = [
      "I pick up my drugs here regularly."
    , "I refused to take opioids."                      # damage + cope
    , "I have to be careful not to be overprescribed."  # damage + cope
    , "I'm worried about the side effects."             # damage + cope
    , "I accidentally took too much drugs once."        # damage
    , "I feel much better after taking the drug."
    , hps_cb_use_place_x_for_purpose_y
    ]


    hps_excrete = [
      "I excreted here."
    , "When I have diarrhea, I feel relieved when I find this place." # evaluate
    , "I complained because there was no toilet paper." # damage + cope
    , "I had to wait in line for a long time." # experience
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    hps_to_eat_inedible_animals_1=[ # Misunderstanding Comedy Creation Task. Answer in English. The speaker talks about x(butcher, restaurant, etc.) but the listener mistakes it for about y(zoo, animal shelter, etc.). Add new 5 statements without any explanations. Respond only new statements you added.
      "The food there is delicious."
    , "The food there is fresh and can be eaten raw or alive."
    , "I got food poisoning from the food there."
    , "I left a rating for it on yelp."
    , "It's Chiba's traditional food."
    , "I couldn't finish my meal, it was too much."
    , "This is too little and not satisfying."
    , "It wasn't crowded here."
    , hps_cb_use_place_x_for_purpose_y
    ]



    hps_eat=[
      "The food there is delicious."
    , "The food there is fresh and can be eaten raw or alive."  # superior
    , "I got food poisoning from the food there."               # damage
    , "I once had trash in the food there."                     # damage
    , "So I asked the person in charge there to apologize."     # damage + cope
    , "I left a rating for it on yelp."                         # evaluate
    , "For some reason there's not very well known."            # inferior
    , "It's true that there are a lot of (raw/spicy) foods."    # inferior
    , "It's Chiba's traditional food."
    , "(Condiments / staple foods) were free."                  # Ancillary Services
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_mourn=[
      "My father's grave is here."                  # usage revealing
    , "I attended a funeral here."                  # usage revealing
    , "I (buried him / scattered his ashes) here."  # usage revealing
    , "He loved this place."
    , "Our family often comes here to reflect."
    , "This place holds many of our memories."      # Pos p
    , "We shared stories about him here."           # Pos p
    , "We planted a tree here in his memory."
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    hps_wedding = [
      "I had my weeding here."
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_kids = [
      "I put my son here."                          # usage revealing
    , "I've been here on school trips."             # usage revealing
    , "My son didn't want to ge into here."         # be opposed
    , "I used to play here a lot as a child."       #
    , "When I was a child, I was left here until my parents finished work." #
    , "When I was a child, my father brought me here to study."             #
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    hps_olds = [
      "I put my grandfather here."                  # usage revealing
    , "My grandfather didn't want to go into here." # be opposed
    , "My grandfather made many friends here."      #
    , "He receives excellent care at this facility."#
    , "We visit him every weekend."                 #
    , "He enjoys the activities they offer here."   #
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_to_folk = [
      "I (had/bought) sex here."                    # usage revealing
    , "For some reason there was no sexual service."# inferior
    , "It's cheaper than call girls nearby."        # superior
    , "I always use rubbers properly."              # properly
    , "It's 300 dollars per hour."                  # cost
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_pick_up = [
      "I picked up girls here."                     # usage revealing
    , "For some reason the success rate was low."   # fail
    , "I made my girlfriend here."                  # usage revealing
    , "Unfortunately, I was found by the girl's boyfriend." # fail
    , "Unfortunately, I got rejected several times."# fail
    , "I come here every weekend."                  # frequency
    , "My friends wanted to go home, but I tried to pick up here." # be opposed + bring others
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_voyeur = [
      "I took a lot of good photos."
    , "I enjoyed the wonderful scenery."                #
    , "I'll use this photo for this year's Christmas card." # past melit
    , "This is one of my favorite shots."               # frequency
    , "I have it framed and displaying it."             # past melit
    , "I bought an expensive camera for this purpose."  # precost
    , "It was difficult to keep the subject still."     # difficulty
    , "My wife wanted to go home early."                # opposed + bring others
    , "I couldn't help but take a picture."             #???
    , "I'm planning to create a photo album."           # future plan
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    hps_complaint = [
      "My wife objected, but I lectured the person in charge."  # damage + cope + opposed
    , "I demanded a refund."                                    # damage + cope
    , "I gave it a low rating in an online review."             # damage + cope
    , "I scold the man in charge, but he didin't take action."  # damage + cope + fail
    , "I couldn't concentrate to (relaxing/reading/sleeping/eating)." # damage
    , "I cancelled my membership."                              # damage + cope
    , "There was inferior to the others."                       # frequency + inferior
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    hps_belong=[
      "I got one for my family."
    , "I asked for a refund as the one I got was faulty." # damage + cope
    , "My wife objected, but I asked for a refund as the one I got was faulty." # opposed + bring others
    , "I've been going there for about ten years." # frequency
    , "Because it's a special anniversary." #
    , "If I had the money I would buy a new one." #
    , "I use it every day."
    , "I'm worried this might get stolen."
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    hps_weaks = [
      "I often enjoy watching them here"
    , hps_cb_use_place_x_for_purpose_y
    ]
    hps_be_when=[
      "I went there as a top priority."
    , "My heart was beating hard as I headed there."
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_water=[ # Add 5 new English statements without any explanations. Only respond with new statements you added.
      "I (swam/fished/drunk the water) here."
    , "The water here is a little sweet."
    , "For some reason, I didn't catch anything."
    , "The sound of the water is very calming."
    , ""
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_ground=[
      "I (cultivated crops/dug the ground) here."
    , "Once something came out of the ground."
    , hps_cb_use_place_x_for_purpose_y
    ]

    hps_break_into=[
      "(Notice: The Ali imagine place was on fire.)"
    , "Before I knew it, I had broken the window and got inside."
    , "I did it for her."
    , "My body just moved on its own."
    , "I frantically searched around for the woman inside."
    ]





    ate_inedible_animal_1_general=["There were a lot of animal", "I'm glad they are protected from poachers.", "I gave my pets to them, I can't keep them so I have no choice.", "There were a lot of rescued animals there."]

    hps_game=["I do it while voice chatting with my colleagues.", "I stream myself doing this on youtube.", "I compete in this as a team." , "I want to become a pro at this."]




####

    def to_eat_inedible_animals_0(): # aia1 # to
        ali_places=[]
        bob_places=[]
        col=[]

        for i in Place.ALL_PLACES:
            if not i.food and i.animal and     hasattr(i, 'ate_inedible_animal_1'): # _1_zoo
                ali_places.append(i.place_name[0])
                col.append(f"<tr><td>{i.place_name}</td><td>{i.ate_inedible_animal_1}</td></tr>")
            if not i.food and i.animal and not hasattr(i, 'ate_inedible_animal_1'): #
                ali_places.append(i.place_name[0])
                col.append(f"<tr><td>{i.place_name}</td><td>                       </td></tr>")
            elif i.food and not i.animal and i.retail: # _1_restaurant
                bob_places.append(i.place_name[0])

        misun_pairs.append(f"[{ali_places} : {bob_places}]")

        table_to_eat_inedible_animals_0 = f"""<table>
        <tr><th colspan="2">to_eat_inedible_animals_0                </th></tr>
        <tr><th>HPS         </th><td>{ate_inedible_animal_1_general}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines    </th><th>HPS(depend on places)      </th></tr>
        {''.join(col)}
        <tr><th>Bob imagines    </th><th>                           </th></tr>
        <tr><td>{bob_places}    </td><th>                           </th></tr>
        </table>
        """

        return table_to_eat_inedible_animals_0

    table_to_eat_inedible_animals_0 = to_eat_inedible_animals_0()
    base.append(table_to_eat_inedible_animals_0)


    def to_eat_inedible_animals_1(i, person): # aia2
        if person == 'Ali':
            return     i.food and not i.animal and i.retail
        elif person == 'Bob':
            return not i.food and     i.animal

    ali_imagines, bob_imagines = gather_imagines(to_eat_inedible_animals_1)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_eat_inedible_animals_1", hps_eat, ali_imagines, bob_imagines))


####

    def to_folk_animals(): # fa1
        ali_places=[]
        bob_places=[]
        col=[]

        for i in Place.ALL_PLACES:
            if hasattr(i, 'ate_inedible_animal_1'): # _1_zoo
                ali_places.append(i.place_name[0])
                col.append(f"<tr><td>{i.place_name}</td><td>{i.ate_inedible_animal_1}</td></tr>")
            elif i.place_name == ['brothel']: # _1_brothel
                bob_places.append(i.place_name[0])

        misun_pairs.append(f"[{ali_places} : {bob_places}]")

        table_to_folk_animals = f"""<table>
        <tr><th colspan="3">to_folk_animals                      </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{ate_inedible_animal_1_general+hps_sexual_if_animal}              </td></tr>
        </table>
        <table>
        <tr><th>Ali imagines    </th><th>HPS(depend on places)  </th></tr>
        {''.join(col)}
        <tr><th>Bob imagines    </th><th>                       </th></tr>
        <tr><td>{bob_places}</td><th>                       </th></tr>
        </table>
        """

        return table_to_folk_animals

    table_to_folk_animals = to_folk_animals()
    base.append(table_to_folk_animals)


    def to_folk_kids(i, person):
        if person == 'Ali':
            return i.kids_olds == 'k'
        elif person == 'Bob':
            return i.place_name == ['brothel'] # _1_brothel

    ali_imagines, bob_imagines = gather_imagines(to_folk_kids)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_folk_kids", hps_kids+hps_sexual_if_kids, ali_imagines, bob_imagines))

    def to_folk_olds(i, person):
        if person == 'Ali':
            return i.kids_olds == 'o'
        elif person == 'Bob':
            return i.place_name == ['brothel'] # _1_brothel

    ali_imagines, bob_imagines = gather_imagines(to_folk_olds)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_folk_olds", hps_olds+hps_sexual_if_olds, ali_imagines, bob_imagines))

    def to_folk(i, person):
        if person == 'Ali':
            return i.place_name == ['brothel']
        elif person == 'Bob':
            return i.animal or i.kids_olds == 'k' or i.kids_olds == 'o'

    ali_imagines, bob_imagines = gather_imagines(to_folk)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_folk", hps_to_folk, ali_imagines, bob_imagines))



###

    hps_stop=["I scolded him, saying everyone is looking at you.", "I asked them to leave."]

    def to_stop():
        col=[]
        for i in Stop.ALL_STOPS:
            ali_places = i.get_st_ali_place_names()
            bob_places = i.get_st_bob_place_names()

            col.append(f"<tr><td>{ali_places}</td><td>{bob_places}</td><td>{i.st_ali_statement, i.st_ali_statement2}</td></tr>")

            misun_pairs.append(f"[{ali_places} : {bob_places}]")

        table_to_stop = f"""<table>
        <tr><th colspan="3">to_stop                                                 </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{hps_stop}              </td></tr>
        </table>
        <table>
        <tr><th>            </th><th>            </th><th>HPS(depend on places)     </th></tr>
        <tr><th>Ali imagines</th><th>Bob imagines</th><th>Ali says</tr>
        {''.join(col)}
        </table>
        """

        return table_to_stop

    table_to_stop = to_stop()
    base.append(table_to_stop)
###
    def to_steal():
        col=[]
        for i in Belong.ALL_BELONGS:
            ali_places = i.get_can_place_names()
            bob_places = i.get_cannot_place_names()

            col.append(f"<tr><td>{ali_places}</td><td>{bob_places}</td><td>{i.belong_name}</td></tr>")

            misun_pairs.append(f"[{ali_places} : {bob_places}]")

        table_to_steal = f"""<table>
        <tr><th colspan="3">to_steal                                                </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{hps_belong}              </td></tr>
        </table>
        <table>
        <tr><th>            </th><th>            </th><th>HPS(depend on places)     </th></tr>
        <tr><th>Ali imagines</th><th>Bob imagines</th><th>I got</tr>
        {''.join(col)}
        </table>
        """

        return table_to_steal

    table_to_steal = to_steal()
    base.append(table_to_steal)
###
    def condition_complaint():

        complaint_table_col = []

        for i in Complaint.ALL_COMPLAINTS:
            noproblem_places = i.get_noproblem_place_names()
            problem_places = i.get_problem_place_names()

            complaint_table_col.append(f"<tr><td>{problem_places}</td><td>{noproblem_places}</td><td>{i.complaint_name}<td>{i.cope_had_bring}</td><td>{i.cope_had_do}</td><td>{i.because_my}</td></tr>")
            misun_pairs.append(f"[{problem_places} : {noproblem_places}]")

        complaint_table = f"""<table>
        <tr><th colspan="3">condition_complaint                                     </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{hps_complaint}           </td></tr>
        </table>
        <table>
        <tr><th>            </th><th>            </th><th colspan = "4">HPS(depend on places)     </th></tr>
        <tr><th>Ali imagines</th><th>Bob imagines</th><th>I asked why it was so</th><th>I had the staff bring     </th><th>I had (the staff / to)</th><th>I complained because my</tr>
        {''.join(complaint_table_col)}
        </table>"""

        return complaint_table

    complaint_table = condition_complaint()
    base.append(complaint_table)


    def to_gawk_at():

        table_col = []

        condition_weaks_ali_imagines = []
        condition_weaks_bob_imagines = []

        for i in Place.ALL_PLACES:
            if hasattr(i, 'weaks_watch'): # _1_comedy_club
                condition_weaks_ali_imagines.append(i.place_name[0])
                table_col.append(f"<tr><td>{i.place_name}</td><td>{i.weaks_watch}</td>")
            elif (i.weaks and not hasattr(i, 'weaks_watch')) or i.emergency: # _1_homeless_shelter, _1_flood_scene
                condition_weaks_bob_imagines.append(i.place_name[0])


        misun_pairs.append(f"[{condition_weaks_ali_imagines} : {condition_weaks_bob_imagines}]")

        to_gawk_at_table = f"""<table>
        <tr><th colspan="2">to_gawk_at                          </th></tr>
        <tr><th>HPS                             </th><td>{hps_weaks}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines                    </th><th></th></tr>
        {''.join(table_col)}
        <tr><th>Bob imagines                    </th><th></th></tr>
        <tr><td>{condition_weaks_bob_imagines}  </td><td></td></tr>
        </table>"""

        return to_gawk_at_table, condition_weaks_ali_imagines, condition_weaks_bob_imagines
    to_gawk_at_table, condition_weaks_ali_imagines, condition_weaks_bob_imagines = to_gawk_at()
    base.append(to_gawk_at_table)


    def condition_be_when():
        name_and_be_when = []
        be_when_bob_imagines_name = []
        tmp_ali_imagines_name = []

        for i in Place.ALL_PLACES:
            if hasattr(i, 'be_when'):
                name_and_be_when.append(f"<tr><td>{i.place_name[0]}</td><td>I was here when my {i.be_when}</td></tr>")
                tmp_ali_imagines_name.append(i.place_name[0])
            elif i.holy_unholy == "u" and i.enjoyment:
                be_when_bob_imagines_name.append(i.place_name[0])

        be_when_table = f"""<table>
        <tr><th colspan="3">condition_be_when</th></tr>
        <tr><th>HPS                         </th><td>{hps_be_when}          </td></tr>
        <tr><th>Ali imagines                </th><th>HPS(depend on places)  </th></tr>
        {''.join(name_and_be_when)}
        <tr><th>Bob imagines                </th></tr>
        <tr><td>{be_when_bob_imagines_name} </td></tr>
        </table>"""

        misun_pairs.append(f"[{tmp_ali_imagines_name} : {be_when_bob_imagines_name}]")
        return be_when_table, tmp_ali_imagines_name, be_when_bob_imagines_name

    be_when_table, tmp_ali_imagines_name, be_when_bob_imagines_name = condition_be_when()
    base.append(be_when_table)

    def to_sneak_a_photo(i, person):
        if person == 'Ali':
            return i.camera_ok_ban == "o"
        elif person == 'Bob':
            return i.camera_ok_ban == "b"

    ali_imagines, bob_imagines = gather_imagines(to_sneak_a_photo)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_sneak_a_photo", hps_voyeur, ali_imagines, bob_imagines))

    def to_pick_up(i, person):
        if person == 'Ali':
            return i.pick_up_spot
        elif person == 'Bob':
            return i.holy_unholy == "h" or i.kids_olds == "k" or i.serious

    ali_imagines, bob_imagines = gather_imagines(to_pick_up)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_pick_up", hps_pick_up, ali_imagines, bob_imagines))



    def condition_kids(i, person):
        if person == 'Ali':
            return i.kids_olds == 'k' or i.educational
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_kids)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_kids", hps_kids, ali_imagines, bob_imagines))

    def condition_olds(i, person):
        if person == 'Ali':
            return i.kids_olds == 'o'
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_olds)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_olds", hps_olds, ali_imagines, bob_imagines))

    def condition_mourn(i, person):
        if person == 'Ali':
            return i.mourn
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.enjoyment

    ali_imagines, bob_imagines = gather_imagines(condition_mourn)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_mourn", hps_mourn, ali_imagines, bob_imagines))

    def condition_wedding(i, person):
        if person == 'Ali':
            return hasattr(i, 'wedding')
        elif person == 'Bob':
            return hasattr(i, 'sex') or (i.holy_unholy == "u" or i.clean_dirty == "d") and not i.enjoyment  #_1_dumpyard

    ali_imagines, bob_imagines = gather_imagines(condition_wedding)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_wedding", hps_wedding, ali_imagines, bob_imagines))


    def condition_excrete(i, person):
        if person == 'Ali':
            return hasattr(i, 'excrete')
        elif person == 'Bob':
            return i.food or i.clean_dirty == "c" or i.holy_unholy == "h"

    ali_imagines, bob_imagines = gather_imagines(condition_excrete)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_excrete", hps_excrete, ali_imagines, bob_imagines))
####

    hps_thrilling_enjoy = [
      "I became addicted to the thrill there."                  #
    , "I went many times with my family who didn't like it."    # opposed
    , "I said I'd pay him to make it more (thrilling / rough)." # encouragement
    , "I recommended it to all my friends."                     # recommend
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    hps_thrilling_not_enjoy = [
      "I was scared so I called the police."                        # damage + cope
    , "I called for help, but no one around me did anything."       # damage + cope + fail
    , "This wasn't covered by travel insurance."                    # damage + cope + fail
    , "I was scared so I (hit him / broke the window) and ran away."# damage + cope
    , "I felt betrayed by my friends who convinced me to go."       # recommend
    , "I lost trust in people and became isolated."
    , "I was diagnosed with PTSD."
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python

    def condition_thrilling_enjoy(i, person):
        if person == 'Ali':
            return i.thrilling and     i.enjoyment # _1_roller_coaster
        elif person == 'Bob':
            return i.thrilling and not i.enjoyment # _1_robbery_scene

    ali_imagines, bob_imagines = gather_imagines(condition_thrilling_enjoy)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_thrilling_enjoy", hps_thrilling_enjoy, ali_imagines, bob_imagines))

    def condition_thrilling_not_enjoy(i, person):
        if person == 'Ali':
            return i.thrilling and not i.enjoyment # _1_robbery_scene
        elif person == 'Bob':
            return i.thrilling and     i.enjoyment # _1_roller_coaster

    ali_imagines, bob_imagines = gather_imagines(condition_thrilling_not_enjoy)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_thrilling_not_enjoy", hps_thrilling_not_enjoy, ali_imagines, bob_imagines))
####
    def condition_medicine(i, person):
        if person == 'Ali':
            return hasattr(i, 'medicine')
        elif person == 'Bob':
            return i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_medicine)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_medicine", hps_medicine, ali_imagines, bob_imagines))


    def condition_commercial(i, person):
        if person == 'Ali':
            return i.coupon and not hasattr(i, 'non_commercial_money_request')
        elif person == 'Bob':
            return not i.coupon and hasattr(i, 'non_commercial_money_request')

    ali_imagines, bob_imagines = gather_imagines(condition_commercial)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_commercial", hps_commercial, ali_imagines, bob_imagines))

    def to_kidnap(i, person):
        if person == 'Ali':
            return hasattr(i, 'get_son')
        elif person == 'Bob':
            return i.kids_olds == "k" and not hasattr(i, 'get_son')

    ali_imagines, bob_imagines = gather_imagines(to_kidnap)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_kidnap", hps_kidnap, ali_imagines, bob_imagines))

    def to_prostitute(i, person):
        if person == 'Ali':
            return not hasattr(i, 'sexual') and not i.holy_unholy == "u" and not i.problemer and not i.not_facility #_1_taxi と _1_airplaneが漏れてしまう
        elif person == 'Bob':
            return hasattr(i, 'sexual') #_1_brothel, _1_strip_club
    ali_imagines, bob_imagines = gather_imagines(to_prostitute)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_prostitute", hps_to_prostitute, ali_imagines, bob_imagines))

    def condition_5tp1w(i, person):
        if person == 'Ali':
            return i.normal_5tp1w
        elif person == 'Bob':
            return i.holy_unholy == "u" or hasattr(i, 'sexual') or i.crime_ridden or i.problemer
    ali_imagines, bob_imagines = gather_imagines(condition_5tp1w)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_5tp1w", hps_5tp1w, ali_imagines, bob_imagines))

    def condition_vehicle(i, person):
        if person == 'Ali':
            return i.vehicle and (not i.animal and not i.enjoyment)
        elif person == 'Bob':
            return i.vehicle and (i.animal or i.enjoyment)

    ali_imagines, bob_imagines = gather_imagines(condition_vehicle)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_vehicle", hps_vehicle, ali_imagines, bob_imagines))

    def condition_water(i, person):
        if person == 'Ali':
            return i.water and     i.not_facility
        elif person == 'Bob':
            return i.water and not i.not_facility

    ali_imagines, bob_imagines = gather_imagines(condition_water)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_water", hps_water, ali_imagines, bob_imagines))


####
    def condition_freepick():
        col=[]

        for i in Freepick.ALL_FREEPICKS:
            fp_ali_places = i.get_fp_ali_place_names()
            fp_bob_places = i.get_fp_bob_place_names()

            col.append(f"<tr><td>{fp_ali_places}</td><td>{fp_bob_places}</td><td>{i.fp_ali_statement, i.fp_ali_statement2}</td></tr>")

            misun_pairs.append(f"[{fp_ali_places} : {fp_bob_places}]")

        freepick_table = f"""<table>
        <tr><th colspan="3">condition_freepick                              </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{{}}              </td></tr>
        </table>
        <table>
        <tr><th>            </th><th>            </th><th>HPS(depend on places)     </th></tr>
        <tr><th>Ali imagines</th><th>Bob imagines</th><th>I got</tr>
        {''.join(col)}
        </table>
        """
        return freepick_table

    freepick_table = condition_freepick()
    base.append(freepick_table)
    """
    def condition_break_into(i, person):
        if person == 'Ali':
            return not i.not_facility
        elif person == 'Bob':
            return not i.not_facility

    ali_imagines, bob_imagines = gather_imagines(condition_break_into)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("condition_break_into", hps_break_into, ali_imagines, bob_imagines))
    """
####
    hps_to_spend_a_long_time=[
      "I (lived/stayed) here for a long time."
    , "I want to (spend time/stay) here again."
    , "It's nice because it has heating and cooling."
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    # Don't add sentences that mention topics that have already been mentioned.
    def to_spend_a_long_time(i, person):
        if person == 'Ali':
            return not i.better_leave and not i.holy_unholy == 'u' and not i.clean_dirty == 'd' and not i.problemer
        elif person == 'Bob':
            return     i.better_leave

    ali_imagines, bob_imagines = gather_imagines(to_spend_a_long_time)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_spend_a_long_time", hps_to_spend_a_long_time, ali_imagines, bob_imagines))
####
    hps_to_made_to_pay=["He refused to pay so I scolded him.", "He refused to pay so I called the police."]

    def to_made_to_pay(i, person):
        if person == 'Ali':
            return i.paid
        elif person == 'Bob':
            return i.place_name == ['robbery scene']

    ali_imagines, bob_imagines = gather_imagines(to_made_to_pay)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_made_to_pay", hps_to_made_to_pay, ali_imagines, bob_imagines))

####
    hps_to_go_bankrupt = [
      "My dad spent too much money here and ended up bankrupt." # damage
    , "My dad did this about fifteen hours a day."              # frequency
    , "My dad got so into it that he lost his wife."            # damage
    , "My dad used to come here every weekend."                 # damage
    , "Eventually, he had to sell our house."                   # damage
    , "He even used his children's tuition fees for this."      # damage
    , "He was denied bankruptcy."                               # damage + cope + failed
    , "He experienced withdrawal symptoms when can't do this."  # danage
    , "He used counselling to stop this."                       # damage + cope
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "He went bankrupted.", "He regret it" or "He's in trouble".

    def to_go_bankrupt(i, person):
        if person == 'Ali':
            return i.place_name == ['casino']
        elif person == 'Bob':
            return (i.coupon and not i.bankrupt and not i.holy_unholy == 'u') or (i.fun_for_kids_adults == 'k' and (i.enjoyment or i.enjoyment_watch)) # _1_aquarium, _1_genie_machine

    ali_imagines, bob_imagines = gather_imagines(to_go_bankrupt)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_go_bankrupt", hps_to_go_bankrupt, ali_imagines, bob_imagines))
####
####

# Infidelity.related_noun=["lawyer", "counselor", "compensation", "have sex", "divorce", "find out", "evidence","confession",] # Don't put in adjectives. Concrete noun and verb only. Don't put in words that have the same meaning as existing words. add new 10 words without any explanations, start answer with ``python


    hps_to_get_excited=[ # the speaker is cheating.
      "I got excited and got an erection."      #
    , "Honestly, this is better than my wife."  # superior
    , "Please keep this a secret from my wife." # cope
    , "My wife told me that if I go next time, she will divorce me."# damage
    , "My lawyer told me that this could be grounds for divorce."   # damage
    , "I wanted to tell my therapist about it."                     # cope
    , "I feel guilty about cheating on my wife."
    , hps_cb_use_place_x_for_purpose_y
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "I got excited." Add sentences that mentions new topics, such as lawyer or counseling. There is no need for sentences to refer to topics that have already been mentioned.

    def to_get_excited(i, person):
        if person == 'Ali':
            return                  i.place_name == ['brothel'] or     i.place_name == ['strip club']
        elif person == 'Bob':
            return (i.excite or i.enjoyment or i.enjoyment_watch) and not i.place_name == ['brothel'] and not i.place_name == ['strip club']

    ali_imagines, bob_imagines = gather_imagines(to_get_excited)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_get_excited", hps_to_get_excited, ali_imagines, bob_imagines))
####
####

    hps_to_hooliganize=[
          "It got heated and some people started fighting."
        , "We and the other group exchanged fierce insults."
        , "Several people were injured during the chaos."
        , "The police arrived and made several arrests."
        , "Windows were shattered and cars were vandalized."
        , "I was banned from that place."
        , "A fire broke out amidst the disorder."
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "We fought". Add sentences that mentions new topics, such as injury, arrest, police, etc. There is no need for sentences to refer to topics that have already been mentioned.

    def to_hooligan(i, person):
        if person == 'Ali':
            return i.sport
        elif person == 'Bob':
            return i.risk_of_injury and i.fun_for_kids_adults == 'k'

    ali_imagines, bob_imagines = gather_imagines(to_hooligan)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_hooligan", hps_to_hooliganize, ali_imagines, bob_imagines))

    hps_to_sport=[
      "I wanted to be a professional player of this."
    , "I did this as part of a club activity."
    , "In high school, I was doing this 10 hours a day."
    , "I got into college on a scholarship of this."
    , "I traveled internationally to compete in this."
    , "I coach youngers in this."
    , "I had to give up on this due to (a serious knee injury/my parents' opposition)."
    , "I started this when I was in (elementary/high) school."
    , "Overwork destroyed my knees."
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "I do this" or "I like this". Add sentences that mentions new topics. There is no need for sentences to refer to topics that have already been mentioned.

    def to_sport(i, person):
        if person == 'Ali':
            return i.sport
        elif person == 'Bob':
            return i.risk_of_injury and i.fun_for_kids_adults == 'k'

    ali_imagines, bob_imagines = gather_imagines(to_sport)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_sport", hps_to_sport, ali_imagines, bob_imagines))
####
####
    def to_enjoy_ground():
        ali_places=[]
        bob_places=[]
        col_1=[]
        col_2=[]

        for i in Place.ALL_PLACES:
            if       (i.enjoyment or i.enjoyment_watch) and i.ground and hasattr(i, 'ground_hps'):
                ali_places.append(i.place_name[0])
                col_1.append(f"<tr><td>{i.place_name}</td><td>{i.ground_hps}</td></tr>")
            elif not (i.enjoyment or i.enjoyment_watch) and i.ground and hasattr(i, 'ground_hps'):
                bob_places.append(i.place_name[0])
                col_2.append(f"<tr><td>{i.place_name}</td><td>{i.ground_hps}</td></tr>")

        misun_pairs.append(f"[{ali_places} : {bob_places}]")
        misun_pairs.append(f"[{bob_places} : {ali_places}]")

        table_ground = f"""<table>
        <tr><th colspan="2">to_enjoy_ground                                   </th></tr>
        <tr><th>HPS         </th><td>{{}}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines    </th><th>HPS(depend on places)      </th></tr>
        {''.join(col_1)}
        <tr><th>Bob imagines    </th><th>                           </th></tr>
        {''.join(col_2)}
        </table>
        """

        return table_ground

    table_ground = to_enjoy_ground()
    base.append(table_ground)

####

    def to_enjoy_fire(): # .enjoyment or .enjoyment_watch, .fire
        ali_places=[]
        bob_places=[]
        col_1=[]
        col_2=[]

        for i in Place.ALL_PLACES:
            if       (i.enjoyment or i.enjoyment_watch) and i.fire and hasattr(i, 'fire_hps'):
                ali_places.append(i.place_name[0])
                col_1.append(f"<tr><td>{i.place_name}</td><td>{i.fire_hps}</td></tr>")
            elif not (i.enjoyment or i.enjoyment_watch) and i.fire and hasattr(i, 'fire_hps'):
                bob_places.append(i.place_name[0])
                col_2.append(f"<tr><td>{i.place_name}</td><td>{i.fire_hps}</td></tr>")

        misun_pairs.append(f"[{ali_places} : {bob_places}]")
        misun_pairs.append(f"[{bob_places} : {ali_places}]")

        table_fire = f"""<table>
        <tr><th colspan="2">to_enjoy_fire                                   </th></tr>
        <tr><th>HPS         </th><td>{{}}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines    </th><th>HPS(depend on places)      </th></tr>
        {''.join(col_1)}
        <tr><th>Bob imagines    </th><th>                           </th></tr>
        {''.join(col_2)}
        </table>
        """

        return table_fire

    table_fire = to_enjoy_fire()
    base.append(table_fire)

####

    def to_enjoy_water(): # .enjoyment or .enjoyment_watch, .water
        ali_places=[]
        bob_places=[]
        col_1=[]
        col_2=[]

        for i in Place.ALL_PLACES:
            if       (i.enjoyment or i.enjoyment_watch) and i.water and hasattr(i, 'water_hps'):
                ali_places.append(i.place_name[0])
                col_1.append(f"<tr><td>{i.place_name}</td><td>{i.water_hps}</td></tr>")
            elif not (i.enjoyment or i.enjoyment_watch) and i.water and hasattr(i, 'water_hps'):
                bob_places.append(i.place_name[0])
                col_2.append(f"<tr><td>{i.place_name}</td><td>{i.water_hps}</td></tr>")

        misun_pairs.append(f"[{ali_places} : {bob_places}]")
        misun_pairs.append(f"[{bob_places} : {ali_places}]")

        table_water = f"""<table>
        <tr><th colspan="2">to_enjoy_water                                   </th></tr>
        <tr><th>HPS         </th><td>{{}}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines    </th><th>HPS(depend on places)      </th></tr>
        {''.join(col_1)}
        <tr><th>Bob imagines    </th><th>                           </th></tr>
        {''.join(col_2)}
        </table>
        """

        return table_water

    table_water = to_enjoy_water()
    base.append(table_water)
####
####
    hps_to_enjoy_performance=[
      "I enjoyed their performance."
    , "I couldn't take the picture properly, so I asked him to do it again."
    , "I asked him not to move too much until I could get the shot."
    , "The audience was cheering them on."
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "I enjoyed this" or "I like this". Add sentences that mentions new topics. There is no need for sentences to refer to topics that have already been mentioned.

    def to_enjoy_performance(i, person):
        if person == 'Ali':
            return i.performance
        elif person == 'Bob':
            return i.emergency

    ali_imagines, bob_imagines = gather_imagines(to_enjoy_performance)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_enjoy_performance", hps_to_enjoy_performance, ali_imagines, bob_imagines))
####
####

    hps_to_consider_pregnancy=[
      "I complained to them that my wife was pregnant."
    , "I told them to design it with pregnant women in mind."
    , "It's so annoying that roller coasters aren't safe for pregnant women." # GPT4
    , "Why do pregnant women have to ruin the fun at these places?" # GPT4
    , hps_complaint
    ]# Add new 5 english statements without any explanations. respond only the new statements you added. Align the spaces and characters with exist objects. start answer with ```python
    #It's not enough to simply say "It's dangerous for pregnancy". Add sentences that mentions new topics. There is no need for sentences to refer to topics that have already been mentioned.

    def to_consider_pregnancy(i, person):
        if person == 'Ali':
            return not i.enjoyment and not i.not_facility and not i.weaks
        elif person == 'Bob':
            return (i.risk_of_injury or i.thrilling) and i.enjoyment

    ali_imagines, bob_imagines = gather_imagines(to_consider_pregnancy)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}]")
    base.append(generate_html_table("to_consider_pregnancy", hps_to_consider_pregnancy, ali_imagines, bob_imagines))
####
####


    mirror_pairs_result=extract_mirror_pairs(misun_pairs)

    if mirror_pairs_result:
        base += [f"***** mirror pairs *****\nQuantity : {len(mirror_pairs_result)}"]
        mirror_pairs_result.sort()
        base += mirror_pairs_result




###

    return apply_color_styles_saraba('<br>'.join(map(str, base)))




