import aristophanes_inst
from agent_output import coloring


def aristophanes_func():
    base=[]
    base.append("*ivw(Ali talks about inanimate. Bob misunderstands that about woman.)*")
    for i in aristophanes_inst.Ivw.ALL_IVW:
        base.append(f"""
        <table>
        </tr><th id="th_cyan">{i.ivw_name}</th><td>{i.line}</td></tr>
        </table>
        """)
    base.append("*wvi(Ali talks about woman. Bob misunderstands that about inanimate.)*")
    for i in aristophanes_inst.Wvi_dict:
        base.append(f"""
        <table>
        <tr><th id="th_cyan">{i}</th><td>{', '.join(aristophanes_inst.Wvi_dict[i])}</td></tr>
        </table>
        """)
    base.append("*avh(Ali talks about animal. Bob misunderstands that about human.)*")
    for i in aristophanes_inst.Avh_dict:
        base.append(f"""
        <table>
        <tr><th id="th_cyan">{i}</th><td>{', '.join(aristophanes_inst.Avh_dict[i])}</td></tr>
        </table>
        """)
    base.append("*hva(Ali talks about human. Bob misunderstands that about animal.)*")
    for i in aristophanes_inst.Hva_dict:
        base.append(f"""
        <table>
        <tr><th id="th_cyan">{i}</th><td>{', '.join(aristophanes_inst.Hva_dict[i])}</td></tr>
        </table>
        """)
    base.append("eve(Ali talks about {ali_place}. Bob misunderstands that about {bob_place})")
    hoge=aristophanes_inst.eve_func()
    base.append(hoge)

    return coloring(''.join(base))
