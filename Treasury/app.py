import random
import streamlit as st
from events import EVENTS

IDLE_CHANCE = 0.15

st.set_page_config(
    page_title="财政部长模拟器",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== 顶层初始化会话变量 ==========
init_keys = ["auto_mode", "day", "event_resolved",
             "current_event", "decision_log"]
for k in init_keys:
    if k not in st.session_state:
        if k == "auto_mode":
            st.session_state[k] = "manual"
        elif k == "day":
            st.session_state[k] = 1
        elif k == "event_resolved":
            st.session_state[k] = True
        elif k == "current_event":
            st.session_state[k] = None
        elif k == "decision_log":
            st.session_state[k] = []


st.title("🏛️ United States Department of the Treasury")
st.subheader("财政部长模拟器")

#大字典
NAME_CN = {
    "budget_balance": "财政余额",
    "gdp_growth": "GDP增长",
    "forex_reserve": "外汇储备",
    "public_satisfaction": "民众满意度",
    "presidential_trust": "总统信任度",
    "public_debt": "公共债务",
    "inflation": "通货膨胀",
    "unemployment": "失业率"
}


#洗牌
def shuffle_event_choices(event: dict):
    indexed = list(enumerate(event["choices"]))
    random.shuffle(indexed)
    shuffled_idx, shuffled_choices = zip(*indexed)
    new_choices = []
    for orig_idx, choice in zip(shuffled_idx, shuffled_choices):
        copied = choice.copy()
        copied["original_index"] = orig_idx
        new_choices.append(copied)
    new_event = event.copy()
    new_event["choices"] = new_choices
    return new_event

#初始设定
def init_simulation(era, auto_mode):
    country = {}
    if era == "bretton_woods":
        country["budget_balance"] = random.randint(52, 88)
        country["gdp_growth"] = random.randint(52, 88)
        country["forex_reserve"] = random.randint(52, 88)
        country["public_satisfaction"] = random.randint(52, 88)
        country["presidential_trust"] = random.randint(52, 88)
        country["public_debt"] = random.randint(18, 55)
        country["inflation"] = random.randint(18, 55)
        country["unemployment"] = random.randint(18, 55)
    else:
        country["budget_balance"] = random.randint(48, 84)
        country["gdp_growth"] = random.randint(48, 84)
        country["forex_reserve"] = random.randint(48, 84)
        country["public_satisfaction"] = random.randint(48, 84)
        country["presidential_trust"] = random.randint(48, 84)
        country["public_debt"] = random.randint(24, 62)
        country["inflation"] = random.randint(24, 62)
        country["unemployment"] = random.randint(24, 62)

    st.session_state.country = country
    st.session_state.era = era
    st.session_state.mode = auto_mode
    st.session_state.auto_mode = auto_mode
    st.session_state.day = 1
    st.session_state.max_day = 45
    st.session_state.secretary_alerts = []
    st.session_state.running = True
    st.session_state.current_event = None
    st.session_state.event_resolved = True
    st.session_state.decision_log = []



#抽取事件
def pick_event(era: str, idle_chance: float = IDLE_CHANCE):
    if random.random() < idle_chance:
        return None
    # 布雷顿森林可以抽取全部事件池
    if era == "bretton_woods":
        pool = EVENTS.copy()
    else:
        pool = [
            e for e in EVENTS
            if e["era"] == "any" or e["era"] == era
        ]
    if not pool:
        return None
    weights = [e["weight"] for e in pool]
    picked = random.choices(pool, weights=weights, k=1)[0]
    return picked

#根据当前副部长模式，决定抽出来的弹窗是部长干还是副部长干
def handle_event_by_mode(event, mode):
    tier = event["tier"]
    if mode == "manual":
        return "popup"
    if mode == "full_auto":
        if tier == 3:
            return "popup"
        target_id = event["auto_choice"]
        selected = next(
            c for c in event["choices"]
            if c["original_index"] == target_id
        )
        return selected["effect"]
    if mode == "crisis_auto":
        if tier == 3:
            target_id = event["auto_choice"]
            selected = next(
                c for c in event["choices"]
                if c["original_index"] == target_id
            )
            return selected["effect"]
        return "popup"
    return "popup"

#国家摘要
def generate_starting_summary():
    c = st.session_state.country
    strengths = []
    weaknesses = []
    if c["forex_reserve"] >= 75:
        strengths.append("外汇储备充足")
    elif c["forex_reserve"] <= 45:
        weaknesses.append("外汇储备偏低")
    if c["public_debt"] <= 32:
        strengths.append("政府债务较轻")
    elif c["public_debt"] >= 59:
        weaknesses.append("政府债务偏高")
    if c["inflation"] <= 32:
        strengths.append("通胀温和可控")
    elif c["inflation"] >= 59:
        weaknesses.append("通胀压力较大")
    if c["unemployment"] <= 32:
        strengths.append("就业情况较好")
    elif c["unemployment"] >= 59:
        weaknesses.append("失业率偏高")
    if c["gdp_growth"] >= 75:
        strengths.append("经济增长势头良好")
    elif c["gdp_growth"] <= 45:
        weaknesses.append("增长动能偏弱")
    if c["budget_balance"] >= 75:
        strengths.append("财政收支充裕")
    elif c["budget_balance"] <= 45:
        weaknesses.append("财政收支紧张")
    if c["public_satisfaction"] >= 75:
        strengths.append("民众支持度较高")
    elif c["public_satisfaction"] <= 45:
        weaknesses.append("民众满意度偏低")
    if c["presidential_trust"] >= 75:
        strengths.append("总统对你较为信任")
    elif c["presidential_trust"] <= 45:
        weaknesses.append("总统对你不太放心")
    if not strengths:
        strengths.append("暂无明显优势")
    if not weaknesses:
        weaknesses.append("暂无明显短板")
    text = (
        f"📌本局开局国情：优势：{'、'.join(strengths)}；"
        f"短板：{'、'.join(weaknesses)}。政治决策需要权衡利弊。"
    )
    return text


#每天自然小幅度波动
def drift_economy():
    country = st.session_state.country
    for k, v in country.items():
        if isinstance(v, (int, float)):
            delta = random.uniform(-1.0, 0.8)
            country[k] = max(0.0, min(100.0, v + delta))

#评价标准
def get_status_label(name, value):
    rules = {
        "budget_balance": {"low": 45, "high": 75},
        "gdp_growth": {"low": 45, "high": 75},
        "forex_reserve": {"low": 45, "high": 75},
        "public_satisfaction": {"low": 45, "high": 75},
        "presidential_trust": {"low": 45, "high": 75},
        "public_debt": {"green": 32, "danger": 59},
        "inflation": {"green": 32, "danger": 59},
        "unemployment": {"green": 32, "danger": 59}
    }
    high_bad = ["inflation", "unemployment", "public_debt"]
    r = rules[name]
    if name in high_bad:
        if value >= r["danger"]:
            return "🔴危险"
        elif value <= r["green"]:
            return "🟢健康"
        else:
            return "🟡留意"
    else:
        if value <= r["low"]:
            return "🔴危险"
        elif value >= r["high"]:
            return "🟢健康"
        else:
            return "🟡留意"

#晨报
def generate_morning_brief():
    data = st.session_state.country
    mode = st.session_state.auto_mode
    warnings = []
    critical = []
    for k, val in data.items():
        tag = get_status_label(k, val)
        cn = NAME_CN[k]
        if "🔴" in tag:
            critical.append(cn)
        elif "🟡" in tag:
            warnings.append(cn)
    brief = ["**副部长晨间简报**"]
    brief.append(f"今天是第 {st.session_state.day} 天。")
    if mode == "manual":
        if warnings:
            brief.append(f"🟡 需要留意：{', '.join(warnings)}")
        if critical:
            brief.append(f"🔴 紧急风险：{', '.join(critical)}")
        if not warnings and not critical:
            brief.append("🟢 当前各项指标平稳，暂无明显风险。")
    elif mode == "crisis_auto":
        all_risk = warnings + critical
        if all_risk:
            brief.append(f"⚠️ 当前风险项：{', '.join(all_risk)}")
        else:
            brief.append("🟢没有达到需要干预的风险水平。")
    elif mode == "full_auto":
        if critical:
            brief.append(f"🔴重大危机：{', '.join(critical)}")
        else:
            brief.append("🟢财政系统运行平稳，日常事务自动处理。")
    return "\n\n".join(brief)

#把事件选择带来的数值变化加进国库里
def apply_delta(delta):
    country = st.session_state.country
    for key, change in delta.items():
        country[key] = max(0.0, min(100.0, country[key] + change))

#结果
def calculate_ending():
    country = st.session_state.country
    pb = country["budget_balance"]
    gdp = country["gdp_growth"]
    forex = country["forex_reserve"]
    satisfy = country["public_satisfaction"]
    trust = country["presidential_trust"]
    debt = country["public_debt"]
    cpi = country["inflation"]
    unemp = country["unemployment"]

    # 🔴失败结局，优先判断
    # 信任跌到危险线下方很深，被解雇
    if trust <= 28:
        title = "🔴 你被总统解雇了"
        desc = "总统对你长期失去信任。虽然国家还没有全面崩盘，你已经被解除财政部长职务，本届任期到此结束。"
        return 0, title, desc

    # 主权信用崩盘：债务、通胀、外汇三项危机任意两项达到深度危机
    crisis_count = 0
    if debt >= 72:
        crisis_count += 1
    if cpi >= 72:
        crisis_count += 1
    if forex <= 28:
        crisis_count += 1
    if crisis_count >= 2:
        title = "🔴 1929坏结局"
        desc = "主权信用彻底崩塌，恶性通货膨胀爆发，政府债务违约，本国货币信用体系瓦解，一场全面的金融危机席卷全国。"
        return 0, title, desc

    # 民众彻底暴动
    if satisfy <= 26:
        title = "🔴 法国大革命"
        desc = "民众满意度跌至谷底，罢工、街头暴乱接连爆发。即便财政账面尚算平稳，国家社会秩序已经失控。"
        return 0, title, desc

    # 🟢顶级完美结局：大部分指标进入仪表盘绿色健康区间
    if (25 <= cpi <= 48 and unemp <= 48 and debt <= 48
        and satisfy >= 72 and trust >= 72
        and pb >= 70 and gdp >= 70 and forex >= 70):
        title = "🟢 我去呀简直汉密尔顿在世"
        desc = "你知道我说的是哪个汉密尔顿。通胀温和、就业稳定、债务可控，民生与政府信用同时保持良好。财政可持续，社会安定，这是最理想的长期局面。"
        return 100, title, desc

    # 🟢财政优先：低债务、强财政，民生中等
    if debt <= 42 and pb >= 72 and cpi <= 52 and 48 <= satisfy <= 68 and gdp >= 58:
        title = "🟢 财政部需要很多很多钱"
        desc = "，不需要很多很多满意度。政府债务很低，财政账面十分健康，通胀保持稳定。但民众满意度只是中等水平，社会内部埋藏长期的民生矛盾。"
        return 90, title, desc

    # 🟢民生优先：满意度很高，债务偏高
    if satisfy >= 70 and gdp >= 58 and cpi <= 55 and 48 <= debt <= 68:
        title = "🟢 于是人们过上了幸福的生活…"
        desc = "高福利带来很高的民众满意度，社会总体稳定繁荣。代价是政府债务持续攀升，长期财政压力正在不断积累。"
        return 85, title, desc

    # 🟡外汇弱势中性结局
    if forex <= 42:
        title = "🟡 至少我们的货币还没有跌到津巴布韦"
        desc = "外汇储备严重不足，本币长期弱势。本国财政政策受到外部国际力量的强烈约束，经济主权不断下降，暂时还没有爆发全面危机。"
        return 50, title, desc

    # 🟡新增：轻度衰退结局
    if (debt >= 62 or cpi >= 62 or unemp >= 62
        or pb <= 50 or gdp <= 50):
        title = "🟡 希望下一任部长能撑过任期"
        desc = "部分经济指标亮起黄灯，财政压力逐步累积，如果政策不及时调整，未来很可能演化成全面危机。"
        return 45, title, desc

    # 🟡兜底：平庸停滞
    title = "🟡 普通的国家"
    desc = "各项经济指标都处在中间区间，没有极端危机，也没有走向真正繁荣。国家在低速增长中长期原地徘徊。"
    return 40, title, desc

# ======================== 主界面开始 ========================
# 开局选择界面
if "country" not in st.session_state:
    st.markdown("## 开始任期")
    era_choice = st.selectbox(
        "选择货币信用体系",
        [
            ("布雷顿森林体系", "bretton_woods"),
            ("现代主权信用货币体系", "fiat")
        ],
        format_func=lambda x: x[0]
    )
    auto_choice = st.selectbox(
        "财政托管模式",
        [
            ("手动：全部财政决策由财政部长下达", "manual"),
            ("危机托管：只有重大危机事件弹出，其余部长处理", "crisis_auto"),
            (
                "全自动托管：副部长处理日常事务；重大危机必须部长亲自决策",
                "full_auto"
            )
        ],
        format_func=lambda x: x[0]
    )
    if st.button("就任", type="primary"):
        init_simulation(era_choice[1], auto_choice[1])
        st.rerun()

else:
    era_name = {
        "bretton_woods": "布雷顿森林：黄金信用体系",
        "fiat": "现代主权信用货币体系"
    }[st.session_state.era]
    auto_name = {
        "manual": "手动：全部财政决策由财政部长下达",
        "crisis_auto": "危机托管：仅重大危机交给部长处理",
        "full_auto": (
            "全自动托管：副部长处理日常事务，重大危机必须部长亲自决策"
        )
    }[st.session_state.auto_mode]

    term_finished = st.session_state.day >= st.session_state.max_day

    # ⭐状态校验放在按钮前面
    evt = st.session_state.current_event
    valid_event = (
        isinstance(evt, dict)
        and "name" in evt
        and "desc" in evt
        and "choices" in evt
    )
    if not valid_event:
        st.session_state.current_event = None
        st.session_state.event_resolved = True
    # 国家开局摘要
    with st.expander("国情摘要", expanded=True):
    	st.write(generate_starting_summary())
    # ========= 当前信息 + 下一天按钮 =========
    col_info, col_next = st.columns([3, 1])
    with col_info:
        info_text = (
            "**当前设置**\n"
            f"- 货币体系：{era_name}\n"
            f"- 管理模式：{auto_name}\n"
            f"- 当前财政周期：第 {st.session_state.day} / {st.session_state.max_day} 天"
        )
        st.info(info_text)
    with col_next:
        next_day_disabled = (not st.session_state.event_resolved) or term_finished
        if st.button("进入下一天", use_container_width=True, disabled=next_day_disabled):
            st.session_state.day += 1
            drift_economy()
            new_evt = pick_event(st.session_state.era)
            if new_evt is None:
                st.session_state.current_event = None
                st.session_state.event_resolved = True
            else:
                new_evt = shuffle_event_choices(new_evt)
                auto_result = handle_event_by_mode(new_evt, st.session_state.mode)
                if auto_result == "popup":
                    st.session_state.current_event = new_evt
                    st.session_state.event_resolved = False
                else:
                    apply_delta(auto_result)
                    st.session_state.current_event = None
                    st.session_state.event_resolved = True
            st.rerun()

    # ========= 任期结束判定 =========
    if term_finished:
        st.markdown("---")
        st.header("🏁 任期结束")
        total_score, ending_title, ending_desc = calculate_ending()
        st.subheader(ending_title)
        st.write(ending_desc)
        st.metric("综合得分", round(total_score, 2))
        if st.button("开启新一届任期", type="primary"):
            del st.session_state["country"]
            st.rerun()

    st.markdown("---")

    # ========== 晨间简报 ==========
    st.markdown("### 📨今日晨间简报")
    st.markdown(generate_morning_brief())

    # ========== 当前事件展示板块 ==========
    st.markdown("### 当前事件")
    if not st.session_state.event_resolved and st.session_state.current_event is not None:
        evt = st.session_state.current_event
        st.subheader(evt["name"])
        st.write(evt["desc"])
        opts = evt["choices"]
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button(opts[0]["text"], use_container_width=True):
                apply_delta(opts[0]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"],
                    "choice": opts[0]["text"]
                })
                st.session_state.event_resolved = True
                st.rerun()
        with col_b:
            if st.button(opts[1]["text"], use_container_width=True):
                apply_delta(opts[1]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"],
                    "choice": opts[1]["text"]
                })
                st.session_state.event_resolved = True
                st.rerun()
        with col_c:
            if st.button(opts[2]["text"], use_container_width=True):
                apply_delta(opts[2]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"],
                    "choice": opts[2]["text"]
                })
                st.session_state.event_resolved = True
                st.rerun()
    else:
        st.success("今天没有突发重大财政事件")

    # ========== 指标表格 ==========
    st.markdown("### 国库核心指标一览")
    table_rows = []
    for key, val in st.session_state.country.items():
        table_rows.append({
            "指标": NAME_CN[key],
            "数值": round(val, 2),
            "状态": get_status_label(key, val)
        })
    st.dataframe(table_rows, use_container_width=True)

    # ========== 决策日志 ==========
    st.markdown("### 任期决策日志")
    if len(st.session_state.decision_log) == 0:
        st.info("你还没有做出任何财政决策。")
    else:
        log_rows = []
        for record in st.session_state.decision_log:
            log_rows.append({
                "天数": record["day"],
                "事件": record["event"],
                "你的选择": record["choice"]
            })
        st.dataframe(log_rows, use_container_width=True)

    st.caption("财政部长模拟器｜每一项政策都有代价。")