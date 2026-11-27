# W3 audit fixes for reel scripts. Ops use ORIGINAL beat indices.
# set: change fields of beat i.  ins: insert a new beat after original index a (-1 = before action, i.e. after len-2).
S, I = "set", "ins"
OPS = [
 ("c-attend", S, 0, {"text": "Your attention shapes what you experience.", "emph": ["attention"]}),
 ("c-attend", S, 4, {"text": "Control your attention, and you shape how your life feels."}),
 ("c-be-good-now", S, 4, {"text": "The Stoics judged a person by their choices. Choices acted on, not theories recited.", "emph": ["choices"]}),
 ("c-flywheel", I, 3, {"text": "Modern data are gentler. Missing one day doesn't derail a habit.", "shots": ["calendar"], "emph": ["gentler"]}),
 ("c-revenge", S, 4, {"text": "Refuse to copy them, and your peace stops depending on what they do.", "emph": ["peace"]}),
 ("c-thousand-li", S, 4, {"text": "Atomic Habits is a more than two thousand year old idea. With better marketing.", "emph": ["marketing"]}),
 ("c-writing-exact", S, 3, {"text": "That's why Bezos banned slides from Amazon's senior meetings, for six page memos.", "emph": ["memos"]}),
 ("e-true-fans", I, 5, {"text": "That's revenue before costs, and few ever reach a thousand. Treat it as a target, not a forecast.", "shots": ["charts"], "emph": ["target"]}),
 ("k-no-one-is-free-without-self-mastery", S, 2, {"by": "Epictetus, Fragments"}),
 ("m-voluntary-discomfort", I, -1, {"text": "Skip the cold if you have a heart condition. Skip fasting if you've had an eating disorder.", "shots": ["heartbeat"], "emph": ["heart"]}),
 ("n-exercise", S, 0, {"text": "Exercise helps the ageing brain. The boost is smaller than the hype.", "emph": ["smaller"]}),
 ("n-exercise", I, 2, {"text": "That was older adults over a year. In younger adults, the thinking boost is small or uncertain.", "shots": ["old_hands"], "emph": ["uncertain"]}),
 ("n-exercise", S, 4, {"text": "Take a brisk twenty minute walk today. Health first. Any brain boost is a bonus.", "emph": ["bonus"]}),
 ("n-hebb", S, 0, {"text": "Repetition strengthens the connections you use.", "emph": ["strengthens"]}),
 ("n-hebb", S, 4, {"text": "Focused repetition, then sleep, is how circuits stick.", "emph": ["sleep"]}),
 ("n-morning-light", I, -1, {"text": "The principle is solid. The exact minutes are rules of thumb.", "shots": ["sunrise"], "emph": ["solid"]}),
 ("n-pleasure-pain", I, 4, {"text": "The balance is a metaphor, and the thirty days come from her clinic, not trials.", "shots": ["weights_scale"], "emph": ["metaphor"]}),
 ("n-sigh", S, 0, {"text": "Two inhales, one long exhale. A quick, free way to calm down.", "emph": ["exhale"]}),
 ("n-sigh", S, 4, {"text": "In one small Stanford study, five minutes a day edged out meditation for mood. Promising, not settled.", "emph": ["Promising"]}),
 ("n-wandering", S, 3, {"text": "And people were less happy while wandering. Pleasant thoughts didn't make them happier.", "emph": ["less"]}),
 ("p-river", I, 1, {"text": "That famous line is Plato's paraphrase. Heraclitus wrote that different waters keep flowing in.", "shots": ["river_flow"], "emph": ["paraphrase"]}),
 ("x-action-before-motivation", I, -1, {"text": "If low mood lasts over two weeks, use this alongside professional care.", "shots": ["conversation"], "emph": ["care"]}),
 ("x-caffeine-properly-dosed", I, -1, {"text": "Start low. Stay under four hundred milligrams a day, and skip it with heart or anxiety problems.", "shots": ["coffee"], "emph": ["low"]}),
 ("x-coffee-at-4pm-costs-you-an-hour-of-sleep", S, 0, {"text": "A big caffeine dose six hours before bed still cut about an hour of sleep.", "emph": ["hour"]}),
 ("x-communities-can-manage-shared-resources", S, 0, {"text": "The standard view said shared resources always get overused.", "emph": ["overused"]}),
 ("x-communities-can-manage-shared-resources", S, 4, {"text": "She shared the Nobel Prize for showing it.", "emph": ["Nobel"]}),
 ("x-complexity-has-diminishing-returns", S, 0, {"text": "Joseph Tainter's bold claim: Rome didn't fall because it was weak.", "emph": ["bold"]}),
 ("x-creatine-3-to-5-grams-a-day-every-day", I, 3, {"text": "It does raise blood creatinine, so tell your doctor before kidney tests.", "shots": ["lab_science"], "emph": ["doctor"]}),
 ("x-delay-is-the-cure-for-anger", S, 0, {"text": "Seneca agreed with the old line: anger is a brief madness.", "emph": ["madness"]}),
 ("x-exercise-rivals-therapy-for-low-mood", I, -1, {"text": "With moderate or severe depression, use it alongside treatment, not instead.", "shots": ["conversation"], "emph": ["alongside"]}),
 ("x-fear-honour-and-interest", S, 3, {"by": "The Athenian envoys at Melos, in Thucydides"}),
 ("x-fine-tune-0-1-of-the-weights", S, 0, {"text": "You don't need to retrain a giant model. Just a tiny fraction of it.", "emph": ["tiny"]}),
 ("x-four-weeks-to-reset", I, -1, {"text": "Safety first. If it's heavy drinking, benzos, opioids or sedatives, don't quit cold turkey. Plan it with a doctor.", "shots": ["heartbeat"], "emph": ["Safety"]}),
 ("x-how-you-react-to-good-news-matters", I, -1, {"text": "The evidence is mostly correlational. Treat it as a habit worth trying.", "shots": ["charts"], "emph": ["habit"]}),
 ("x-how-you-react-to-good-news-matters-most", S, 1, {"text": "Active, enthusiastic replies go with more trust and intimacy.", "emph": ["enthusiastic"]}),
 ("x-how-you-react-to-good-news-matters-most", S, 4, {"text": "It's shown in couples and close friends. At work, it's plausible but less tested.", "emph": ["couples"]}),
 ("x-hubs-make-networks-robust-and-fragile-at", S, 3, {"text": "Your friends tend to have more friends than you. Popular people show up on many lists.", "emph": ["Popular"]}),
 ("x-legibility-kills-what-it-can-t-see", I, 1, {"text": "Add a state forcing the plan through, and a society too weak to resist.", "shots": ["military"], "emph": ["forcing"]}),
 ("x-let-the-model-think-in-tokens", S, 3, {"text": "With the zero-shot think step by step trick, it paved the way for reasoning models.", "emph": ["reasoning"]}),
 ("x-make-memory-a-choice", S, 0, {"text": "Fifteen minutes a day, compounding for years.", "emph": ["compounding"]}),
 ("x-make-the-first-offer", S, 2, {"text": "Precise numbers anchor harder. Four thousand eight fifty, not five thousand. But precise and extreme can backfire.", "emph": ["backfire"]}),
 ("x-make-the-first-offer", S, 4, {"text": "Before your next negotiation, prepare a well-researched, precise opening number.", "emph": ["precise"]}),
 ("x-melatonin-is-a-clock-not-a-sedative", I, -1, {"text": "Label doses are unreliable. Pick a tested brand, and ask a doctor if you take other medication.", "shots": ["lab_science"], "emph": ["unreliable"]}),
 ("x-move-before-you-think", S, 2, {"text": "During, right after or later, the boost was about the same.", "emph": ["same"]}),
 ("x-never-name-the-first-number", I, 3, {"text": "That fits when they know the pay band and you don't. Know the market? Open first.", "shots": ["chess"], "emph": ["market"]}),
 ("x-no-regression-can-replace-good-design", S, 0, {"text": "John Snow found cholera's cause by walking door to door.", "emph": ["door"]}),
 ("x-prefill-computes-decode-waits-on-memory", S, 2, {"text": "Prefill is compute-bound. Decoding waits on memory, unless you batch many requests.", "emph": ["batch"]}),
 ("x-save-15-split-three-ways", I, 2, {"text": "Outside the US? Think global stocks and home-currency bonds, in tax-efficient local funds.", "shots": ["map_old"], "emph": ["global"]}),
 ("x-shrinking-every-estimate-beats-trusting-", S, 2, {"text": "With four or more averages, pull each one toward the overall mean.", "emph": ["four"]}),
 ("x-six-levers-of-persuasion", I, 3, {"text": "Newer editions add a seventh, unity. And many effects are smaller than the legends.", "shots": ["old_books"], "emph": ["seventh"]}),
 ("x-symmetry-organises-physics", S, 2, {"text": "Each continuous symmetry implies something that's conserved.", "emph": ["continuous"]}),
 ("x-systems-with-no-author", S, 1, {"text": "He spends his last year obeying the process anyway.", "emph": ["year"]}),
 ("x-talk-to-yourself-by-name", I, -1, {"text": "The evidence is promising but modest. Picturing the scene from outside is better tested.", "shots": ["window_think"], "emph": ["modest"]}),
 ("x-the-bias-variance-trade-off", I, 2, {"text": "Expected error is bias squared, plus variance, plus noise you can't remove.", "shots": ["equations"], "emph": ["noise"]}),
 ("x-the-iliad-s-first-word-is-rage", S, 3, {"text": "Two enemies weep together, and it closes on a funeral. No triumph.", "emph": ["funeral"]}),
 ("x-the-optimal-gap", S, 1, {"text": "Follow-up research put it at ten to twenty percent of how long you need to remember.", "emph": ["twenty"]}),
 ("x-the-optimal-gap", I, 3, {"text": "For a whole year, the ideal gap shrinks to about five percent.", "shots": ["calendar"], "emph": ["five"]}),
 ("x-the-whole-can-reverse-what-every-part-sa", S, 1, {"text": "Yet department by department, the gap vanished or slightly favoured women.", "emph": ["vanished"]}),
 ("x-three-funds-whole-market", I, 1, {"text": "Outside the US, use a global stock fund and home-currency bonds in local, tax-efficient funds.", "shots": ["map_old"], "emph": ["global"]}),
 ("x-tune-the-learning-rate-first", S, 1, {"text": "The learning rate matters most. Re-tune it for every setting you compare.", "emph": ["Re-tune"]}),
 ("x-wake-at-the-same-time", S, 0, {"text": "A regular wake time matters as much as total hours.", "emph": ["regular"]}),
 ("x-what-others-do-beats-what-they-say", S, 1, {"text": "Most guests reuse their towels can work better.", "emph": ["reuse"]}),
 ("x-what-others-do-beats-what-they-say", I, 1, {"text": "But the towel study replicated weakly. Expect small nudges, not guaranteed wins.", "shots": ["broken_glass"], "emph": ["weakly"]}),
 ("x-where-to-push-a-system", S, 4, {"text": "Stronger still: the paradigm. Strongest: the power to step outside any paradigm.", "emph": ["outside"]}),
 ("x-your-gpu-is-mostly-waiting-not-computing", S, 0, {"text": "You paid for the compute. Much of the time, your GPU is waiting.", "emph": ["waiting"]}),
 ("x-your-gpu-is-mostly-waiting-not-computing", S, 1, {"text": "Unless you're careful, training time goes into moving memory around.", "emph": ["memory"]}),
 ("x-your-model-is-great-because-it-saw-the-t", S, 0, {"text": "Leakage was found in nearly three hundred published ML papers.", "emph": ["hundred"]}),
 ("x-your-next-job-comes-from-an-acquaintance", I, 3, {"text": "A huge LinkedIn experiment agreed, but moderately weak ties helped most. The weakest helped less.", "shots": ["phone_scroll"], "emph": ["moderately"]}),
 ("x-your-savings-rate-decides-retirement", S, 3, {"text": "The usual target is twenty five times your yearly spending. Outside the US, aim nearer thirty.", "emph": ["thirty"]}),
 ("y-flow", S, 0, {"text": "Flow lives where a high challenge meets high skill.", "emph": ["challenge"]}),
 ("y-flow", S, 4, {"text": "Challenge matched to skill, with clear goals and instant feedback.", "emph": ["matched"]}),
 ("y-flow", S, 5, {"text": "Make your next work block a real challenge for your skill, with one clear goal.", "emph": ["challenge"]}),
 ("y-good-life", I, -1, {"text": "It's observational, and the first cohorts were all men. A strong link, not proof.", "shots": ["old_hands"], "emph": ["observational"]}),
 ("y-helplessness", I, 4, {"text": "That circuit evidence is mostly from rats. In people, it's plausible but less tested.", "shots": ["lab_science"], "emph": ["rats"]}),
 ("y-reappraisal", I, 3, {"text": "The studies are small and the effects modest. But the trick is free.", "shots": ["charts"], "emph": ["free"]}),
 ("y-sdt", S, 4, {"text": "Expected, controlling rewards erode the drive for things you already enjoy.", "emph": ["controlling"]}),
 ("y-treadmill", S, 0, {"text": "The new car feeling fades.", "emph": ["fades"]}),
 ("y-treadmill", S, 1, {"text": "We adapt to most things. Raises. Gadgets. Big wins.", "emph": ["adapt"]}),
 ("y-treadmill", I, 2, {"text": "But not all. Disability, long unemployment and divorce can weigh for years.", "shots": ["storm_clouds"], "emph": ["years"]}),
]

def apply(scripts_dir):
    import json, os, collections
    by = collections.defaultdict(list)
    for cid, op, i, f in OPS: by[cid].append((op, i, f))
    done = []
    for cid, ops in by.items():
        p = os.path.join(scripts_dir, cid + ".json")
        if not os.path.exists(p): print("MISSING", cid); continue
        s = json.load(open(p)); beats = s["beats"]; n = len(beats)
        # keep stale emph words only if they still appear
        for op, i, f in ops:
            if op == S:
                b = beats[i]; b.update(f)
                if "text" in f and "emph" not in f:
                    b["emph"] = [e for e in b.get("emph", []) if e.lower() in f["text"].lower()]
        ins = sorted([(n - 2 if i == -1 else i, f) for op, i, f in ops if op == I], key=lambda x: -x[0])
        for a, f in ins: beats.insert(a + 1, dict(f))
        json.dump(s, open(p, "w"), indent=1); done.append(cid)
    return done

if __name__ == "__main__":
    import sys; d = apply(sys.argv[1] if len(sys.argv) > 1 else "scripts"); print(len(d), "scripts patched")
