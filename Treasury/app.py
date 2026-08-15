import random
import streamlit as st
from events import EVENTS
IDLE_CHANCE = 0.15
st.set_page_config(
    page_title="财政部长模拟器",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ===================== 新增双语语言模块（仅新增，不改动原有代码） =====================
# 会话状态默认中文
if "lang_global" not in st.session_state:
    st.session_state.lang_global = "zh"
# 界面固定文本双语词典，原有中文完全保留不修改
UI_LANG = {
    "zh": {
        "page_title": "财政部长模拟器",
        "main_title": "🏛️ United States Department of the Treasury",
        "sub_title": "财政部长模拟器",
        "start_term": "## 开始任期",
        "select_system": "选择货币信用体系",
        "select_mode": "财政托管模式",
        "take_office": "就任",
        "era_bretton": "布雷顿森林体系",
        "era_fiat": "现代主权信用货币体系",
        "mode_manual": "手动：全部财政决策由财政部长下达",
        "mode_crisis_auto": "危机托管：只有重大危机事件弹出，其余部长处理",
        "mode_full_auto": "全自动托管：副部长处理日常事务；重大危机必须部长亲自决策",
        "era_name_bretton": "布雷顿森林：黄金信用体系",
        "era_name_fiat": "现代主权信用货币体系",
        "info_current_setting": "**当前设置**",
        "info_system": "- 货币体系：",
        "info_mode": "- 管理模式：",
        "info_cycle": "- 当前财政周期：第 ",
        "info_cycle_suffix": " / ",
        "info_cycle_day": " 天",
        "next_day_btn": "进入下一天",
        "expander_summary": "国情摘要",
        "term_end_header": "🏁 任期结束",
        "new_term_btn": "开启新一届任期",
        "morning_brief_header": "### 📨今日晨间简报",
        "event_header": "### 当前事件",
        "no_event_tip": "今天没有突发重大财政事件",
        "metric_table_header": "### 国库核心指标一览",
        "table_col_name": "指标",
        "table_col_val": "数值",
        "table_col_status": "状态",
        "log_header": "### 任期决策日志",
        "empty_log_tip": "你还没有做出任何财政决策。",
        "log_col_day": "天数",
        "log_col_event": "事件",
        "log_col_choice": "你的选择",
        "page_caption": "财政部长模拟器｜每一项政策都有代价。",
        "strength_tag": "优势：",
        "weakness_tag": "短板：",
        "brief_title": "**副部长晨间简报**",
        "brief_today": "今天是第 ",
        "brief_today_suffix": " 天。",
        "brief_warn": "🟡 需要留意：",
        "brief_critical": "🔴 紧急风险：",
        "brief_safe": "🟢 当前各项指标平稳，暂无明显风险。",
        "brief_risk_all": "⚠️ 当前风险项：",
        "brief_risk_none": "🟢没有达到需要干预的风险水平。",
        "brief_crisis_big": "🔴重大危机：",
        "brief_auto_safe": "🟢财政系统运行平稳，日常事务自动处理。"
    },
    "en": {
        "page_title": "Secretary of the Treasury Simulator",
        "main_title": "🏛️ United States Department of the Treasury",
        "sub_title": "Secretary of the Treasury Simulator",
        "start_term": "## Start Your Term",
        "select_system": "Select Monetary Credit System",
        "select_mode": "Treasury Management Mode",
        "take_office": "Take Office",
        "era_bretton": "Bretton Woods System",
        "era_fiat": "Modern Fiat Credit Currency System",
        "mode_manual": "Manual: All fiscal decisions made by Treasury Secretary",
        "mode_crisis_auto": "Crisis Auto: Only major crisis popups; routine handled by deputy",
        "mode_full_auto": "Full Auto: Deputy handles daily work; Secretary must resolve major crises",
        "era_name_bretton": "Bretton Woods: Gold-Backed Credit System",
        "era_name_fiat": "Modern Fiat Monetary System",
        "info_current_setting": "**Current Settings**",
        "info_system": "- Monetary System: ",
        "info_mode": "- Management Mode: ",
        "info_cycle": "- Current Fiscal Cycle: Day ",
        "info_cycle_suffix": " / ",
        "info_cycle_day": "",
        "next_day_btn": "Proceed To Next Day",
        "expander_summary": "National Economic Overview",
        "term_end_header": "🏁 Term Completed",
        "new_term_btn": "Start A New Term",
        "morning_brief_header": "### 📨 Daily Morning Brief",
        "event_header": "### Current Incident",
        "no_event_tip": "No major unexpected fiscal incidents today",
        "metric_table_header": "### Core National Treasury Indicators",
        "table_col_name": "Indicator",
        "table_col_val": "Value",
        "table_col_status": "Status",
        "log_header": "### Term Decision Log",
        "empty_log_tip": "You have not made any fiscal decisions yet.",
        "log_col_day": "Day",
        "log_col_event": "Incident",
        "log_col_choice": "Your Choice",
        "page_caption": "Secretary of the Treasury Simulator | Every policy carries tradeoffs.",
        "strength_tag": "Strengths: ",
        "weakness_tag": "Weaknesses: ",
        "brief_title": "**Deputy Secretary Morning Briefing**",
        "brief_today": "Today is Day ",
        "brief_today_suffix": ".",
        "brief_warn": "🟡 Watch Closely: ",
        "brief_critical": "🔴 Critical Risks: ",
        "brief_safe": "🟢 All indicators stable, no immediate risks detected.",
        "brief_risk_all": "⚠️ Active Risk Items: ",
        "brief_risk_none": "🟢 No risks requiring intervention.",
        "brief_crisis_big": "🔴 Major Crises: ",
        "brief_auto_safe": "🟢 Treasury system stable, daily tasks processed automatically."
    }
}
# 指标名称双语映射，原有中文NAME_CN完全保留
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
NAME_EN = {
    "budget_balance": "Fiscal Balance",
    "gdp_growth": "GDP Growth",
    "forex_reserve": "Foreign Exchange Reserves",
    "public_satisfaction": "Public Satisfaction",
    "presidential_trust": "Presidential Confidence",
    "public_debt": "National Public Debt",
    "inflation": "Inflation Rate",
    "unemployment": "Unemployment Rate"
}
# 状态标签双语
STATUS_CN = {
    "🔴危险": "🔴危险",
    "🟡留意": "🟡留意",
    "🟢健康": "🟢健康"
}
STATUS_EN = {
    "🔴危险": "🔴 Critical",
    "🟡留意": "🟡 Caution",
    "🟢健康": "🟢 Healthy"
}
# 结局文本双语字典（原有中文结局文本完全不动，仅新增英文）
ENDING_TEXT = {
    "zh": {
        "fired_title": "🔴 你被总统解雇了",
        "fired_desc": "总统对你长期失去信任。虽然国家还没有全面崩盘，你已经被解除财政部长职务，本届任期到此结束。",
        "crash_title": "🔴 1929坏结局",
        "crash_desc": "主权信用彻底崩塌，恶性通货膨胀爆发，政府债务违约，本国货币信用体系瓦解，一场全面的金融危机席卷全国。",
        "revolt_title": "🔴 法国大革命",
        "revolt_desc": "民众满意度跌至谷底，罢工、街头暴乱接连爆发。即便财政账面尚算平稳，国家社会秩序已经失控。",
        "perfect_title": "🟢 我去呀简直汉密尔顿在世",
        "perfect_desc": "你知道我说的是哪个汉密尔顿。通胀温和、就业稳定、债务可控，民生与政府信用同时保持良好。财政可持续，社会安定，这是最理想的长期局面。",
        "fiscal_win_title": "🟢 财政部需要很多很多钱",
        "fiscal_win_desc": "，不需要很多很多满意度。政府债务很低，财政账面十分健康，通胀保持稳定。但民众满意度只是中等水平，社会内部埋藏长期的民生矛盾。",
        "people_win_title": "🟢 于是人们过上了幸福的生活…",
        "people_win_desc": "高福利带来很高的民众满意度，社会总体稳定繁荣。代价是政府债务持续攀升，长期财政压力正在不断积累。",
        "weak_forex_title": "🟡 至少我们的货币还没有跌到津巴布韦",
        "weak_forex_desc": "外汇储备严重不足，本币长期弱势。本国财政政策受到外部国际力量的强烈约束，经济主权不断下降，暂时还没有爆发全面危机。",
        "recession_title": "🟡 希望下一任部长能撑过任期",
        "recession_desc": "部分经济指标亮起黄灯，财政压力逐步累积，如果政策不及时调整，未来很可能演化成全面危机。",
        "normal_title": "🟡 普通的国家",
        "normal_desc": "各项经济指标都处在中间区间，没有极端危机，也没有走向真正繁荣。国家在低速增长中长期原地徘徊。",
        "score_label": "综合得分"
    },
    "en": {
        "fired_title": "🔴 Dismissed by the President",
        "fired_desc": "The President has lost long-term confidence in you. Though the nation has not fully collapsed, you are relieved of your duties as Treasury Secretary, ending your term immediately.",
        "crash_title": "🔴 Catastrophe of 1929",
        "crash_desc": "Sovereign credit collapses completely; hyperinflation erupts, government defaults on debt, domestic currency credit system disintegrates, and a full-scale financial crisis engulfs the country.",
        "revolt_title": "🔴 Popular Revolution",
        "revolt_desc": "Public satisfaction hits rock bottom; strikes and street riots break out continuously. Even if fiscal books remain stable, domestic social order is out of control.",
        "perfect_title": "🟢 Second Coming of Hamilton",
        "perfect_desc": "You know exactly which Hamilton this refers to. Mild inflation, stable employment, manageable debt, strong public support and presidential trust. Sustainable public finance and social stability, the ideal long-term state.",
        "fiscal_win_title": "🟢 Treasury Prioritizes Surplus Capital",
        "fiscal_win_desc": "Public approval remains secondary. Low national debt, robust fiscal balance and stable inflation, yet moderate public satisfaction hides long-term social conflicts.",
        "people_win_title": "🟢 Citizens Live Prosperous Lives…",
        "people_win_desc": "Generous welfare programs lift public satisfaction and stabilize society. The tradeoff is rising national debt, creating lasting long-term fiscal pressure.",
        "weak_forex_title": "🟡 Currency Not Yet Collapsed Completely",
        "weak_forex_desc": "Severely depleted foreign reserves weaken domestic currency. Domestic fiscal policy is heavily constrained by international forces, eroding economic sovereignty with no full crisis yet.",
        "recession_title": "🟡 The Next Secretary Will Face Hardship",
        "recession_desc": "Multiple economic indicators flash warning signals. Mounting fiscal pressure risks escalating into a full crisis without timely policy adjustments.",
        "normal_title": "🟡 Mediocre Stagnant Nation",
        "normal_desc": "All economic indicators sit in neutral territory, with neither catastrophic collapse nor genuine prosperity. The nation stagnates under slow growth.",
        "score_label": "Overall Score"
    }
}
# 顶部语言切换单选框，仅新增，不修改原有逻辑
lang_selector = st.radio(
    "Language / 语言",
    ["zh", "en"],
    format_func=lambda x: "中文" if x == "zh" else "English",
    horizontal=True
)
st.session_state.lang_global = lang_selector
L = UI_LANG[st.session_state.lang_global]
# ==============================================
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
# 标题替换为双语读取，原有中文文本完全保留在词典内
st.title(L["main_title"])
st.subheader(L["sub_title"])
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
    # 双语拼接，中文原文完全保留
    if st.session_state.lang_global == "zh":
        text = (
            f"📌本局开局国情：{L['strength_tag']}{'、'.join(strengths)}；"
            f"{L['weakness_tag']}{'、'.join(weaknesses)}。政治决策需要权衡利弊。"
        )
    else:
        # 配套英文国情描述（不删除原有中文，仅切换展示）
        strength_en_map = {
            "外汇储备充足": "Sufficient foreign exchange reserves",
            "外汇储备偏低": "Low foreign exchange reserves",
            "政府债务较轻": "Low national public debt",
            "政府债务偏高": "High national public debt",
            "通胀温和可控": "Mild and manageable inflation",
            "通胀压力较大": "Severe inflation pressure",
            "就业情况较好": "Strong employment performance",
            "失业率偏高": "High unemployment rate",
            "经济增长势头良好": "Robust economic growth momentum",
            "增长动能偏弱": "Weak growth momentum",
            "财政收支充裕": "Healthy fiscal surplus",
            "财政收支紧张": "Tight fiscal balance",
            "民众支持度较高": "High public approval",
            "民众满意度偏低": "Low public satisfaction",
            "总统对你较为信任": "Strong presidential confidence in you",
            "总统对你不太放心": "Low presidential trust in you",
            "暂无明显优势": "No distinct strengths",
            "暂无明显短板": "No obvious weaknesses"
        }
        en_strengths = [strength_en_map[s] for s in strengths]
        en_weaknesses = [strength_en_map[w] for w in weaknesses]
        text = (
            f"📌 Opening Economic Profile: {L['strength_tag']}{', '.join(en_strengths)}; "
            f"{L['weakness_tag']}{', '.join(en_weaknesses)}. Every political decision carries tradeoffs."
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
    tag_cn = ""
    if name in high_bad:
        if value >= r["danger"]:
            tag_cn = "🔴危险"
        elif value <= r["green"]:
            tag_cn = "🟢健康"
        else:
            tag_cn = "🟡留意"
    else:
        if value <= r["low"]:
            tag_cn = "🔴危险"
        elif value >= r["high"]:
            tag_cn = "🟢健康"
        else:
            tag_cn = "🟡留意"
    # 根据语言返回对应标签
    if st.session_state.lang_global == "zh":
        return STATUS_CN[tag_cn]
    else:
        return STATUS_EN[tag_cn]
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
    brief = [L["brief_title"]]
    brief.append(f"{L['brief_today']}{st.session_state.day}{L['brief_today_suffix']}")
    if mode == "manual":
        if warnings:
            brief.append(f"{L['brief_warn']}{', '.join(warnings)}")
        if critical:
            brief.append(f"{L['brief_critical']}{', '.join(critical)}")
        if not warnings and not critical:
            brief.append(L["brief_safe"])
    elif mode == "crisis_auto":
        all_risk = warnings + critical
        if all_risk:
            brief.append(f"{L['brief_risk_all']}{', '.join(all_risk)}")
        else:
            brief.append(L["brief_risk_none"])
    elif mode == "full_auto":
        if critical:
            brief.append(f"{L['brief_crisis_big']}{', '.join(critical)}")
        else:
            brief.append(L["brief_auto_safe"])
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
    lang = st.session_state.lang_global
    ET = ENDING_TEXT[lang]
    # 🔴失败结局，优先判断
    # 信任跌到危险线下方很深，被解雇
    if trust <= 28:
        title = ET["fired_title"]
        desc = ET["fired_desc"]
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
        title = ET["crash_title"]
        desc = ET["crash_desc"]
        return 0, title, desc
    # 民众彻底暴动
    if satisfy <= 26:
        title = ET["revolt_title"]
        desc = ET["revolt_desc"]
        return 0, title, desc
    # 🟢顶级完美结局：大部分指标进入仪表盘绿色健康区间
    if (25 <= cpi <= 48 and unemp <= 48 and debt <= 48
        and satisfy >= 72 and trust >= 72
        and pb >= 70 and gdp >= 70 and forex >= 70):
        title = ET["perfect_title"]
        desc = ET["perfect_desc"]
        return 100, title, desc
    # 🟢财政优先：低债务、强财政，民生中等
    if debt <= 42 and pb >= 72 and cpi <= 52 and 48 <= satisfy <= 68 and gdp >= 58:
        title = ET["fiscal_win_title"]
        desc = ET["fiscal_win_desc"]
        return 90, title, desc
    # 🟢民生优先：满意度很高，债务偏高
    if satisfy >= 70 and gdp >= 58 and cpi <= 55 and 48 <= debt <= 68:
        title = ET["people_win_title"]
        desc = ET["people_win_desc"]
        return 85, title, desc
    # 🟡外汇弱势中性结局
    if forex <= 42:
        title = ET["weak_forex_title"]
        desc = ET["weak_forex_desc"]
        return 50, title, desc
    # 🟡新增：轻度衰退结局
    if (debt >= 62 or cpi >= 62 or unemp >= 62
        or pb <= 50 or gdp <= 50):
        title = ET["recession_title"]
        desc = ET["recession_desc"]
        return 45, title, desc
    # 🟡兜底：平庸停滞
    title = ET["normal_title"]
    desc = ET["normal_desc"]
    return 40, title, desc
# ======================== 主界面开始 ========================
# 开局选择界面
if "country" not in st.session_state:
    st.markdown(L["start_term"])
    # 下拉框双语映射，原有中文value不变
    era_options_zh = [("布雷顿森林体系", "bretton_woods"), ("现代主权信用货币体系", "fiat")]
    era_options_en = [("Bretton Woods System", "bretton_woods"), ("Modern Fiat Credit Currency System", "fiat")]
    mode_options_zh = [
        ("手动：全部财政决策由财政部长下达", "manual"),
        ("危机托管：只有重大危机事件弹出，其余部长处理", "crisis_auto"),
        ("全自动托管：副部长处理日常事务；重大危机必须部长亲自决策", "full_auto")
    ]
    mode_options_en = [
        ("Manual: All fiscal decisions made by Treasury Secretary", "manual"),
        ("Crisis Auto: Only major crisis popups; routine handled by deputy", "crisis_auto"),
        ("Full Auto: Deputy handles daily work; Secretary must resolve major crises", "full_auto")
    ]
    if st.session_state.lang_global == "zh":
        era_display = era_options_zh
        mode_display = mode_options_zh
    else:
        era_display = era_options_en
        mode_display = mode_options_en
    era_choice = st.selectbox(
        L["select_system"],
        era_display,
        format_func=lambda x: x[0]
    )
    auto_choice = st.selectbox(
        L["select_mode"],
        mode_display,
        format_func=lambda x: x[0]
    )
    if st.button(L["take_office"], type="primary"):
        init_simulation(era_choice[1], auto_choice[1])
        st.rerun()
else:
    # 时代名称双语映射
    era_map_zh = {
        "bretton_woods": "布雷顿森林：黄金信用体系",
        "fiat": "现代主权信用货币体系"
    }
    era_map_en = {
        "bretton_woods": "Bretton Woods: Gold-Backed Credit System",
        "fiat": "Modern Fiat Monetary System"
    }
    mode_map_zh = {
        "manual": "手动：全部财政决策由财政部长下达",
        "crisis_auto": "危机托管：仅重大危机交给部长处理",
        "full_auto": "全自动托管：副部长处理日常事务，重大危机必须部长亲自决策"
    }
    mode_map_en = {
        "manual": "Manual: All fiscal decisions made by Treasury Secretary",
        "crisis_auto": "Crisis Auto: Only major crisis popups; routine handled by deputy",
        "full_auto": "Full Auto: Deputy handles daily work; Secretary must resolve major crises"
    }
    if st.session_state.lang_global == "zh":
        era_name = era_map_zh[st.session_state.era]
        auto_name = mode_map_zh[st.session_state.auto_mode]
    else:
        era_name = era_map_en[st.session_state.era]
        auto_name = mode_map_en[st.session_state.auto_mode]
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
    with st.expander(L["expander_summary"], expanded=True):
        st.write(generate_starting_summary())
    # ========= 当前信息 + 下一天按钮 =========
    col_info, col_next = st.columns([3, 1])
    with col_info:
        info_text = (
            f"{L['info_current_setting']}\n"
            f"{L['info_system']}{era_name}\n"
            f"{L['info_mode']}{auto_name}\n"
            f"{L['info_cycle']}{st.session_state.day}{L['info_cycle_suffix']}{st.session_state.max_day}{L['info_cycle_day']}"
        )
        st.info(info_text)
    with col_next:
        next_day_disabled = (not st.session_state.event_resolved) or term_finished
        if st.button(L["next_day_btn"], use_container_width=True, disabled=next_day_disabled):
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
        st.header(L["term_end_header"])
        total_score, ending_title, ending_desc = calculate_ending()
        st.subheader(ending_title)
        st.write(ending_desc)
        ET = ENDING_TEXT[st.session_state.lang_global]
        st.metric(ET["score_label"], round(total_score, 2))
        if st.button(L["new_term_btn"], type="primary"):
            del st.session_state["country"]
            st.rerun()
    st.markdown("---")
    # ========== 晨间简报 ==========
    st.markdown(L["morning_brief_header"])
    st.markdown(generate_morning_brief())
    # ========== 当前事件展示板块【已完整修复双语读取，其余代码不动】 ==========
    st.markdown(L["event_header"])
    if not st.session_state.event_resolved and st.session_state.current_event is not None:
        evt = st.session_state.current_event
        lang = st.session_state.lang_global
        st.subheader(evt["name"][lang])
        st.write(evt["desc"][lang])
        opts = evt["choices"]
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            btn_text = opts[0]["text"][lang]
            if st.button(btn_text, use_container_width=True):
                apply_delta(opts[0]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"][lang],
                    "choice": btn_text
                })
                st.session_state.event_resolved = True
                st.rerun()
        with col_b:
            btn_text = opts[1]["text"][lang]
            if st.button(btn_text, use_container_width=True):
                apply_delta(opts[1]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"][lang],
                    "choice": btn_text
                })
                st.session_state.event_resolved = True
                st.rerun()
        with col_c:
            btn_text = opts[2]["text"][lang]
            if st.button(btn_text, use_container_width=True):
                apply_delta(opts[2]["effect"])
                st.session_state.decision_log.append({
                    "day": st.session_state.day,
                    "event": evt["name"][lang],
                    "choice": btn_text
                })
                st.session_state.event_resolved = True
                st.rerun()
    else:
        st.success(L["no_event_tip"])
    # ========== 指标表格 ==========
    st.markdown(L["metric_table_header"])
    table_rows = []
    lang = st.session_state.lang_global
    for key, val in st.session_state.country.items():
        ind_name = NAME_CN[key] if lang == "zh" else NAME_EN[key]
        table_rows.append({
            L["table_col_name"]: ind_name,
            L["table_col_val"]: round(val, 2),
            L["table_col_status"]: get_status_label(key, val)
        })
    st.dataframe(table_rows, use_container_width=True)
    # ========== 决策日志 ==========
    st.markdown(L["log_header"])
    if len(st.session_state.decision_log) == 0:
        st.info(L["empty_log_tip"])
    else:
        log_rows = []
        for record in st.session_state.decision_log:
            log_rows.append({
                L["log_col_day"]: record["day"],
                L["log_col_event"]: record["event"],
                L["log_col_choice"]: record["choice"]
            })
        st.dataframe(log_rows, use_container_width=True)
    st.caption(L["page_caption"])