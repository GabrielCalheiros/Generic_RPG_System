# Eidos RPG System: Comprehensive Ruleset Audit & Completion Plan

An in-depth analysis of the current Eidos RPG ruleset has revealed that while the narrative foundation, critical injury tables, and flavor text are incredibly rich, the document has several structural inconsistencies, duplicate skills, missing standard rules, and untyped or missing chapters. 

This document serves as your road map to fully complete the Eidos rulebook.

---

## 1. Chapter-by-Chapter Content & Image Audit

### Chapter 0: Presentation
*   **Text Status:** **Needs Major Rewrite.** 
    *   It claims the book is divided into "six chapters," but we now have 9 chapters.
    *   It outlines chapters that do not exist or uses incorrect numbers (e.g., claiming Chapter 1 is Character Creation, which is actually split into Chapters 1-6).
    *   Lines 18 and 26 are **exact duplicates** of a paragraph describing Chapter 3 (Survival) and Chapter 4 (Injuries).
*   **Image Status:** Complete (`presentation01.pdf`, `presentation02.pdf`). However, the book lacks a **Title/Cover Page** (flagged in the master file comments as `% Add cover`).

### Chapter 1: Personality
*   **Text Status:** **Narratively complete.** However, the detailed Alignment, Morality, and Personality Disorders are purely descriptive. There are no rules on how these traits affect gameplay rolls.
[Author note: Yes, it is purely descriptive. And thats how it should be.]
*   **Image Status:** Highly illustrated (`personality01` through `personality06`). No additional artwork is strictly required.

### Chapter 2: Spirituality and Religion
*   **Text Status:** **Narratively complete.** The Adherence, Tolerance, Demeanor, and Roles are beautifully detailed. Like Chapter 1, they are purely descriptive and lack mechanical triggers or bonuses.
*   **Image Status:** Excellent (`religion01` through `religion08`). Complete.

### Chapter 3: Physical Description
*   **Text Status:** **Complete.**
*   **Image Status:** Good (`physical_01` through `physical_05`), but the original master file comments flagged: `% 8. Add More Images to Physical Description Chapter`. 

### Chapter 4: Skills
*   **Text Status:** **Major Gaps & Duplications.**
    *   **Structure Bug:** The `\subsection{\textbf{Crafting}}` header is entirely empty. All crafting skills (Alchemy, Armorer, Blacksmith, Brewing, etc.) are incorrectly nested under the `\subsection{\textbf{Knowledge and Academic}}` header.
    *   **Academic Skills Missing:** The description talks about history, languages, and sciences, but **zero** actual academic skills are defined. We need to import skills like *Ancient History, Astronomy, Archaeology, Medicine, Occultism, Linguistics, and Theology* from the `Notes/skills.txt` file.
    *   **Duplicated Skills:** 
        *   `Calligraphy` is listed under both *Communication* (line 123) and *Knowledge/Crafting* (line 272).
        *   `Juggling` is listed under both *Communication* (line 177) and *Performance and Artistry* (line 412).
        *   `Cooking` (line 290) and `Culinary Arts` (line 424) are duplicates.
        *   `Sculpting` (line 320) and `Sculpture` (line 394) are duplicates.
*   **Image Status:** **0 Images.** This chapter completely lacks any artwork. We should add at least 2–3 illustrations.

### Chapter 5: Background
*   **Text Status:** **Incomplete.** Currently, it is only a list of writing prompts (questions). It lacks any tables for generating random backgrounds, childhood events, or heritage hooks.
*   **Image Status:** **0 Images.** Master file comments flagged: `% Add images to Background`.

### Chapter 6: Clothing and Equipment
*   **Text Status:** **Severely Incomplete.** 
    *   It defines 4 general "Armor Levels" but has **no weapon lists**, **no shield rules**, and **no item lists** (despite having electrum/gold rules in `Notes/item_list.txt`).
    *   There is no explanation of how armor actually interacts with combat mechanics.
*   **Image Status:** **0 Images.** Needs weapon, armor, and gear illustrations.

### Chapter 7: Conflict Mechanics
*   **Text Status:** **Mechanically Incomplete.**
    *   It consists almost entirely of 20-entry critical hit tables for 3 damage types (cutting, stabbing, impact) across 9 body regions.
    *   It lacks rules for: active defenses (parrying/dodging), weapon stats, shield block rules, ranged combat, unarmed combat, movement, tactical actions (aiming, full-out attack), and healing.
    *   **Typos:** 
        *   Line 17: `\section{Conflic Resolution}` -> Typo ("Conflic").
        *   Line 19: `utilize a 2 20d roll` -> Typo ("2 20d roll" instead of "2d20 roll").
*   **Image Status:** Highly illustrated (`combat01` through `combat17`). Complete.

