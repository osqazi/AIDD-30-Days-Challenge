---
name: "plot-consistency-checker"
description: "Analyze a story, outline, or manuscript for plot holes, timeline errors, character inconsistencies, motivation gaps, and logical flaws. Use whenever the user shares a plot summary, book outline, script, or asks 'does my story make sense?' or 'check my plot for holes'."
version: "1.0.0"
---

# Plot Consistency Checker Skill

## When to Use This Skill

- User shares a book outline, chapter summary, or full plot and asks for feedback
- User says: “check my plot for holes,” “is my story logical?,” “does this timeline work?,” “are my characters consistent?”
- User is worried about continuity, foreshadowing, cause-and-effect, or stakes
- User wants a professional “plot doctor” review before writing or revising

## How This Skill Works

1. **Ingest the story**: Read the provided outline, summary, or chapters
2. **Map key elements**: Timeline, character arcs, major events, stakes, world rules, revelations
3. **Run consistency checks**: Timeline/math, geography/travel, character knowledge & memory, motivation & behaviour, magic/system rules, foreshadowing & payoff, cause-and-effect chains
4. **Flag issues**: Clearly label each problem with severity (Minor / Medium / Major / Story-Breaker)
5. **Suggest fixes**: Actionable solutions or alternatives for every issue

## Output Format

Always structure the feedback exactly like this:

- **Overall Verdict**: One-sentence summary (e.g., “Strong foundation with only minor timeline issues” or “Several major logic gaps that need fixing before writing”)
- **Big Wins**: 3–5 things that already work brilliantly
- **Consistency Issues** (categorised by severity):
  - **Major / Story-Breakers**
    - Description → Why it breaks the story → Suggested fix
  - **Medium Issues**
    - Same format
  - **Minor / Polish-Level**
    - Same format
- **Timeline Overview** (if relevant): Bullet-point chronology of major events with any contradictions highlighted
- **Character Consistency Check**: Quick table or bullets confirming each main character’s arc and knowledge state
- **Final Recommendation**: “Ready to write,” “Fix majors first,” or “Needs structural rework”

## Example

**Input**: User pastes a 12-chapter fantasy novel outline in which a princess escapes a tower in Chapter 3 using a magic rope that only works at midnight, but later in Chapter 9 the same rope is used at noon, and the villain somehow knows her exact location despite her using a cloaking amulet that was established as “undetectable.”

**Output**:

- **Overall Verdict**: Solid high-stakes quest with two major magic-rule contradictions that currently break reader trust.

- **Big Wins**:
  - Clear 3-Act structure with rising stakes
  - Princess’s character arc from helpless to leader is well-foreshadowed
  - Villain’s motivation is consistent and sympathetic
  - Emotional climax in Chapter 11 pays off earlier sacrifices beautifully

- **Consistency Issues**:

  **Major / Story-Breakers**
  - Magic rope only works at midnight (Ch. 3) but is used at noon in Ch. 9 → Directly contradicts established rule the reader has accepted → Fix: Either change Ch. 9 to midnight or establish earlier that prolonged use “charges” the rope for daytime use
  - Cloaking amulet is “completely undetectable by any magic” (Ch. 4) yet villain tracks her perfectly in Ch. 10 → Undermines tension and makes earlier escape feel pointless → Fix: Reveal the villain is using non-magical means (blood bond, spy network, traitor) or give the amulet a specific weakness the villain exploits

  **Medium Issues**
  - Hero learns the ancient prophecy in Ch. 6 but already references it in dialogue in Ch. 2 → Minor retcon feel → Fix: Move prophecy reveal to Ch. 1 or rephrase Ch. 2 line as rumour/hearsay
  - Travel from Eldergrove to the Capital takes 4 days on horseback (Ch. 5) but only 1 day when fleeing in Ch. 11 → Inconsistent world geography → Fix: Add that they took secret mountain pass + magical horses, or adjust earlier journey

  **Minor / Polish-Level**
  - Character eye colour changes from grey to green between Ch. 7 and Ch. 8 → Easy one-line fix
  - Sword name spelled “Dawnbreaker” and “Dawnbringer” interchangeably → Choose one

- **Timeline Overview**:
  - Day 1: Tower escape at midnight
  - Day 5–8: Journey to Eldergrove
  - Day 12: Prophecy revealed
  - Day 20: Battle at Capital (consistent)

- **Character Consistency Check**:
  - Princess: Starts naïve → gradually competent (perfect arc)
  - Villain: Always one step ahead because of spy network (now believable after fix)
  - Sidekick: Comic relief but never forgets his tragic backstory (consistent)

- **Final Recommendation**: Fix the two major magic-rule contradictions and this outline is ready for full manuscript writing. Excellent work overall!