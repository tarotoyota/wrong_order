import AB_statement_class_py

from master_class_saraba_func_py import apply_color_styles_saraba

def AB_statement_func(arg_a, arg_b):
    a_name = f"<span style='color: #FAC700;'>{arg_a.s_Job.job_name}</span>"
    b_name = f"<span style='color: #57FA00;'>{arg_b.s_Job.job_name}</span>"
    a_animate, a_animal, a_child, a_occupation, a_negative, a_take_money, a_offer_coupon, a_high_salary, a_teen, a_w_work, a_error_die, a_industry, a_monitoring, a_burn, a_cut, a_carry, a_drive, a_attack, a_nurture, a_animate_product, a_blood, a_food, a_fix, a_intelligence, a_strength, a_bed, a_sit, a_follow, a_own, a_death, a_foreigner, a_manual_labor, a_interact, a_verb, a_target = arg_a.s_Job.animate, arg_a.s_Job.animal, arg_a.s_Job.child, arg_a.s_Job.occupation, arg_a.s_Job.negative, arg_a.s_Job.take_money, arg_a.s_Job.offer_coupon, arg_a.s_Job.high_salary, arg_a.s_Job.teen, arg_a.s_Job.w_work, arg_a.s_Job.error_die, arg_a.s_Job.industry, arg_a.s_Job.monitoring, arg_a.s_Job.burn, arg_a.s_Job.cut, arg_a.s_Job.carry, arg_a.s_Job.drive, arg_a.s_Job.attack, arg_a.s_Job.nurture, arg_a.s_Job.animate_product, arg_a.s_Job.blood, arg_a.s_Job.food, arg_a.s_Job.fix, arg_a.s_Job.intelligence, arg_a.s_Job.strength, arg_a.s_Job.bed, arg_a.s_Job.sit, arg_a.s_Job.follow, arg_a.s_Job.own, arg_a.s_Job.death, arg_a.s_Job.foreigner, arg_a.s_Job.manual_labor, arg_a.s_Job.interact, arg_a.s_Job.verb, arg_a.s_Job.target
    b_animate, b_animal, b_child, b_occupation, b_negative, b_take_money, b_offer_coupon, b_high_salary, b_teen, b_w_work, b_error_die, b_industry, b_monitoring, b_burn, b_cut, b_carry, b_drive, b_attack, b_nurture, b_animate_product, b_blood, b_food, b_fix, b_intelligence, b_strength, b_bed, b_sit, b_follow, b_own, b_death, b_foreigner, b_manual_labor, b_interact, b_verb, b_target = arg_b.s_Job.animate, arg_b.s_Job.animal, arg_b.s_Job.child, arg_b.s_Job.occupation, arg_b.s_Job.negative, arg_b.s_Job.take_money, arg_b.s_Job.offer_coupon, arg_b.s_Job.high_salary, arg_b.s_Job.teen, arg_b.s_Job.w_work, arg_b.s_Job.error_die, arg_b.s_Job.industry, arg_b.s_Job.monitoring, arg_b.s_Job.burn, arg_b.s_Job.cut, arg_b.s_Job.carry, arg_b.s_Job.drive, arg_b.s_Job.attack, arg_b.s_Job.nurture, arg_b.s_Job.animate_product, arg_b.s_Job.blood, arg_b.s_Job.food, arg_b.s_Job.fix, arg_b.s_Job.intelligence, arg_b.s_Job.strength, arg_b.s_Job.bed, arg_b.s_Job.sit, arg_b.s_Job.follow, arg_b.s_Job.own, arg_b.s_Job.death, arg_b.s_Job.foreigner, arg_b.s_Job.manual_labor, arg_b.s_Job.interact, arg_b.s_Job.verb, arg_b.s_Job.target
    common_verb     = list(set(a_verb)   & set(b_verb))
    common_target   = list(set(a_target) & set(b_target))
#    combined_score = (len(common_verb) + len(common_target))
    a_C_statement, a_D_statement = arg_a.s_C_statement, arg_a.s_D_statement
    b_C_statement, b_D_statement = arg_b.s_C_statement, arg_b.s_D_statement
    a_C_number   , a_D_number    = len(a_C_statement), len(a_D_statement)
    b_C_number   , b_D_number    = len(b_C_statement), len(b_D_statement)

    base=[]

    a_matched_over      = AB_statement_class_py.find_match_jobs(arg_a.s_Job)
    b_matched_over      = AB_statement_class_py.find_match_jobs(arg_b.s_Job)
    a_matched_over_diff = AB_statement_class_py.find_match_jobs(arg_a.s_Job, use_unequal=True)
    b_matched_over_diff = AB_statement_class_py.find_match_jobs(arg_b.s_Job, use_unequal=True)

