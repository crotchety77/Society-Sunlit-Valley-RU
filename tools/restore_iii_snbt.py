import os
import re

src = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley (1)\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"
dst = r"D:\ModrinthApp\profiles\Society_ Sunlit Valley\config\ftbquests\quests\chapters\iii__advanced_farming.snbt"

with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

# 4 new quests from priority 1
new_quests = """\t\t{
\t\t\tdependencies: ["44A512703C4A9990"]
\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.questA455A4E0D7D074E.description2}"
\t\t\t]
\t\t\tid: "0A455A4E0D7D074E"
\t\t\trewards: [{
\t\t\t\tid: "7E326A0759D9BB95"
\t\t\t\titem: "society:yard_work_yearly"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\ttasks: [{
\t\t\t\tid: "61C5BAFB3E290916"
\t\t\t\titem: "moreminecarts:chiseled_organic_glass"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\tx: 10.5d
\t\t\ty: -0.5d
\t\t}
\t\t{
\t\t\tdependencies: ["263CCA4D2EAF2629"]
\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest17C8B0197B8636E7.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest17C8B0197B8636E7.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest17C8B0197B8636E7.description3}"
\t\t\t]
\t\t\tid: "17C8B0197B8636E7"
\t\t\trewards: [{
\t\t\t\tid: "163D852C0FE5BA60"
\t\t\t\titem: "society:yard_work_yearly"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\tsubtitle: "{ftbquests.chapter.iii__advanced_farming.quest17C8B0197B8636E7.subtitle}"
\t\t\ttasks: [{
\t\t\t\tid: "6CD0ECDBBA6F65C0"
\t\t\t\titem: "society:caterpillar_box"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\tx: 5.0d
\t\t\ty: -4.5d
\t\t}
\t\t{
\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description2}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description3}"
\t\t\t\t"{@pagebreak}"
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description4}"
\t\t\t\t"{@pagebreak}"
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.description5}"
\t\t\t]
\t\t\tid: "263CCA4D2EAF2629"
\t\t\trewards: [{
\t\t\t\tid: "694D864C0AD86F86"
\t\t\t\titem: "longwings:apple_butterfly_brew_block"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\ttasks: [{
\t\t\t\tid: "0FC6161D26208EE7"
\t\t\t\titem: "society:caterpillar_eggs"
\t\t\t\ttype: "item"
\t\t\t}]
\t\t\ttitle: "{ftbquests.chapter.iii__advanced_farming.quest263CCA4D2EAF2629.title}"
\t\t\tx: 5.0d
\t\t\ty: -6.0d
\t\t}
\t\t{
\t\t\tdependencies: ["66E1AC55824DF1D9"]
\t\t\tdescription: [
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.description1}"
\t\t\t\t""
\t\t\t\t"{ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.description2}"
\t\t\t]
\t\t\ticon: "society:ribbit_hut_block"
\t\t\tid: "3DE36C9FBCB58800"
\t\t\tmin_required_tasks: 1
\t\t\trewards: [{
\t\t\t\texclude_from_claim_all: true
\t\t\t\tid: "5D016D7DF3355B6A"
\t\t\t\ttable_id: 369102599118070839L
\t\t\t\ttype: "choice"
\t\t\t}]
\t\t\tsubtitle: "{ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.subtitle}"
\t\t\ttasks: [
\t\t\t\t{
\t\t\t\t\tid: "2DA4C5918EDD2952"
\t\t\t\t\titem: {
\t\t\t\t\t\tCount: 1
\t\t\t\t\t\tid: "society:invitation"
\t\t\t\t\t\ttag: {
\t\t\t\t\t\t\ttype: {
\t\t\t\t\t\t\t\tid: "society:witch"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tmatch_nbt: true
\t\t\t\t\ttype: "item"
\t\t\t\t}
\t\t\t\t{
\t\t\t\t\ticon: {
\t\t\t\t\t\tCount: 1
\t\t\t\t\t\tid: "society:villager"
\t\t\t\t\t\ttag: {
\t\t\t\t\t\t\ttype: {
\t\t\t\t\t\t\t\tid: "society:witch"
\t\t\t\t\t\t\t}
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t\tid: "47A5E6018A6FB99F"
\t\t\t\t\tstage: "invited_witch"
\t\t\t\t\ttitle: "{ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.task.5162785442142075295.title}"
\t\t\t\t\ttype: "gamestage"
\t\t\t\t}
\t\t\t]
\t\t\ttitle: "{ftbquests.chapter.iii__advanced_farming.quest3DE36C9FBCB58800.title}"
\t\t\tx: -1.5d
\t\t\ty: 2.0d
\t\t}
"""

# Insert new quests before the closing `\t]` of `quests: [`
# Find the line `\t]` that closes quests list
idx = text.rfind('\n\t]')
if idx != -1:
    reconstructed = text[:idx] + "\n" + new_quests + text[idx:]
    with open(dst, 'w', encoding='utf-8') as f:
        f.write(reconstructed)
    print(f"Successfully restored {dst}!")
    print(f"Original size: {len(text)} bytes, New size: {len(reconstructed)} bytes")
else:
    print("Error: closing bracket not found!")
