@pytest.fixture(autouse=True)
    def load_readme(self):
        path = os.path.join(ROOT, "README.md")
        assert os.path.isfile(path), "README.md not found"
        self.text = open(path).read()

    PLACEHOLDERS = ["YOUR ANSWER", "YOUR OBSERVATION", "YOUR REFLECTION", "PASTE"]

    def _filled(self, marker):
        m = re.search(
            rf"{re.escape(marker)}.*?\n(.*?)", self.text, re.DOTALL)
        if not m:
            return False
        content = m.group(1).strip()
        return bool(content) and not any(p in content for p in self.PLACEHOLDERS)

    def test_student_name_filled(self):
        line = self.text.split("Student Name")[1].split("\n")[0]
        assert "___" not in line, "Student name is still blank"

    def test_q1_answered(self):
        assert self._filled("Q1."), \
            "Q1 still placeholder — answer what count_clashes() measures"

    def test_q2_answered(self):
        assert self._filled("Q2."), \
            "Q2 still placeholder — answer what generate_neighbor() does"

    def test_q3_answered(self):
        assert self._filled("Q3."), \
            "Q3 still placeholder — explain the acceptance probability line"

    def test_exp1_timetable_pasted(self):
        assert self._filled("Copy the printed timetable"), \
            "Experiment 1 timetable not pasted"

    def test_exp1_observation_written(self):
        assert self._filled("Look at plots/experiment_1.png"), \
            "Experiment 1 plot observation still blank"

    def test_exp2_results_table_filled(self):
        section = self.text[
            self.text.find("Experiment 2"):self.text.find("## Summary")]
        rows = [l for l in section.split("\n") if l.startswith("| 0.")]
        filled = [r for r in rows
                  if r.count("|") >= 4 and
                  any(c.strip() not in ("", "Yes", "No", " ")
                      for c in r.split("|")[2:5])]
        assert len(filled) >= 2, \
            f"Experiment 2 table: only {len(filled)} rows have data (need ≥ 2)"

    def test_exp2_observation_written(self):
        assert self._filled("Compare the three plots"), \
            "Experiment 2 observation (compare plots) still blank"

    def test_exp2_best_rate_answered(self):
        assert self._filled("Which cooling_rate gave the best result"), \
            "Experiment 2 'Which cooling_rate gave best result?' not answered"

    def test_reflection_written(self):
        assert self._filled("most important thing you learned about Simulated"), \
            "Summary reflection still blank"


# =============================================================================
# SECTION D — Code was modified  (15 pts)
# =============================================================================

class TestCodeModified:

    @pytest.fixture(autouse=True)
    def load_code(self):
        self.code = open(os.path.join(ROOT, "sa_timetable.py")).read()

    def test_exp2_rate_080_present(self):
        assert "0.80" in self.code or "0.8," in self.code or \
               "cooling_rate = 0.8\n" in self.code, \
            "cooling_rate=0.80 not found in code — add Experiment 2a block"

    def test_exp2_rate_095_present(self):
        assert "0.95" in self.code, \
            "cooling_rate=0.95 not found in code — add Experiment 2b block"

    def test_exp2_three_plot_saves(self):
        count = self.code.count("experiment_2")
        assert count >= 3, \
            f"Expected 3 experiment_2 plot saves in code, found {count}"