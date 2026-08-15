EVENTS = [
    # ========== Tier 1 日常扰动 weight = 70 ==========
    # era = any
    {
        "id": "crop_harvest",
        "name": {
            "zh": "农业收成小幅波动",
            "en": "Minor Fluctuations in Agricultural Harvests"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "国内粮食收成出现轻微波动，粮价存在上行的微小压力。",
            "en": "Domestic grain output fluctuates slightly, creating mild upward pressure on food prices."
        },
        "choices": [
            {
                "text": {
                    "zh": "推进中长期农田水利与农业基础设施升级计划",
                    "en": "Launch medium-to-long term farm irrigation and agricultural infrastructure upgrade programs"
                },
                "effect": {"budget_balance": -3, "inflation": 2, "gdp_growth": 2}
            },
            {
                "text": {
                    "zh": "维持现行农业支持政策，适度投放储备粮平抑短期价格",
                    "en": "Maintain current agricultural support policies and release grain reserves to stabilize short-term prices"
                },
                "effect": {"inflation": 1, "gdp_growth": 1}
            },
            {
                "text": {
                    "zh": "临时出台粮食市场指导价，稳定居民生活成本",
                    "en": "Temporarily set official grain price caps to stabilize household living costs"
                },
                "effect": {"public_satisfaction": 2, "gdp_growth": -3, "unemployment": 1}
            }
        ]
    },
    {
        "id": "consumer_sentiment",
        "name": {
            "zh": "民众消费信心轻微起伏",
            "en": "Slight Shifts in Consumer Confidence"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "消费者对未来收入看法略有摇摆，市场消费意愿小幅变化。",
            "en": "Consumers hold uncertain outlooks on future income, leading to minor shifts in market consumption willingness."
        },
        "choices": [
            {
                "text": {
                    "zh": "安排阶段性消费刺激项目，提振居民短期消费意愿",
                    "en": "Roll out temporary consumption stimulus packages to lift short-term household spending"
                },
                "effect": {"budget_balance": -3, "gdp_growth": 3, "inflation": 2}
            },
            {
                "text": {
                    "zh": "保持现有政策基调，等待市场信心自然修复",
                    "en": "Keep existing policy stance and allow market confidence to recover organically"
                },
                "effect": {"public_satisfaction": -1, "gdp_growth": 0}
            },
            {
                "text": {
                    "zh": "政府发布经济前景说明，引导公众消费预期",
                    "en": "Release official economic outlook statements to guide public consumption expectations"
                },
                "effect": {"presidential_trust": 1, "inflation": 2, "gdp_growth": -2}
            }
        ]
    },
    {
        "id": "small_trade_order",
        "name": {
            "zh": "收到一笔中等规模外贸订单",
            "en": "Receipt of a Medium-Sized Foreign Trade Order"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "海外客户抛出一笔不大不小的外贸订单，国内出口企业迎来小幅机会。",
            "en": "Overseas clients place a moderate-sized export order, creating minor opportunities for domestic exporters."
        },
        "choices": [
            {
                "text": {
                    "zh": "设立专项出口信贷额度，协助企业承接海外订单",
                    "en": "Create dedicated export credit lines to help firms secure overseas orders"
                },
                "effect": {"budget_balance": -3, "gdp_growth": 3, "forex_reserve": 3}
            },
            {
                "text": {
                    "zh": "交由出口企业自主评估订单风险，政府不额外干预",
                    "en": "Let export firms assess order risks independently with no extra government intervention"
                },
                "effect": {"gdp_growth": 1, "forex_reserve": 1}
            },
            {
                "text": {
                    "zh": "适度调整出口规费水平，补充财政收入来源",
                    "en": "Moderately adjust export fees to expand fiscal revenue streams"
                },
                "effect": {"budget_balance": 2, "forex_reserve": -3, "gdp_growth": -2}
            }
        ]
    },
    {
        "id": "local_business_proposal",
        "name": {
            "zh": "本土小企业提交扶持申请",
            "en": "Domestic Small Businesses Submit Support Applications"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "一批本土中小企业向政府提出扶持与减税诉求。",
            "en": "A group of domestic small and medium enterprises submit requests for subsidies and tax relief."
        },
        "choices": [
            {
                "text": {
                    "zh": "推出普惠性减税方案，减轻中小企业经营负担",
                    "en": "Implement broad-based tax cuts to reduce operating burdens for small businesses"
                },
                "effect": {"budget_balance": -3, "gdp_growth": 3, "unemployment": -3}
            },
            {
                "text": {
                    "zh": "筛选部分优质项目给予有限度财政帮扶",
                    "en": "Select high-quality projects to receive limited fiscal assistance"
                },
                "effect": {"gdp_growth": 1, "budget_balance": -1}
            },
            {
                "text": {
                    "zh": "暂缓新增中小企业扶持政策，优先保障财政平衡",
                    "en": "Pause new small business support policies to prioritize fiscal balance"
                },
                "effect": {"budget_balance": 2, "public_satisfaction": -3, "unemployment": 2}
            }
        ]
    },
    {
        "id": "minor_road_repair",
        "name": {
            "zh": "小型市政道路修缮工程",
            "en": "Minor Municipal Road Renovation Works"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "城市多条道路出现轻微破损，地方政府提出小型修缮计划。",
            "en": "Multiple urban roads suffer minor damage, and local governments propose small-scale repair plans."
        },
        "choices": [
            {
                "text": {
                    "zh": "批准完整道路翻新方案，一次性完成全线修缮",
                    "en": "Approve full road renovation plans and complete all repairs in one phase"
                },
                "effect": {"budget_balance": -3, "gdp_growth": 3}
            },
            {
                "text": {
                    "zh": "优先处置存在安全隐患的路段，其余道路延后维护",
                    "en": "Prioritize repairing hazardous road segments and delay maintenance for others"
                },
                "effect": {"budget_balance": -1, "public_satisfaction": 1}
            },
            {
                "text": {
                    "zh": "把市政道路维护项目纳入下一年度预算再实施",
                    "en": "Postpone road maintenance projects to next year’s budget cycle"
                },
                "effect": {"budget_balance": 2, "public_satisfaction": -3, "gdp_growth": -2}
            }
        ]
    },
    {
        "id": "congress_small_budget_talk",
        "name": {
            "zh": "国会讨论小额预算调整",
            "en": "Congress Debates Minor Budget Revisions"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "国会就一项小规模财政预算调整展开讨论，各方意见不一。",
            "en": "Congress holds debates over a minor fiscal budget adjustment with divided opinions across parties."
        },
        "choices": [
            {
                "text": {
                    "zh": "与国会多数派充分协商，接纳主要修订意见",
                    "en": "Negotiate fully with congressional majority and adopt core revision proposals"
                },
                "effect": {"presidential_trust": 3, "budget_balance": -2}
            },
            {
                "text": {
                    "zh": "提交折中预算草案，逐步推动两院达成共识",
                    "en": "Submit compromise budget drafts to gradually build bicameral consensus"
                },
                "effect": {"presidential_trust": 0, "budget_balance": 0}
            },
            {
                "text": {
                    "zh": "坚持行政部门原有预算提案，减少妥协空间",
                    "en": "Uphold the original executive budget proposal with limited concessions"
                },
                "effect": {"presidential_trust": -3, "budget_balance": 2}
            }
        ]
    },
    {
        "id": "tourism_season",
        "name": {
            "zh": "旅游旺季小幅带动经济",
            "en": "Tourism Season Provides Mild Economic Boost"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "旅游旺季到来，外来游客数量小幅上升。",
            "en": "The peak tourism season arrives, bringing a moderate rise in inbound visitors."
        },
        "choices": [
            {
                "text": {
                    "zh": "短期追加旅游配套设施投入，提升接待能力",
                    "en": "Temporarily fund tourism infrastructure expansions to boost visitor capacity"
                },
                "effect": {"budget_balance": -3, "gdp_growth": 3, "forex_reserve": 3}
            },
            {
                "text": {
                    "zh": "维持现有旅游服务体系，依靠市场自发承接客流",
                    "en": "Retain existing tourism services and let market forces handle visitor flows"
                },
                "effect": {"gdp_growth": 1, "forex_reserve": 1, "public_satisfaction": 1}
            },
            {
                "text": {
                    "zh": "适度上调景区与配套服务收费，提高旅游收益",
                    "en": "Moderately raise scenic spot and service fees to increase tourism revenue"
                },
                "effect": {"budget_balance": 2, "forex_reserve": -3, "public_satisfaction": -3}
            }
        ]
    },
    {
        "id": "minor_labor_petition",
        "name": {
            "zh": "小规模工人请愿诉求",
            "en": "Small-Scale Worker Petition Demands"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "一小部分工人发起和平请愿，提出薪资和劳动条件诉求。",
            "en": "A small group of workers stages a peaceful petition demanding higher wages and improved labor conditions."
        },
        "choices": [
            {
                "text": {
                    "zh": "推动行业薪酬标准上调，改善整体劳动待遇",
                    "en": "Advocate higher industry wage standards to improve overall labor benefits"
                },
                "effect": {"budget_balance": -2, "public_satisfaction": 3, "unemployment": -2}
            },
            {
                "text": {
                    "zh": "主持劳资谈判，达成有限度改善劳动条件的协议",
                    "en": "Mediate labor-management talks to reach limited agreements on working conditions"
                },
                "effect": {"public_satisfaction": 1}
            },
            {
                "text": {
                    "zh": "维持现行劳工规章，不对请愿作出额外承诺",
                    "en": "Keep current labor regulations and make no extra concessions to petitioners"
                },
                "effect": {"public_satisfaction": -3, "presidential_trust": -2, "unemployment": 2}
            }
        ]
    },
    {
        "id": "energy_price_tiny_fluctuate",
        "name": {
            "zh": "国际油价小幅震荡",
            "en": "Minor Volatility in Global Oil Prices"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "国际原油价格出现小幅上下波动，尚未形成明显趋势。",
            "en": "Global crude oil prices swing slightly with no clear long-term trend established."
        },
        "choices": [
            {
                "text": {
                    "zh": "动用一部分战略石油储备平抑国内油价波动",
                    "en": "Release portions of strategic petroleum reserves to stabilize domestic fuel prices"
                },
                "effect": {"budget_balance": -3, "inflation": -3, "gdp_growth": 2}
            },
            {
                "text": {
                    "zh": "国内成品油价格跟随国际市场正常调整",
                    "en": "Adjust domestic fuel prices in line with global market movements"
                },
                "effect": {"inflation": 1}
            },
            {
                "text": {
                    "zh": "设置临时油价补贴，隔离国际油价波动影响",
                    "en": "Implement temporary fuel subsidies to shield the economy from oil price swings"
                },
                "effect": {"budget_balance": -3, "inflation": -2, "public_debt": 2}
            }
        ]
    },
    {
        "id": "media_rumor_small",
        "name": {
            "zh": "一条影响很小的市场传闻",
            "en": "Low-Impact Market Rumor Circulates Online"
        },
        "era": "any",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "社交媒体流传一条影响有限的经济传闻，市场情绪轻微扰动。",
            "en": "A low-impact economic rumor spreads across social media, creating mild market jitters."
        },
        "choices": [
            {
                "text": {
                    "zh": "官方发布澄清说明，稳定市场预期",
                    "en": "Release official clarifications to stabilize market expectations"
                },
                "effect": {"budget_balance": -1, "presidential_trust": 3}
            },
            {
                "text": {
                    "zh": "暂不公开回应，观察舆情后续演变",
                    "en": "Withhold public statements and monitor public sentiment developments"
                },
                "effect": {"presidential_trust": -1}
            },
            {
                "text": {
                    "zh": "要求平台清理不实信息，管控相关话题传播",
                    "en": "Order platforms to remove false information and restrict related topic circulation"
                },
                "effect": {"public_satisfaction": -3, "presidential_trust": -2}
            }
        ]
    },
    # era = bretton_woods
    {
        "id": "small_gold_inflow",
        "name": {
            "zh": "少量黄金流入本国储备",
            "en": "Minor Gold Inflows to National Reserves"
        },
        "era": "bretton_woods",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "少量黄金流入本国官方储备，对外清偿能力得到微小提升。",
            "en": "Small volumes of gold enter official national reserves, marginally boosting external repayment capacity."
        },
        "choices": [
            {
                "text": {
                    "zh": "将流入黄金全部归入长期官方储备资产",
                    "en": "Classify all incoming gold as long-term official reserve assets"
                },
                "effect": {"forex_reserve": 3}
            },
            {
                "text": {
                    "zh": "保留大部分黄金储备，小部分进行变现操作",
                    "en": "Retain most gold reserves and monetize a small portion"
                },
                "effect": {"forex_reserve": 1, "budget_balance": 1}
            },
            {
                "text": {
                    "zh": "适时出售新增黄金头寸，优化短期国库现金流",
                    "en": "Sell newly acquired gold holdings to improve short-term treasury cash flow"
                },
                "effect": {"forex_reserve": -3, "budget_balance": 3}
            }
        ]
    },
    {
        "id": "allies_small_gold_discuss",
        "name": {
            "zh": "盟国之间一次小型黄金事务磋商",
            "en": "Minor Gold Affairs Consultation with Allied Nations"
        },
        "era": "bretton_woods",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "盟国召集小型磋商，讨论黄金兑换与结算的细节问题。",
            "en": "Allied nations host a small consultation to negotiate details of gold convertibility and settlement."
        },
        "choices": [
            {
                "text": {
                    "zh": "积极参与磋商，推动多边货币合作安排",
                    "en": "Participate actively in talks to advance multilateral monetary cooperation frameworks"
                },
                "effect": {"forex_reserve": 2, "presidential_trust": 3}
            },
            {
                "text": {
                    "zh": "派出代表有限参与磋商，谨慎表达本国立场",
                    "en": "Send representatives for limited participation and state national positions cautiously"
                },
                "effect": {"forex_reserve": 1}
            },
            {
                "text": {
                    "zh": "降低本次磋商参与层级，避免作出新承诺",
                    "en": "Lower delegation rank for consultations to avoid new binding commitments"
                },
                "effect": {"forex_reserve": -2, "presidential_trust": -3}
            }
        ]
    },
    # era = fiat
    {
        "id": "short_term_capital_flow",
        "name": {
            "zh": "短期国际小额资金进出",
            "en": "Small-Scale Short-Term Cross-Border Capital Flows"
        },
        "era": "fiat",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "少量短期国际游资短暂流入流出本国金融市场。",
            "en": "Small volumes of short-term international speculative capital flow in and out of domestic financial markets."
        },
        "choices": [
            {
                "text": {
                    "zh": "完善跨境短期资本监测框架，适度加强流动管理",
                    "en": "Strengthen cross-border short-term capital monitoring and moderately tighten flow regulations"
                },
                "effect": {"forex_reserve": 3, "gdp_growth": -2}
            },
            {
                "text": {
                    "zh": "沿用当前资本流动管理规则，保持政策连续性",
                    "en": "Maintain existing capital flow regulations to preserve policy consistency"
                },
                "effect": {"forex_reserve": 1}
            },
            {
                "text": {
                    "zh": "简化跨境资金审批，进一步放开短期资本项目",
                    "en": "Simplify cross-border capital approval and further liberalize short-term capital accounts"
                },
                "effect": {"forex_reserve": -3, "inflation": 3}
            }
        ]
    },
    {
        "id": "central_bank_micro_adjust",
        "name": {
            "zh": "央行微小公开市场微调",
            "en": "Minor Central Bank Open Market Tweaks"
        },
        "era": "fiat",
        "tier": 1,
        "weight": 70,
        "auto_choice": 1,
        "desc": {
            "zh": "央行可以进行一次非常轻微的流动性微调操作。",
            "en": "The central bank may execute a very minor liquidity adjustment operation."
        },
        "choices": [
            {
                "text": {
                    "zh": "收紧公开市场投放，适度回笼市场流动性",
                    "en": "Tighten open market injections and moderately withdraw market liquidity"
                },
                "effect": {"inflation": -3, "gdp_growth": -3}
            },
            {
                "text": {
                    "zh": "维持现有流动性水平，货币政策保持不变",
                    "en": "Maintain current liquidity levels with unchanged monetary policy"
                },
                "effect": {}
            },
            {
                "text": {
                    "zh": "加大公开市场买入，向市场补充流动性",
                    "en": "Expand open market purchases to inject additional liquidity into markets"
                },
                "effect": {"gdp_growth": 3, "inflation": 3}
            }
        ]
    },
    # ========== Tier 2 灰犀牛前兆 weight = 25 ==========
    # era = any
    {
        "id": "inflation_rise_warning",
        "name": {
            "zh": "通胀开始缓慢上行预警",
            "en": "Early Warning of Gradually Rising Inflation"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "物价指数连续几个月缓慢抬升，通胀压力正在逐步累积。",
            "en": "Price indices creep upward for consecutive months, with inflationary pressure steadily building."
        },
        "choices": [
            {
                "text": {
                    "zh": "较早收紧总需求，主动压低通胀上行趋势",
                    "en": "Tighten aggregate demand early to actively cool rising inflation trends"
                },
                "effect": {"inflation": -6, "gdp_growth": -5, "unemployment": 4}
            },
            {
                "text": {
                    "zh": "小幅调整宏观政策，持续跟踪物价数据渐进应对",
                    "en": "Make modest macro policy adjustments and respond gradually based on price tracking data"
                },
                "effect": {"inflation": -2, "gdp_growth": -1}
            },
            {
                "text": {
                    "zh": "优先保障经济增速，暂时容忍物价温和上升",
                    "en": "Prioritize economic growth and temporarily tolerate mild price increases"
                },
                "effect": {"inflation": 5, "gdp_growth": 3, "public_debt": 4}
            }
        ]
    },
    {
        "id": "export_downtrend",
        "name": {
            "zh": "出口数据连续走弱",
            "en": "Sustained Downward Trend in Export Figures"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "海外需求放缓，出口订单连续下滑，出口部门压力慢慢加大。",
            "en": "Slowing overseas demand causes consecutive export order declines, mounting pressure on export industries."
        },
        "choices": [
            {
                "text": {
                    "zh": "布局长期出口产业升级，开拓新兴海外市场",
                    "en": "Invest in long-term export industrial upgrading and develop emerging overseas markets"
                },
                "effect": {"budget_balance": -5, "gdp_growth": 5, "forex_reserve": 4}
            },
            {
                "text": {
                    "zh": "设置阶段性出口支持措施，缓冲短期下行压力",
                    "en": "Launch temporary export support measures to buffer short-term downward pressures"
                },
                "effect": {"gdp_growth": 2, "forex_reserve": 2, "budget_balance": -2}
            },
            {
                "text": {
                    "zh": "逐步退出出口扶持政策，交由行业自行调整",
                    "en": "Phase out export support policies and let industries adjust independently"
                },
                "effect": {"gdp_growth": -6, "forex_reserve": -5, "unemployment": 5}
            }
        ]
    },
    {
        "id": "housing_price_climb",
        "name": {
            "zh": "房地产价格持续上涨，泡沫苗头",
            "en": "Persistent Housing Price Growth Signals Asset Bubble Risks"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "房地产价格持续攀升，资产价格泡沫开始显现苗头。",
            "en": "Real estate prices surge continuously, revealing early signs of an asset price bubble."
        },
        "choices": [
            {
                "text": {
                    "zh": "提高房地产融资门槛，抑制过快的资产价格上涨",
                    "en": "Raise real estate financing thresholds to curb excessive asset price inflation"
                },
                "effect": {"gdp_growth": -5, "inflation": -4, "unemployment": 3}
            },
            {
                "text": {
                    "zh": "出台一组温和调控工具，平缓房地产市场升温节奏",
                    "en": "Introduce mild regulatory tools to slow overheating in real estate markets"
                },
                "effect": {"inflation": -2, "gdp_growth": -1}
            },
            {
                "text": {
                    "zh": "保持房地产融资环境宽松，支持不动产投资拉动增长",
                    "en": "Maintain loose real estate financing to support growth via property investment"
                },
                "effect": {"inflation": 5, "gdp_growth": 4, "public_debt": 5}
            }
        ]
    },
    {
        "id": "unemployment_slow_up",
        "name": {
            "zh": "失业率逐步爬升",
            "en": "Gradual Rise in Unemployment Rate"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "就业市场慢慢转冷，失业率连续小幅走高。",
            "en": "Labor markets gradually weaken, pushing the unemployment rate steadily higher in small increments."
        },
        "choices": [
            {
                "text": {
                    "zh": "推出中长期职业培训与公共就业岗位扩容计划",
                    "en": "Roll out medium-long term vocational training and public job expansion programs"
                },
                "effect": {"budget_balance": -5, "unemployment": -6, "public_satisfaction": 4}
            },
            {
                "text": {
                    "zh": "启动短期就业补贴项目，缓解阶段性失业压力",
                    "en": "Launch temporary employment subsidy programs to ease cyclical joblessness"
                },
                "effect": {"unemployment": -2, "budget_balance": -1}
            },
            {
                "text": {
                    "zh": "缩减就业领域财政支出，依靠劳动力市场自发出清",
                    "en": "Cut fiscal spending on employment programs and rely on natural labor market adjustments"
                },
                "effect": {"unemployment": 6, "public_satisfaction": -5, "budget_balance": 4}
            }
        ]
    },
    {
        "id": "public_debt_growing",
        "name": {
            "zh": "政府债务持续扩张",
            "en": "Continuous Expansion of National Public Debt"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "政府财政赤字不断累积，公共债务规模持续扩大。",
            "en": "Persistent fiscal deficits accumulate, steadily expanding the scale of national public debt."
        },
        "choices": [
            {
                "text": {
                    "zh": "启动中期财政整顿方案，有序压缩赤字水平",
                    "en": "Launch medium-term fiscal consolidation plans to systematically reduce deficit levels"
                },
                "effect": {"public_debt": -5, "gdp_growth": -4, "public_satisfaction": -3}
            },
            {
                "text": {
                    "zh": "放缓新增债务投放节奏，平稳调整财政结构",
                    "en": "Slow the pace of new debt issuance to gradually restructure public finances"
                },
                "effect": {"public_debt": -2}
            },
            {
                "text": {
                    "zh": "维持扩张性财政支出，优先拉动当前总需求",
                    "en": "Sustain expansionary fiscal spending to prioritize boosting current aggregate demand"
                },
                "effect": {"public_debt": 6, "inflation": 4, "presidential_trust": -4}
            }
        ]
    },
    {
        "id": "strike_spread",
        "name": {
            "zh": "罢工范围慢慢扩大",
            "en": "Gradual Expansion of Labor Strike Activity"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "局部行业罢工开始扩散，劳资矛盾逐步蔓延。",
            "en": "Strikes originating in isolated industries spread outward, widening labor-management tensions."
        },
        "choices": [
            {
                "text": {
                    "zh": "推动劳资利益再平衡，提高劳工保障标准",
                    "en": "Rebalance labor-management interests by raising worker protection standards"
                },
                "effect": {"budget_balance": -4, "public_satisfaction": 5, "unemployment": -3}
            },
            {
                "text": {
                    "zh": "政府作为第三方介入调解，促成劳资双方谈判",
                    "en": "Government intervenes as neutral mediator to facilitate labor-management negotiations"
                },
                "effect": {"unemployment": -1, "public_satisfaction": 2}
            },
            {
                "text": {
                    "zh": "维护现有企业经营秩序，限制罢工进一步扩散",
                    "en": "Uphold existing business operations and restrict further strike expansion"
                },
                "effect": {"public_satisfaction": -6, "gdp_growth": -5, "unemployment": 4}
            }
        ]
    },
    {
        "id": "foreign_trade_dispute",
        "name": {
            "zh": "与他国逐步产生贸易摩擦",
            "en": "Mounting Trade Frictions with Foreign Nations"
        },
        "era": "any",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "本国与其他国家之间贸易摩擦一点点增多，贸易环境逐渐恶化。",
            "en": "Trade conflicts with foreign nations multiply incrementally, steadily worsening external trade conditions."
        },
        "choices": [
            {
                "text": {
                    "zh": "主动开展高层贸易磋商，寻求双边长期和解",
                    "en": "Initiate high-level trade talks to pursue long-term bilateral reconciliation"
                },
                "effect": {"forex_reserve": -4, "gdp_growth": 5, "presidential_trust": 4}
            },
            {
                "text": {
                    "zh": "保持谈判沟通渠道，同步完善本国贸易防御机制",
                    "en": "Keep negotiation channels open while strengthening domestic trade defense frameworks"
                },
                "effect": {"gdp_growth": 2, "forex_reserve": 1}
            },
            {
                "text": {
                    "zh": "对对方贸易措施采取对等的贸易回应行动",
                    "en": "Implement reciprocal trade countermeasures against foreign restrictive policies"
                },
                "effect": {"gdp_growth": -5, "forex_reserve": -6, "public_satisfaction": -3}
            }
        ]
    },
    # era = bretton_woods
    {
        "id": "gold_sell_off",
        "name": {
            "zh": "黄金抛售浪潮",
            "en": "Wave of Gold Redemption Sell-Offs"
        },
        "era": "bretton_woods",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "海外央行逐步将美元兑换成黄金，本国黄金储备承受越来越大的压力。",
            "en": "Foreign central banks gradually convert US dollars into gold, mounting sustained pressure on domestic gold reserves."
        },
        "choices": [
            {
                "text": {
                    "zh": "设置短期黄金兑换额度管理，保护本国储备安全",
                    "en": "Impose temporary gold conversion quotas to safeguard national reserve security"
                },
                "effect": {"forex_reserve": 3, "presidential_trust": -5, "inflation": 3}
            },
            {
                "text": {
                    "zh": "适度调节黄金兑付节奏，维持既有兑换承诺不变",
                    "en": "Moderate the pace of gold redemptions while honoring all existing convertibility pledges"
                },
                "effect": {"forex_reserve": -3, "presidential_trust": 1}
            },
            {
                "text": {
                    "zh": "完全满足各国黄金兑换申请，依靠储备自然消化压力",
                    "en": "Fulfill all foreign gold redemption requests and absorb pressure via reserve drawdowns"
                },
                "effect": {"forex_reserve": -6, "budget_balance": -4, "presidential_trust": -4}
            }
        ]
    },
    {
        "id": "allies_pressure_dollar",
        "name": {
            "zh": "盟友对美元黄金兑换提出压力",
            "en": "Allied Nations Demand Reforms to Dollar-Gold Convertibility"
        },
        "era": "bretton_woods",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "盟友公开对美元与黄金兑换机制表达不满，国际协调压力上升。",
            "en": "Allied governments publicly voice dissatisfaction with the dollar-gold exchange system, raising international coordination pressures."
        },
        "choices": [
            {
                "text": {
                    "zh": "启动国际货币体系改革讨论，回应盟友主要诉求",
                    "en": "Launch negotiations on international monetary system reform to address core allied demands"
                },
                "effect": {"forex_reserve": -4, "presidential_trust": 6}
            },
            {
                "text": {
                    "zh": "开展外交沟通安抚盟友，将深层改革议题延后讨论",
                    "en": "Diplomatically reassure allies and postpone negotiations on structural systemic reforms"
                },
                "effect": {"presidential_trust": 2, "forex_reserve": -2}
            },
            {
                "text": {
                    "zh": "坚持现有货币兑换规则，不作出结构性让步",
                    "en": "Uphold current monetary convertibility rules with no structural concessions"
                },
                "effect": {"forex_reserve": -5, "presidential_trust": -6}
            }
        ]
    },
    # era = fiat
    {
        "id": "currency_confidence_shake",
        "name": {
            "zh": "资本外流与货币信心动摇",
            "en": "Capital Outflows Erode Domestic Currency Confidence"
        },
        "era": "fiat",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "海外投资者缓慢减持本国资产，资本持续小幅流出，市场对本币的信心开始动摇。",
            "en": "Foreign investors gradually divest domestic assets, creating steady mild capital outflows and weakening market faith in the national currency."
        },
        "choices": [
            {
                "text": {
                    "zh": "动用外汇储备进行持续汇率干预，稳定本币价格",
                    "en": "Deploy foreign exchange reserves for sustained currency intervention to stabilize exchange rates"
                },
                "effect": {"forex_reserve": -5, "inflation": -3, "presidential_trust": 5}
            },
            {
                "text": {
                    "zh": "通过政策沟通引导预期，辅以小规模外汇市场操作",
                    "en": "Guide market expectations via policy communications paired with limited forex market operations"
                },
                "effect": {"forex_reserve": -2, "inflation": -1}
            },
            {
                "text": {
                    "zh": "减少对外汇市场的直接干预，让汇率更多由市场决定",
                    "en": "Reduce direct forex intervention and allow market forces to set exchange rate levels"
                },
                "effect": {"forex_reserve": -6, "inflation": 5, "presidential_trust": -5}
            }
        ]
    },
    {
        "id": "sovereign_bond_sell",
        "name": {
            "zh": "国际投资者逐步抛售本国国债",
            "en": "Foreign Investors Gradually Offload National Sovereign Bonds"
        },
        "era": "fiat",
        "tier": 2,
        "weight": 25,
        "auto_choice": 1,
        "desc": {
            "zh": "海外投资者慢慢抛售本国主权债券，融资成本开始走高。",
            "en": "Overseas investors steadily sell off domestic sovereign debt securities, pushing borrowing costs upward."
        },
        "choices": [
            {
                "text": {
                    "zh": "推进财政收缩计划，改善长期国债信用基本面",
                    "en": "Implement fiscal contraction plans to strengthen long-term sovereign credit fundamentals"
                },
                "effect": {"public_debt": -5, "gdp_growth": -4, "budget_balance": 5}
            },
            {
                "text": {
                    "zh": "央行适度参与国债市场，平缓债券收益率波动",
                    "en": "Central bank conducts moderate treasury purchases to smooth bond yield volatility"
                },
                "effect": {"public_debt": -1, "inflation": 2}
            },
            {
                "text": {
                    "zh": "继续按照原有计划发行国债，不调整融资节奏",
                    "en": "Continue scheduled treasury bond issuances with no changes to borrowing timelines"
                },
                "effect": {"public_debt": 6, "gdp_growth": -5, "budget_balance": -4}
            }
        ]
    },
    # ========== Tier 3 黑天鹅 weight = 5 ==========
    # era = any
    {
        "id": "sudden_global_recession",
        "name": {
            "zh": "全球经济骤然衰退",
            "en": "Abrupt Global Economic Recession"
        },
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "毫无预兆，全球主要经济体同时陷入快速衰退，外部需求骤然萎缩。不想写原因了。",
            "en": "Without warning, all major global economies plunge into rapid recession, triggering an abrupt collapse in external demand."
        },
        "choices": [
            {
                "text": {
                    "zh": "推出大规模内需刺激方案，对冲外部需求下滑",
                    "en": "Launch large-scale domestic demand stimulus packages to offset collapsing external demand"
                },
                "effect": {"gdp_growth": -3, "budget_balance": -6, "public_debt": 7}
            },
            {
                "text": {
                    "zh": "采取适度、有边界的托底政策，承受一部分外部冲击",
                    "en": "Adopt limited targeted support policies while absorbing partial external economic shocks"
                },
                "effect": {"gdp_growth": -12, "forex_reserve": -7, "unemployment": 7}
            },
            {
                "text": {
                    "zh": "保持原有财政与货币立场，依靠经济体自身完成调整",
                    "en": "Maintain baseline fiscal and monetary stances, letting the economy self-correct organically"
                },
                "effect": {"gdp_growth": -24, "forex_reserve": -21, "unemployment": 20}
            }
        ]
    },
    {
        "id": "world_oil_supply_shock",
        "name": {
            "zh": "国际原油供给突然中断",
            "en": "Sudden Global Crude Oil Supply Disruption"
        },
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "突发地缘冲突导致国际原油供应骤然中断，油价瞬间暴涨。坐一次飞机价格飙升至500万美金！",
            "en": "Unexpected geopolitical conflict severs global crude supplies, sending oil prices skyrocketing overnight."
        },
        "choices": [
            {
                "text": {
                    "zh": "集中释放战略石油储备，缓解国内能源供应紧张",
                    "en": "Massively release strategic petroleum reserves to ease domestic energy shortages"
                },
                "effect": {"forex_reserve": -5, "budget_balance": -6, "inflation": -4}
            },
            {
                "text": {
                    "zh": "分批次释放少量储备，其余由市场消化油价上涨影响",
                    "en": "Release small reserve tranches incrementally and let markets absorb residual price hikes"
                },
                "effect": {"inflation": 9, "gdp_growth": -8, "unemployment": 7}
            },
            {
                "text": {
                    "zh": "不动用战略储备，允许国内能源价格跟随国际市场上行",
                    "en": "Hold strategic reserves intact and allow domestic energy prices to track global surges"
                },
                "effect": {"inflation": 23, "gdp_growth": -21, "unemployment": 20}
            }
        ]
    },
    {
        "id": "president_sudden_death",
        "name": {
            "zh": "总统暴毙了孩子们",
            "en": "Sudden Presidential Death Shocks the Nation"
        },
        "era": "any",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "现任总统毫无征兆骤然离世，或许是暗杀？国家政治稳定性受到巨大冲击。",
            "en": "The sitting president passes away without warning, potentially by assassination, delivering a severe blow to national political stability."
        },
        "choices": [
            {
                "text": {
                    "zh": "延迟权力交接流程，等待内部各方达成新的共识",
                    "en": "Delay formal power transfer to negotiate new consensus among internal political factions"
                },
                "effect": {"presidential_trust": -10, "gdp_growth": -8, "public_satisfaction": -9}
            },
            {
                "text": {
                    "zh": "依照既有程序组建过渡团队，维持政策大体连续",
                    "en": "Form a transitional government per legal procedures to preserve broad policy continuity"
                },
                "effect": {"presidential_trust": -6, "public_satisfaction": -5, "gdp_growth": -4}
            },
            {
                "text": {
                    "zh": "各派系重新博弈，对现行经济政策进行较大幅度调整",
                    "en": "Allow political factions to renegotiate power and implement sweeping economic policy overhauls"
                },
                "effect": {"presidential_trust": -22, "inflation": 22, "gdp_growth": -20}
            }
        ]
    },
    # era = bretton_woods
    {
        "id": "cuba_missile_crisis",
        "name": {
            "zh": "古巴导弹危机——JFK回合！",
            "en": "Cuban Missile Crisis – JFK Term!"
        },
        "era": "bretton_woods",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "冷战军事对峙骤然爆发，局势一夜之间滑向危险边缘。",
            "en": "A sudden Cold War military standoff erupts, pushing global tensions to the brink overnight."
        },
        "choices": [
            {
                "text": {
                    "zh": "提升军事部署等级，施加强硬军事压力",
                    "en": "Escalate military deployments to apply hardline strategic pressure"
                },
                "effect": {"public_debt": 10, "forex_reserve": -6, "inflation": 7}
            },
            {
                "text": {
                    "zh": "作出有限军事姿态，同时保持外交谈判通道畅通",
                    "en": "Make limited military posturing while keeping diplomatic negotiation channels open"
                },
                "effect": {"public_debt": 6, "forex_reserve": -5, "inflation": 4}
            },
            {
                "text": {
                    "zh": "采取全面对抗姿态处理",
                    "en": "Adopt an all-out confrontational strategic posture"
                },
                "effect": {"public_debt": 24, "forex_reserve": -22, "presidential_trust": -20}
            }
        ]
    },
    {
        "id": "panic_gold_rush",
        "name": {
            "zh": "各国集中挤兑黄金",
            "en": "Panic Gold Redemption Run by Foreign Central Banks"
        },
        "era": "bretton_woods",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "一夜之间多国央行同时要求把美元兑换成黄金，大规模黄金挤兑突然爆发。",
            "en": "Overnight, dozens of foreign central banks simultaneously demand dollar-to-gold conversions, triggering a massive gold reserve run."
        },
        "choices": [
            {
                "text": {
                    "zh": "临时暂停黄金兑换业务，争取国际协商时间",
                    "en": "Temporarily suspend gold convertibility to secure time for international negotiations"
                },
                "effect": {"forex_reserve": -3, "presidential_trust": -7, "inflation": 6}
            },
            {
                "text": {
                    "zh": "继续履行黄金兑换义务，通过外交渠道呼吁各方克制",
                    "en": "Continue honoring gold redemption obligations while diplomatically urging foreign restraint"
                },
                "effect": {"forex_reserve": -8, "budget_balance": -6, "presidential_trust": -5}
            },
            {
                "text": {
                    "zh": "按照原有兑换条款无条件满足所有央行提取黄金要求",
                    "en": "Unconditionally fulfill all central bank gold withdrawal requests per original convertibility terms"
                },
                "effect": {"forex_reserve": -24, "budget_balance": -21, "presidential_trust": -20}
            }
        ]
    },
    # era = fiat
    {
        "id": "global_bank_panic",
        "name": {
            "zh": "国际大型银行突发危机",
            "en": "Sudden Collapse of a Major Global Bank"
        },
        "era": "fiat",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "一家重量级跨国大型银行毫无预警破产！",
            "en": "A systemically critical multinational bank collapses with zero advance warning!"
        },
        "choices": [
            {
                "text": {
                    "zh": "出台广泛金融兜底承诺，稳定整个金融市场信心",
                    "en": "Issue sweeping financial backstop guarantees to restore confidence across all markets"
                },
                "effect": {"public_debt": 7, "budget_balance": -5, "inflation": 6}
            },
            {
                "text": {
                    "zh": "选择性救助关键金融机构，其余机构交由市场处置",
                    "en": "Selectively rescue systemically vital financial firms and let others resolve via market forces"
                },
                "effect": {"gdp_growth": -8, "unemployment": 6, "public_debt": 5}
            },
            {
                "text": {
                    "zh": "不设立专项救助计划，允许金融机构自行承担损失",
                    "en": "Refuse targeted bailout programs and let financial institutions absorb their own losses"
                },
                "effect": {"gdp_growth": -23, "unemployment": 22, "public_debt": 20}
            }
        ]
    },
    {
        "id": "panic_capital_flight",
        "name": {
            "zh": "国际资本恐慌式集体出逃",
            "en": "Panic-Driven Mass Flight of International Capital"
        },
        "era": "fiat",
        "tier": 3,
        "weight": 5,
        "auto_choice": 1,
        "desc": {
            "zh": "市场情绪毫无征兆瞬间反转，国际资本在极短时间内大规模恐慌撤离本国。",
            "en": "Market sentiment flips violently without warning, triggering massive panicked international capital outflows in a short window."
        },
        "choices": [
            {
                "text": {
                    "zh": "紧急完善跨境资本流动管理规则，抑制资本快速外流",
                    "en": "Rapidly strengthen cross-border capital flow regulations to stem rapid outflows"
                },
                "effect": {"forex_reserve": -4, "gdp_growth": -6, "presidential_trust": -5}
            },
            {
                "text": {
                    "zh": "动用少量外汇储备进行干预，配合预期管理",
                    "en": "Deploy limited forex reserve interventions paired with market expectation management"
                },
                "effect": {"forex_reserve": -7, "inflation": 7, "budget_balance": -5}
            },
            {
                "text": {
                    "zh": "保持资本项目政策不变，让跨境资本自由流动",
                    "en": "Leave capital account policies unchanged and maintain fully free cross-border capital movement"
                },
                "effect": {"forex_reserve": -24, "inflation": 22, "presidential_trust": -21}
            }
        ]
    }
]