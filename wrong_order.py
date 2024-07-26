# /home/tarotoyota/wrong_order.py
from wrong_order_inst import Place
from wrong_order_inst import Complaint
from wrong_order_inst import Belong
from master_class_saraba_func_py import apply_color_styles_saraba

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

    def condition_belong():
        hps_belong=["I got one for my family.", "I asked for a refund as the one I got was faulty.", "My wife objected, but I got one.", "I've been going there for about ten years.", "Because it's a special anniversary.", "If I had the money I would buy a new one."]

        belong_table_col=[]

        for i in Belong.ALL_BELONGS:
            cannot_places = i.get_cannot_place_names()
            can_places = i.get_can_place_names()

            belong_table_col.append(f"<tr><td>{can_places}</td><td>{cannot_places}</td><td>{i.belong_name}</td></tr>")
            misun_pairs.append(f"[{can_places} : {cannot_places}],")

        belong_table = f"""<table>
        <tr><th colspan="3">condition_belong                                        </th></tr>
        <tr><th colspan="2">HPS                  </th><td>{hps_belong}              </td></tr>
        </table>
        <table>
        <tr><th>            </th><th>            </th><th>HPS(depend on places)     </th></tr>
        <tr><th>Ali imagines</th><th>Bob imagines</th><th>I got</tr>
        {''.join(belong_table_col)}
        </table>
        """

        return belong_table

    belong_table = condition_belong()
    base.append(belong_table)

    def condition_complaint():
        hps_complaint = ["I lectured the person in charge.", "I demanded a refund.", "I gave it a low rating in an online review.", "I scold the man in charge, but he didin't take action.", "I couldn't concentrate to (relaxing/reading/sleeping/eating).", "I cancelled my membership."]  # いつか実装

        complaint_table_col = []

        for i in Complaint.ALL_COMPLAINTS:
            noproblem_places = i.get_noproblem_place_names()
            problem_places = i.get_problem_place_names()

            complaint_table_col.append(f"<tr><td>{problem_places}</td><td>{noproblem_places}</td><td>{i.complaint_name}<td>{i.cope_had_bring}</td><td>{i.cope_had_do}</td><td>{i.because_my}</td></tr>")
            misun_pairs.append(f"[{problem_places} : {noproblem_places}],")

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


    def condition_weaks():
        hps_weaks = ["I often enjoy watching them here"]

        table_col = []

        condition_weaks_ali_imagines = []
        condition_weaks_bob_imagines = []

        for i in Place.ALL_PLACES:
            if hasattr(i, 'weaks_watch'):
                condition_weaks_ali_imagines.append(i.place_name[0])
                table_col.append(f"<tr><td>{i.place_name}</td><td>{i.weaks_watch}</td>")
            elif i.weaks and not hasattr(i, 'weaks_watch'):
                condition_weaks_bob_imagines.append(i.place_name[0])

        misun_pairs.append(f"[{condition_weaks_ali_imagines} : {condition_weaks_bob_imagines}],")

        weaks_table = f"""<table>
        <tr><th colspan="2">condition_weaks                          </th></tr>
        <tr><th>HPS                             </th><td>{hps_weaks}</td></tr>
        </table>
        <table>
        <tr><th>Ali imagines                    </th><th></th></tr>
        {''.join(table_col)}
        <tr><th>Bob imagines                    </th><th></th></tr>
        <tr><td>{condition_weaks_bob_imagines}  </td><td></td></tr>
        </table>"""

        return weaks_table, condition_weaks_ali_imagines, condition_weaks_bob_imagines
    weaks_table, condition_weaks_ali_imagines, condition_weaks_bob_imagines = condition_weaks()
    base.append(weaks_table)


    def condition_be_when():
        name_and_be_when = []
        be_when_bob_imagines_name = []
        tmp_ali_imagines_name = []
        hps_be_when=["I went there as a top priority.", "My heart was beating hard as I headed there."]

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

        misun_pairs.append(f"[{tmp_ali_imagines_name} : {be_when_bob_imagines_name}],")
        return be_when_table, tmp_ali_imagines_name, be_when_bob_imagines_name

    be_when_table, tmp_ali_imagines_name, be_when_bob_imagines_name = condition_be_when()
    base.append(be_when_table)



    hps_voyeur = [
        "I took a lot of good photos.", "I enjoyed the wonderful scenery.",
        "I'll use this photo for this year's Christmas card.", "This is one of my favorite shots.",
        "I have it framed and displaying it.", "I bought an expensive camera for this purpose.",
        "It was difficult to keep the subject still."
    ]

    def condition_voyeur(i, person):
        if person == 'Ali':
            return i.camera_ok_ban == "o"
        elif person == 'Bob':
            return i.camera_ok_ban == "b"

    ali_imagines, bob_imagines = gather_imagines(condition_voyeur)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_voyeur", hps_voyeur, ali_imagines, bob_imagines))

    hps_pick_up = [
        "I picked up girls here.", "For some reason the success rate was low.",
        "I made my girlfriend here.", "Unfortunately, I was found by the girl's boyfriend.",
        "Unfortunately, I got rejected several times.", "I come here every weekend."
    ]

    def condition_pic(i, person):
        if person == 'Ali':
            return i.pick_up_spot
        elif person == 'Bob':
            return i.holy_unholy == "h" or i.kids_olds == "k" or i.serious

    ali_imagines, bob_imagines = gather_imagines(condition_pic)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_pic", hps_pick_up, ali_imagines, bob_imagines))


    hps_pervert = ["I (had/bought) sex here.", "For some reason there was no sexual service.", "It's cheaper than call girls nearby.", "I always use rubbers properly.", "It's 300 dollars per hour."]

    def condition_pervert(i, person):
        if person == 'Ali':
            return hasattr(i, 'sex')
        elif person == 'Bob':
            return i.kids_olds == 'k' or i.animal

    ali_imagines, bob_imagines = gather_imagines(condition_pervert)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_pervert", hps_pervert, ali_imagines, bob_imagines))

    hps_kids = ["I put my son here.","I used to play here a lot as a child.", "When I was a child, I was left here until my parents finished work.", "When I was a child, my father brought me here to study.", "I've been here on school trips."]

    def condition_kids(i, person):
        if person == 'Ali':
            return i.kids_olds == 'k' or i.educational
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_kids)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_kids", hps_kids, ali_imagines, bob_imagines))

    hps_olds = ["I put my grandfather here.", "My grandfather didn't want to go into here.","My grandfather made many friends here.","He receives excellent care at this facility.","We visit him every weekend.","He enjoys the activities they offer here."]

    def condition_olds(i, person):
        if person == 'Ali':
            return i.kids_olds == 'k'
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_olds)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_olds", hps_olds, ali_imagines, bob_imagines))

    hps_mourn=["My father's grave is here.", "I attended a funeral here.", "I (buried him / scattered his ashes) here.", "He loved this place.","Our family often comes here to reflect.","This place holds many of our memories.","We shared stories about him here."]

    def condition_mourn(i, person):
        if person == 'Ali':
            return i.mourn
        elif person == 'Bob':
            return hasattr(i, 'sex') or i.holy_unholy == "u" or i.clean_dirty == "d" or i.enjoyment

    ali_imagines, bob_imagines = gather_imagines(condition_mourn)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_mourn", hps_mourn, ali_imagines, bob_imagines))

    hps_wedding = ["I had my weeding here.", "It's true that it's a little far away, so it may have been inconvenient for attendees."]

    def condition_wedding(i, person):
        if person == 'Ali':
            return hasattr(i, 'wedding')
        elif person == 'Bob':
            return hasattr(i, 'sex') or (i.holy_unholy == "u" or i.clean_dirty == "d") and not i.enjoyment  #_1_dumpyard

    ali_imagines, bob_imagines = gather_imagines(condition_wedding)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_wedding", hps_wedding, ali_imagines, bob_imagines))

    hps_eat=["The food there is delicious.", "The food there is fresh and can be eaten raw or alive.", "I got food poisoning from the food there.", "I once had trash in the food there.", "So I asked the person in charge there to apologize.", "I left a rating for it on yelp.", "For some reason there's not very well known.", "It's Chiba's traditional food."]

    def condition_eat(i, person):
        if person == 'Ali':
            return i.food
        elif person == 'Bob':
            return not i.food and i.animal and not i.not_facility

    ali_imagines, bob_imagines = gather_imagines(condition_eat)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_eat", hps_eat, ali_imagines, bob_imagines))

    hps_excrete = ["I excreted here.", "When I have diarrhea, I feel relieved when I find this place.", "I complained because there was no toilet paper."]

    def condition_excrete(i, person):
        if person == 'Ali':
            return hasattr(i, 'excrete')
        elif person == 'Bob':
            return i.food or i.clean_dirty == "c" or i.holy_unholy == "h"

    ali_imagines, bob_imagines = gather_imagines(condition_excrete)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_excrete", hps_excrete, ali_imagines, bob_imagines))

    hps_thrilling = ["I became addicted to the thrill there.", "I went many times with my family who didn't like it.", "I said I'd pay him to make it more thrilling.", "I was scared so I called the police.", "I called for help, but no one around me did anything.", "This wasn't covered by travel insurance.", "I was scared so I (hit him / broke the window) and ran away."]

    def condition_thrilling(i, person):
        if person == 'Ali':
            return i.thrilling and i.enjoyment
        elif person == 'Bob':
            return i.thrilling and not i.enjoyment

    ali_imagines, bob_imagines = gather_imagines(condition_thrilling)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_thrilling", hps_thrilling, ali_imagines, bob_imagines))

    hps_medicine = ["I pick up my drugs here regularly.", "I refused to take opioids.", "I have to be careful not to be overprescribed.", "I'm worried about the side effects.", "I accidentally took too much drugs once.", "I feel much better after taking the drug."] #

    def condition_medicine(i, person):
        if person == 'Ali':
            return hasattr(i, 'medicine')
        elif person == 'Bob':
            return i.crime_ridden

    ali_imagines, bob_imagines = gather_imagines(condition_medicine)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_medicine", hps_medicine, ali_imagines, bob_imagines))

    hps_bankrupt = ["My father spent too much money here and ended up bankrupt.", "My father was addicted to this place.","My father used to come here every weekend.","Eventually, he had to sell our house.", "He even used his company's money and his children's tuition fees for this."] # Add new 10 statements in English without any explanations. start answer with ```python. Only respond with new statements you added. Don't add statements what similar with exist ones.

    def condition_bankrupt(i, person):
        if person == 'Ali':
            return i.coupon and i.bankrupt # _1_casino
        elif person == 'Bob':
            return i.coupon and not i.bankrupt # _1_genie_machine

    ali_imagines, bob_imagines = gather_imagines(condition_bankrupt)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_bankrupt", hps_bankrupt, ali_imagines, bob_imagines))

    hps_commercial = ["They accepted credit cards.","They were handing out numbered tickets because there were so many people.","I got a receipt.","They gave me the correct change.","They had a friend referral system.","They gave me coupons."]

    def condition_commercial(i, person):
        if person == 'Ali':
            return i.coupon and not hasattr(i, 'non_commercial_money_request')
        elif person == 'Bob':
            return not i.coupon and hasattr(i, 'non_commercial_money_request')

    ali_imagines, bob_imagines = gather_imagines(condition_commercial)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_commercial", hps_commercial, ali_imagines, bob_imagines))

    hps_get_son = ["I met my son here for the first time and became a father.", "I brought my son home from here."]

    def condition_get_son(i, person):
        if person == 'Ali':
            return hasattr(i, 'get_son')
        elif person == 'Bob':
            return i.kids_olds == "k" and not hasattr(i, 'get_son')

    ali_imagines, bob_imagines = gather_imagines(condition_get_son)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_get_son", hps_get_son, ali_imagines, bob_imagines))

    hps_sexual_if_animal=["I saw monkeys there.", "There were about 4 years old children.", "I saw a baby."]

    def condition_sexual_if_animal(i, person):
        if person == 'Ali':
            return i.animal
        elif person == 'Bob':
            return hasattr(i, 'sexual') #_1_brothel, _1_strip_club
    ali_imagines, bob_imagines = gather_imagines(condition_sexual_if_animal)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_sexual_if_animal", hps_sexual_if_animal, ali_imagines, bob_imagines))

    hps_sexual_if_kids=["There were about 4 years old children.", "I saw a baby."]

    def condition_sexual_if_kids(i, person):
        if person == 'Ali':
            return i.kids_olds == 'k'
        elif person == 'Bob':
            return hasattr(i, 'sexual') #_1_brothel, _1_strip_club
    ali_imagines, bob_imagines = gather_imagines(condition_sexual_if_kids)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_sexual_if_kids", hps_sexual_if_kids, ali_imagines, bob_imagines))

    hps_sexual_if_olds=["There were about 95 years old hugs.", "There were bedridden, demented, and wheelchair-bound olds."]

    def condition_sexual_if_olds(i, person):
        if person == 'Ali':
            return i.kids_olds == 'o'
        elif person == 'Bob':
            return hasattr(i, 'sexual') #_1_brothel, _1_strip_club
    ali_imagines, bob_imagines = gather_imagines(condition_sexual_if_olds)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_sexual_if_olds", hps_sexual_if_olds, ali_imagines, bob_imagines))

    hps_sexual_work = ["My son is working here.", "My son works here eight hours a day.", "It took a while for him to become a permanent employee here."]

    def condition_sexual_work(i, person):
        if person == 'Ali':
            return i.coupon #_1_fish_market
        elif person == 'Bob':
            return hasattr(i, 'sexual') #_1_brothel, _1_strip_club
    ali_imagines, bob_imagines = gather_imagines(condition_sexual_work)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_sexual_work", hps_sexual_work, ali_imagines, bob_imagines))

    hps_5tp1w = ["I used to (come, use) here about five times a week.", "This is like my second home.", "I made friends with the people here.","This place is my escape from reality.",]# Add new 10 statements in English without any explanations. start answer with ```python. Only respond with new statements you added. Don't add statements what similar with exist ones.

    def condition_5tp1w(i, person):
        if person == 'Ali':
            return i.normal_5tp1w
        elif person == 'Bob':
            return i.holy_unholy == "u" or hasattr(i, 'sexual') or i.crime_ridden or i.problemer
    ali_imagines, bob_imagines = gather_imagines(condition_5tp1w)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_5tp1w", hps_5tp1w, ali_imagines, bob_imagines))

    hps_vehicle = ["I took it from China to India.", "There was on-board sales.","I put in high octane gasoline but it still wouldn't start.", "This only went {n} kilometers per hour.","There were about {n} people on it."]

    def condition_vehicle(i, person):
        if person == 'Ali':
            return i.vehicle and (not i.animal and not i.enjoyment)
        elif person == 'Bob':
            return i.vehicle and (i.animal or i.enjoyment)

    ali_imagines, bob_imagines = gather_imagines(condition_vehicle)
    misun_pairs.append(f"[{ali_imagines} : {bob_imagines}],")
    base.append(generate_html_table("condition_vehicle", hps_vehicle, ali_imagines, bob_imagines))

