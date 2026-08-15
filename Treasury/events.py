EVENTS = [
    # ========== Tier 1 日常扰动 weight = 70 ==========
    # era = any
    {
        "id": "crop_harvest",
        "name": "农业收成小幅波动",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "国内粮食收成出现轻微波动，粮价存在上行的微小压力。",
        "choices": [
            {"text": "推进中长期农田水利与农业基础设施升级计划", "effect": {"budget_balance": -3, "inflation": 2, "gdp_growth": 2}},
            {"text": "维持现行农业支持政策，适度投放储备粮平抑短期价格", "effect": {"inflation": 1, "gdp_growth": 1}},
            {"text": "临时出台粮食市场指导价，稳定居民生活成本", "effect": {"public_satisfaction": 2, "gdp_growth": -3, "unemployment": 1}}
        ]
    },
    {
        "id": "consumer_sentiment",
        "name": "民众消费信心轻微起伏",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "消费者对未来收入看法略有摇摆，市场消费意愿小幅变化。",
        "choices": [
            {"text": "安排阶段性消费刺激项目，提振居民短期消费意愿", "effect": {"budget_balance": -3, "gdp_growth": 3, "inflation": 2}},
            {"text": "保持现有政策基调，等待市场信心自然修复", "effect": {"public_satisfaction": -1, "gdp_growth": 0}},
            {"text": "政府发布经济前景说明，引导公众消费预期", "effect": {"presidential_trust": 1, "inflation": 2, "gdp_growth": -2}}
        ]
    },
    {
        "id": "small_trade_order",
        "name": "收到一笔中等规模外贸订单",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "海外客户抛出一笔不大不小的外贸订单，国内出口企业迎来小幅机会。",
        "choices": [
            {"text": "设立专项出口信贷额度，协助企业承接海外订单", "effect": {"budget_balance": -3, "gdp_growth": 3, "forex_reserve": 3}},
            {"text": "交由出口企业自主评估订单风险，政府不额外干预", "effect": {"gdp_growth": 1, "forex_reserve": 1}},
            {"text": "适度调整出口规费水平，补充财政收入来源", "effect": {"budget_balance": 2, "forex_reserve": -3, "gdp_growth": -2}}
        ]
    },
    {
        "id": "local_business_proposal",
        "name": "本土小企业提交扶持申请",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "一批本土中小企业向政府提出扶持与减税诉求。",
        "choices": [
            {"text": "推出普惠性减税方案，减轻中小企业经营负担", "effect": {"budget_balance": -3, "gdp_growth": 3, "unemployment": -3}},
            {"text": "筛选部分优质项目给予有限度财政帮扶", "effect": {"gdp_growth": 1, "budget_balance": -1}},
            {"text": "暂缓新增中小企业扶持政策，优先保障财政平衡", "effect": {"budget_balance": 2, "public_satisfaction": -3, "unemployment": 2}}
        ]
    },
    {
        "id": "minor_road_repair",
        "name": "小型市政道路修缮工程",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "城市多条道路出现轻微破损，地方政府提出小型修缮计划。",
        "choices": [
            {"text": "批准完整道路翻新方案，一次性完成全线修缮", "effect": {"budget_balance": -3, "gdp_growth": 3}},
            {"text": "优先处置存在安全隐患的路段，其余道路延后维护", "effect": {"budget_balance": -1, "public_satisfaction": 1}},
            {"text": "把市政道路维护项目纳入下一年度预算再实施", "effect": {"budget_balance": 2, "public_satisfaction": -3, "gdp_growth": -2}}
        ]
    },
    {
        "id": "congress_small_budget_talk",
        "name": "国会讨论小额预算调整",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "国会就一项小规模财政预算调整展开讨论，各方意见不一。",
        "choices": [
            {"text": "与国会多数派充分协商，接纳主要修订意见", "effect": {"presidential_trust": 3, "budget_balance": -2}},
            {"text": "提交折中预算草案，逐步推动两院达成共识", "effect": {"presidential_trust": 0, "budget_balance": 0}},
            {"text": "坚持行政部门原有预算提案，减少妥协空间", "effect": {"presidential_trust": -3, "budget_balance": 2}}
        ]
    },
    {
        "id": "tourism_season",
        "name": "旅游旺季小幅带动经济",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "旅游旺季到来，外来游客数量小幅上升。",
        "choices": [
            {"text": "短期追加旅游配套设施投入，提升接待能力", "effect": {"budget_balance": -3, "gdp_growth": 3, "forex_reserve": 3}},
            {"text": "维持现有旅游服务体系，依靠市场自发承接客流", "effect": {"gdp_growth": 1, "forex_reserve": 1, "public_satisfaction": 1}},
            {"text": "适度上调景区与配套服务收费，提高旅游收益", "effect": {"budget_balance": 2, "forex_reserve": -3, "public_satisfaction": -3}}
        ]
    },
    {
        "id": "minor_labor_petition",
        "name": "小规模工人请愿诉求",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "一小部分工人发起和平请愿，提出薪资和劳动条件诉求。",
        "choices": [
            {"text": "推动行业薪酬标准上调，改善整体劳动待遇", "effect": {"budget_balance": -2, "public_satisfaction": 3, "unemployment": -2}},
            {"text": "主持劳资谈判，达成有限度改善劳动条件的协议", "effect": {"public_satisfaction": 1}},
            {"text": "维持现行劳工规章，不对请愿作出额外承诺", "effect": {"public_satisfaction": -3, "presidential_trust": -2, "unemployment": 2}}
        ]
    },
    {
        "id": "energy_price_tiny_fluctuate",
        "name": "国际油价小幅震荡",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "国际原油价格出现小幅上下波动，尚未形成明显趋势。",
        "choices": [
            {"text": "动用一部分战略石油储备平抑国内油价波动", "effect": {"budget_balance": -3, "inflation": -3, "gdp_growth": 2}},
            {"text": "国内成品油价格跟随国际市场正常调整", "effect": {"inflation": 1}},
            {"text": "设置临时油价补贴，隔离国际油价波动影响", "effect": {"budget_balance": -3, "inflation": -2, "public_debt": 2}}
        ]
    },
    {
        "id": "media_rumor_small",
        "name": "一条影响很小的市场传闻",
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "社交媒体流传一条影响有限的经济传闻，市场情绪轻微扰动。",
        "choices": [
            {"text": "官方发布澄清说明，稳定市场预期", "effect": {"budget_balance": -1, "presidential_trust": 3}},
            {"text": "暂不公开回应，观察舆情后续演变", "effect": {"presidential_trust": -1}},
            {"text": "要求平台清理不实信息，管控相关话题传播", "effect": {"public_satisfaction": -3, "presidential_trust": -2}}
        ]
    },
    # era = bretton_woods
    {
        "id": "small_gold_inflow",
        "name": "少量黄金流入本国储备",
        "era": "bretton_woods",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "少量黄金流入本国官方储备，对外清偿能力得到微小提升。",
        "choices": [
            {"text": "将流入黄金全部归入长期官方储备资产", "effect": {"forex_reserve": 3}},
            {"text": "保留大部分黄金储备，小部分进行变现操作", "effect": {"forex_reserve": 1, "budget_balance": 1}},
            {"text": "适时出售新增黄金头寸，优化短期国库现金流", "effect": {"forex_reserve": -3, "budget_balance": 3}}
        ]
    },
    {
        "id": "allies_small_gold_discuss",
        "name": "盟国之间一次小型黄金事务磋商",
        "era": "bretton_woods",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "盟国召集小型磋商，讨论黄金兑换与结算的细节问题。",
        "choices": [
            {"text": "积极参与磋商，推动多边货币合作安排", "effect": {"forex_reserve": 2, "presidential_trust": 3}},
            {"text": "派出代表有限参与磋商，谨慎表达本国立场", "effect": {"forex_reserve": 1}},
            {"text": "降低本次磋商参与层级，避免作出新承诺", "effect": {"forex_reserve": -2, "presidential_trust": -3}}
        ]
    },
    # era = fiat
    {
        "id": "short_term_capital_flow",
        "name": "短期国际小额资金进出",
        "era": "fiat",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "少量短期国际游资短暂流入流出本国金融市场。",
        "choices": [
            {"text": "完善跨境短期资本监测框架，适度加强流动管理", "effect": {"forex_reserve": 3, "gdp_growth": -2}},
            {"text": "沿用当前资本流动管理规则，保持政策连续性", "effect": {"forex_reserve": 1}},
            {"text": "简化跨境资金审批，进一步放开短期资本项目", "effect": {"forex_reserve": -3, "inflation": 3}}
        ]
    },
    {
        "id": "central_bank_micro_adjust",
        "name": "央行微小公开市场微调",
        "era": "fiat",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": "央行可以进行一次非常轻微的流动性微调操作。",
        "choices": [
            {"text": "收紧公开市场投放，适度回笼市场流动性", "effect": {"inflation": -3, "gdp_growth": -3}},
            {"text": "维持现有流动性水平，货币政策保持不变", "effect": {}},
            {"text": "加大公开市场买入，向市场补充流动性", "effect": {"gdp_growth": 3, "inflation": 3}}
        ]
    },

        # ========== Tier 2 灰犀牛前兆 weight = 25 ==========
    # era = any
    {
        "id": "inflation_rise_warning",
        "name": "通胀开始缓慢上行预警",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "物价指数连续几个月缓慢抬升，通胀压力正在逐步累积。",
        "choices": [
            {"text": "较早收紧总需求，主动压低通胀上行趋势", "effect": {"inflation": -6, "gdp_growth": -5, "unemployment": 4}},
            {"text": "小幅调整宏观政策，持续跟踪物价数据渐进应对", "effect": {"inflation": -2, "gdp_growth": -1}},
            {"text": "优先保障经济增速，暂时容忍物价温和上升", "effect": {"inflation": 5, "gdp_growth": 3, "public_debt": 4}}
        ]
    },
    {
        "id": "export_downtrend",
        "name": "出口数据连续走弱",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "海外需求放缓，出口订单连续下滑，出口部门压力慢慢加大。",
        "choices": [
            {"text": "布局长期出口产业升级，开拓新兴海外市场", "effect": {"budget_balance": -5, "gdp_growth": 5, "forex_reserve": 4}},
            {"text": "设置阶段性出口支持措施，缓冲短期下行压力", "effect": {"gdp_growth": 2, "forex_reserve": 2, "budget_balance": -2}},
            {"text": "逐步退出出口扶持政策，交由行业自行调整", "effect": {"gdp_growth": -6, "forex_reserve": -5, "unemployment": 5}}
        ]
    },
    {
        "id": "housing_price_climb",
        "name": "房地产价格持续上涨，泡沫苗头",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "房地产价格持续攀升，资产价格泡沫开始显现苗头。",
        "choices": [
            {"text": "提高房地产融资门槛，抑制过快的资产价格上涨", "effect": {"gdp_growth": -5, "inflation": -4, "unemployment": 3}},
            {"text": "出台一组温和调控工具，平缓房地产市场升温节奏", "effect": {"inflation": -2, "gdp_growth": -1}},
            {"text": "保持房地产融资环境宽松，支持不动产投资拉动增长", "effect": {"inflation": 5, "gdp_growth": 4, "public_debt": 5}}
        ]
    },
    {
        "id": "unemployment_slow_up",
        "name": "失业率逐步爬升",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "就业市场慢慢转冷，失业率连续小幅走高。",
        "choices": [
            {"text": "推出中长期职业培训与公共就业岗位扩容计划", "effect": {"budget_balance": -5, "unemployment": -6, "public_satisfaction": 4}},
            {"text": "启动短期就业补贴项目，缓解阶段性失业压力", "effect": {"unemployment": -2, "budget_balance": -1}},
            {"text": "缩减就业领域财政支出，依靠劳动力市场自发出清", "effect": {"unemployment": 6, "public_satisfaction": -5, "budget_balance": 4}}
        ]
    },
    {
        "id": "public_debt_growing",
        "name": "政府债务持续扩张",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "政府财政赤字不断累积，公共债务规模持续扩大。",
        "choices": [
            {"text": "启动中期财政整顿方案，有序压缩赤字水平", "effect": {"public_debt": -5, "gdp_growth": -4, "public_satisfaction": -3}},
            {"text": "放缓新增债务投放节奏，平稳调整财政结构", "effect": {"public_debt": -2}},
            {"text": "维持扩张性财政支出，优先拉动当前总需求", "effect": {"public_debt": 6, "inflation": 4, "presidential_trust": -4}}
        ]
    },
    {
        "id": "strike_spread",
        "name": "罢工范围慢慢扩大",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "局部行业罢工开始扩散，劳资矛盾逐步蔓延。",
        "choices": [
            {"text": "推动劳资利益再平衡，提高劳工保障标准", "effect": {"budget_balance": -4, "public_satisfaction": 5, "unemployment": -3}},
            {"text": "政府作为第三方介入调解，促成劳资双方谈判", "effect": {"unemployment": -1, "public_satisfaction": 2}},
            {"text": "维护现有企业经营秩序，限制罢工进一步扩散", "effect": {"public_satisfaction": -6, "gdp_growth": -5, "unemployment": 4}}
        ]
    },
    {
        "id": "foreign_trade_dispute",
        "name": "与他国逐步产生贸易摩擦",
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "本国与其他国家之间贸易摩擦一点点增多，贸易环境逐渐恶化。",
        "choices": [
            {"text": "主动开展高层贸易磋商，寻求双边长期和解", "effect": {"forex_reserve": -4, "gdp_growth": 5, "presidential_trust": 4}},
            {"text": "保持谈判沟通渠道，同步完善本国贸易防御机制", "effect": {"gdp_growth": 2, "forex_reserve": 1}},
            {"text": "对对方贸易措施采取对等的贸易回应行动", "effect": {"gdp_growth": -5, "forex_reserve": -6, "public_satisfaction": -3}}
        ]
    },
    # era = bretton_woods
    {
        "id": "gold_sell_off",
        "name": "黄金抛售浪潮",
        "era": "bretton_woods",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "海外央行逐步将美元兑换成黄金，本国黄金储备承受越来越大的压力。",
        "choices": [
            {"text": "设置短期黄金兑换额度管理，保护本国储备安全", "effect": {"forex_reserve": 3, "presidential_trust": -5, "inflation": 3}},
            {"text": "适度调节黄金兑付节奏，维持既有兑换承诺不变", "effect": {"forex_reserve": -3, "presidential_trust": 1}},
            {"text": "完全满足各国黄金兑换申请，依靠储备自然消化压力", "effect": {"forex_reserve": -6, "budget_balance": -4, "presidential_trust": -4}}
        ]
    },
    {
        "id": "allies_pressure_dollar",
        "name": "盟友对美元黄金兑换提出压力",
        "era": "bretton_woods",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "盟友公开对美元与黄金兑换机制表达不满，国际协调压力上升。",
        "choices": [
            {"text": "启动国际货币体系改革讨论，回应盟友主要诉求", "effect": {"forex_reserve": -4, "presidential_trust": 6}},
            {"text": "开展外交沟通安抚盟友，将深层改革议题延后讨论", "effect": {"presidential_trust": 2, "forex_reserve": -2}},
            {"text": "坚持现有货币兑换规则，不作出结构性让步", "effect": {"forex_reserve": -5, "presidential_trust": -6}}
        ]
    },
    # era = fiat
    {
        "id": "currency_confidence_shake",
        "name": "资本外流与货币信心动摇",
        "era": "fiat",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "海外投资者缓慢减持本国资产，资本持续小幅流出，市场对本币的信心开始动摇。",
        "choices": [
            {"text": "动用外汇储备进行持续汇率干预，稳定本币价格", "effect": {"forex_reserve": -5, "inflation": -3, "presidential_trust": 5}},
            {"text": "通过政策沟通引导预期，辅以小规模外汇市场操作", "effect": {"forex_reserve": -2, "inflation": -1}},
            {"text": "减少对外汇市场的直接干预，让汇率更多由市场决定", "effect": {"forex_reserve": -6, "inflation": 5, "presidential_trust": -5}}
        ]
    },
    {
        "id": "sovereign_bond_sell",
        "name": "国际投资者逐步抛售本国国债",
        "era": "fiat",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": "海外投资者慢慢抛售本国主权债券，融资成本开始走高。",
        "choices": [
            {"text": "推进财政收缩计划，改善长期国债信用基本面", "effect": {"public_debt": -5, "gdp_growth": -4, "budget_balance": 5}},
            {"text": "央行适度参与国债市场，平缓债券收益率波动", "effect": {"public_debt": -1, "inflation": 2}},
            {"text": "继续按照原有计划发行国债，不调整融资节奏", "effect": {"public_debt": 6, "gdp_growth": -5, "budget_balance": -4}}
        ]
    },

    # ========== Tier 3 黑天鹅 weight = 5 ==========
    # era = any
    {
        "id": "sudden_global_recession",
        "name": "全球经济骤然衰退",
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "毫无预兆，全球主要经济体同时陷入快速衰退，外部需求骤然萎缩。不想写原因了。",
        "choices": [
            {"text": "推出大规模内需刺激方案，对冲外部需求下滑", "effect": {"gdp_growth": -8, "budget_balance": -10, "public_debt": 9}},
            {"text": "采取适度、有边界的托底政策，承受一部分外部冲击", "effect": {"gdp_growth": -12, "forex_reserve": -7, "unemployment": 7}},
            {"text": "保持原有财政与货币立场，依靠经济体自身完成调整", "effect": {"gdp_growth": -24, "forex_reserve": -21, "unemployment": 20}}
        ]
    },
    {
        "id": "world_oil_supply_shock",
        "name": "国际原油供给突然中断",
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "突发地缘冲突导致国际原油供应骤然中断，油价瞬间暴涨。做一次飞机价格飙升至500万美金！",
        "choices": [
            {"text": "集中释放战略石油储备，缓解国内能源供应紧张", "effect": {"forex_reserve": -9, "budget_balance": -8, "inflation": -4}},
            {"text": "分批次释放少量储备，其余由市场消化油价上涨影响", "effect": {"inflation": 9, "gdp_growth": -8, "unemployment": 7}},
            {"text": "不动用战略储备，允许国内能源价格跟随国际市场上行", "effect": {"inflation": 23, "gdp_growth": -21, "unemployment": 20}}
        ]
    },
    {
        "id": "president_sudden_death",
        "name": "总统突然暴毙",
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "现任总统毫无征兆骤然离世，或许是暗杀？国家政治稳定性受到巨大冲击。",
        "choices": [
            {"text": "延迟权力交接流程，等待内部各方达成新的共识", "effect": {"presidential_trust": -10, "gdp_growth": -8, "public_satisfaction": -9}},
            {"text": "依照既有程序组建过渡团队，维持政策大体连续", "effect": {"presidential_trust": -7, "public_satisfaction": -6, "gdp_growth": -5}},
            {"text": "各派系重新博弈，对现行经济政策进行较大幅度调整", "effect": {"presidential_trust": -22, "inflation": 22, "gdp_growth": -20}}
        ]
    },
    # era = bretton_woods
    {
        "id": "cuba_missile_crisis",
        "name": "古巴导弹危机——JFK回合！",
        "era": "bretton_woods",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "冷战军事对峙骤然爆发，局势一夜之间滑向危险边缘。",
        "choices": [
            {"text": "提升军事部署等级，施加强硬军事压力", "effect": {"public_debt": 10, "forex_reserve": -8, "inflation": 9}},
            {"text": "作出有限军事姿态，同时保持外交谈判通道畅通", "effect": {"public_debt": 6, "forex_reserve": -5, "inflation": 4}},
            {"text": "采取全面对抗姿态处理", "effect": {"public_debt": 24, "forex_reserve": -22, "presidential_trust": -20}}
        ]
    },
    {
        "id": "panic_gold_rush",
        "name": "各国集中挤兑黄金",
        "era": "bretton_woods",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "一夜之间多国央行同时要求把美元兑换成黄金，大规模黄金挤兑突然爆发。",
        "choices": [
            {"text": "临时暂停黄金兑换业务，争取国际协商时间", "effect": {"forex_reserve": -3, "presidential_trust": -9, "inflation": 8}},
            {"text": "继续履行黄金兑换义务，通过外交渠道呼吁各方克制", "effect": {"forex_reserve": -8, "budget_balance": -6, "presidential_trust": -5}},
            {"text": "按照原有兑换条款无条件满足所有央行提取黄金要求", "effect": {"forex_reserve": -24, "budget_balance": -21, "presidential_trust": -20}}
        ]
    },
    # era = fiat
    {
        "id": "global_bank_panic",
        "name": "国际大型银行突发危机",
        "era": "fiat",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "一家重量级跨国大型银行毫无预警破产！",
        "choices": [
            {"text": "出台广泛金融兜底承诺，稳定整个金融市场信心", "effect": {"public_debt": 9, "budget_balance": -8, "inflation": 7}},
            {"text": "选择性救助关键金融机构，其余机构交由市场处置", "effect": {"gdp_growth": -8, "unemployment": 6, "public_debt": 5}},
            {"text": "不设立专项救助计划，允许金融机构自行承担损失", "effect": {"gdp_growth": -23, "unemployment": 22, "public_debt": 20}}
        ]
    },
    {
        "id": "panic_capital_flight",
        "name": "国际资本恐慌式集体出逃",
        "era": "fiat",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": "市场情绪毫无征兆瞬间反转，国际资本在极短时间内大规模恐慌撤离本国。",
        "choices": [
            {"text": "紧急完善跨境资本流动管理规则，抑制资本快速外流", "effect": {"forex_reserve": -4, "gdp_growth": -9, "presidential_trust": -7}},
            {"text": "动用少量外汇储备进行干预，配合预期管理", "effect": {"forex_reserve": -7, "inflation": 7, "budget_balance": -5}},
            {"text": "保持资本项目政策不变，让跨境资本自由流动", "effect": {"forex_reserve": -24, "inflation": 22, "presidential_trust": -21}}
        ]
    }
]