import re, json

# Read current H5
html = open(r'D:\Users\Admin\Desktop\航海计算APP\index_cur.html', encoding='utf-8').read()

# === STEP 1: Replace night orders Chinese sentences with English ones from mini program ===
english_sentences = """  {cat:"Safety",text:"Call me at any time if in any doubt."},
  {cat:"Safety",text:"Keep a sharp lookout by sight and hearing."},
  {cat:"Safety",text:"Strictly comply with COLREGS at all times."},
  {cat:"Safety",text:"Maintain safe speed for prevailing conditions."},
  {cat:"Safety",text:"If in doubt, reduce speed or stop engines."},
  {cat:"Safety",text:"When in doubt — CALL ME. Do not hesitate."},
  {cat:"Avoidance",text:"If CPA less than 1.0 NM, call me at once."},
  {cat:"Avoidance",text:"Do not overtake without my permission."},
  {cat:"Avoidance",text:"Keep well clear of all fishing vessels."},
  {cat:"Avoidance",text:"Do not assume give-way vessels will give way."},
  {cat:"Avoidance",text:"Make bold alterations to avoid close quarters."},
  {cat:"Avoidance",text:"Call me if any vessel approaches within 5 NM."},
  {cat:"Avoidance",text:"Do not cross ahead of another vessel."},
  {cat:"Avoidance",text:"Maintain safe passing distance at least 1 NM."},
  {cat:"Weather",text:"If wind exceeds 7 Bft, call me."},
  {cat:"Weather",text:"If visibility drops below 2 NM, call me at once."},
  {cat:"Weather",text:"In sudden fog, call me immediately."},
  {cat:"Weather",text:"Reduce speed if excessive slamming or rolling."},
  {cat:"Weather",text:"If swell height exceeds 4 m, call me."},
  {cat:"Weather",text:"In heavy weather, secure all loose gear."},
  {cat:"Weather",text:"Close all watertight doors in heavy weather."},
  {cat:"Weather",text:"If barometer drops rapidly, call me."},
  {cat:"Navigation",text:"Call me 30 min before pilot station arrival."},
  {cat:"Navigation",text:"Verify position before every course change."},
  {cat:"Navigation",text:"Call me before entering TSS or precautionary area."},
  {cat:"Navigation",text:"Test steering gear one hour before arrival."},
  {cat:"Navigation",text:"Keep echo sounder on in shallow water."},
  {cat:"Navigation",text:"Set radar to appropriate range for conditions."},
  {cat:"Navigation",text:"Do not enter restricted area without me on bridge."},
  {cat:"Navigation",text:"Call me when approaching waypoint."},
  {cat:"Navigation",text:"Call me if UKC less than 2.0 m."},
  {cat:"Navigation",text:"Hand steer when in pilotage waters."},
  {cat:"Engine",text:"If any machinery alarm sounds, call me."},
  {cat:"Engine",text:"If engine RPM fluctuates abnormally, call me."},
  {cat:"Engine",text:"Monitor main engine parameters every hour."},
  {cat:"Engine",text:"Call me if cooling water temperature rises suddenly."},
  {cat:"Engine",text:"If abnormal vibration detected, reduce RPM and call me."},
  {cat:"Engine",text:"Do not switch fuel without chief engineer approval."},
  {cat:"Engine",text:"If bunkering, monitor transfer continuously."},
  {cat:"Security",text:"Report all unidentified vessels approaching the ship."},
  {cat:"Security",text:"Keep accommodation doors secured at night."},
  {cat:"Security",text:"Keep all external lights at night as per regulations."},
  {cat:"Security",text:"Check steering gear room every watch."},
  {cat:"Security",text:"Report any unauthorised person on board."},
  {cat:"Security",text:"Lower gangway only after port clearance."},
  {cat:"Pollution",text:"No garbage disposal overboard at any time."},
  {cat:"Pollution",text:"Do not discharge any oily water."},
  {cat:"Pollution",text:"Save all garbage in designated bins."},
  {cat:"Pollution",text:"Only incinerate in port with permission."},
  {cat:"Cargo",text:"Monitor cargo temperature every hour."},
  {cat:"Cargo",text:"Check lashing every watch in heavy weather."},
  {cat:"Cargo",text:"If cargo shifts, call me immediately."},
  {cat:"Cargo",text:"Monitor ballast operations every watch."},
  {cat:"Cargo",text:"Ensure hatch covers are properly secured."},
  {cat:"Cargo",text:"Check reefer container alarms each watch."},
  {cat:"Crew",text:"No crew on deck without officer permission at night."},
  {cat:"Crew",text:"OOW must ensure helmsman is alert at all times."},
  {cat:"Crew",text:"All lookouts must be properly rested."},
  {cat:"Crew",text:"Do not allow unauthorised personnel on the bridge."},
  {cat:"Crew",text:"Call me if any crew member is unwell."},
  {cat:"Emergency",text:"In case of fire, sound alarm and muster crew."},
  {cat:"Emergency",text:"Lifeboat and liferaft equipment must be ready."},
  {cat:"Emergency",text:"EPIRB and SART in standby at all times."},
  {cat:"Emergency",text:"If man overboard, release lifebuoy immediately."},
  {cat:"Emergency",text:"Emergency steering drill to be conducted weekly."},
  {cat:"Emergency",text:"All emergency exits and fire doors clear."}"""

