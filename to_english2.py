"""Comprehensive Chinese→English replacement for the H5 page."""
import re, sys

h = open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', encoding='utf-8').read()

# Build comprehensive replacement dict from ALL remaining Chinese strings
# Read the context file to find each string's location, then determine the correct English
replacements = {
    # ===== ETA Page =====
    '起始': 'Depart',
    '航程参数': 'Passage Parameters',
    '航程距离': 'Distance',
    '海里': 'NM',
    '航速': 'Speed',
    '航速 (kn)': 'Speed (kn)',
    '航速 (kn)速查': 'Speed (kn) Lookup',
    '航行Time': 'Transit Time',
    '抵达Time': 'Arrival Time',
    '抵达Time (目的地LT)': 'Arrival Time (Dest LT)',
    '抵达Time (LT)': 'Arrival Time (LT)',
    '抵达': 'Arrival',
    '目的地': 'Destination',
    '航速速查表': 'Speed Lookup Table',
    '重置': 'Reset',
    '自动计算': 'Auto Calc',
    '计算结果ETA': 'Results',
    
    # ===== True Wind Page =====
    '船舶运动': 'Ship Motion',
    'COG·SOG': 'COG · SOG',
    '视风': 'Apparent Wind',
    '视风向': 'Rel. Wind Dir.',
    '视风速': 'AWS',
    '真风结果': 'True Wind Results',
    '真风向': 'TWD',
    '真风速': 'TWS',
    '相对方向': 'Relative Dir.',
    '相对船首方向': 'Rel. to bow',
    '左舷': 'Port',
    '右舷': 'Stbd',
    '船首风': 'Head Wind',
    '船尾风': 'Stern Wind',
    '左正横风': 'Port Beam Wind',
    '右正横风': 'Stbd Beam Wind',
    '左舷受风': 'Port Side',
    '右舷受风': 'Stbd Side',
    '左舷尾风': 'Port Quarter',
    '右舷尾风': 'Stbd Quarter',
    '顺风': 'Following Wind',
    '受风': 'Wind Side',
    '方位参考': 'Compass Reference',
    
    # ===== Density Draft Page =====
    '密度修正': 'Density Correction',
    '吃水变化': 'Draft Change',
    '当前水密度': 'Current ρ',
    '目标水密度': 'Target ρ',
    '当前平均吃水': 'Current Mean Draft',
    '新首吃水': 'New Fwd Draft',
    '新尾吃水': 'New Aft Draft',
    '新平均吃水': 'New Mean Draft',
    '计算吃水变化': 'Calculate Draft Change',
    '修正结果': 'Correction Results',
    '吃水变化Δd': 'Draft Change Δd',
    '当前首吃水': 'Current Fwd',
    '当前尾吃水': 'Current Aft',
    '水密度变化': 'Density Change',
    '用于首尾修正': 'for draft correction',
    '自动计算或手动': 'Auto or manual',
    '自动计算': 'Auto',
    '手动': 'Manual',
    '输入目标密度': 'Enter target density',
    '密度修正后载货量': 'Corrected Cargo Capacity',
    '装货港密度': 'Load Port Density',
    '港口水密度': 'Port Water Density',
    '目标密度': 'Target Density',
    '当前密度': 'Current Density',
    '吃水': 'Draft',
    '当前吃水': 'Current Draft',
    
    # ===== Cargo Capacity Page =====
    '夏季': 'Summer',
    '夏季排水量': 'Summer Displacement',
    '排水量': 'Displacement',
    '载货量结果': 'Cargo Capacity Results',
    '轻船重量': 'Light Ship',
    '吨': 't',
    '常数': 'Constant',
    '消耗品': 'Consumables',
    '安全余量': 'Safety Margin',
    
    # ===== Fuel Page =====
    '航次信息': 'Voyage Info',
    '航次编号': 'Voyage No.',
    '海上': 'Sea Legs',
    '海上航行': 'Sea Passage',
    '港内': 'Port Stays',
    '港内作业': 'Port Operations',
    '油耗率': 'Consumption Rate',
    '燃油计划': 'Bunker Plan',
    '总燃油需求': 'Total Fuel Required',
    '港口水密度': 'Port Density',
    
    # ===== Dew Point Page =====
    '干球': 'Dry Bulb',
    '湿球': 'Wet Bulb',
    '干球温度': 'Dry Bulb Temp',
    '湿球温度': 'Wet Bulb Temp',
    '计算露点': 'Calculate Dew Point',
    '判断通风': 'Ventilation Check',
    '露点结果': 'Dew Point Results',
    '舱内': 'Hold',
    '舱外': 'Outside',
    '舱内露点': 'Hold Dew Point',
    '舱外露点': 'Outside Dew Point',
    '通风判断': 'Ventilation Verdict',
    '动态': 'Dynamic',
    '评估': 'Assessment',
    '可以通风': 'VENTILATE',
    '禁止通风': 'DO NOT VENTILATE',
    '谨慎通风': 'CAUTION',
    
    # ===== Squat Page =====
    '船舶下沉量': 'Squat',
    '船体参数': 'Hull Parameters',
    '船长': 'Length',
    '船宽': 'Beam',
    '船速': 'Speed',
    '首尾柱间长': 'LBP',
    '下沉量结果': 'Squat Results',
    '水深': 'Depth',
    '水道类型': 'Water Type',
    '当前': 'Current',
    '当前UKC': 'Current UKC',
    '下沉后UKC': 'UKC After Squat',
    '计算下沉量': 'Calculate Squat',
    '受限水道': 'Confined Water',
    '开阔水道': 'Open Water',
    '开阔': 'Open',
    '受限': 'Confined',
    '宽度': 'Width',
    '船底至水底': 'Clearance',
    'UKC': 'UKC',
    
    # ===== Night Orders - categories =====
    '安全': 'Safety',
    '瞭望': 'Lookout',
    '值班': 'Watchkeeping',
    '船位': 'Position',
    '航路': 'Route',
    '航行': 'Navigation',
    '机舱': 'Engine Room',
    '主机': 'Main Engine',
    '驾驶台': 'Bridge',
    '通信': 'Communication',
    '油污': 'Oil Pollution',
    '压载': 'Ballast',
    '冰区': 'Ice Navigation',
    '医疗': 'Medical',
    '引水': 'Pilot',
    '日出': 'Sunrise',
    '日落': 'Sunset',
    '分': 'min',
    '时': 'h',
    '日': 'd',
    '以上': '',
    '不得': 'Do not',
    '保持': 'Maintain',
    '必须': 'Must',
    '及时': 'Promptly',
    '注意': 'Note',
    '核对': 'Verify',
    '准确': 'Accurate',
    '始终': 'Always',
    '严格': 'Strictly',
    '按照': 'According to',
    
    # ===== General =====
    '计算器': 'Calculator',
    '计算': 'Calculate',
    '距离': 'Distance',
    '速度': 'Speed',
    '时间': 'Time',
    '默认': 'Default',
    '选填': 'Optional',
    '当前状态': 'Status',
    '上一条': 'Previous',
    '下一条': 'Next',
    '条命令': 'orders',
    '厘米': 'cm',
    '米': 'm',
    '节': 'kn',
    '厘': 'cm',
    '小时': 'h',
    '吨位': 'Tonnage',
    '船长': 'Master',
    
    # ===== Buttons =====
    '一键生成': 'Generate',
    '重置全部': 'Reset All',
    '计算并填入 Cb': '✓ Apply Cb',
    
    # ===== Lookup table =====
    '计算结果': 'Results',
    
    # ===== Cb panel =====
    '方形系数 Cb': 'Block Coeff. Cb',
    '排水量': 'Displacement',
    'Cb = 排水体积 / (L × B × d)': 'Cb = Δ / (L × B × d)',
    '计算 Cb': 'Calculate Cb',
    '自动计算Cb': 'Auto Cb',
}

# Apply replacements (from longest to shortest to avoid partial matches)
for cn in sorted(replacements.keys(), key=len, reverse=True):
    en = replacements[cn]
    # Make sure CN is enclosed in non-alphanumeric context to avoid breaking code
    # Just do direct replace for now
    count = h.count(cn)
    if count > 0:
        h = h.replace(cn, en)

# Count remaining Chinese
remaining = re.findall(r'[\u4e00-\u9fff]{2,}', h)
print(f'Applied {len(replacements)} replacements')
print(f'Remaining Chinese strings: {len(remaining)}')
if remaining:
    for s in sorted(set(remaining)):
        print(f'  LEFT: "{s}"')

open(r'D:\Users\Admin\Desktop\航海计算APP\index_english2.html', 'w', encoding='utf-8').write(h)
print('Saved index_english2.html')
