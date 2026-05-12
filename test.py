# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# completion = client.chat.completions.create(
#   model="gpt-4o",
#   messages=[
#     {"role": "developer", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
  
# )

# print(completion.choices[0].message)


import os
import re
import csv
import random
import math
from collections import defaultdict, Counter
from statistics import mean, pstdev

# ===== Safety: Read API key from environment =====
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-4o"
TEMPERATURE = 0.0
SEED = 42
random.seed(SEED)

# ===== Dataset =====
# You can expand these easily. For each item, provide:
# - id: unique id
# - category: "arithmetic" | "language" | "algebra"
# - question: string
# - answer: target final answer as a string (normalized format used by compare function)
#
# For word problems, keep answers numeric or short text where possible and define a normalizer below.
ITEMS = [
    # --- Simple arithmetic (10) ---
    {"id":"A1","category":"arithmetic","question":"What is 37 + 28?", "answer":"65"},
    {"id":"A2","category":"arithmetic","question":"Compute 125 - 87.","answer":"38"},
    {"id":"A3","category":"arithmetic","question":"What is 14 × 9?","answer":"126"},
    {"id":"A4","category":"arithmetic","question":"What is 144 ÷ 12?","answer":"12"},
    {"id":"A5","category":"arithmetic","question":"What is 2^5?","answer":"32"},
    {"id":"A6","category":"arithmetic","question":"Compute 18 + 27 - 11.","answer":"34"},
    {"id":"A7","category":"arithmetic","question":"What is 48 ÷ 6?","answer":"8"},
    {"id":"A8","category":"arithmetic","question":"Compute (13 - 5) × 4.","answer":"32"},
    {"id":"A9","category":"arithmetic","question":"What is 9 × 7?","answer":"63"},
    {"id":"A10","category":"arithmetic","question":"Compute 100 - (17 + 23).","answer":"60"},

    # --- Language-based math (10) ---
    {"id":"L1","category":"language","question":"A jar has 15 red marbles and 9 blue marbles. How many marbles are in the jar?", "answer":"24"},
    {"id":"L2","category":"language","question":"Sara has twice as many stickers as Ben. Ben has 13 stickers. How many does Sara have?","answer":"26"},
    {"id":"L3","category":"language","question":"A car travels 180 km in 3 hours. What is its average speed in km/h?","answer":"60"},
    {"id":"L4","category":"language","question":"A rectangle’s length is 10 and width is 6. What is its area?","answer":"60"},
    {"id":"L5","category":"language","question":"I buy 3 notebooks at $4 each and pay with $20. How much change do I get?","answer":"8"},
    {"id":"L6","category":"language","question":"A tank holds 120 liters. It’s 35% full. How many liters are in the tank?","answer":"42"},
    {"id":"L7","category":"language","question":"A train leaves at 2:15 pm and arrives at 5:05 pm. How long is the trip in minutes?","answer":"170"},
    {"id":"L8","category":"language","question":"A recipe needs 2.5 cups of flour. I have 1.75 cups. How many more cups do I need?","answer":"0.75"},
    {"id":"L9","category":"language","question":"A class has 24 students. 3/8 are absent. How many are present?","answer":"15"},
    {"id":"L10","category":"language","question":"The price after a 20% discount is $40. What was the original price?","answer":"50"},

    # --- Upper-level algebra (10) ---
    {"id":"U1","category":"algebra","question":"Solve for x: 2x + 5 = 19.","answer":"7"},
    {"id":"U2","category":"algebra","question":"Solve for x: 3x - 7 = 11.","answer":"6"},
    {"id":"U3","category":"algebra","question":"Solve the system: x + y = 9 and x - y = 3. What is x?","answer":"6"},
    {"id":"U4","category":"algebra","question":"Solve the system: 2x + 3y = 13 and x - y = 1. What is y?","answer":"3"},
    {"id":"U5","category":"algebra","question":"Find the roots of x^2 - 5x + 6 = 0. Give the smaller root.","answer":"2"},
    {"id":"U6","category":"algebra","question":"Find the roots of x^2 - 5x + 6 = 0. Give the larger root.","answer":"3"},
    {"id":"U7","category":"algebra","question":"If f(x)=2x^2-3x+1, compute f(4).","answer":"21"},
    {"id":"U8","category":"algebra","question":"Simplify: (x^2 - 9)/(x - 3), for x ≠ 3. What is the simplified expression’s value at x=5?","answer":"8"},
    {"id":"U9","category":"algebra","question":"Solve for x: (x/3) + (x/2) = 10.","answer":"12"},
    {"id":"U10","category":"algebra","question":"If a geometric sequence has a1 = 3 and ratio r = 2, what is a5?","answer":"48"},
]

