# Assignment 1 — Simulated Annealing: Exam Timetable Scheduling
## Observation Report

Student Name  : T.charmitha 
Student ID    : 2310040110
Date Submitted: 02/04/2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the plots/ folder contains all required images
4. Commit this README and the plots/ folder to your GitHub repo

---

## Before You Begin — Read the Code

Open sa_timetable.py and read through it. Then answer these questions.

Q1. What does `count_clashes()` measure? What value means a perfect timetable?

 count_clashes() measures the number of conflicts in the timetable, such as overlapping classes, teacher conflicts, or room clashes. It evaluates how “bad” a timetable is based on these violations. A value of 0 means a perfect timetable with no clashes. 

Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?

 generate_neighbor() creates a slightly modified version of the current timetable by making a small random change, such as swapping time slots or rooms. This helps explore nearby possible solutions. The new timetable differs only in a small part, making it a “neighbor” of the current solution. 

Q3. In `run_sa()`, there is this line:
if delta < 0 or random.random() < math.exp(-delta / T):
What does this line decide? Why does SA sometimes accept a worse solution?

 This line decides whether to accept the new solution based on its quality and probability. If the new solution is better (delta < 0), it is always accepted; if worse, it may still be accepted with a probability depending on temperature T. Simulated Annealing accepts worse solutions to avoid getting stuck in local optima and to explore more of the solution space. 

---

## Experiment 1 — Baseline Run

Instructions: Run the program without changing anything.
python sa_timetable.py

Fill in this table:

| Metric | Your result |
|--------|-------------|
| Number of iterations completed |1379 |
| Clashes at iteration 1 |12 |
| Final best clashes |3 |
| Did SA reach 0 clashes? (Yes / No) |No |

Copy the printed timetable output here:
Final Timetable
------------------------------------------
  Slot 1:  Geography
  Slot 2:  Chemistry, English
  Slot 3:  History, Computer Science, Economics
  Slot 4:  Biology, Statistics
  Slot 5:  Mathematics, Physics
------------------------------------------
  Total clashes : 3

  Iterations     : 1379
  Start clashes  : 12
  Final clashes  : 3 

Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).  
*Where does the biggest drop in clashes happen? Does the curve flatten out?*
 The graph shows a sharp decrease in the number of clashes during the initial iterations, indicating rapid improvement at the start. The biggest drop happens early on when the algorithm is exploring widely and quickly finding better solutions. After that, the curve gradually flattens out, showing smaller improvements as it converges toward an optimal or near-optimal timetable. 

---

## Experiment 2 — Effect of Cooling Rate

Instructions: In sa_timetable.py, find the # EXPERIMENT 2 block in __main__.  
Copy it three times and run with cooling_rate = 0.80, 0.95, and 0.995.  
Save plots as experiment_2a.png, experiment_2b.png, experiment_2c.png.

Results table:

| cooling_rate | Final clashes | Iterations completed | Reached 0 clashes? |
|-------------|---------------|----------------------|--------------------|
| 0.80        |8               |Low                      | No                   |
| 0.95        |3               |Medium                      | No                   |
| 0.995       |3               |High                      | No                   |