# Replace the ORDERS array in the script
old_orders_match = re.search(r'var ORDERS=\[.*?\];', html, re.DOTALL)
if old_orders_match:
    old_orders = old_orders_match.group()
    new_orders = 'var ORDERS=[\n' + english_sentences + '\n];'
    html = html.replace(old_orders, new_orders)
    pass

# === STEP 2: Chinese → English UI text replacements ===
replacements = {
    # Home page
    '⚓ 航海计算': '⚓ Navigation Calculator',
    
    # ETA page
    'ETA 计算器': 'ETA Calculator',
    'Navigational ETA Calculator': 'Estimated Time of Arrival',
    '当前日期时间': 'Current Date & Time',
    '输入参数': 'Input Parameters',
    '目标 ETA（可选）': 'Target ETA (Optional)',
    '目标到达日期 & 时间': 'Target Arrival Date & Time',
    '日期': 'Date',
    '时间': 'Time',
    '船舶时区': 'Ship UTC',
    '目的时区': 'Dest UTC',
    '剩余距离 (NM)': 'Distance Remaining (NM)',
    '平均航速 (kts)': 'Average Speed (kts)',
    '输入海里数': 'Enter distance in NM',
    '输入航速': 'Enter speed in kts',
    '计算 ETA': 'CALCULATE ETA',
    '计算结果': 'Results',
    '预计到达 ETA': 'Estimated Time of Arrival',
    '航行时间': 'Transit Time',
    '天': 'days',
    '时': 'hrs',
    '分': 'mins',
    '速查表（以平均航速为中心）': 'Speed Lookup Table (centered on avg speed)',
    '所需航速': 'Required Speed',
    '节(kn)': 'kn',
    '到达时间': 'Arrival',
    '到达日期': 'Date',
    '到达星期': 'Day',
    '所需航速以达到目标 ETA': 'Speed Required to Meet Target ETA',
    
    # Night Orders
    '夜航命令': 'Night Orders',
    "Captain's Night Orders Generator": "Captain's Night Orders",
    '换一批': '🔄 Refresh',
    '复制全部': '📋 Copy All',
    '同一天生成的命令组合相同': 'Same seed for same date, click Refresh for new set',
    '已复制': 'Copied!',
    '复制失败': 'Copy failed',
    '请先生成命令': 'Generate orders first',
    '条命令': 'orders',
    '生成夜航命令': 'GENERATE NIGHT ORDERS',
    
    # True Wind
    '真风计算': 'True Wind',
    'True Wind Direction & Speed Calculator': 'True Wind Calculator',
    '船舶参数': 'Ship Parameters',
    '船首向 COG (°)': 'COG (°)',
    '船速 SOG (kn)': 'SOG (kn)',
    '视风参数 (Apparent Wind)': 'Apparent Wind',
    '相对风向 (°)': 'Rel. Wind Dir. (°)',
    '视风速 AWS (kn)': 'AWS (kn)',
    '0=船首, 90=右舷, 180=船尾, 270=左舷': '0=bow, 90=starboard, 180=stern, 270=port',
    '计算真风': 'CALCULATE TRUE WIND',
    '计算结果 (True Wind)': 'Results',
    '真风风速 TWS': 'TWS',
    '真风方向 TWD (真北)': 'TWD (True)',
    '真风相对方向': 'TWD Relative',
    '右舷': 'Stbd',
    '左舷': 'Port',
    '方位参考': 'Compass Reference',
    
    # Density Draft
    '吃水密度修正': 'Density Draft Correction',
    'Vessel Data': 'Vessel Data',
    'Water Density': 'Water Density',
    'Current Draft (m)': 'Current Draft (m)',
    'Displacement (t)': 'Displacement (t)',
    'Current ρ₁ (t/m³)': 'Current ρ₁ (t/m³)',
    'New ρ₂ (t/m³)': 'New ρ₂ (t/m³)',
    'Fwd': 'Fwd',
    'Aft': 'Aft',
    'Mean Draft (m)': 'Mean Draft (m)',
    'Or input directly': 'Or input mean directly',
    
    # Cargo Capacity
    '最大载货量': 'Cargo Capacity',
    'Max Allowable Values': 'Max Allowable Values',
    'Ship Constants': 'Ship Constants',
    'Stores & Consumables (t)': 'Stores & Consumables (t)',
    'Max Draft (m)': 'Max Draft (m)',
    'Max Displacement (t)': 'Max Displacement (t)',
    'Light Ship (t)': 'Light Ship (t)',
    'Constant (t)': 'Constant (t)',
    'Lub Oil': 'Lub Oil',
    'Stores': 'Stores',
    'Other': 'Other',
    'Water Density (t/m³)': 'Water Density (t/m³)',
    
    # Fuel Consumption
    '航次燃油计算': 'Voyage Fuel Consumption',
    'Voyage Info': 'Voyage Info',
    'Voyage No.': 'Voyage No.',
    'From': 'From',
    'To': 'To',
    'Sea Legs': 'Sea Legs',
    'Port Stays': 'Port Stays',
    'Safety Margin (%)': 'Safety Margin (%)',
    'ROB': 'ROB',
    
    # Dew Point
    '露点通风判断': 'Dew Point Ventilation',
    'Input Dry & Wet Bulb Temperatures': 'Dry & Wet Bulb Temperatures',
    'CARGO HOLD': 'CARGO HOLD',
    'OUTSIDE AIR': 'OUTSIDE AIR',
    'Dry Bulb (°C)': 'Dry Bulb (°C)',
    'Wet Bulb (°C)': 'Wet Bulb (°C)',
    'Dew Point': 'Dew Point',
    'Atm. Press (hPa)': 'Atm. Pressure (hPa)',
    'Result': 'Result',
    'Hold Dew Point': 'Hold Dew Point',
    'Outside Dew Point': 'Outside Dew Point',
    'Difference (Hold − Out)': 'Difference (Hold − Out)',
    
    # Squat
    '下沉量计算': 'Squat / UKC Calculator',
    '船舶下沉量 / UKC 计算': 'Squat & UKC Calculator',
    '输入参数': 'Input Parameters',
    '吃水 Draft (m)': 'Draft (m)',
    '水深 Depth (m)': 'Depth (m)',
    '船速 Speed (kn)': 'Speed (kn)',
    '方形系数 Cb': 'Block Coeff. Cb',
    '开阔水道': 'Open Water',
    '受限水道': 'Confined Water',
    '计算下沉量': 'CALCULATE SQUAT',
    '计算结果': 'Results',
    '开阔水道下沉量': 'Squat (Open)',
    '受限水道下沉量': 'Squat (Confined)',
    '当前 UKC': 'Current UKC',
    '下沉后 UKC': 'UKC After Squat',
    
    # Common
    'CALCULATE': 'CALCULATE',
    '计算结果': 'Results',
    '返回': 'Back',
    'Captain LZH': 'Captain LZH',
    
    # Meter/units
    '米': 'm',
    '节': 'kn',
    
    # Cb reference
    'Cb 典型参考值': 'Typical Cb Values',
    'Oil Tanker: 0.80-0.85': 'Oil Tanker: 0.80-0.85',
    'Bulk Carrier: 0.75-0.83': 'Bulk Carrier: 0.75-0.83',
    'Container: 0.60-0.70': 'Container: 0.60-0.70',
    'General Cargo: 0.65-0.75': 'General Cargo: 0.65-0.75',
    'Passenger: 0.55-0.65': 'Passenger: 0.55-0.65',
    'LNG Carrier: 0.70-0.78': 'LNG Carrier: 0.70-0.78',
    
    # Dew point verdict
    '可以通风': 'VENTILATE',
    '禁止通风': 'DO NOT VENTILATE',
    '谨慎通风': 'VENTILATE WITH CAUTION',
    '舱内露点高于舱外': 'Hold DP > Outside: VENTILATE',
    '舱内露点低于舱外': 'Hold DP < Outside: DO NOT VENTILATE',
    '舱内露点略低于舱外': 'Hold DP slightly < Outside: VENTILATE WITH CAUTION',
    '舱内露点低于舱外': 'Hold DP < Outside Air',
    '避免结露': 'Avoid condensation',
    
    # Status text
    '请填写完整': 'Please fill all fields',
    '请手动复制': 'Copy manually',
    '吃水超过水深': 'Draft exceeds depth!',
    '水上距离': 'Water depth above keel',
    '压载水排放须符合公约要求并记录': '',
    '垃圾按分类要求处理': '',
    # These are from the night orders that we already replaced
}