# ===== Few-shot exemplars =====
TRAD_EXAMPLES = [
    ("What is 8 + 5?", "13"),
    ("A pen costs $2 and a notebook costs $3. What is the total cost?", "$5"),
    ("Solve for x: x + 4 = 11.", "7"),
]

COT_EXAMPLES = [
    # The instruction will ask the model to think carefully but OUTPUT ONLY the final answer.
    ("What is 12 × 7?", "84"),
    ("A box has 6 red and 4 blue balls. How many total?", "10"),
    ("Solve for x: 5x - 10 = 20.", "6"),
]

def build_traditional_prompt(question: str) -> list:
    msgs = [{"role":"system","content":"You are a precise math solver. Give only the final answer."}]
    msgs.append({"role":"user","content":"Here are examples. Provide just the final answer.\n\n" + "\n".join(
        [f"Q: {q}\nA: {a}" for q,a in TRAD_EXAMPLES]
    )})
    msgs.append({"role":"user","content":f"Q: {question}\nA:"})
    return msgs

def build_cot_prompt(question: str) -> list:
    msgs = [{"role":"system","content":"You are a careful math solver. Think carefully, but OUTPUT ONLY the final answer."}]
    fewshot = "\n".join([f"Q: {q}\nA: {a}" for q,a in COT_EXAMPLES])
    # Encourage internal reasoning while constraining the output.
    instruction = (
        "Solve the problem carefully. Use any internal reasoning you need, "
        "but respond with ONLY the final numeric/symbolic answer (no steps)."
    )
    msgs.append({"role":"user","content":f"{instruction}\n\nExamples:\n{fewshot}"})
    msgs.append({"role":"user","content":f"Q: {question}\nA:"})
    return msgs

# ===== Parsing and comparison =====
CURRENCY_RE = re.compile(r"^\$?\s*([-+]?\d*\.?\d+)\s*$")
NUMBER_RE = re.compile(r"^\s*([-+]?\d*\.?\d+)\s*$")

def normalize(ans: str):
    """Normalize a short answer to compare. Returns string for consistent comparison."""
    if ans is None:
        return None
    s = str(ans).strip()
    # If currency, strip $ and spaces
    m = CURRENCY_RE.match(s)
    if m:
        val = m.group(1)
        # Drop trailing .0
        if val.endswith(".0"):
            val = val[:-2]
        return val
    # Pure number
    m2 = NUMBER_RE.match(s)
    if m2:
        val = m2.group(1)
        if val.endswith(".0"):
            val = val[:-2]
        return val
    # Clean trivial punctuation
    s = s.replace(" units","").replace(" minutes","").replace(" km/h","").replace(" liters","")
    s = s.replace(" cups","").replace(" students","").replace(" present","")
    s = s.replace("$","").strip().rstrip(".")
    return s

def is_correct(pred: str, gold: str) -> bool:
    if pred is None:
        return False
    p = normalize(pred)
    g = normalize(gold)
    return p == g

def call_model(messages):
    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=TEMPERATURE
    )
    content = resp.choices[0].message.content if resp and resp.choices else ""
    # Keep the first line / short segment; force brevity
    if content is None:
        return ""
    return content.strip().splitlines()[0]

