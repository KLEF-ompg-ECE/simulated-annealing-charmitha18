current   = [random.randint(0, NUM_SLOTS - 1) for _ in range(NUM_EXAMS)]
    current_c = count_clashes(current)
    best      = current[:]
    best_c    = current_c

    T         = initial_temp
    clash_log = []
    temp_log  = []

    for _ in range(max_iterations):
        if T < min_temp:
            break

        neighbour   = generate_neighbor(current)
        neighbour_c = count_clashes(neighbour)
        delta       = neighbour_c - current_c   # positive = worse

        # Always accept improvements; sometimes accept worse solutions
        if delta < 0 or random.random() < math.exp(-delta / T):
            current   = neighbour
            current_c = neighbour_c

        if current_c < best_c:
            best   = current[:]
            best_c = current_c

        clash_log.append(best_c)
        temp_log.append(T)
        T *= cooling_rate

        if best_c == 0:
            break   # perfect solution -- stop early

    return best, best_c, clash_log, temp_log


# =============================================================================
# OUTPUT HELPERS
# =============================================================================

def print_timetable(timetable):
    print("\n  Final Timetable")
    print("-" * 42)
    for slot in range(NUM_SLOTS):
        in_slot = [EXAMS[i] for i in range(NUM_EXAMS) if timetable[i] == slot]
        print(f"  Slot {slot+1}:  {', '.join(in_slot) if in_slot else '(empty)'}")
    print("-" * 42)
    print(f"  Total clashes : {count_clashes(timetable)}\n")


def save_plot(clash_log, temp_log, filename, title):
    os.makedirs("plots", exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    ax1.plot(clash_log, color="crimson", linewidth=1.5)
    ax1.set_ylabel("Best Clashes")
    ax1.set_title(f"SA Convergence - {title}")
    ax1.grid(True, alpha=0.3)
    ax2.plot(temp_log, color="steelblue", linewidth=1.5)
    ax2.set_ylabel("Temperature")
    ax2.set_xlabel("Iteration")
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"  Saved -> {filename}")


# =============================================================================
# RUN YOUR EXPERIMENTS HERE
# =============================================================================

if name == "main":

    # ==========================================================================
    # EXPERIMENT 1 - Baseline
    # Run as-is. Do NOT change any parameters here.
    # ==========================================================================
    print("=" * 48)
    print("  EXPERIMENT 1 - Baseline")
    print("=" * 48)

    tt, clashes, clash_log, temp_log = run_sa(
        initial_temp=100.0, cooling_rate=0.995,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt)
    print(f"  Iterations     : {len(clash_log)}")
    print(f"  Start clashes  : {clash_log[0]}")
    print(f"  Final clashes  : {clashes}")
    save_plot(clash_log, temp_log,
              "plots/experiment_1.png", "Baseline  cooling_rate=0.995")

    # ==========================================================================
    # EXPERIMENT 2 - Effect of Cooling Rate
    # TODO: Copy this block THREE times below (for 0.80, 0.95, and 0.995).
    #       Change cooling_rate and the plot filename each time.
    #       Record results in README.md.
    # ==========================================================================

    # --- Copy and edit below this line ---

    tt2, clashes2, cl2, tl2 = run_sa(
        initial_temp=100.0, cooling_rate=0.80,    # <- change this
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2)
    print(f"  Final clashes : {clashes2}")
    save_plot(cl2, tl2, "plots/experiment_2a.png", "cooling_rate=0.80")   # <- change filename
    
    #-------------------
    tt3, clashes3, cl3, tl3 = run_sa(
        initial_temp=100.0, cooling_rate=0.95,    # <- change this
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt3)
    print(f"  Final clashes : {clashes3}")
    save_plot(cl3, tl3, "plots/experiment_2b.png", "cooling_rate=0.95")
    
    #-------------------

    tt4, clashes4, cl4, tl4 = run_sa(
        initial_temp=100.0, cooling_rate=0.995,    # <- change this
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt4)
    print(f"  Final clashes : {clashes4}")
    save_plot(cl4, tl4, "plots/experiment_2c.png", "cooling_rate=0.995")