#    misun_pairs = [str(item) for item in misun_pairs]


###


    import re
    from typing import List, Tuple, Union

    def parse_list_string(list_string: str) -> List[str]:
        # リスト形式の文字列を解析してリストに変換
        # 例: "['a', 'b', 'c']" -> ['a', 'b', 'c']
        list_string = list_string.strip()[1:-1]  # 最初と最後のブラケットを削除
        items = [item.strip().strip("'").strip('"') for item in list_string.split(',')]
        return items

    def is_mirror_pair(pair1: Tuple[Union[str, List[str]], Union[str, List[str]]],
                       pair2: Tuple[Union[str, List[str]], Union[str, List[str]]]) -> bool:
        # ペアが逆になっている場合はミラーとする
        return pair1 == (pair2[1], pair2[0])

    def tupleify(pair: Tuple[Union[str, List[str]], Union[str, List[str]]]) -> Tuple[Union[str, Tuple], Union[str, Tuple]]:
        # リストをタプルに変換
        left, right = pair
        if isinstance(left, list):
            left = tuple(left)
        if isinstance(right, list):
            right = tuple(right)
        return (left, right)

    def pair_to_string(pair: Tuple[Union[str, List[str]], Union[str, List[str]]]) -> str:
        left, right = pair
        left_str = repr(left) if isinstance(left, list) else str(left)
        right_str = repr(right) if isinstance(right, list) else str(right)
        return f"[{left_str} : {right_str}]"

    def extract_mirror_pairs(misun_pairs: str) -> List[str]:
        # 入力を強制的に文字列に変換
        misun_pairs = str(misun_pairs)

        # 正規表現パターンを定義
        pattern = re.compile(r'\[(.*?)\s*:\s*(.*?)\]')

        # 全てのマッチを見つける
        matches = pattern.findall(misun_pairs)

        pairs = []

        for match in matches:
            left = match[0].strip()
            right = match[1].strip()

            # リストのような文字列をリストに変換
            if left.startswith('[') and left.endswith(']'):
                left = parse_list_string(left)
            if right.startswith('[') and right.endswith(']'):
                right = parse_list_string(right)

            pairs.append((left, right))

        # ミラーペアを探す
        mirror_pairs = []
        seen_pairs = set()

        for pair in pairs:
            t_pair = tupleify(pair)
            if t_pair not in seen_pairs:
                mirror_pair = tupleify((pair[1], pair[0]))
                if mirror_pair in map(tupleify, pairs):
                    mirror_pairs.append(pair)
                    seen_pairs.add(t_pair)
                    seen_pairs.add(mirror_pair)

        # 文字列に変換して返す
        return [pair_to_string(pair) for pair in mirror_pairs]

###






    mirror_pairs = extract_mirror_pairs(misun_pairs)


    base += mirror_pairs
#    base += misun_pairs
    return apply_color_styles_saraba('<br>'.join(map(str, base)))