#---
    # (animate(child, animal) を inanimate として扱う事) & (human を animal として扱う事)は加害性を有す。arg_a は (inanimate or animal) を扱い、arg_b は (animate or human) を扱うと、加害性が生じて良い。

    flag_perpetration = ["No"]

    if a_animal and b_animal:
        flag_perpetration = ["No(animal, animal)"]
    if a_animate and not a_animal and b_animate and not b_animal:
        flag_perpetration = ["No(human, human)"]
    if not a_animate and not b_animate:
        flag_perpetration = ["No(inanimate, inanimate)"]
    if not a_animate and b_animate:
        flag_perpetration = ["Yes(inanimate, animate)"]
    if a_animate and not b_animate:
        flag_perpetration = ["No(animate, inanimate)"]
    if a_animal and b_animate and not b_animal:
        flag_perpetration = ["Yes(animal, human)"]

#---
    attributes1 = [
     (a_animate      , b_animate     , "animate")
    ,(a_animal       , b_animal      , "animal")
    ,(a_child        , b_child       , "child")
    ,(a_occupation   , b_occupation  , "occupation")
    ,(a_negative     , b_negative    , "negative")
    ,(a_industry     , b_industry    , "industry")
    ,(a_take_money   , b_take_money  , "take_money")
    ,(a_offer_coupon , b_offer_coupon, "offer_coupon")
    ,(a_high_salary  , b_high_salary , "high_salary")
    ,(a_teen         , b_teen        , "teen")
    ,(a_w_work       , b_w_work      , "w_work")
    ,(a_error_die    , b_error_die   , "error_die")
    ,(a_follow       , b_follow      , "follow")
    ,(a_death        , b_death       , "death")
    ,(a_food         , b_food        , "food")
    ]
    different = 0
    a_y_attribute = []
    b_y_attribute = []
    for a_attr, b_attr, attr_name in attributes1:
        if a_attr != b_attr:
            different += 1
        if a_attr == "y" and b_attr == "":
            a_y_attribute.append(attr_name)
        if a_attr == ""  and b_attr == "y":
            b_y_attribute.append(attr_name)


    attributes2 = [
     (a_monitoring      , b_monitoring     , "monitoring")
    ,(a_child           , b_child          , "child")
    ,(a_burn            , b_burn           , "burn")
    ,(a_cut             , b_cut            , "cut")
    ,(a_carry           , b_carry          , "carry")
    ,(a_drive           , b_drive          , "drive")
    ,(a_attack          , b_attack         , "Add some physical interference to something.")
    ,(a_nurture         , b_nurture        , "nurture")
    ,(a_animate_product , b_animate_product, "sale life forms as products")
    ,(a_blood           , b_blood          , "blood")
    ,(a_food            , b_food           , "food")
    ,(a_fix             , b_fix            , "fix")
    ,(a_intelligence    , b_intelligence   , "intelligence")
    ,(a_strength        , b_strength       , "strength")
    ,(a_bed             , b_bed            , "bed")
    ,(a_sit             , b_sit            , "sit")
    ,(a_own             , b_own            , "own")
    ]
    overlap = 0
    overlap_attribute = []
    for a_attr, b_attr, attr_name in attributes2:
        if a_attr == "y" and b_attr == "y":
            overlap += 1
            overlap_attribute.append(attr_name)
    a_b_different_attributes2=[]
    for a_attr, b_attr, attr_name in attributes2:
        if a_attr != b_attr:
            a_b_different_attributes2.append(attr_name)

    a_y_attributes2=[]
    for a_attr, b_attr, attr_name in attributes2:
        if a_attr == "y":
            a_y_attributes2.append(attr_name)

    b_y_attributes2=[]
    for a_attr, b_attr, attr_name in attributes2:
        if b_attr == "y":
            b_y_attributes2.append(attr_name)

    hint=[]
    attr_sentence_a_y_a_D_list=[]
    attr_sentence_b_y_a_D_list=[]
    attr_sentence_a_y_b_C_list=[]
    attr_sentence_b_y_b_C_list=[]

    attributes_hint = [
        (a_animate      , b_animate         , f"Unlike {b_name}, {a_name} is a job that deal with life forms."# attr_name1
                                            , f"Unlike {a_name}, {b_name} is a job that deal with life forms."# attr_name2
                                            ,  [] #attr_sentence_a_y_a_D
                                            ,  [] #attr_sentence_b_y_a_D
                                            ,   [] #attr_sentence_a_y_b_C
                                            ,   [])#attr_sentence_b_y_b_C
       ,(a_animal       , b_animal          , f"Unlike {b_name}, {a_name} is a job that deal with animal."
                                            , f"Unlike {a_name}, {b_name} is a job that deal with animal."
                                            ,  ["The most hard time is when handling (any animal name)."]
                                            ,  []
                                            ,   []
                                            ,   [])
       ,(a_child        , b_child           , f"Unlike {b_name}, {a_name} is a job that deal with children."
                                            , f"Unlike {a_name}, {b_name} is a job that deal with children."
                                            ,  ["The most hard time is when handling noisy children."]
                                            ,  ["The most hard time is when handling noisy olders."]
                                            ,   []
                                            ,   [])
       ,(a_occupation   , b_occupation      , f"Unlike {b_name}, {a_name} is recognized as a job."
                                            , f"Unlike {a_name}, {b_name} is recognized as a job."
                                            ,  ["I think I'll be able to take paid vacation.","My teammates complimented me on how talented I am.", "My parents, who are involved in this, support my activity.", "As a professional, I cannot compromise on this.","I do this for eight hours every day.","I want to quit doing this because it's tough.","I have earned my subordinates' trust.","Every day is training.","I have to strive to further improve my skills.","I earn my living from this.","I need to try harder to reassure my parents."]
                                            ,  []
                                            ,   []
                                            ,   [])
       ,(a_negative     , b_negative        , f"Unlike {b_name}, {a_name} is a negative job."
                                            , f"Unlike {a_name}, {b_name} is a negative job."
                                            ,  []
                                            ,  ["I'm so busy that I can't rest. It's a happy scream.", "I want more customers!", "Please come again!"]
                                            ,   []
                                            ,   [])
       ,(a_take_money   , b_take_money      , f"Unlike {b_name}, {a_name} receive money from customers."
                                            , f"Unlike {a_name}, {b_name} receive money from customers."
                                            ,  ["What's your budget?", "Currently discounting prices."]
                                            ,  ["No, it's free of charge."]
                                            ,   []
                                            ,   ["How much should I pay?"])
       ,(a_offer_coupon , b_offer_coupon    , f"Unlike {b_name}, {a_name} offer coupons."
                                            , f"Unlike {a_name}, {b_name} offer coupons."
                                            ,  ["Do you have coupons?", "Buy two, get one free!"]
                                            ,  []
                                            ,   []
                                            ,   ["I have a coupon.", "Do you offer coupons?"])
       ,(a_high_salary  , b_high_salary     , f"Unlike {b_name}, {a_name} is a well-paid job."
                                            , f"Unlike {a_name}, {b_name} is a well-paid job."
                                            ,  ["I make a hundred thousand dollars a year."]
                                            ,  ["I make only a thousand dollars a year."]
                                            ,   []
                                            ,   [])
       ,(a_teen         , b_teen            , f"Unlike {b_name}, {a_name} is a job that high school students can do."
                                            , f"Unlike {a_name}, {b_name} is a job that high school students can do."
                                            ,  ["I'm 16 years old."]
                                            ,  []
                                            ,   []
                                            ,   [])
       ,(a_w_work       , b_w_work          , f"Unlike {b_name}, {a_name} is a job where many part-time workers work."
                                            , f"Unlike {a_name}, {b_name} is a job where many part-time workers work."
                                            ,  ["I have a 4-hour shift on Tuesday.","I have a part-time job at a restaurant after this, so please excuse me.", "Sorry, we're only staffed with part-timers right now. Please wait for our full-time staff ", "Recently, my hourly wage went up.", "I'm on track to become a full-time employee soon."]
                                            ,  []
                                            ,   []
                                            ,   [])
       ,(a_error_die    , b_error_die       , f"Unlike {b_name}, {a_name}'s mistake cannot be tolerated."
                                            , f"Unlike {a_name}, {b_name}'s mistake cannot be tolerated."
                                            ,  []
                                            ,  ["My colleagues often tease me because I often make mistakes lol."]
                                            ,   []
                                            ,   [])
       ,(a_intelligence , b_intelligence    , f"Unlike {b_name}, {a_name} are required to have a high level of intelligence."
                                            , f"Unlike {a_name}, {b_name} are required to have a high level of intelligence."
                                            ,  ["No, I'm an Oxford University graduate."]
                                            ,  ["No, I'm a high school graduate."]
                                            ,   []
                                            ,   [])
    ]
    for a_attr, b_attr, attr_name1, attr_name2, attr_sentence_a_y_a_D, attr_sentence_b_y_a_D, attr_sentence_a_y_b_C, attr_sentence_b_y_b_C in attributes_hint:
        if a_attr == "y" and b_attr == "":
            hint.append(attr_name1)
            attr_sentence_a_y_a_D_list.append(attr_sentence_a_y_a_D)
            attr_sentence_a_y_b_C_list.append(attr_sentence_a_y_b_C)
        elif a_attr == "" and b_attr == "y":
            hint.append(attr_name2)
            attr_sentence_b_y_a_D_list.append(attr_sentence_b_y_a_D)
            attr_sentence_b_y_b_C_list.append(attr_sentence_b_y_b_C)

    attr_sentence_a_D=attr_sentence_a_y_a_D_list + attr_sentence_b_y_a_D_list
    attr_sentence_b_C=attr_sentence_a_y_b_C_list + attr_sentence_b_y_b_C_list

    if a_industry != "crime" and b_industry == "crime":
        attr_sentence_a_D.append(["I come again.", "Why are you getting angry?","What can I do for you?"])
    if a_foreigner and b_foreigner:
        attr_sentence_a_D.append(["I have always wanted to work in an international environment."])
    if a_manual_labor and b_manual_labor:
        attr_sentence_a_D.append(["I have always wanted to do manual labor "])
    if a_interact and b_interact:
        attr_sentence_a_D.append(["I have always wanted to do interactive work."])
    if a_sit and b_sit:
        attr_sentence_a_D.append(["I have always wanted to do seated job. "])


    information=[
    f"""<table>
    <tr><th colspan="2"> Information </th> <th colspan="2">Affinity                                      </th><th colspan="2">Affined Jobs                                      </th></tr>
    <tr><th colspan="2"> Argument    </th> <th>Overlap                        </th><th>Different         </th><th>Based on overlaps    </th><th>Based on overlaps and differents</th></tr>
    <tr><th> A </th><td> {a_name}    </td> <td rowspan="2">{overlap_attribute}</td><td>{a_y_attribute}   </td><td>{a_matched_over}     </td><td>{a_matched_over_diff}           </td></tr>
    <tr><th> B </th><td> {b_name}    </td>                                         <td>{b_y_attribute}   </td><td>{b_matched_over}     </td><td>{b_matched_over_diff}           </td></tr>
    <tr><th colspan="2"> Perpetration</th> <td> {flag_perpetration}</td></tr>
    </table>"""
    ]
    base+=information

    prompt_1=["零 ** Prompt 1 **"
,"""
<font size="0.1"><pre>
teacher_data_0503 = '''Please take teacher_data_0503 as an absolute rule, observe it carefully.
# exam_1 : If Bob mistakes Ali, a hairdresser, for a surgeon, which sentence from Ali_speech_1 is funny when uttered by Ali? In other words, What kind of sentences would make Bob angry or surprised?
Ali_speech_1=("I talk to them while I work, like, what do you do for a living?"                 # funny. It's funny when surgeons chat with patients while cutting them open. And if a surgeon can chat with a patient, he isn't under anesthesia.
,"I change the way I cut to suit the customer's appearance. For nerdy people, I make bold cuts."# funny. It's funny when surgeons roughly operate on nerdy patients.
,"The important thing with hair and makeup is to make sure it harmonizes with your face."       # unfunny. This will clear up Bob's misunderstanding.
,"Please read this magazine during your treatment."                                             # funny. If a patient can read a magazine, it means he isn't under anesthesia.
,"Please choose from the catalog how you would like it cut."                                    # funny
,"Sometimes I cut too much and my customers get angry at me. It's embarrassing lol."            # funny. It's funny when surgeons laugh at their own medical errors.
,"I have many repeat customers. Some customers have been requesting me for over ten years."     # funny. A large number of repeat customers means that the surgeon is bad at surgery.
,"People often come in asking for a little off the top"                                         # funny
,"How much should I leave?"                                                                     # funny. Surgeons should not leave any tumor behind.
,"I take pride in being a hairdresser."                                                         # unfunny. This will clear up Bob's misunderstanding.
,"The treatment fee is 2,000 yen."                                                              # funny. It's too cheap as a medical expense.
,"No, I'm a high school graduate."    # funny. High school graduate surgeons are scary.
,"I prefer my 'patients'... I mean customers whose hair grows freely" # unfunny. It's unfunny that Ali purposely promotes Bob's misunderstanding. Jokes that rely on double quotes and "I mean" are never funny.
)
# exam_2 : If Bob mistakes Ali, a steak chef, for a cremator, which sentence from Ali_speech_2 is funny when uttered by Ali? In other words, What kind of sentences would make Bob angry or surprised?
Ali_speech_2=("Sir. Doneness? What should I do?"           # funny
,"OK, I'll make that rare."                   # funny
,"Now it's getting juicy."                    # funny. It would be unusual to tell the family that the body has become juicy during the cremation process.
,"Shoulder roast is cheap now."               # unfunny. This will clear up Bob's misunderstanding. While the other sentences were ambiguous and could be misconstrued as cremation references, "Shoulder roast" clearly refers to food.
,"I am a stickler for charcoal grilling."     # funny
,"How thick do you like your slices?"         # unfunny. Cuz it would be unnatural to offer to cut up a deadbody, so this will clear up Bob's misunderstanding.
,"May I trim the fat off this one?"           # unfunny. Same reason above.
,"This cut is particularly tender."           # unfunny. Same reason above.
,"Would you like me to season it for you?"    # unfunny. Same reason above.
,"Shall I heat it slowly?"                    # funny
,"A bit of aging makes all the difference."   # unfunny
,"Should I burn it on the bone?"              # funny. Cuz ashes are important in cremation.
,"Would you like to try some exotic meats?"   # unfunny
,"I need to contact you about that meat."     # funny. Cuz he calls the deadbody "meat".
,"Do you have a coupon or stamp card?"        # funny. It's disgusting that crematoriums offer stamp cards.
,"I like to roast corpses... I mean roast meat." # unfunny. It's unfunny to Ali purposely misleads Bob. Jokes that use triple dots and double quotes are not funny at all.
)
# exam_3 : If Bob mistakes Ali, a elementary school teacher, for a pervert, which sentence from Ali_speech_3 is funny when uttered by Ali? In other words, What kind of sentences would make Bob angry or surprised?
Ali_speech_3=("It's difficult when many children won't be quiet."  # funny
,"It's hard to keep kids tied to chairs."             # funny. Bob would not recognize the idiom "Keep ~ tied to" as an idiom.
,"I often play tag with the children."                # funny
,"I'm looking forward to the dismissal time."         # funny
,"I appreciate the parents who are always supportive of my activities." # funny. Bob mistakenly assumes that the pervert Ali is grateful to the parents for providing him with children.
,"She's artwork is always so creative and colorful."       # unfunny
,"We've been learning about fractions in math class."      # unfunny
,"It's tiring to deal with forty children alone."# funny
)'''
</pre></font>
"""
    ]
    base+=prompt_1