# Apply replacements (exact substring matches)
for cn, en in replacements.items():
    if cn in html:
        html = html.replace(cn, en)
    else:
        pass

# === STEP 3: Fix page title ===
html = html.replace('<title>航海计算助手</title>', '<title>Navigation Calculator</title>')

# === STEP 4: Fix home page subtitle ===
html = html.replace('Navigation Calculator', 'Navigation Calculator')

# === STEP 5: Fix the menu item descriptions ===
html = html.replace('航速/距离/时间/ETA', 'Speed/Distance/Time/ETA')
html = html.replace('Night Orders 一键生成', 'Night Orders Generator')
html = html.replace('真风风向/风速计算', 'True Wind Dir. & Speed')
html = html.replace('水密度变化→首尾吃水', 'Density → Draft Correction')
html = html.replace('排水量/轻船/常数/消耗品', 'Disp./Light Ship/Const./Cons.')
html = html.replace('海上段/港内段/ROB', 'Sea Legs/Port/ROB')
html = html.replace('干湿球温度→通风决策', 'Wet/Dry Bulb → Ventilation')
html = html.replace('Squat / UKC 计算', 'Squat / UKC Calculator')

# === STEP 6: Save ===
open(r'D:\Users\Admin\Desktop\航海计算APP\index_english.html', 'w', encoding='utf-8').write(html)
print('\nSaved index_english.html')
