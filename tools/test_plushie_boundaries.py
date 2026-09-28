import sys
sys.stdout.reconfigure(encoding='utf-8')

# Test logic simulating globalAnimalHandlers.js exactly

def test_plushie_modifiers(trait_type, quality, roll, plushie_count_in_radius, furniture_count_in_radius, logs_found):
    quality_mult = quality + 1
    new_drops = []
    double_drops = False
    reset_day = False
    probability_increase = 0
    process_items = False
    
    if trait_type == 0: # Aquatic
        if roll < 0.05 * quality_mult:
            new_drops.append("jelly")
    elif trait_type == 1: # Woodsy
        if len(logs_found) > 0:
            new_drops.append(f"{quality_mult * 8}x logs")
    elif trait_type == 2: # Eldritch
        new_drops.append(f"{quality_mult}x raw_silver")
    elif trait_type == 3: # Wrathful
        new_drops.append(f"{quality_mult * 3}x raw_lead")
    elif trait_type == 4: # Sommelier
        if roll < 0.25 * quality_mult:
            process_items = True
    elif trait_type == 5: # Sunlit
        if roll < (0.05 * quality_mult):
            new_drops.append("sunlit_crystal")
    elif trait_type == 6: # Hungry
        if roll < 0.1 * quality_mult:
            reset_day = True
    elif trait_type == 7: # Anxious
        probability_increase = 0.25 * quality_mult
    elif trait_type == 8: # Shy
        # radius = 3 - (quality_mult - 1) = 3 - quality
        # if plushie_count_in_radius == 1 -> doubleDrops = true
        if plushie_count_in_radius == 1:
            double_drops = True
    elif trait_type == 9: # Cheerful
        if plushie_count_in_radius > (28 - 4 * quality_mult):
            double_drops = True
    elif trait_type == 10: # Chill
        new_drops.append(f"{quality_mult}x pristine_diamond")
    elif trait_type == 11: # Machiavellian
        new_drops.append(f"{quality_mult}x netherite_scrap")
    elif trait_type == 12: # Cutesy
        new_drops.append(f"{quality_mult}x furniture_box")
    elif trait_type == 13: # Fashionista
        if furniture_count_in_radius >= (28 - 4 * quality_mult):
            double_drops = True
    elif trait_type == 14: # Neutral
        if roll < 0.1 * quality_mult:
            double_drops = True

    return {
        "newDrops": new_drops,
        "doubleDrops": double_drops,
        "resetDay": reset_day,
        "probabilityIncrease": probability_increase,
        "processItems": process_items
    }

print("=================================================================")
print("             EXHAUSTIVE BOUNDARY SIMULATION TESTS                ")
print("=================================================================")

print("\n--- 1. CHEERFUL (type 9, operator: >) ---")
for q in range(4):
    q_mult = q + 1
    thresh = 28 - 4 * q_mult
    res_below = test_plushie_modifiers(9, q, 0, thresh - 1, 0, [])["doubleDrops"]
    res_exact = test_plushie_modifiers(9, q, 0, thresh, 0, [])["doubleDrops"]
    res_above = test_plushie_modifiers(9, q, 0, thresh + 1, 0, [])["doubleDrops"]
    print(f"Quality ★{q+1} (Threshold {thresh}): count={thresh-1} -> {res_below} | count={thresh} -> {res_exact} | count={thresh+1} -> {res_above}")
    assert res_below == False, f"Expected False for {thresh-1}"
    assert res_exact == False, f"Expected False for {thresh}"
    assert res_above == True, f"Expected True for {thresh+1}"

print("\n--- 2. FASHIONISTA (type 13, operator: >=) ---")
for q in range(4):
    q_mult = q + 1
    thresh = 28 - 4 * q_mult
    res_below = test_plushie_modifiers(13, q, 0, 0, thresh - 1, [])["doubleDrops"]
    res_exact = test_plushie_modifiers(13, q, 0, 0, thresh, [])["doubleDrops"]
    res_above = test_plushie_modifiers(13, q, 0, 0, thresh + 1, [])["doubleDrops"]
    print(f"Quality ★{q+1} (Threshold {thresh}): count={thresh-1} -> {res_below} | count={thresh} -> {res_exact} | count={thresh+1} -> {res_above}")
    assert res_below == False, f"Expected False for {thresh-1}"
    assert res_exact == True, f"Expected True for {thresh}"
    assert res_above == True, f"Expected True for {thresh+1}"

print("\n--- 3. SHY (type 8, operator: == 1) ---")
for q in range(4):
    res_0 = test_plushie_modifiers(8, q, 0, 0, 0, [])["doubleDrops"] # should not happen physically since plushie itself is 1
    res_1 = test_plushie_modifiers(8, q, 0, 1, 0, [])["doubleDrops"] # only itself
    res_2 = test_plushie_modifiers(8, q, 0, 2, 0, [])["doubleDrops"] # itself + 1 neighbor
    print(f"Quality ★{q+1} (Radius {3-q}): count=0 -> {res_0} | count=1 (no neighbors) -> {res_1} | count=2 (has neighbor) -> {res_2}")
    assert res_1 == True
    assert res_2 == False

print("\nAll boundary assertion tests PASSED perfectly!")