### Chapter 8: Survival Mechanics
*   **Text Status:** **Incomplete.** 
    *   Lacks overland travel and wilderness exploration rules.
    *   Explains *Fatigue Points* but does not define how they are accumulated or tracked.
    *   Lists scavenging rolls but does not define target difficulties.
    *   No rules for recovering from injuries or treating wounds.
*   **Image Status:** Good (`survival01`, `survival02`), but master notes flagged: `% Add images to Survival Chapter`.

---

## 2. Chapters to Be Created

To fulfill the vision outlined in the Presentation, we must create two new files:

1.  **Chapter 9: Game Master Tools (`chapters/ch9_gm_tools.tex`)**
    *   Rules for worldbuilding, NPC generation (using attributes and backgrounds), encounter scaling, and running campaigns.
2.  **Chapter 10: Magic and Optional Rules (`chapters/ch10_optional_rules.tex`)**
    *   Tabletop magic system (mana/spellcasting mechanics, spell lists, magic item creation).
    *   Optional tactical combat rules.

---

## 3. Places Where Explanations of Mechanics Need Incrementing

1.  **The 2d20 Resolution System:**
    *   *What needs expansion:* Eidos uses a "2d20 roll" to hit target numbers (5 to 39). The book **never explains** how the roll is calculated. Do players sum the two dice? Do they take the higher? How do skills or attributes modify the roll?
2.  **Character Attributes:**
    *   *What needs expansion:* The book refers to "mental rolls" and "physical rolls" but **does not define** what attributes characters have (e.g., Strength, Agility, Intelligence). There are no attribute generation rules.
3.  **Active Defenses:**
    *   *What needs expansion:* In combat, can players dodge, parry, or block? How is an attack roll contested?
4.  **Armor & Shields in Combat:**
    *   *What needs expansion:* Chapter 6 lists armor narrative effects, but how does armor reduce damage or prevent critical injuries? What does a shield do mechanically?
5.  **Healing & Recovery:**
    *   *What needs expansion:* How do characters heal wounds that take "1d4 days" or "1d4 weeks"? What does First Aid or Medicine do?

---

## 4. Final Completion Checklist

Here is the checklist of what needs to be done to finish the rulebook:

### Phase 1: Text Cleanup & Bug Fixes
- [ ] **Chapter 0:** Correct the chapter count to 10, fix chapter summaries, and delete the duplicate paragraph on lines 18 & 26.
- [ ] **Chapter 7:** Correct typos: `Conflic Resolution` -> `Conflict Resolution`, and `2 20d roll` -> `2d20 roll`.
- [ ] **Chapter 4:** 
    - [ ] Create a proper, populated `\subsection{\textbf{Crafting}}` section.
    - [ ] Clean up nested list under `Knowledge and Academic`.
    - [ ] Remove duplicate skills (`Calligraphy`, `Juggling`, `Cooking`/`Culinary Arts`, `Sculpting`/`Sculpture`).
    - [ ] Populate `Knowledge and Academic` with actual skills from `Notes/skills.txt` (e.g., Medicine, Occultism, History).

### Phase 2: Mechanical Integration
- [ ] **The Core System:** Define exactly how a 2d20 roll is resolved, and how attributes and skills modify it.
- [ ] **Attributes:** Define character attributes (e.g., Strength, Agility, Mind, Presence) and how they are generated.
- [ ] **Combat Rules:** Write explicit rules for:
    - [ ] Active Defense (Dodge/Parry).
    - [ ] Ranged & Unarmed Combat.
    - [ ] Mechanical impact of Armor Levels (e.g., damage reduction or critical roll modifiers).
    - [ ] Shield mechanics.
- [ ] **Healing Rules:** Define how resting, First Aid, and Medicine restore health, treat status effects, and heal critical wounds.
- [ ] **Equipment Lists:** Build weapons, armor, and adventuring gear tables with pricing/weight in Chapter 6.

### Phase 3: New Chapter Creation
- [ ] Create **Chapter 9: Game Master Tools** (NPC generators, worldbuilding guidance).
- [ ] Create **Chapter 10: Magic & Optional Rules** (Spellcasting, mana, spell list, optional variants).

### Phase 4: Artistic & Layout Polish
- [ ] **Add Cover Page:** Design a custom LaTeX cover page with title, author, and version.
- [ ] **Create & Add Images:** 
    - [ ] Add 2–3 images for **Chapter 4 (Skills)**.
    - [ ] Add 1–2 images for **Chapter 5 (Background)**.
    - [ ] Add 2–3 images for **Chapter 6 (Clothing & Equipment)**.
    - [ ] Add more images to **Chapter 3 (Physical Description)** and **Chapter 8 (Survival)**.
