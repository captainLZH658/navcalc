# Mini Program 1.1.1 → H5 Comparison Report
# ==========================================

## 1. ETA Calculator
### Mini Program Fields:
- Current date (picker mode=date) + current time (picker mode=time)
- Ship UTC (selector -12 to +14) + Dest UTC (selector)
- Distance (NM) + Speed (kts) - digit inputs
- Target ETA date + time (optional pickers)
- CALCULATE button
- Results: ETA date/time/weekday, transit days/hours/mins
- Lookup table (speed lookup centered on input speed)
- Speed required to meet target ETA
- Footer: Captain LZH

### H5 Current:
- Has all fields but Chinese labels
- Need English conversion

## 2. True Wind
### Mini Program:
- COG (°) + SOG (kn) inputs
- Relative wind direction (°) + AWS (kn) - highlighted inputs
- CALCULATE button
- Results: TWS, TWD, TWD relative + port/starboard label
- Compass reference grid

## 3. Density Draft
### Mini Program:
- Displacement (t) + TPC (t/cm) - in "Vessel Data" card
- Current ρ₁ (t/m³) + New ρ₂ (t/m³) - in "Water Density" card
- Current Draft: Fwd + Aft inputs + Mean draft
- CALCULATE button
- Results: Draft change (Δd) + New Fwd/Aft

## 4. Cargo Capacity
### Mini Program:
- Max Draft (m) + Max Displacement (t) + Water Density (t/m³)
- Light Ship (t) + Constant (t)
- Stores: HSFO, LSFO, MGO, FW, Lub Oil, Stores, Other (7 items)
- CALCULATE button
- Results: Corrected Disp, Total Consumables, Cargo Capacity

## 5. Fuel Consumption
### Mini Program:
- Voyage No., From, To
- Sea Legs: 5 legs × (From, To, Dist, Speed, HSFO, LSFO, MGO)
- Port Stays: 5 ports × (Name, Days, HSFO, LSFO, MGO)
- ROB: HSFO, LSFO, MGO + Safety Margin (%)
- CALCULATE button
- Results: per-leg breakdown + totals

## 6. Dew Point
### Mini Program:
- Cargo Hold: Dry bulb + Wet bulb + calculated DP
- Outside Air: Dry bulb + Wet bulb + calculated DP
- Atmospheric Pressure (hPa)
- CALCULATE button
- Results: Hold DP, Outside DP, Difference, Verdict

## 7. Night Orders
### Mini Program:
- Date label + count
- 10 random orders from 67-sentence bank (seeded by date)
- Refresh + Copy All buttons
- Note about daily seed

## 8. Squat
### Mini Program:
- Draft (m) + Depth (m)
- Speed (kn) + Cb (with reference + auto-calc toggle)
- Water type: Open/Confined selector
- CALCULATE button
- Results: Squat (open/confined), UKC before/after
- Cb auto-calc: L, B, d, Δ