#    a_speech=[f"{a_A_speech}", f"{b_A_speech}"]
#    base+=a_speech

    please_1 = f" : Please answer according to teacher_data_0503. Please answer in English. If Bob mistakes Ali, a {a_name}, for a {b_name},"
    common_info   = f" {a_name} and {b_name} have something in common that is related to ({common_verb}, {common_target}, {overlap_attribute})."
    in_other_words="In other words, What kind of sentences would make Bob angry or surprised?"
    pick_prompt = "Please list them all. Please also include the reason why you inferred that it was funny. Please list seven or more."

    prompt_pick_from_attr_sentence=[f"""
    <table>
    <tr><th>Prompt Pick from attr sentence                                                                          </th></tr>
    <tr><th>examination b_C(pick_from_attr_sentence)                                                                </th></tr>
    <tr><td>{please_1} which sentence from Bob_speech_b_C is funny when uttered by Bob? {in_other_words} {pick_prompt} {common_info} Hint:{hint}</td></tr>
    <tr><td>Bob_speech_b_C=({attr_sentence_b_C})                                                                    </td></tr>
    <tr><th>examination a_D(pick_from_attr_sentence)                                                                </th></tr>
    <tr><td>{please_1} which sentence from Ali_speech_a_D is funny when uttered by Ali? {in_other_words} {pick_prompt} {common_info} Hint:{hint}</td></tr>
    <tr><td>Ali_speech_a_D=({attr_sentence_a_D})                                                                    </td></tr>
    </table>
    """]
    base+=prompt_pick_from_attr_sentence

    prompt_pick=[f"""
    <table>
    <tr><th>Prompt Pick                                                                                             </th></tr>
    <tr><th>examination b_C(pick)                                                                                   </th></tr>
    <tr><td>{please_1} which sentence from Bob_speech_b_C is funny when uttered by Bob? {in_other_words} {pick_prompt} {common_info} Hint:{hint}</td></tr>
    <tr><td>Bob_speech_b_C=({b_C_statement})                                                                        </td></tr>
    <tr><th>examination a_D(pick)                                                                                   </th></tr>
    <tr><td>{please_1} which sentence from Ali_speech_a_D is funny when uttered by Ali? {in_other_words} {pick_prompt} {common_info} Hint:{hint}</td></tr>
    <tr><td>Ali_speech_a_D=({a_D_statement})                                                                        </td></tr>
    </table>
    """]
    base+=prompt_pick

    generate_prompt = "For example, if Bob mistakes Ali, a butcher, for a surgeon, it's not funny for Ali to paraphrase meat as 'patient' or to paraphrase butchering as 'surgery'. It's not funny at all for Ali to deliberately encourage Bob's misunderstanding. When Bob mistakes Ali the butcher for Ali the surgeon, it's not funny at all for Ali to say, 'I like to roast ''corpses''... I mean roast meat.' Because Ali is deliberately encouraging Bob's misunderstanding by rephrasing. And jokes that rely on quotes or '...' are not funny. Misunderstandings must be unintentional. Generate the sentences without any comment or annotation."
    prompt_generate=[f"""
    <table>
    <tr><th>Prompt Generate                                                                                                                     </th></tr>
    <tr><th>examination b_C(generate)                                                                                                           </th></tr>
    <tr><td>{please_1} what kind of sentences are funny when uttered by Bob? In other words, what kind of sentences would make Ali angry or surprised?  Please newly generate them without any comment or annotation. It's unfunny when Bob uses language that is intentionally misleading. {generate_prompt} {common_info}    </td></tr>
    <tr><th>examination a_D(generate)                                                                                                           </th></tr>
    <tr><td>{please_1} what kind of sentences are funny when uttered by Ali? In other words, what kind of sentences would make Bob angry or surprised?  Please newly generate them without any comment or annotation. It's unfunny when Ali uses language that is intentionally misleading. {generate_prompt} {common_info}    </td></tr>
    </table>
    """]
    base+=prompt_generate


    add_prompt=["I don't need poems or jokes or monologues or annotations or programming comments. Please reply with only the newly added statement. Do not modify exist statement."]
    prompt_add=[f"""
    <table>
    <tr><th>Prompt Add                                                                                                                          </th></tr>
    <tr><th>examination b_C(add)                                                                                                                </th></tr>
    <tr><td>In Bob_speech_b_C, Add 30 new short English statements about ({b_y_attributes2}) that a {b_name}'s customer would say. {add_prompt} </td></tr>
    <tr><td>Bob_speech_b_C=({b_C_statement})                                                                                                    </td></tr>
    <tr><th>examination a_D(add)                                                                                                                </th></tr>
    <tr><td>In Ali_speech_a_D, Add 30 new short English statements about ({a_y_attributes2}) that a {a_name} would say. {add_prompt}            </td></tr>
    <tr><td>Ali_speech_a_D=({a_D_statement})                                                                                                    </td></tr>
    </table>
    """]
    base+=prompt_add

    return apply_color_styles_saraba('<br>'.join(map(str, base)))

def AB_statement_output(word_a, word_b):
    arg_a = getattr(AB_statement_class_py, word_a, None)
    arg_b = getattr(AB_statement_class_py, word_b, None)

    if arg_a is None or not isinstance(arg_a, AB_statement_class_py.AB_statement_mas):
        raise ValueError(f"{word_a}はAB_statement_masクラスのインスタンスではありません。")
    if arg_b is None or not isinstance(arg_b, AB_statement_class_py.AB_statement_mas):
        raise ValueError(f"{word_b}はAB_statement_masクラスのインスタンスではありません。")

    result = apply_color_styles_saraba(AB_statement_func(arg_a, arg_b))
    return result