def evaluate():
    items = ITEMS[:]
    random.shuffle(items)

    rows = []
    per_cat = {"traditional": defaultdict(list), "cot": defaultdict(list)}
    pair_table = Counter()  # For McNemar: (trad_correct, cot_correct) tallies

    for it in items:
        q, gold, cat, iid = it["question"], it["answer"], it["category"], it["id"]

        # Traditional
        trad_msgs = build_traditional_prompt(q)
        trad_out = call_model(trad_msgs)
        trad_ok = is_correct(trad_out, gold)

        # CoT-style
        cot_msgs = build_cot_prompt(q)
        cot_out = call_model(cot_msgs)
        cot_ok = is_correct(cot_out, gold)

        per_cat["traditional"][cat].append(1 if trad_ok else 0)
        per_cat["cot"][cat].append(1 if cot_ok else 0)

        pair_table[(trad_ok, cot_ok)] += 1

        rows.append({
            "id": iid,
            "category": cat,
            "question": q,
            "gold": gold,
            "traditional_pred": trad_out,
            "traditional_correct": int(trad_ok),
            "cot_pred": cot_out,
            "cot_correct": int(cot_ok),
        })

    # Write CSV
    with open("results.csv","w",newline="",encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # Compute metrics
    def acc(vals): return sum(vals)/len(vals) if vals else 0.0

    cats = sorted(set(it["category"] for it in items))
    trad_accs = [acc(per_cat["traditional"][c]) for c in cats]
    cot_accs  = [acc(per_cat["cot"][c]) for c in cats]

    trad_overall = acc([x for c in cats for x in per_cat["traditional"][c]])
    cot_overall  = acc([x for c in cats for x in per_cat["cot"][c]])

    # Equality / Parity metrics
    def parity_metrics(accs):
        if not accs: return {"worst":0.0,"range":0.0,"std":0.0}
        w = min(accs); b = max(accs)
        r = b - w
        s = pstdev(accs) if len(accs) > 1 else 0.0
        return {"worst":w, "range":r, "std":s}

    trad_par = parity_metrics(trad_accs)
    cot_par  = parity_metrics(cot_accs)

    # McNemar’s test
    n01 = pair_table[(True, False)]   # Traditional correct, CoT wrong
    n10 = pair_table[(False, True)]   # Traditional wrong, CoT correct
    # Continuity corrected chi-square
    mcnemar_chi = (abs(n01 - n10) - 1)**2 / (n01 + n10) if (n01 + n10) > 0 else 0.0

    # Pretty print summary
    def pct(x): return f"{100*x:.1f}%"

    print("\n=== RESULTS SUMMARY ===")
    print(f"Model: {MODEL}, temperature={TEMPERATURE}")
    print("\nOverall Accuracy:")
    print(f"  Traditional: {pct(trad_overall)}")
    print(f"  CoT-style  : {pct(cot_overall)}")

    print("\nPer-Category Accuracy:")
    for i,c in enumerate(cats):
        print(f"  {c:>10}: Traditional={pct(trad_accs[i])} | CoT-style={pct(cot_accs[i])}")

    print("\nEquality (Parity) Metrics (higher worst, lower range/std are better):")
    print(f"  Traditional -> worst={pct(trad_par['worst'])}, range={pct(trad_par['range'])}, std={trad_par['std']:.3f}")
    print(f"  CoT-style   -> worst={pct(cot_par['worst'])}, range={pct(cot_par['range'])}, std={cot_par['std']:.3f}")

    print("\nMcNemar’s Test (continuity-corrected):")
    print(f"  n01 (Trad correct, CoT wrong): {n01}")
    print(f"  n10 (Trad wrong, CoT correct): {n10}")
    print(f"  Chi-square ≈ {mcnemar_chi:.3f}  (1 d.f.)")
    print("  For reference, chi^2 = 3.84 corresponds to p ≈ 0.05.")

    print("\nSaved per-item results to results.csv")

if __name__ == "__main__":
    evaluate()

